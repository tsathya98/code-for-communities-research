# Track 5 feasibility spike — Cyclone Impact & Infrastructure Vulnerability

Run date: 26 Sep 2026. Pilot: **Cyclone Fani (2019) × Puri district, Odisha.** Nothing here needed credentials.

## Verdict

**Feasible, and the data is better than expected.** We can build a full replay with real tracks, real official assets and real satellite ground truth. The remaining risks are all things we check with keys: Gemini on Vertex AI, Odia text-to-speech, Earth Engine quota, and WeatherNext access.

## Verified data (public, no auth)

| Need | Source | Result |
|---|---|---|
| Cyclone track + wind radii | IBTrACS v04r01, North Indian basin (`../spikes/data/ibtracs_NI.csv`) | 3-hourly fixes with quadrant R34/R50/R64 and RMW for Fani, Amphan, Michaung, Dana, Montha and others. **Updated to 24 Sep 2026**, with a live provisional Bay of Bengal system since 22 Sep 2026 |
| Cyclone shelters | OSDMA shelter map (the page embeds JSON) (`../spikes/data/osdma_shelters_puri.json`) | **177 official shelters in Puri with GPS**, scheme (NCRMP / MCS / MFS / ICZMP / IRCS), block and village. Works for every district through `?district=` |
| Critical infrastructure | OSM Overpass (bbox around Puri) (`../spikes/data/osm_puri.json`) | 27 substations, 52 power lines, 71 hospitals, 51 health centres, 36 clinics, 49 schools, police, fire, water works, 1,076 trunk/primary/secondary road segments |
| SAR (for flood mapping) | Sentinel-1 GRD, checked via Planetary Computer STAC | Pre-landfall 27/28 Apr; post-landfall **4, 5, 6 May** and 9/10 May (S1A + S1B, 6-day revisit) |
| Optical | Sentinel-2 L2A | Clear 20–30 Apr, 100% cloud at landfall, clear again **15/18 May**. Good for vegetation and tree-loss damage mapping |
| Earth Engine catalog | STAC | S1_GRD, S2_SR_HARMONIZED, GPM IMERG V07, ERA5-Land, Copernicus DEM, JRC GSW, WorldPop, GHSL, Dynamic World, Open Buildings v3, ESA WorldCover, **VIIRS VNP46A2 daily night lights (to 23 Sep 2026)**, **GFS 0.25° and ECMWF IFS near-real-time forecasts** |
| Google AI forecast | WeatherNext 2 in Earth Engine (`projects/gcp-public-data-weathernext/assets/weathernext_2_0_0`) | 64-member ensemble, 15-day lead, 2022–present. **Gated: a data request form is required** (BigQuery WeatherNext 3 approval takes 5–7 business days) |
| Model | `gemini-3.7-flash` (GA Aug 2026) | Input: text, image, video, audio, PDF. Structured output, function calling, Maps and Search grounding, 1M context. **No Live API and no audio output**, so voice uses Cloud Text-to-Speech |

## Spike result: [`fani_exposure.py`](../spikes/fani_exposure.py)

Join of Fani's track with 448 Puri assets:

1. **Binary wind bands are useless at district scale.** All 448 assets fall inside R64 (Fani's 64-kt radius was about 75–110 km). A band-only map is exactly the "map theatre" the judges will penalise.
2. **A Holland parametric wind field discriminates.** It uses Vmax and RMW from the track, with B = 1.5 assumed. Modelled peak wind is 75–125 kt across assets, and substations can be ranked, e.g. Puri 117 kt at 29.5 km from the track. This is the deterministic hazard layer.
3. **Best-track hindsight gives only +4 h of "lead time".** An honest replay must use the forecasts issued at the time: the IMD/RSMC bulletins and forecast-track graphics, from 25 Apr onward. Gemini reading those PDFs and cone images into a structured forecast track is a genuine multimodal use. The IMD site refused connections from this machine; ReliefWeb mirrors the forecast-track graphics.

## Credentialed checks — [`gee_gemini_check.py`](../spikes/gee_gemini_check.py) (26 Sep, project `argmax-cyclone-2026`)

| Check | Result |
|---|---|
| Earth Engine via ADC | **Works with plain `gcloud auth application-default login` plus the quota project**. No EE-specific scope or `earthengine authenticate` needed. 9 S1 scenes over Puri for 25 Apr–12 May 2019; mean elevation 4.2 m (Copernicus DEM; it is superseded, so use `COPERNICUS/DEM/GLO30_2024_1`) |
| `gemini-3.7-flash` on Vertex AI | **Only on the `global` endpoint**; `asia-south1` and `us-central1` return 404. Structured JSON works (it correctly gave ବାତ୍ୟା, Odia for cyclone). `gemini-3.8-flash` is also listed; keep 3.7 because the track names it |
| Cloud Text-to-Speech | **No Odia (or-IN) voice.** Chirp3-HD voices exist for te, ta, bn, hi, mr, gu, kn, ml, pa and en-IN |
| Gemini TTS (`gemini-2.5-flash-tts`, global) | Produced 9.1 s of audio from an Odia advisory (`../spikes/data/odia_advisory_test.wav`). **Odia pronunciation still needs a native-listener check** |
| Night-light backtest (VNP46A2) | The **gap-filled band hides the blackout**: it carries pre-storm values into cloudy post-landfall nights, so Puri showed −2.5% loss. With raw `DNB_BRDF_Corrected_NTL` masked to `Mandatory_Quality_Flag ≤ 1`: **median loss 74% across 27 substations; Puri 94%, Samangara 94%** |
| Wind vs outage | Spearman(modelled peak wind, light loss) = **0.10**. Inside one district every substation saw 75–125 kt and the grid failed as a network, so per-asset wind can't explain per-asset outage. **The backtest must span a wider area with a real hazard gradient** (e.g. 300 km across the track, Ganjam to Balasore) and include upstream transmission-line exposure, not just a point-wind check |
| Gemini on a SAR pre/post composite | Structured `SarEvidence` returned. It correctly placed the post-landfall darkening (possible standing water) in the western inland/agricultural zone and the SW floodplain, and listed sensible caveats (seasonal flooding, irrigation). **It missed that ~45% of the tile has no data** (swath edge). Lesson: pass deterministic metrics (coverage %, flood-mask area) in the prompt; Gemini explains, code measures. Also mosaic several passes to cover the full bbox |

## Backtest design (the strongest part of the pitch)

Fani's damage was mostly **wind**, so the ground truth comes from several damage pathways:

- **Power:** VIIRS night-light loss around each substation (daily VNP46A2), comparing before with 4–10 May. This checks the predicted substation risk against the observed blackout.
- **Vegetation / structure:** Sentinel-2 NDVI loss, comparing 20–30 Apr with 15–18 May.
- **Flood:** Sentinel-1 SAR change, 27/28 Apr against 4–6 May. Fani flooding was modest, so use Michaung 2023 (Chennai) or Amphan 2020 as the second scenario to show the rain and surge pathway.

## Architecture implications

- Hazard (track to wind field) and exposure scoring are **deterministic code**. Gemini extracts forecasts from bulletins, reads SAR/optical/night-light evidence tiles, explains each ranked action and writes the multilingual advisory. A human approves every dispatch (EDA: exception → drilldown → action).
- For live mode: IBTrACS provisional feed plus GFS/ECMWF from Earth Engine now, and WeatherNext 2 ensemble spread once access is approved.

## Still to verify (needs credentials)

1. Earth Engine: project registration and quota; S1 / VNP46A2 / S2 reductions over Puri run in reasonable time; `getThumbURL` evidence tiles.
2. `gemini-3.7-flash` on Vertex AI: which region/global endpoint; structured output on a satellite tile plus a bulletin PDF.
3. Cloud Text-to-Speech: call `voices.list` to confirm or-IN (Odia), te-IN, bn-IN, hi-IN. If Odia is missing, fall back to Odia text plus Hindi/English audio, or look for a Chirp 3 HD voice.
4. IMD bulletin retrieval from an Indian network, or through ReliefWeb.

## Setup status

- Done (26 Sep):
  - Created GCP project **`argmax-cyclone-2026`** ("Argmax Cyclone", number 489356738785) on billing account "My Billing Account 1".
  - Enabled APIs: Earth Engine, Vertex AI, Generative Language, Text-to-Speech, Translate, Speech, Cloud Run, Cloud Build, Artifact Registry, Secret Manager, Maps and Geocoding, Firestore, BigQuery, Storage.
  - `gcloud auth login` and Application Default Credentials login, as tsathya98@gmail.com.
- `earthengine authenticate` shows "This app is blocked" (Google blocks the EE default OAuth client). **Skip it**: use ADC with the EE scope instead (below).
- Pending (user):
  - Register the project for Earth Engine non-commercial use:
    - Answer **"Unpaid usage"** in the questionnaire. The Limited / Basic / Professional / Premium page is the *commercial* flow (from usage fees up to $2,000/month).
    - Then pick the **Contributor** tier: 1,000 EECU-hours/month, which needs an active billing account but has no EE charge. The default Community tier gives 150 EECU-hours/month. Partner (100k EECU-hours) needs an application, takes weeks, and is for nonprofits, universities and government.
    - Exhausting the quota puts the project in restricted mode, not a hard stop.
  - ~~Re-run ADC login with the EE scope~~. Not needed: the plain ADC login plus `set-quota-project argmax-cyclone-2026` (done 26 Sep) works for Earth Engine.
  - Earth Engine registration: **done 26 Sep** (non-commercial, individual, Contributor tier).
  - Submit the **WeatherNext data request form**.
  - Share a Gemini API key (for development) and a Maps Platform browser key.
- On Windows, PowerShell's default Restricted execution policy blocks `gcloud.ps1` and `firebase.ps1`. Use `gcloud.cmd` / `firebase.cmd`, or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
