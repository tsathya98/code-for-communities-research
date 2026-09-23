# Build with AI: Code for Communities — Second Edition

## Executive interpretation for Team Argmax

This is an India-first Google Cloud hackathon with five public-interest AI tracks. It rewards a credible path from a narrow pilot to cross-state/national deployment — not the impossible claim that a solo team has solved a national ministry's entire system.

Your winning narrative should be:

> A field decision arrives in a familiar form (voice, photo, a small form, a simulated operations feed). Google AI turns it into a structured, explainable risk or recommendation. A decision-maker sees the reason, urgency, and recommended action on a map/dashboard. The design can scale because its data schema, language layer, and service boundaries are state-agnostic.

## Official contest facts

| Topic | Confirmed detail |
|---|---|
| Event format | Hybrid |
| Eligibility | Developers, AI/ML practitioners, product thinkers, freelancers, students, professionals, startups across India |
| Team | 1–4 people; solo is explicitly allowed |
| Cost | Free |
| Registration deadline | 30 September 2026, with API timestamp 18:29 UTC / 23:59 IST |
| Prototype deadline | 30 September 2026; API timestamp is also 18:29 UTC / 23:59 IST |
| Prize pool | INR 10 lakh |
| Shortlist | Top 20 announced 16 October; virtual demo day 23 October |
| Mandatory technology | Google AI — generative AI, predictive modelling, or computer vision. No qualifying Google AI integration means the submission is not considered. |
| Geographic framing | India first; cross-border BRICS portability is a rule/design criterion, not permission to assume foreign data access. |

### Timeline

- 11 Aug: launch; registration/team formation open.
- 14 Aug: introductory/problem-explainer session.
- 30 Sep: registration and prototype submission close. (The visual timeline says submission began 10 Aug; API says 11 Aug.)
- 1–15 Oct: prototype evaluation.
- 16 Oct: Top 20 announced.
- 23 Oct: virtual demo day.
- In-person demo day: October, but date and venue are TBA.

## What actually has to be built and submitted

### Prototype requirements

1. A functioning end-to-end flow for the chosen track's core use case.
2. Meaningful Google AI integration.
3. Real or realistic data: public data, sample data, or APIs when a live feed is unavailable.
4. India-scale design, rather than a one-city-only toy.
5. Multilingual and/or voice support where the selected track calls for it.

### Submission package

1. Source code in a public or access-granted GitHub repository.
2. A **3–5 minute** working end-to-end demo video.
3. A **10–12 slide** pitch deck: problem, solution, AI approach, users, deployability, India-wide scale.
4. A 2–3 line solution description.
5. A live deployed prototype link.

### Scoring means what it says

| Weight | What judges need to see |
|---:|---|
| 25% AI / technical execution | Google AI changes an outcome; not merely a chatbot that narrates a dashboard. The demonstrated workflow really runs. |
| 20% Problem–solution fit | A focused user and decision. Avoid “one super-app for all civic issues.” |
| 20% India reach | Bounded pilot, portable schema, multiple-language/data-partition story, and clearly declared assumptions. |
| 20% Deployability / scalability | A ministry, district, or state could run a pilot within weeks. Include a human approval point, data minimisation, and rollout plan. |
| 15% Impact potential | A measurable operational outcome: fewer stock-outs, earlier alerts, better targeting, lower response time, lower input use, etc. |

## Non-negotiable design guardrails

- Build during the contest period; a pre-existing project needs a substantial extension.
- Keep code original or correctly license/cite reused components and datasets.
- Do not automate high-consequence allocation or alerts without a human review/override.
- Treat citizen reports as *signals*, not truth. Preserve confidence, corroboration, provenance, and an abuse path.
- Use synthetic or aggregated health/citizen data for the demo. Do not put personal health records, Aadhaar, or unconsented location traces into the product.
- Make recommendation logic inspectable: show source evidence, time range, confidence, limitations, and why the recommendation changed.

---

## Track 1 — AI for Digital Public Infrastructure & Governance

### The real job

Transform fragmented citizen requests arriving as voice, text, or messaging reports into a structured demand ledger. Combine that ledger with a small set of public demographic/infrastructure/investment indicators to identify a hotspot and rank candidate public works for a policymaker.

This is **not** “make a chatbot for complaints.” The hard and valuable steps are: multilingual intake, issue/geography extraction, deduplication, evidence-aware clustering, priority scoring, and an auditable recommendation.

### Minimum credible end-to-end demo

1. Resident sends Hindi/Tamil/English voice or text report: “the borewell has been dry for two weeks near X school.”
2. Speech/text pipeline transcribes, translates if needed, extracts issue, location, urgency, and evidence using Gemini structured output.
3. Similar reports cluster into a ward/block hotspot. The dashboard shows cluster evidence and confidence, not just a red dot.
4. The system joins aggregate context: population, service coverage, existing allocation/project status (public or clearly synthetic).
5. A transparent score ranks two or three candidate actions and provides an explanation: demand volume, vulnerable population proxy, service gap, cost/feasibility proxy, and uncertainty.
6. Officer reviews, edits/approves, and exports a short decision brief.

### Strong architecture

`voice/text -> STT + Translation -> Gemini extraction -> validation + PII redaction -> geocoding / admin-area resolution -> complaint/event store -> dedupe + clustering -> aggregate scoring -> officer dashboard -> human decision + audit trail`

Use a data contract such as `request_id, language, transcript, category, admin_unit, geocode_precision, urgency, evidence_refs, confidence, consent, created_at`. Keep names/phone numbers out of the analytics plane.

### Good data and AI choices

- Google Speech-to-Text / Translation for the voice-first requirement; Gemini 3.7 Flash for schema-constrained extraction, summarisation, and explanation.
- Maps/geocoding only at a privacy-appropriate admin-unit level.
- data.gov.in datasets for demo context; state an exact dataset and refresh date.
- Use deterministic weighted scoring for the final priority rank; use Gemini to extract/summarise, not to hide the policy decision.

### Failure modes judges will notice

- Ranking projects purely through an opaque LLM prompt.
- No multilingual demonstration.
- Calling raw complaint count “need” without dedupe or population normalisation.
- Showing citizens' precise addresses or personal details to every dashboard user.

### Solo feasibility

**High.** This is the strongest “agentic workflow + map + explainability” track for a solo full-stack builder. Limit the pilot to water/sanitation in 3–5 wards, but show a configurable taxonomy and partitioned data architecture.

---

## Track 2 — Clean Air & Climate Resilience

### The real job

Fuse observed signals into an incident triage and short-horizon forecasting workflow: citizen photo/sensor signal + station/satellite/weather context -> hotspot confidence -> projected air-quality risk -> authority-ready alert.

The word *federated* matters architecturally: cities/states may train/share model updates or standardised risk signals without pooling every raw photo or report. You do not need to implement production federated learning; define the boundary and simulate one model-update exchange.

### Minimum credible end-to-end demo

1. A resident uploads a geotagged smoke/industrial-emission photo or a low-cost sensor reading.
2. Gemini multimodal classifies the observation and returns structured evidence (`source_type`, `suspected_activity`, `confidence`, `safety_note`).
3. Join it with a nearby CPCB/AQI time series, wind/rain features, and a satellite/fire proxy.
4. Produce an incident card: confidence, area, likely dispersion direction, predicted PM2.5 risk band for the next 6–24h, affected corridor, and recommended verification/escalation.
5. Officer acknowledges or rejects; the dashboard records the outcome to improve thresholds.

### Data and implementation notes

- CPCB is a real public baseline for station AQI. The contest text asks for hyper-local gaps, so show why the citizen observation adds coverage rather than claiming to replace calibrated monitors.
- The CPCB/Sameer model is a useful precedent: public complaints can contain photos and automatically captured geocoordinates, then route to accountable agencies.
- Earth Engine can prepare historical/satellite-derived features; weather data can be a cached public response for the demo. Label forecast outputs as prototypes and uncertainty bands, not regulatory-grade measurements.
- A simple model (gradient boosting or calibrated rule baseline) can forecast a risk band; Gemini is compelling for vision evidence and officer-readable rationale.

### Failure modes

- Diagnosing emission sources as facts from a single image.
- Using a false-precision AQI number without a calibrated sensor/validated model.
- “Federated” only in the slide deck. At least isolate a city data plane, a shared model registry, and a cross-city schema.

### Solo feasibility

**Medium.** Pick one industrial corridor and one pollutant/risk category. Avoid building a satellite science platform from scratch. This becomes strong if the evidence fusion and alert workflow are exquisitely clear.

---

## Track 3 — Smart Health & Supply Chain Resilience

### The real job

Make PHC operations visible enough to forecast shortages and recommend safe reallocations. A dashboard alone is insufficient; show an operations loop from facility update to alert to approval to transfer receipt.

### Minimum credible end-to-end demo

1. Three to ten simulated PHCs send daily stock, consumption, patient-footfall, bed and attendance events.
2. System calculates days-of-stock remaining and forecasts demand for one essential medicine (for example ORS, antibiotics, insulin, or a fictional SKU).
3. It flags a credible stock-out risk with reason and confidence.
4. Optimiser suggests a cross-district transfer from facility B to facility A, constrained by buffer stock, expiry, travel time, and approval authority.
5. District officer accepts/modifies/rejects. Transfer lifecycle and audit log update the dashboard.

### Technical reasoning

- Separate operational facts from AI: inventory arithmetic and minimum stock rules must be deterministic.
- Use a basic demand model with seasonality/event features; back-test on generated but plausible historical data.
- Use Gemini for natural-language situation summaries, anomaly explanation, and structured extraction from a photographed stock register only if you can demonstrate validation.
- “Federated” should mean states keep patient/facility-level data local while sharing non-identifying model artifacts or aggregate demand features.

### Essential safety and ethics

- Do not use identifiable patient records. Footfall can be an aggregate count.
- Never recommend a transfer that drops the donor below its safety stock.
- Explain clinical/supply assumptions and require a responsible human approval.

### Solo feasibility

**High–medium.** It is very demoable with a polished simulated data stream and clear constraints. It risks looking generic unless you demonstrate the transfer lifecycle, expiry/buffer constraints, and a truly useful forecast.

---

## Track 4 — Agricultural Intelligence

### The real job

Give a smallholder a local, regenerative crop/input advisory plus a disease-diagnosis path, grounded in plot/soil/weather/satellite context. The challenge is to make advice actionable and safe, not to produce a fluent farming chat bot.

### Minimum credible end-to-end demo

1. Farmer chooses a language and gives/enters village, crop stage, plot size and soil data; optionally uploads a leaf photo.
2. System uses a crop-disease vision workflow to provide a **probabilistic** diagnosis, asks for disambiguating observations, and offers an escalation path rather than presenting medical certainty for plants.
3. It joins weather forecast, recent vegetation/soil proxy, and Soil Health Card fields.
4. Output is a short voice/text advisory: current risk, crop-specific regenerative action, fertiliser/input rationale, water/soil conservation practice, next review date, and confidence/limitations.
5. Agronomist/extension worker dashboard sees aggregated crop risks without exposing farmer data broadly.

### Data realism

- The Soil Health Card source is particularly valuable: it contains fields for plot/crop/location/test results and the programme tests 12 soil parameters. Use those schema concepts even with synthetic test records.
- Satellite features should be visible in the reasoning: NDVI-like trend, rainfall anomaly, crop calendar. Explain that they are support signals, not ground truth.
- Gemini 3.7 Flash accepts images and structured outputs, making it suitable for photo triage and multilingual explanation. A specialised/deterministic rule layer should guard agronomic dosage advice.

### Failure modes

- One image -> confident disease diagnosis -> pesticide instruction.
- Generic “use AI for crops” with no weather/soil/plot differentiation.
- Calling a conventional high-input prescription “regenerative.” Define regenerative metrics: organic carbon, input efficiency, residue cover, water retention, crop diversity, or reduced chemical overuse.

### Solo feasibility

**Medium–high.** Scope to one crop and one district season. This can be visually compelling, but source attribution and advice safeguards must be excellent.

---

## Track 5 — Track-Based Cyclone Impact & Infrastructure Vulnerability Forecaster

### The real job

Convert a cyclone forecast track and weather/satellite/geospatial layers into anticipatory local decisions: which assets and communities face risk, why, what should be verified/hardened/evacuated, and which agency receives which advisory.

The model name is real: Google lists `gemini-3.7-flash` as a stable native multimodal reasoning model. It supports text/image/video/audio/PDF input, structured outputs and function calling. Use it to read and contextualise evidence; do not present it as the physical storm-surge simulator.

### Minimum credible end-to-end demo

1. Operator loads a named historical/stub cyclone track or an official warning bulletin. Clearly label it **scenario mode** unless using a verified real-time official source.
2. Geospatial service derives a storm-buffer/exposure envelope and joins it to a small asset set: roads, power substations, shelters, health facilities, vulnerable villages.
3. A transparent risk formula combines hazard intensity/proximity, rainfall/surge proxy, asset criticality, accessibility, and population/vulnerability proxy.
4. Dashboard ranks actions: inspect substation, open/stock shelter, send evacuation-preparedness advisory, pre-position medical inventory. Clicking a recommendation shows the data and assumptions.
5. Gemini turns the structured incident record plus map/image evidence into a concise, multilingual authority alert; an authorised human approves dispatch in the demo.

### What “simulation” should mean in a hackathon

Do not claim a hydrodynamic storm-surge model unless you are actually running one with validated bathymetry, tide, wind and pressure inputs. A credible prototype is a **vulnerability scenario model**: track corridor + elevation/coastal exposure + rainfall proxy + critical infrastructure proximity + acknowledged uncertainty. State exactly which layer is a proxy.

### Data and tools

- Earth Engine: historical/satellite flood/land/water/vegetation features and map export.
- IMD/RSMC: authoritative warning/track context where a documented feed/bulletin is available.
- Google Maps or open geospatial data: asset and routing visualization. Use synthetic sensitive asset locations if necessary.
- Gemini 3.7 Flash: multimodal evidence extraction, structured advisory generation, and scenario-question answering. Use function-calling/tool boundaries for the actual risk calculation.

### Failure modes

- “Predicting a cyclone” from scratch rather than consuming official meteorological forecasts.
- Simulating surge without stating assumptions or calibration limits.
- Auto-sending emergency messages without human approval.
- Map theatre: red markers with no action priority or decision explanation.

### Solo feasibility

**High if scoped sharply.** A historical cyclone replay for one coastal district, ten assets, and three action types is ideal: visually impressive, technically rich, and demonstrably deployable. This is the recommended track if you enjoy geospatial work and can make the risk methodology honest.

---

## Choosing one track as a solo entrant

| If your strongest asset is… | Best track | Reason |
|---|---|---|
| Full-stack/product + language/agent workflow | Track 1 | Natural end-to-end AI proof, clear public-good story, manageable synthetic ops data. |
| Data/forecasting + operations research | Track 3 | Great opportunity to show an actual decision engine and safe constraints. |
| Mapping/geospatial + presentation | Track 5 | Strong visual demo and direct use of named GEE/Gemini components. |
| Vision + multilingual consumer UX | Track 4 | Powerful farmer journey, but needs careful agronomic safety claims. |
| Environmental data fusion | Track 2 | Differentiated but most vulnerable to unconvincing data/forecast claims. |

**My recommendation:** choose Track 5 if you can work with maps and are willing to use a historical cyclone replay; otherwise choose Track 1. Both let a solo team deliver a memorable end-to-end workflow without pretending to own an entire public system.

## A solo build plan that fits the scoring

### 1. Define the thin wedge (first)

Write a one-sentence decision: “For [named pilot geography], help [named officer/user] decide [one action] within [time horizon] using [three evidence sources].” If the sentence has multiple actions or nationwide coverage, shrink it.

### 2. Build the credible path, not the dashboard first

Implement the golden path in this order:

1. Evidence ingestion (one realistic event/input).
2. Google AI structured extraction/classification.
3. Deterministic/runnable model or score.
4. One ranked recommendation with explanation.
5. Human approval/override and audit result.
6. Dashboard/map around that path.

### 3. Make “India scale” visible

- Configuration-driven languages, taxonomy and state/administrative-unit partitions.
- A documented canonical event schema and OpenAPI/JSON schema.
- Queued/stateless services and separate raw vs aggregate/analytics stores.
- Feature/model version logged with every recommendation.
- Explicit pilot expansion plan: district -> state -> national federation.

### 4. Demo-video arc (3–5 minutes)

1. 0:00–0:25: a real operational decision and baseline pain.
2. 0:25–1:10: a citizen/facility/farmer/operator input in a local language or with an image.
3. 1:10–2:15: show Google AI turning input into a structured signal; display evidence/confidence.
4. 2:15–3:15: map/dashboard recommendation and transparent calculation.
5. 3:15–4:00: human approves/overrides and outcome/audit trail updates.
6. 4:00–4:40: architecture, data safety and district-to-nation scale story.

### 5. Deck structure (10–12 slides)

1. Name, one-line promise, chosen pilot.
2. User/decision and harm from the status quo.
3. Why current systems miss the signal.
4. Solution workflow.
5. Live-product screenshots.
6. Google AI role, inputs/outputs and model safety.
7. Data sources and what is synthetic.
8. Methodology/score/forecast validation or limitations.
9. Impact metrics and pilot success criteria.
10. Deployment architecture, governance and privacy.
11. India/BRICS scalability plan.
12. Pilot ask and roadmap.

## Pre-submission checklist

- [ ] The live link works in an incognito browser and has a graceful demo-data fallback.
- [ ] Google AI's input, output, and measurable contribution are visible in the product and deck.
- [ ] At least one local language/voice flow is demonstrated if Track 1; multilingual support is still a scoring-quality signal elsewhere.
- [ ] All datasets have a source/license note; synthetic data is clearly labelled.
- [ ] Recommendation contains confidence/evidence/assumptions and a human approval step.
- [ ] GitHub repository contains setup, architecture, data dictionary, model/AI prompts or schemas, licences, and a 2-minute local demo path.
- [ ] Video is 3–5 minutes and shows the working deployment, not only slides.
- [ ] Deck is 10–12 slides and includes a deployability plan.
- [ ] Submission description has a clear 2–3 line value proposition.
- [ ] You have asked organizers about credit eligibility and the one-day start-date discrepancy if it changes how you describe build timing.

