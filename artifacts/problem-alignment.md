# Track 5: problem statement vs what ShadowCast does (updated 27 Sep 2026, after surge, rain, roads, parametric cover, live feed and Gemini multimodal)

## Submission description (2–3 lines)

> ShadowCast turns a cyclone forecast into a named, timed list of the hospitals, shelters, substations and arterial roads it will knock out, up to 68 hours before landfall: wind, storm surge and rain at every site, each agency's actions due before gales arrive, and a district parametric trigger. Every model is scored against what really happened: outages against NASA night lights (AUC 0.97 on Fani, 0.79 on Hudhud, a storm it never saw), rain against NASA GPM and surge against IMD. Gemini 3.8 Flash on Vertex AI reads IMD's bulletin PDFs and satellite images, hears officers' spoken questions, and drafts CAP alerts in English, Hindi and the local language for an officer to approve; it is live on Google Cloud for three Indian coasts.

## The official statement (Hack2Skill event page)

- **Problem:** in the Bay of Bengal, move from post-landfall recovery to pre-landfall action: evacuation planning, infrastructure hardening and parametric-insurance liquidity.
- **Challenge:** an AI predictive risk and vulnerability platform using Google Earth Engine satellite feeds, real-time meteorological data and Gemini 3.7 Flash's multimodal reasoning. It should:
  - simulate storm surges;
  - predict local rainfall damage pathways;
  - map exposure for critical infrastructure (power grids, arterial roads, medical shelters);
  - automate early-warning advisory dispatch to local and disaster management authorities.

## Requirement-by-requirement

| Ask | Before (26 Sep) | Now | What we have | What's still missing |
|---|---|---|---|---|
| Pre-landfall action, not recovery | Strong | Strong | Brief with per-agency actions, each due before gales reach its first site; replay from T−68 h | — |
| Infrastructure hardening | Strong | Strong | Per-site outage odds for power, health, water, shelters, police and fire | — |
| Evacuation planning | Partial | Good | Shelters ranked; an evacuation action for sites in the surge zone; each shelter's access road and when it closes (NH316 Bhubaneswar–Puri unsafe at T−4 h) | Routing around cut roads; shelter capacity |
| Parametric-insurance liquidity | Missing | Good | Illustrative district cover (25/50/100% at 64/83/96 kt). Hindsight replays show trigger times; forecasts show payout odds. Basis-risk check: triggered districts lost power at 18% of lit substations, the rest 0% | Illustrative terms, not a real product |
| Earth Engine satellite feeds | Good | Strong | VIIRS night lights, WorldPop, Copernicus DEM, DeltaDTM, ETOPO1, geoBoundaries, GPM IMERG; evidence images rendered from Earth Engine | Used at build time, not streamed live |
| Real-time meteorological data | Partial | Good | Live card: GDACS cyclones and NDMA SACHET warnings in force today, from the archiver (every 6 h). ECMWF ensemble as issued, replayed for Dana | No active storm to run live forecasts on; the live forecast pipeline is replay-only |
| Gemini multimodal reasoning | Partial | Strong | PDF (IMD bulletins), image (before/after VIIRS and field photos), audio (spoken questions in Odia or Hindi), TTS, tool calling | The statement names 3.7 Flash; we run 3.8, its successor |
| Simulate storm surge | Missing | Good | 1D wind setup on ETOPO1 shelf transects plus inverse barometer, carried inland over DeltaDTM. In IMD's reported range on all four storms (Fani 2.3 vs 1.5 m) | Not a hydrodynamic model: no tide, waves or rivers. Few sites flood at 0.3 m (Fani 0) |
| Rainfall damage pathways | Missing | Good | R-CLIPER storm rain per site and road; extreme rain on low ground puts roads at risk and feeds ranking reasons. Rank correlation with GPM 0.72–0.96 | River flooding and runoff not modelled; Amphan rain ρ 0.14 |
| Critical infrastructure: power grids | Strong | Strong | Substations and power plants, calibrated outage model | Per-utility calibration |
| Critical infrastructure: medical and shelters | Strong | Strong | Hospitals, health centres, clinics, cyclone shelters | — |
| Critical infrastructure: arterial roads | Missing | Good | OSM motorway, trunk and primary: cut (surge or ≥ 90 kt, IMD's extremely-severe class), at risk (≥ 64 kt or extreme rain on low ground), closing time; Fani 3,896 of 9,761 km cut | Thresholds follow IMD's damage classes; not checked against recorded road closures |
| Advisory dispatch to authorities | Good | Good | CAP 1.2 in three languages, officer approval signed on the server, Firestore audit log, TTS audio, IMD bulletin checked first | Nothing is sent, by design (exercise mode) |

## Wow factor: honest read

**What lands with judges**

1. **Proven by satellite, failures published.** Most entries show predictions; ShadowCast shows its score against NASA night lights, holds out coast segments, tests on an unseen storm (Hudhud 0.79) and publishes where it fails (Amphan 0.44).
2. **Real forecasts, as issued.** The Dana replay uses ECMWF's ensemble exactly as it stood 68 hours out, not hindsight.
3. **The official picture beside the model.** Gemini reads IMD's bulletin PDF into the Brief next to ShadowCast's surge; the live card shows today's real NDMA warnings.
4. **Gemini is used for everything it can do.** It reads PDFs, sees before/after satellite images (and agrees with the model on Khordha, Puri and Cuttack), hears a spoken Odia or Hindi question, and speaks the approved alert.
5. **Money that tracks losses.** The parametric trigger fired where power actually failed (18% vs 0%).
6. **A named, timed deadline instead of a cone.** "Mot shelter, 99%, gales 16 h before landfall; NH316 closes at T−4 h."

**What could undercut it**

- The Brief's "surge flood 0" tile on Fani sits next to a 2.6 m surge crest. The crest is real, but the 0.3 m flood threshold is rarely crossed on DeltaDTM ground. Be ready to explain it, or don't linger on that tile in the video.
- Everything is a replay: no cyclone is active now, so "live" means the warnings card, not a live forecast.
- The parametric cover is illustrative, and the road thresholds are IMD classes, not validated closures.
- Gemini latency on camera, and unverified Odia TTS quality (get a native listener).
- The screen is dense; the video must guide the eye (Brief → Prepare → Prove).
