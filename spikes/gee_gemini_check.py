"""Feasibility spike (credentialed): Earth Engine backtest + Gemini multimodal evidence reading for Fani/Puri.

1. Night-light backtest: VIIRS VNP46A2 radiance around each OSM substation, pre (20 Apr-1 May 2019) vs
   post (4-10 May 2019), compared with the Holland peak wind from fani_exposure.py (Spearman rank correlation).
2. SAR evidence tile: Sentinel-1 VV same-orbit pre (22 Apr) / post (4 May) RGB composite exported as a PNG and
   read by gemini-3.7-flash into a structured evidence record.
Prereqs: ADC with quota project argmax-cyclone-2026; run fani_exposure.py first.
Run from the spikes directory: uv run --with earthengine-api --with google-genai --with pandas --with requests python gee_gemini_check.py
"""

import json
from pathlib import Path

import ee
import pandas as pd
import requests
from google import genai
from google.genai import types
from pydantic import BaseModel

PROJECT = "argmax-cyclone-2026"
DATA = Path(__file__).parent / "data"
PURI = [85.6, 19.7, 86.2, 20.1]
NTL_BAND = "DNB_BRDF_Corrected_NTL"


class SarFinding(BaseModel):
    """One region of change Gemini identifies in the SAR composite."""

    location_in_image: str
    change_type: str
    evidence: str
    confidence: float


class SarEvidence(BaseModel):
    """Structured evidence record for a pre/post SAR composite."""

    summary: str
    findings: list[SarFinding]
    limitations: str


def nightlight_backtest() -> pd.DataFrame:
    """Measure post-landfall night-light loss per substation and correlate it with modelled peak wind.

    Returns:
        pd.DataFrame: substations with max_wind_kt, ntl_pre, ntl_post and ntl_loss_pct.
    """
    exposure = pd.read_csv(DATA / "fani_puri_exposure.csv")
    subs = exposure[exposure.kind == "substation"].reset_index(drop=True)
    points = ee.FeatureCollection([
        ee.Feature(ee.Geometry.Point([r.lon, r.lat]).buffer(1500), {"idx": i}) for i, r in subs.iterrows()
    ])
    # Raw radiance, high-quality retrievals only (flag 0/1): the gap-filled band carries pre-storm values into
    # cloudy post-landfall nights and hides the blackout.
    ntl = ee.ImageCollection("NASA/VIIRS/002/VNP46A2").map(
        lambda img: img.select(NTL_BAND).updateMask(img.select("Mandatory_Quality_Flag").lte(1)))
    pair = ntl.filterDate("2019-04-20", "2019-05-02").median().rename("pre").addBands(
        ntl.filterDate("2019-05-04", "2019-05-11").median().rename("post"))
    stats = pair.reduceRegions(points, ee.Reducer.mean(), 500).getInfo()["features"]
    values = pd.DataFrame([f["properties"] for f in stats]).set_index("idx").sort_index().reindex(range(len(subs)))
    subs["ntl_pre"], subs["ntl_post"] = values.get("pre").to_numpy(), values.get("post").to_numpy()
    subs["ntl_loss_pct"] = (100 * (1 - subs.ntl_post / subs.ntl_pre)).round(1)
    return subs[["name", "lat", "lon", "min_dist_km", "max_wind_kt", "ntl_pre", "ntl_post", "ntl_loss_pct"]]


def sar_evidence() -> SarEvidence:
    """Export a same-orbit Sentinel-1 VV pre/post composite and have Gemini read it into structured evidence.

    Returns:
        SarEvidence: Gemini's structured description of the change visible in the composite.
    """
    region = ee.Geometry.Rectangle(PURI)
    s1 = (ee.ImageCollection("COPERNICUS/S1_GRD").filterBounds(region)
          .filter(ee.Filter.eq("instrumentMode", "IW")).filter(ee.Filter.eq("orbitProperties_pass", "DESCENDING"))
          .select("VV"))
    pre = s1.filterDate("2019-04-22", "2019-04-23").mosaic().focalMedian(30, "circle", "meters")
    post = s1.filterDate("2019-05-04", "2019-05-05").mosaic().focalMedian(30, "circle", "meters")
    composite = ee.Image.cat([pre, post, post]).clip(region)
    url = composite.getThumbURL({"region": region, "dimensions": 1024, "min": -22, "max": 0, "format": "png"})
    png = requests.get(url, timeout=120).content
    (DATA / "fani_sar_prepost.png").write_bytes(png)

    client = genai.Client(vertexai=True, project=PROJECT, location="global")
    prompt = (
        "This is a Sentinel-1 SAR VV backscatter composite of Puri district, Odisha, India (bbox lon 85.6-86.2, "
        "lat 19.7-20.1; north is up; Bay of Bengal to the south-east). Channels: R = 22 Apr 2019 (before Cyclone Fani), "
        "G and B = 4 May 2019 (one day after landfall near Puri on 3 May). Red/magenta areas darkened after landfall "
        "(possible new standing water); cyan areas brightened (possible structural/vegetation change or debris). "
        "Describe the notable change regions, stay conservative, and state limitations of a single SAR pair."
    )
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=[types.Part.from_bytes(data=png, mime_type="image/png"), prompt],
        config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=SarEvidence,
                                           thinking_config=types.ThinkingConfig(thinking_level="low")),
    )
    return response.parsed


def main() -> None:
    """Run both credentialed checks and print their results; writes CSV/PNG/JSON outputs under data/.

    Returns:
        None
    """
    ee.Initialize(project=PROJECT)
    subs = nightlight_backtest()
    subs.to_csv(DATA / "fani_substation_ntl_backtest.csv", index=False)
    print(subs.sort_values("max_wind_kt", ascending=False).to_string(index=False))
    valid = subs.dropna(subset=["ntl_loss_pct"])
    spearman = valid.max_wind_kt.rank().corr(valid.ntl_loss_pct.rank())
    print(f"\nSpearman(max_wind_kt, ntl_loss_pct) = {spearman:.2f}"
          f"  (n={len(valid)}, median loss {valid.ntl_loss_pct.median():.0f}%)")

    evidence = sar_evidence()
    (DATA / "fani_sar_evidence.json").write_text(evidence.model_dump_json(indent=2))
    print("\nGemini SAR evidence:\n" + json.dumps(evidence.model_dump(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
