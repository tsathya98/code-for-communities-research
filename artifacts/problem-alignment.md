# Track 5: problem statement vs what ShadowCast does (27 Sep 2026)

## Submission description (2–3 lines)

> ShadowCast turns a cyclone forecast into a named, timed list of the hospitals, shelters and substations that will lose power, up to 68 hours before landfall, with each agency's actions due before gales arrive. Its outage model is learned from NASA night-light satellite data and scored after every storm: AUC 0.97 on Fani and 0.79 on Hudhud, a storm it never saw. Gemini 3.8 Flash on Vertex AI explains the ranking and drafts CAP alerts in English, Hindi and the local language for an officer to approve. It is live on Google Cloud for three Indian coasts.

## The official statement (Hack2Skill event page)

- **Problem:** in the Bay of Bengal, move from post-landfall recovery to pre-landfall action: evacuation planning, infrastructure hardening and parametric-insurance liquidity.
- **Challenge:** an AI predictive risk and vulnerability platform using Google Earth Engine satellite feeds, real-time meteorological data and Gemini 3.7 Flash's multimodal reasoning. It should:
  - simulate storm surges;
  - predict local rainfall damage pathways;
  - map exposure for critical infrastructure (power grids, arterial roads, medical shelters);
  - automate early-warning advisory dispatch to local and disaster management authorities.

## Requirement-by-requirement

| Ask | Status | What we have |
|---|---|---|
| Pre-landfall action, not recovery | Strong | Brief with per-agency actions due before gales; replay from T−68 h |
| Infrastructure hardening | Strong | Per-site outage odds; power, health, water, shelters, police and fire |
| Evacuation planning | Partial | Shelters ranked and actions to open and stock them; the advisory tells people to move. No evacuation routing or capacity |
| Parametric-insurance liquidity | Missing | — |
| Earth Engine satellite feeds | Good | VIIRS night lights (ground truth), WorldPop and Copernicus DEM, used at build time rather than live |
| Real-time meteorological data | Partial | ECMWF ensemble as issued (replayed). The archiver has collected GDACS, SACHET, IBTrACS and Open-Meteo since 26 Sep, but there is no live mode in the UI |
| Gemini multimodal reasoning | Partial | Gemini 3.8 Flash with tool calling, text only; the multimodal part is unused. The brief names 3.7 Flash; 3.8 is its successor |
| Simulate storm surge | Missing | Wind only; site elevation is already computed but unused |
| Rainfall damage pathways | Missing | — |
| Critical infrastructure: power grids | Strong | Substations and power plants, with a calibrated outage model |
| Critical infrastructure: medical and shelters | Strong | Hospitals, health centres, clinics, cyclone shelters |
| Critical infrastructure: arterial roads | Missing | — |
| Advisory dispatch to authorities | Good | CAP 1.2 in three languages, officer approval, audit log, TTS audio. Nothing is sent, by design (exercise mode) |

## Cheapest ways to close the gaps (not started)

1. **Surge exposure proxy:** elevation plus distance to coast plus the storm's right-front quadrant, labelled as a proxy and not a hydrodynamic model. Half a day.
2. **Rainfall:** GPM IMERG accumulation per site from Earth Engine, then low-lying and heavy rain combined into a "flood pathway" flag. Half a day.
3. **Gemini multimodal:** Gemini reads the official IMD bulletin (PDF) or the before/after night-light tiles. Half a day.
4. **Parametric trigger:** a per-district payout trigger from modelled wind at insured sites, shown in Prove. A few hours.
5. **Arterial roads:** exposure of OSM trunk and primary roads. A day; lowest value per hour.
