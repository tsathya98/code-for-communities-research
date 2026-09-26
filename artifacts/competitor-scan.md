# Competitor and prior-art scan (26 Sep 2026)

**Question:** has anyone publicly built what ShadowCast does?
**Method:** GitHub repo, README and code search plus web search; the closest competitors were cloned and grepped.
**Answer:** no public project does the whole pipeline. Every individual piece has been done before, and several Track 5 teams already overlap on the "table stakes".

## Closest prior art

| Rank | Project | Overlap | Difference from ShadowCast |
|---|---|---|---|
| 1 | [CLIMADA](https://github.com/CLIMADA-project/climada_python) + climada_petals [`TCForecast`](https://climada-petals.readthedocs.io/en/latest/tutorial/climada_hazard_TCForecast.html) (476★, active) | Reads ECMWF ensemble TC BUFR, builds Holland wind fields, computes impact on exposure. This is our hazard core | Generic economic damage curves (Emanuel 2011). No P(outage) per named asset, no night-light calibration, no reasons, no agent or advisory |
| 2 | [510 / Netherlands Red Cross Typhoon IBF model](https://github.com/rodekruis/Typhoon-Impact-based-forecasting-model) | ML plus ECMWF ensemble before landfall; operational (triggers funding releases for the Philippine Red Cross) | Predicts % of houses destroyed per municipality; not per asset, not power, not India |
| 3 | NDMA/IMD Web-DCRA ([paper](https://www.researchgate.net/publication/333194177)) | Operational in India: forecast wind swath × infrastructure/population → district impact warnings | Closed; district level; no calibrated outage model, no ensemble probabilities, no post-event proof |
| 4 | Hurricane outage ML: Guikema's SGHOPM; ORNL night lights for outage prediction ([OSTI](https://www.osti.gov/pages/biblio/1846366)); [arXiv 2410.00017](https://arxiv.org/html/2410.00017v1); STO-CAST ([arXiv 2512.06644](https://arxiv.org/abs/2512.06644)); [PNNL OWL-I](https://github.com/JRice15/global_outage_detection) | Night lights (or utility records) as the outage label is established science | US/China, grid cells; not named Indian assets; not tied to advisories |
| 5 | NASA Black Marble on Fani ([article](https://appliedsciences.nasa.gov/our-impact/news/suomi-npp-viirs-black-marble-product-tracks-power-outages-odisha-india-cyclone-fani)); IOP 2025 recovery study of 396 storms ([paper](https://iopscience.iop.org/article/10.1088/2634-4505/ade474)) | Night-light outage after cyclones | Describes the outage after the event; does not forecast it |

## Track 5 competitor repos (all created September 2026, 0–3★)

- **[komallbarhate/cyclone-forecaster](https://github.com/komallbarhate/cyclone-forecaster) ("CycloneShield"), the closest.**
  - Overlap: Fani, IBTrACS, Holland/Willoughby wind, OSM assets, Gemini advisories in EN/HI/OR, and an "honest validation" slide.
  - Difference: it validates flood extent from its surge model against Sentinel-1 (IoU/F1). There is no outage validation, no ensemble and no fitted outage model.
- **[v1r4t/CycloSac](https://github.com/v1r4t/CycloSac):** Holland wind, a surge lookup table, hand-tuned fragility scores and cascade triggers on 35 assets; Michaung replayed at T−48 h.
- **[Pratik-y-SDE/StromTracker](https://github.com/Pratik-y-SDE/StromTracker) and [ashishjoseph11/StormTrace](https://github.com/ashishjoseph11/StormTrace):** identical READMEs. IMD track, Google Earth Engine, officer approval workflow and audit log, so the approval gate is not unique.
- **[SwagataGhosh7/Bayshield-AI](https://github.com/SwagataGhosh7/Bayshield-AI):** Gemini writes CAP 1.2 XML, plus audio alerts and a CSV audit export.
- **[Uday-Mahajan-Dev/cycloneguard](https://github.com/Uday-Mahajan-Dev/cycloneguard):** IBTrACS, a "Holland_SLOSH" surge model, OSM assets, CAP XML and Gemini for Puri; risk comes from rule thresholds on flood depth.
- **Others:**
  - LLM-reasoned or heuristic dashboards: singhshagun221-lab, saurabh0477, adityayashrajkaran.
  - A random forest on synthetic features: Nandanikumari027.
  - Only track replay built so far: PrithviJayachandraM.
- **Related, not hackathon entries:** [NavneetK04/odisha-cyclone-risk](https://github.com/NavneetK04/odisha-cyclone-risk) (CLIMADA catastrophe model) and [Kit-ty8/Bengal-HealthCAT-Model](https://github.com/Kit-ty8/Bengal-HealthCAT-Model).

## Verdict

**Table stakes, where others match us:**
- Holland wind on IBTrACS
- OSM exposure
- Gemini advisories in Odia/Hindi
- CAP 1.2 XML
- TTS audio
- Approval gate plus audit
- The Fani replay

**Novel in combination; no public repo or competitor found doing any of these:**
1. A per-asset outage probability **learned from real labels** (VIIRS VNP46A2 night-light loss in Odisha after Fani). Competitors use thresholds, fragility guesses or LLM judgement.
2. **As-issued ECMWF ensemble → per-asset probabilities** 68–20 h before landfall, applied to Indian assets.
3. **Per-asset outage verification** against satellites after landfall. The closest competitor validates flood, not outage.

## Actions for the pitch and the build

- **Strengthen the evidence.**
  - Add a spatial holdout for Fani: fit on some districts, score on the others. AUC 0.97 in sample will draw scrutiny.
  - Add Amphan 2020 as a strong out-of-sample storm.
- **Credit prior art.** Name CLIMADA and the 510 IBF model: "we apply Red Cross–style impact-based forecasting to Indian grid assets, calibrated on satellite ground truth". Informed judges will know them.
- **Lead with the three novel points.** Present the table stakes as expected, not as the wow.
