"""Feasibility spike: deterministic wind-exposure envelope for Cyclone Fani (2019) over Puri assets.

Joins IBTrACS quadrant wind radii (JTWC/USA fields, nautical miles) with OSDMA cyclone shelters
and OSM critical infrastructure, and reports each asset's worst wind band and lead time.
Run from the spikes directory: uv run --with pandas python fani_exposure.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data"
EARTH_RADIUS_KM = 6371.0
NM_TO_KM = 1.852
HOLLAND_B = 1.5
BANDS = [("R64", 64), ("R50", 50), ("R34", 34)]
QUADRANTS = ["NE", "SE", "SW", "NW"]
OSM_KINDS = {
    ("power", "substation"): "substation",
    ("power", "plant"): "power_plant",
    ("amenity", "hospital"): "hospital",
    ("amenity", "clinic"): "clinic",
    ("healthcare", "centre"): "health_centre",
    ("amenity", "school"): "school",
    ("amenity", "fire_station"): "fire_station",
    ("amenity", "police"): "police",
    ("man_made", "water_works"): "water_works",
    ("man_made", "water_tower"): "water_works",
}


def load_assets() -> pd.DataFrame:
    """Load OSDMA shelters and OSM point assets into one frame.

    Returns:
        pd.DataFrame: columns asset_id, kind, name, source, lat, lon.
    """
    shelters = json.loads((DATA / "osdma_shelters_puri.json").read_text())
    rows = [
        {"asset_id": f"shelter:{i}", "kind": "cyclone_shelter", "name": s["name"], "source": f"OSDMA/{s['shelter']}",
         "lat": s["lat"], "lon": s["lon"]}
        for i, s in enumerate(shelters)
    ]
    for el in json.loads((DATA / "osm_puri.json").read_text()):
        tags = el.get("tags", {})
        kind = next((k for (key, val), k in OSM_KINDS.items() if tags.get(key) == val), None)
        point = el.get("center") or {"lat": el.get("lat"), "lon": el.get("lon")}
        if kind and point["lat"] is not None:
            rows.append({"asset_id": f"osm:{el['type']}/{el['id']}", "kind": kind, "name": tags.get("name"),
                         "source": "OSM", "lat": point["lat"], "lon": point["lon"]})
    return pd.DataFrame(rows)


def load_track(name: str, season: int) -> pd.DataFrame:
    """Load one storm's 3-hourly IBTrACS track with quadrant wind radii.

    Args:
        name (str): IBTrACS storm name, e.g. "FANI".
        season (int): Storm season year.

    Returns:
        pd.DataFrame: ISO_TIME, LAT, LON, USA_WIND and USA_R{34,50,64}_{quadrant} columns (nm).
    """
    df = pd.read_csv(DATA / "ibtracs_NI.csv", skiprows=[1], low_memory=False)
    track = df[(df.NAME == name) & (df.SEASON == season)].copy()
    radius_cols = [f"USA_R{b}_{q}" for _, b in BANDS for q in QUADRANTS]
    for col in ["LAT", "LON", "USA_WIND", "USA_RMW", *radius_cols]:
        track[col] = pd.to_numeric(track[col], errors="coerce")
    track["ISO_TIME"] = pd.to_datetime(track.ISO_TIME)
    return track[["ISO_TIME", "LAT", "LON", "USA_WIND", "USA_RMW", *radius_cols]].reset_index(drop=True)


def exposure(assets: pd.DataFrame, track: pd.DataFrame) -> pd.DataFrame:
    """Compute worst wind band, closest approach and first-exposure time for every asset.

    For each track fix the asset's bearing from the storm centre selects the quadrant radius; the asset
    is inside a band when its great-circle distance is within that radius. Missing radii mean "no band".

    Args:
        assets (pd.DataFrame): Output of load_assets.
        track (pd.DataFrame): Output of load_track.

    Returns:
        pd.DataFrame: assets plus min_dist_km, closest_time, band (R64/R50/R34/None) and band_first_time.
    """
    alat, alon = np.radians(assets.lat.to_numpy())[:, None], np.radians(assets.lon.to_numpy())[:, None]
    tlat, tlon = np.radians(track.LAT.to_numpy())[None, :], np.radians(track.LON.to_numpy())[None, :]
    dlat, dlon = alat - tlat, alon - tlon
    hav = np.sin(dlat / 2) ** 2 + np.cos(tlat) * np.cos(alat) * np.sin(dlon / 2) ** 2
    dist_km = 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(hav))
    bearing = (np.degrees(np.arctan2(np.sin(dlon) * np.cos(alat),
                                     np.cos(tlat) * np.sin(alat) - np.sin(tlat) * np.cos(alat) * np.cos(dlon))) + 360) % 360
    quadrant = (bearing // 90).astype(int)  # 0=NE, 1=SE, 2=SW, 3=NW

    out = assets.copy()
    # Holland (1980) gradient-wind profile, B=1.5 assumed; V = Vmax * sqrt((Rm/r)^B * exp(1 - (Rm/r)^B))
    rm_km = track.USA_RMW.to_numpy()[None, :] * NM_TO_KM
    x = (rm_km / np.maximum(dist_km, 1.0)) ** HOLLAND_B
    wind_kt = track.USA_WIND.to_numpy()[None, :] * np.sqrt(x * np.exp(1 - x))
    out["max_wind_kt"] = np.nanmax(wind_kt, axis=1).round(0)
    closest = dist_km.argmin(axis=1)
    out["min_dist_km"] = dist_km.min(axis=1).round(1)
    out["closest_time"] = track.ISO_TIME.to_numpy()[closest]
    out["band"], out["band_first_time"] = None, pd.NaT
    for band, knots in reversed(BANDS):  # weakest first so stronger bands overwrite
        radii_km = track[[f"USA_R{knots}_{q}" for q in QUADRANTS]].to_numpy().T * NM_TO_KM  # (4, n_fixes)
        inside = dist_km <= radii_km[quadrant, np.arange(len(track))[None, :]]  # NaN radius -> False
        hit = inside.any(axis=1)
        out.loc[hit, "band"] = band
        out.loc[hit, "band_first_time"] = track.ISO_TIME.to_numpy()[inside[hit].argmax(axis=1)]
    return out


def main() -> None:
    """Run the Fani/Puri exposure spike and print a summary; writes data/fani_puri_exposure.csv.

    Returns:
        None
    """
    track = load_track("FANI", 2019)
    result = exposure(load_assets(), track)
    result.to_csv(DATA / "fani_puri_exposure.csv", index=False)
    landfall = pd.Timestamp("2019-05-03 03:30")  # IMD: landfall near Puri 08:00-10:00 IST
    print(f"track fixes: {len(track)}  assets: {len(result)}")
    print(pd.crosstab(result.kind, result.band.fillna("outside"), margins=True).to_string())
    first = result.dropna(subset=["band_first_time"]).groupby("band").band_first_time.min()
    print("\nearliest band entry per band (hours before landfall):")
    for band, ts in first.items():
        print(f"  {band}: {ts}  ({(landfall - ts).total_seconds() / 3600:+.0f} h)")
    print("\nHolland max wind (kt) by asset kind:")
    print(result.groupby("kind").max_wind_kt.describe()[["min", "50%", "max"]].to_string())
    print("\nsubstations ranked by modelled peak wind:")
    subs = result[result.kind == "substation"].sort_values("max_wind_kt", ascending=False)
    print(subs[["name", "lat", "lon", "min_dist_km", "max_wind_kt"]].fillna({"name": "?"}).head(10).to_string(index=False))


if __name__ == "__main__":
    main()
