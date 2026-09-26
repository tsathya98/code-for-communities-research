# Architecture: Track 5 cyclone impact forecaster (v1, 26 Sep 2026)

> *"A post-mortem, written 48 hours before the storm."* Impact-based forecasting per named asset, which then **proves itself** against satellite ground truth.
> Principle: **solution first**. Build the golden demo path end to end, then optimise.

## 1. What the product does (Predict → Prioritise → Prepare → Prove)

| Step | User sees | Computed by |
|---|---|---|
| **Predict** | Storm track and forecast cone, a wind/rain/surge hazard field over the district, and a timeline scrubber (T-72 h → landfall → T+7 d) | Geo service: Holland wind field, WeatherNext 2 / ECMWF / GFS rain, DeltaDTM surge proxy |
| **Prioritise** | Ranked at-risk assets (substations, hospitals, shelters, roads), each with a reason and a calibrated probability, e.g. *"Puri 132 kV: 117 kt modelled; P(outage) 0.86, from the Fani backtest"* | Deterministic score in the geo service; Gemini explains, never scores |
| **Prepare** | Typed action cards (pre-position DG sets, open/stock shelter, stage line crews, close road) plus a draft **CAP 1.2** advisory in Odia/Telugu/Hindi/English, with audio. **An officer approves before dispatch** | Agent (AI SDK `ToolLoopAgent`, `toolApproval: 'user-approval'`), Gemini structured output, Gemini-TTS |
| **Prove** | Backtest panel (predicted vs observed outage, Spearman, loss-by-wind-band chart), and after landfall an automatic verification of observed blackouts (VIIRS) and floods (Sentinel-1/GFM) per asset, with a hit/miss scorecard | Geo service (Earth Engine) plus a Gemini evidence reader that receives the deterministic metrics |

**Modes:** `Replay` (Fani 2019 first, then Montha 2025 and Dana 2024), `Live` (current GDACS/SACHET/WeatherNext system), `Backtest`.

## 2. System diagram

```
                         ┌──────────────────────────── Vercel ────────────────────────────┐
  Officer (browser) ───▶ │ Next.js (App Router) operations console                          │
                         │  • Google Maps JS + deck.gl overlay (assets, cone, EE tiles)     │
                         │  • Timeline scrubber · P/P/P/P panels · agent chat (useChat)     │
                         │ Route handlers                                                   │
                         │  • /api/agent  → ToolLoopAgent (gemini-3.8-flash, Vertex global) │
                         │      tools: getScenario · rankAssets · getEvidence · runBacktest │
                         │             verifyPostEvent · draftAdvisory · dispatchAdvisory*  │
                         │      *toolApproval: 'user-approval'  (the human gate)            │
                         │  • /api/geo/*  → thin proxy to the Cloud Run geo service         │
                         └───────────────┬──────────────────────────────┬──────────────────┘
                     Vercel OIDC → GCP Workload Identity Federation (no keys)
                                         │                              │
┌──────────────────────── Google Cloud (argmax-cyclone-2026) ───────────▼──────────────────┐
│ Vertex AI (global): gemini-3.8-flash (agent, bulletin/CAP parsing, evidence reading,      │
│                     advisory drafting) · gemini-2.5-flash-tts (Odia/Telugu/Hindi audio)   │
│                                                                                            │
│ Cloud Run: geo-service (Python/FastAPI) ─── Earth Engine (VIIRS, S1, IMERG, GFS, DeltaDTM,│
│   /scenarios /hazard /rank /evidence       WorldPop, Open Buildings) · getMapId tiles      │
│   /backtest /verify /tiles                                                                  │
│                                                                                            │
│ Cloud Run Job: feed-archiver (every 6 h, Cloud Scheduler) — LIVE since 26 Sep              │
│   GDACS events · NDMA SACHET CAP alerts · WeatherNext 2 ensemble snapshot (Open-Meteo) ·   │
│   IBTrACS active  (ECMWF tracks: full history already on gs://ecmwf-open-data)             │
│                                                                                            │
│ Cloud Storage: scenario artifacts (tracks, hazard grids, asset tables, backtests), archive │
│ Firestore: advisories, approvals, audit log (append-only), action states                   │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```

## 3. Components

### Web app (Vercel): `apps/web`
- **Next.js App Router, TypeScript, Tailwind/shadcn.**
- **Map:** `@vis.gl/react-google-maps` plus a deck.gl `GoogleMapsOverlay`. Layers: storm track and cone, asset points coloured by probability, the hazard raster as Earth Engine XYZ tiles, and before/after satellite tiles.
- **Agent:** AI SDK 7 `ToolLoopAgent` on `@ai-sdk/google-vertex`, with `location: 'global'` and model `gemini-3.8-flash` (verified end to end on 26 Sep). The client uses `useChat` with `InferAgentUIMessage` typed tool parts, rendered as generative-UI cards (asset card, action card, advisory preview, backtest chart).
- **Human gate:** `dispatchAdvisory` and state-changing action tools use `toolApproval: 'user-approval'`. The approval request renders as an approve/edit/reject card. Every decision is written to the Firestore audit log.

### Geo service (Cloud Run): `services/geo`
FastAPI, grown directly from `spikes/fani_exposure.py` and `spikes/gee_gemini_check.py`.

| Endpoint | Returns |
|---|---|
| `GET /scenarios` | Available storms (replay + live) with issue times |
| `GET /scenarios/{id}/track?issued=` | Forecast track/cone **as issued at that time**, not hindsight (GDACS/ECMWF/Weather Lab; best track only for Prove) |
| `GET /hazard/{id}` | Per-asset peak wind, rain accumulation, surge proxy, arrival time; hazard tile URLs |
| `GET /rank/{id}?region=` | Ranked assets: score, P(outage), reasons[], evidence refs, stable `subject_key` |
| `GET /evidence/{asset}` | Wind timeline, elevation, population served, historical analogue, tile URLs |
| `GET /backtest/{storm}` | Spearman, loss by wind band, calibration curve, per-asset table |
| `POST /verify/{storm}` | Post-event observed NTL loss and S1 flood fraction per asset, plus a hit/miss matrix |

**Deterministic scoring (v1):**
- `P(outage)` is a logistic fit of wind → NTL-loss > 50 %, trained on Fani and to be validated on Montha/Dana.
- Asset score = P(impact) × criticality weight (hospital > substation > shelter > school) × population served (WorldPop in a buffer).
- Every output carries a model version and data timestamps.

### Feed archiver (Cloud Run Job + Scheduler): `services/archiver` — **live since 26 Sep 2026**
- Snapshots the feeds that have no public history, so a live storm can later be replayed as-issued: GDACS, NDMA SACHET CAP, WeatherNext 2 (Open-Meteo serves only the latest run) and IBTrACS active.
- ECMWF ensemble cyclone tracks are **not** archived. ECMWF's Google Cloud mirror `gs://ecmwf-open-data` keeps full history (e.g. Montha 27 Oct 2025, Dana 23 Oct 2024), which enables as-issued replays of past storms.
- Writes `gs://argmax-cyclone-2026-archive/{source}/{YYYY}/{MM}/{DD}/{HHMM}Z/…` plus a per-run manifest.

### Gemini's roles (it does real work, never the arithmetic)

1. **Parse official inputs:** SACHET CAP XML and IMD/GDACS bulletins or forecast-track images become a structured track and warnings.
2. **Read evidence:** SAR/optical/night-light tiles, *plus* deterministic metrics (coverage %, flood-mask area) passed in the prompt, become a structured evidence record with caveats.
3. **Draft advisories:** ranked assets plus the district become a CAP 1.2 `info` block per language (en/or/te/hi), audience-specific, cited to evidence.
4. **Run the operator agent:** answers "why is this hospital red?" by calling tools, and drafts action plans.
5. **Speak:** Gemini-TTS produces Odia, Telugu and Hindi audio for approved advisories.

## 4. Data (all verified; see `track5-feasibility-spike.md` and `deep-research-tracks.md`)

| Layer | Source |
|---|---|
| Tracks | IBTrACS (best track, backtest); GDACS API and ECMWF open data (as-issued forecasts); Weather Lab CSV (WeatherNext cyclone tracks) |
| Hazard | WeatherNext 2 ensemble via Open-Meteo (64 members); GPM IMERG; GFS/ECMWF IFS in EE; DeltaDTM surge proxy |
| Exposure | OSM (substations, lines, hospitals, health centres, schools, roads); OSDMA shelters (Odisha, all districts); WorldPop; Open Buildings |
| Truth | VIIRS VNP46A2 (raw band, quality-masked); Sentinel-1; Copernicus GFM; International Charter / HDX extents |
| Official alerts | NDMA SACHET CAP 1.2 RSS (read, and match the output format) |

**Pilot:** Odisha coast (Ganjam–Balasore) for Fani. North Andhra for Montha as the second scenario. The schema is state-agnostic.

## 5. Repository layout (new public product repo)

```
apps/web/            Next.js console + AI SDK agent (Vercel)
services/geo/        FastAPI geo service (Cloud Run, uv)
services/archiver/   feed archiver job (Cloud Run Job, uv)
data/                small committed seeds (scenario manifests); large artifacts in GCS
infra/               gcloud scripts: WIF, Run, Scheduler, bucket, Firestore
docs/                architecture, data dictionary, prompts/schemas, licences
```

This uses plain pnpm plus uv workspaces. Nx can wrap it later if it earns its keep; solution first.

## 6. Security and privacy
- **Auth between the two clouds:** Vercel OIDC tokens are exchanged via GCP Workload Identity Federation for a least-privilege service account (Vertex user, Run invoker, Firestore user). No JSON keys.
- **No personal data.** Only public infrastructure and aggregate population. Synthetic items, if any, are labelled.
- **IMD/SACHET remain the authority.** Our output is a *draft* advisory for official approval.

## 7. Build order (solution first)

| # | Milestone | Done when |
|---|---|---|
| M0 | Feed archiver live ✅ | Done 26 Sep: 4/4 sources archived; every 6 h |
| M1 | Geo service v0 ✅ | Done 26 Sep: live on Cloud Run; Fani and Dana scenarios; 3,325 assets ranked with P(outage) and reasons. Fani AUC 0.97 after the 15-minute track densification (eyewall fix). Next: ECMWF ensemble as issued (probabilistic), Amphan held-out test |
| M2 | Console v0 | Map + timeline + ranked list on Vercel (Predict/Prioritise) |
| M3 | Agent + Prepare | Advisory drafted in CAP 1.2 (en/or), approve → Firestore audit → Odia audio |
| M4 | Prove | Backtest panel + post-event verification with SAR/NTL tiles and Gemini evidence |
| M5 | Live mode + polish | GDACS/SACHET live scenario, second storm (Montha), demo video, deck |

## 8. Demo video golden path (3–5 min)
1. **Cold open:** Fani, 3 May 2019, 1.2 M people evacuated, but Puri's grid dark for weeks.
2. **Replay at T-48 h:** the as-issued forecast arrives, and Gemini reads the bulletin.
3. **Predict → Prioritise:** the hazard field sweeps the coast; the ranked list names Puri substation, hospitals and shelters with reasons.
4. **Prepare:** the agent drafts actions and an Odia CAP advisory, the officer approves, audio plays, and the audit log updates.
5. **Prove:** scrub to T+2 d. Night lights go dark exactly where predicted; SAR shows floodwater. The backtest chart reveals *>100 kt → 82 % blackout; ≤80 kt → ~0 %*.
6. **Scale:** switch to Live and show the current Bay of Bengal system. Close with the architecture and the path from Odisha to every coastal state.
