# Deep research: all five tracks (26 Sep 2026)

Five parallel research passes, one per track, used the same rubric: data realism (endpoints probed, not just named), existing systems, competition, innovation gap, Google-stack fit and risks. A GitHub crowding scan and a check of the **first edition's** tracks and winners were added. **Verdict: Track 5 stays the pick.**

## Headline findings

1. **Tracks 1–4 are re-runs of the first edition (June 2026), and each already has a winner** ([Technosports](https://technosports.co.in/googles-code-for-communities-turns-7000/), [GDG](https://gdg.community.dev/events/details/google-gdg-bangalore-presents-build-with-ai-code-for-communities/)):

   | Track | First-edition winner (what they built) |
   |---|---|
   | 1 Governance | Tech Jays — *Praja Svaram*, voice/WhatsApp grievance filing |
   | 2 Clean Air | Code_smashers — Delhi-NCR pollution hotspot tracker (sensor + satellite + citizen) |
   | 3 Health | Noida Boys — *HealthGrid AI*, rural health-resource tracking |
   | 4 Agri | Vishwakarma Devs — *KisanVaani*, toll-free crop advisory |
   | **5 Cyclone** | **New in this edition. No precedent winner** |

2. **The government already ships the obvious version of Tracks 1, 2 and 4:**
   - Track 1: Samadhan Didi (DARPG + Bhashini voice bot in 22 languages, May 2026), IGMS 2.0 (IIT Kanpur) and Andhra Pradesh's Mana Mitra on WhatsApp.
   - Track 2: CPCB SAMEER and Green Delhi (84k+ complaints a year), plus Google's own Air View+.
   - Track 4: Bharat-VISTAAR (Feb 2026), NPSS pest ID and MahaVISTAAR-AI.

3. **Same-edition GitHub crowding.** These are lower bounds, since private repos are invisible:
   - Track 3 has about 15 public repos that implement the challenge text almost word for word, including federated learning, IDSP-aware forecasting and OCR.
   - Tracks 1 and 4 have dozens.
   - Track 5 has about 5–7: AeroRelief AI (live on Vercel; Puri, parametric trigger, Odia CAP, SAR; figures look synthetic), CycloneShield AI (live; Jelesnianski surge, Open-Meteo), cyclone-data (HAND flood model calibrated on Hudhud), SagarShield-AI, CopperNick-Vision, and odisha-cyclone-risk (offline CLIMADA cat model).
   - **No Track 5 entry does a per-asset outage backtest against satellite ground truth.**

## Scorecard (1–10, from the per-track research)

| Track | Wow | Innovation | Data realism | Solo feasibility | India reach | Impact | What must be synthetic |
|---|---|---|---|---|---|---|---|
| 1 Governance | 6 | 5 (7 with a demand-vs-investment gap engine) | 5 | 6 | 8 | 7 | **Citizen requests** (no public text or location at national scale) |
| 2 Clean Air | 8 | 6 (the base idea already won edition 1) | 8 | 6 | 8 | 7 | Citizen photos, low-cost sensor feeds |
| 3 Health | 5 | 4 | 5 | 7 | 7 | 8 | **All facility stock, beds and attendance** (DVDMS/HMIS facility data is govt-login) |
| 4 Agri | 6 | 5 (7 with the SHC natural-farming engine) | 8 | 6 | 9 | 6 | Farmer identity (AgriStack gated); disease data is proxy |
| **5 Cyclone** | **7–9** | **6–8** (verified loop) | **8** | 6 | 6 | 7 | **Nothing essential**; surge and non-Odisha shelters are proxies |

Track 5's wow score is 7 in its own agent's view and 9 in ours. The difference is the demo: satellite before/after, whole districts going dark, a live storm if one forms, and a backtest reveal.

## Track 5 data realism: confirmed

| Layer | Status | Source (confirmed = probed on 26 Sep) |
|---|---|---|
| Best tracks + wind radii | REAL, confirmed | IBTrACS NI (to 24 Sep 2026) |
| Forecast tracks / cones | REAL, confirmed | **GDACS API** (no login; GeoJSON tracks, forecast points, wind buffers; archive incl. Fani event 1000561, Montha 1001232); **ECMWF open data** track BUFR (CC-BY; **files kept only ~4 days, so archive them now**) |
| AI ensemble forecast | REAL, confirmed | **WeatherNext 2 via Open-Meteo** (`google_weathernext2_ensemble`, 64 members, free, no request form); Weather Lab cyclone-track CSV/ATCF (CC-BY, ~2023+); WeatherNext Cyclones open-sourced 6 Aug 2026 (Apache-2.0). The EE copy is still gated |
| Official Indian warnings | REAL, confirmed | **NDMA SACHET CAP 1.2 RSS**, per state (e.g. `rss_odisha.xml`), with Odia/Telugu blocks and alert polygons. IMD API is IP-whitelisted |
| Rainfall | REAL, confirmed | GPM IMERG V07 (EE, to 25 Sep 2026); GFS/ECMWF IFS in EE |
| Storm surge | **PROXY** | Physics estimate on **DeltaDTM** (CC-BY, 30 m, in the EE community catalog), cross-checked with GDACS/JRC Delft3D surge maps (images only); INCOIS advisories aren't machine-readable |
| Infrastructure | REAL, confirmed | OSM substations and power lines (264 substations Ganjam–Balasore; 327 in north-coastal AP), hospitals and health centres, roads |
| Cyclone shelters | REAL (Odisha) / PROXY elsewhere | OSDMA embedded JSON (177 Puri; all districts). WB list has no GPS; AP/TN are behind closed portals; OSM has only 18 named shelters |
| Population / buildings | REAL | WorldPop, GHSL, Open Buildings 2.5D Temporal (EE) |
| Ground truth | REAL, confirmed | VIIRS VNP46A2 night lights (our backtest); Sentinel-1; Copernicus GFM flood maps; HDX Amphan flood extents; International Charter activations (Fani 608, Montha 998) |
| Voice | REAL | Gemini-TTS lists **Odia (or-IN) as Preview**, which matches our 9.1 s test. Classic Cloud TTS has no Odia |

**Season:** no named cyclone yet in 2026 (the next name is *Arnab*). Deep Depression BOB 06 / TC ONE-26 crossed near Kalingapatnam on 23 Sep. GDACS shows an Orange/Red cyclone hitting India in Oct–Dec in most years since 2019 (Bulbul, Nivar, Sitrang, Michaung, Dana, Montha, Ditwah), so a live storm during judging is likely but not guaranteed.

## Why Track 5 still wins

- **No first-edition precedent, and the least crowded field.**
- **The most real data of any track**, with no essential synthetic layer. Every other track has to fake its core operational data.
- **A verified differentiator already in hand:** across 263 substations, modelled wind correlates with observed light loss (Spearman 0.61). Above 100 kt the median loss is 82 %; at ≤80 kt it is about 0 %. No competitor proves its model.
- **Plugs into national rails:** outputs are SACHET-compatible CAP 1.2 advisories, the format NDMA already uses.

**Positioning:** *"The only cyclone forecaster that proves itself."*
- Forecast per named asset (WeatherNext 2 + ECMWF ensembles).
- Backtest with honest error bars (Fani, then Montha/Dana).
- Verify automatically after landfall (night lights + Sentinel-1/GFM).
- Emit CAP advisories with Odia voice.
- **No invented ₹ figures or bus counts.** That is the weakness in competitor entries.

## Actions this implies

1. **Start archiving now**: ECMWF track BUFR, GDACS events and SACHET CAP feeds, so an October/November storm can be demoed live.
2. Use Open-Meteo WeatherNext 2 immediately; keep the EE WeatherNext request as optional.
3. Surge = DeltaDTM physics proxy, labelled as a proxy.
4. Keep IMD/SACHET as the authority. We draft advisories; officers approve.

## Per-track notes (for reference)

- **Track 1:** only defensible as a demand-vs-investment *gap engine* (PMGSY GeoSadak, JJM, UDISE+, NFHS-5, MPLADS/GPDP). Intake is solved by Samadhan Didi. WhatsApp bans open-ended AI assistants from 15 Jan 2026.
- **Track 2:** only defensible as a *verification-and-routing* layer (Gemini attribution → FIRMS/geostationary fires ±2 h/2 km + S5P anomaly + station/Google AQ + upwind check → Delhi agency). Stubble is ~4 % of Delhi PM2.5 on average, so pitch hidden local sources and the 4–6 pm fires polar satellites miss.
- **Track 3:** win only on evidence (EpiClim/IDSP back-tested demand + OR-Tools transfers + data-freshness risk). Facility stock must be synthetic.
- **Track 4:** the unauthenticated Soil Health Card GraphQL backend returns live district soil data and government natural-farming prescriptions, but the field is saturated and competes with government systems.
