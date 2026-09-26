"""Feasibility spike: deterministic wind-exposure envelope for Cyclone Fani (2019) over Odisha assets.

Joins IBTrACS quadrant wind radii and a Holland wind profile (JTWC/USA fields) with OSDMA cyclone shelters and
OSM critical infrastructure, and reports each asset's worst wind band, peak modelled wind and lead time.
Substations also get the peak wind along the OSM power lines that connect to them (feeder exposure).
Run from the spikes directory: uv run --with pandas --with requests python fani_exposure.py [puri|coast]
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests

DATA = Path(__file__).parent / "data"
EARTH_RADIUS_KM = 6371.0
NM_TO_KM = 1.852
HOLLAND_B = 1.5
FEEDER_SNAP_KM = 0.5
BANDS = [("R64", 64), ("R50", 50), ("R34", 34)]
QUADRANTS = ["NE", "SE", "SW", "NW"]
REGIONS = {
    "puri": {"bbox": (19.70, 85.40, 20.20, 86.30), "shelters": "osdma_shelters_puri.json"},
    "coast": {"bbox": (19.00, 84.40, 21.70, 87.60), "shelters": None},  # Ganjam to Balasore
}
OVERPASS_URLS = ["https://overpass.kumi.systems/api/interpreter", "https://overpass-api.de/api/interpreter"]
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


def fetch_osm(region: str) -> list[dict]:
    """Return OSM point assets and power lines (with geometry) for a region, downloading once via Overpass.

    Args:
        region (str): Key of REGIONS.

    Returns:
        list[dict]: Overpass elements; ways carry a "geometry" list of {lat, lon} vertices.
    """
    path = DATA / f"osm_{region}.json"
    if path.exists():
        return json.loads(path.read_text())
    bb = ",".join(map(str, REGIONS[region]["bbox"]))
    query = f"""[out:json][timeout:300];
(
 nwr["power"~"^(substation|plant)$"]({bb});
 way["power"~"^(line|minor_line)$"]({bb});
 nwr["amenity"~"^(hospital|clinic|school|police|fire_station)$"]({bb});
 nwr["healthcare"="centre"]({bb});
 nwr["man_made"~"^(water_works|water_tower)$"]({bb});
);
out tags geom;"""
    for url in OVERPASS_URLS:
        try:
            response = requests.post(url, data={"data": query}, timeout=330, headers={"User-Agent": "argmax-spike"})
            response.raise_for_status()
            break
        except requests.RequestException as exc:
            print(f"overpass failed at {url}: {exc}")
    else:
        raise RuntimeError("all Overpass endpoints failed")
    elements = response.json()["elements"]
    path.write_text(json.dumps(elements))
    return elements


def load_assets(region: str, elements: list[dict]) -> pd.DataFrame:
    """Build the point-asset table from OSDMA shelters (if the region has them) and OSM elements.

    Args:
        region (str): Key of REGIONS.
        elements (list[dict]): Output of fetch_osm.

    Returns:
        pd.DataFrame: columns asset_id, kind, name, source, lat, lon.
    """
    shelters_file = REGIONS[region]["shelters"]
    shelters = json.loads((DATA / shelters_file).read_text()) if shelters_file else []
    rows = [
        {"asset_id": f"shelter:{i}", "kind": "cyclone_shelter", "name": s["name"], "source": f"OSDMA/{s['shelter']}",
         "lat": s["lat"], "lon": s["lon"]}
        for i, s in enumerate(shelters)
    ]
    for el in elements:
        tags = el.get("tags", {})
        kind = next((k for (key, val), k in OSM_KINDS.items() if tags.get(key) == val), None)
        geometry = el.get("geometry") or [{"lat": el.get("lat"), "lon": el.get("lon")}]
        points = [p for p in geometry if p and p.get("lat") is not None]
        if kind and points:
            rows.append({"asset_id": f"osm:{el['type']}/{el['id']}", "kind": kind, "name": tags.get("name"),
                         "source": "OSM", "lat": np.mean([p["lat"] for p in points]),
                         "lon": np.mean([p["lon"] for p in points])})
    return pd.DataFrame(rows)


def load_track(name: str, season: int) -> pd.DataFrame:
    """Load one storm's 3-hourly IBTrACS track with quadrant wind radii and radius of maximum wind.

    Args:
        name (str): IBTrACS storm name, e.g. "FANI".
        season (int): Storm season year.

    Returns:
        pd.DataFrame: ISO_TIME, LAT, LON, USA_WIND, USA_RMW and USA_R{34,50,64}_{quadrant} columns (kt / nm).
    """
    df = pd.read_csv(DATA / "ibtracs_NI.csv", skiprows=[1], low_memory=False)
    track = df[(df.NAME == name) & (df.SEASON == season)].copy()
    radius_cols = [f"USA_R{b}_{q}" for _, b in BANDS for q in QUADRANTS]
    for col in ["LAT", "LON", "USA_WIND", "USA_RMW", *radius_cols]:
        track[col] = pd.to_numeric(track[col], errors="coerce")
    track["ISO_TIME"] = pd.to_datetime(track.ISO_TIME)
    return track[["ISO_TIME", "LAT", "LON", "USA_WIND", "USA_RMW", *radius_cols]].reset_index(drop=True)


def exposure(points: pd.DataFrame, track: pd.DataFrame) -> pd.DataFrame:
    """Compute peak Holland wind, worst wind band, closest approach and first-exposure time for every point.

    For each track fix the point's bearing from the storm centre selects the quadrant radius; the point is inside
    a band when its great-circle distance is within that radius. Missing radii mean "no band". The Holland (1980)
    profile V = Vmax * sqrt((Rm/r)^B * exp(1 - (Rm/r)^B)) with B = HOLLAND_B gives a continuous wind estimate.

    Args:
        points (pd.DataFrame): Any frame with lat/lon columns (assets or power-line vertices).
        track (pd.DataFrame): Output of load_track.

    Returns:
        pd.DataFrame: points plus max_wind_kt, min_dist_km, closest_time, band and band_first_time.
    """
    plat = np.radians(points.lat.to_numpy(dtype=float))[:, None]
    plon = np.radians(points.lon.to_numpy(dtype=float))[:, None]
    tlat, tlon = np.radians(track.LAT.to_numpy())[None, :], np.radians(track.LON.to_numpy())[None, :]
    dlat, dlon = plat - tlat, plon - tlon
    hav = np.sin(dlat / 2) ** 2 + np.cos(tlat) * np.cos(plat) * np.sin(dlon / 2) ** 2
    dist_km = 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(hav))
    bearing = (np.degrees(np.arctan2(np.sin(dlon) * np.cos(plat),
                                     np.cos(tlat) * np.sin(plat) - np.sin(tlat) * np.cos(plat) * np.cos(dlon))) + 360) % 360
    quadrant = (bearing // 90).astype(int)  # 0=NE, 1=SE, 2=SW, 3=NW

    out = points.copy()
    x = (track.USA_RMW.to_numpy()[None, :] * NM_TO_KM / np.maximum(dist_km, 1.0)) ** HOLLAND_B
    out["max_wind_kt"] = np.nanmax(track.USA_WIND.to_numpy()[None, :] * np.sqrt(x * np.exp(1 - x)), axis=1).round(0)
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


def feeder_exposure(substations: pd.DataFrame, elements: list[dict], track: pd.DataFrame) -> pd.Series:
    """Peak modelled wind along the OSM power lines that touch each substation (within FEEDER_SNAP_KM).

    A substation loses supply when any line feeding it fails, so the relevant hazard is the worst wind anywhere on
    its connected lines, not only at the substation point.

    Args:
        substations (pd.DataFrame): Substation rows with lat/lon.
        elements (list[dict]): Output of fetch_osm.
        track (pd.DataFrame): Output of load_track.

    Returns:
        pd.Series: line_max_wind_kt aligned to substations.index (NaN when no line connects).
    """
    vertices = pd.DataFrame([
        {"line": el["id"], "lat": p["lat"], "lon": p["lon"]}
        for el in elements if el.get("tags", {}).get("power") in ("line", "minor_line") for p in el.get("geometry", [])
    ])
    line_wind = exposure(vertices, track).groupby("line").max_wind_kt.max()
    km_per_deg = np.pi * EARTH_RADIUS_KM / 180
    vlat, vlon = vertices.lat.to_numpy(np.float32), vertices.lon.to_numpy(np.float32)
    result = {}
    for idx, sub in substations.iterrows():  # equirectangular distance is exact enough at 0.5 km
        d_km = km_per_deg * np.hypot(vlat - sub.lat, (vlon - sub.lon) * np.cos(np.radians(sub.lat)))
        touching = vertices.line.to_numpy()[d_km <= FEEDER_SNAP_KM]
        result[idx] = line_wind.loc[np.unique(touching)].max() if len(touching) else np.nan
    return pd.Series(result, name="line_max_wind_kt")


def main() -> None:
    """Run the Fani exposure spike for the region given on the command line; writes data/fani_{region}_exposure.csv.

    Returns:
        None
    """
    region = sys.argv[1] if len(sys.argv) > 1 else "puri"
    track = load_track("FANI", 2019)
    elements = fetch_osm(region)
    result = exposure(load_assets(region, elements), track)
    subs = result.kind == "substation"
    result.loc[subs, "line_max_wind_kt"] = feeder_exposure(result[subs], elements, track)
    result.to_csv(DATA / f"fani_{region}_exposure.csv", index=False)

    landfall = pd.Timestamp("2019-05-03 03:30")  # IMD: landfall near Puri 08:00-10:00 IST
    print(f"region: {region}  track fixes: {len(track)}  assets: {len(result)}")
    print(pd.crosstab(result.kind, result.band.fillna("outside"), margins=True).to_string())
    first = result.dropna(subset=["band_first_time"]).groupby("band").band_first_time.min()
    print("\nearliest band entry per band (hours before landfall):")
    for band, ts in first.items():
        print(f"  {band}: {ts}  ({(landfall - ts).total_seconds() / 3600:+.0f} h)")
    print("\nmodelled wind (kt) by asset kind:")
    print(result.groupby("kind").max_wind_kt.describe()[["count", "min", "50%", "max"]].to_string())
    print(f"\nsubstations with a connected OSM line: {result.loc[subs, 'line_max_wind_kt'].notna().sum()} / {subs.sum()}")


if __name__ == "__main__":
    main()
