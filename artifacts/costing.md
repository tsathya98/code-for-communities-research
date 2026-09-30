# ShadowCast running costs (27 Sep 2026)

Prices come from Google's public pricing pages, read on 27 Sep 2026 (Vertex AI generative AI, Text-to-Speech, Cloud Run, Firestore, Cloud Storage, Google Maps Platform). Usage figures come from the live project `argmax-cyclone-2026`. Token counts per call are **estimates**, not measurements. Rupees are at about ₹88 per US$. The billing account is billed in INR at Google's SKU prices.

## What runs, and what it costs today

| Service | What we use | Free allowance | Our cost |
|---|---|---|---|
| Vertex AI, Gemini 3.8 Flash (global) | Duty analyst, advisory drafts, reading bulletin PDFs and satellite images, voice questions | None. Introductory price $0.75 in / $3.75 out per 1M tokens until 31 Dec 2026, then $1.50 / $7.50 | The only real cost: about 2–3 US cents per question |
| Gemini Live (`gemini-live-2.5-flash-native-audio`) | Live voice calls with the analyst | None. $3 per 1M audio tokens in, $12 per 1M audio tokens out; each turn re-bills the call so far | Roughly 3 to 5 US cents a minute of talk (estimate) |
| Gemini 2.5 Flash TTS | Advisory audio and spoken chat replies | None. $0.50 per 1M text tokens in, $10 per 1M audio tokens out (25 tokens per second of audio) | About 1.5 US cents per minute of audio |
| Cloud Run `shadowcast-geo` | 1 vCPU, 1 GiB, scales to zero, at most 3 instances | 180,000 vCPU-s, 360,000 GiB-s and 2M requests a month | ₹0 at demo and pilot traffic |
| Cloud Run job `shadowcast-archiver` | Four runs a day, about 20 s each | 240,000 vCPU-s a month for jobs | ₹0 (about 2,400 vCPU-s a month) |
| Cloud Scheduler | 1 job | 3 jobs per billing account | ₹0 |
| Firestore (default database) | Audit log and cached Gemini readings | 1 GiB, 50,000 reads and 20,000 writes a day | ₹0 |
| Cloud Storage (asia-south1) | 49 MB of scenarios, 47 MB of archive, growing about 30 MB a day | Mumbai has no free tier; about $0.02 per GB-month | Under ₹5 a month; about ₹30 a month after a year of archiving |
| Artifact Registry | 422 MB of container images | 0.5 GB | ₹0 for now; $0.10 per GB-month beyond that |
| Earth Engine | Build time only: scenarios, evidence images. Nothing at request time | Non-commercial registration | ₹0 |
| Google Maps JavaScript API | Dynamic Maps loads | 10,000 loads a month, then $7 per 1,000 | ₹0 unless public traffic |
| Vercel | Next.js console and Gemini routes | Hobby plan free (non-commercial) | ₹0; Pro is $20 per seat per month |

Budget `shadowcast-monthly` is ₹2,000 (raised from ₹1,000 on 30 Sep 2026), with alerts at 50, 90 and 100% plus a forecast alert. Actual spend to date is in the Cloud console under **Billing › Reports**; billing export to BigQuery is not set up, so it can't be read from the CLI.

## Estimated Gemini cost per action

| Action | Tokens (estimated) | Cost now | From 1 Jan 2027 |
|---|---|---|---|
| Duty-analyst question (about 3 tool steps) | ~20k in, ~2k out | ~$0.023 | ~$0.045 |
| Advisory draft in three languages | ~25k in, ~4k out | ~$0.034 | ~$0.068 |
| Spoken question | Adds ~32 tokens per second of audio | Negligible | Negligible |
| Reading a bulletin PDF or before/after images | ~5k in, ~1k out, once per storm (cached in Firestore) | < $0.01 | < $0.02 |
| One minute of advisory audio | 1,500 audio tokens | $0.015 | $0.015 |

## Scenarios

| Scenario | Assumptions | Monthly cost |
|---|---|---|
| Judging (Oct 2026) | ~50 judges: 250 questions, 50 drafts, 50 minutes of audio | ~$8 ≈ ₹700, inside the ₹1,000 budget |
| Pilot, one cyclone season in Odisha | 30 district officers: 1,000 questions, 200 drafts, 600 minutes of audio, ~9,000 map loads; Vercel Pro | ~$60 ≈ ₹5,300 now; ~$100 ≈ ₹8,800 at 2027 Gemini prices |
| Three states (Odisha, Andhra, West Bengal) | 3× the pilot, and map loads pass the free 10,000 | ~$200–300 ≈ ₹18,000–26,000 |

## Levers if costs rise

- Gemini context caching: cached input is billed at a tenth of the price ($0.075 per 1M), and the system prompt repeats on every step.
- Route simple lookups to Gemini Flash-Lite ($0.25–0.30 in per 1M).
- Readings are already cached in Firestore, so a bulletin or image is read once per storm, not per user.
- Add a lifecycle rule moving archive objects older than 90 days to Coldline, and a cleanup policy on Artifact Registry images.
- Keep the console officer-facing: public traffic is what would make the Maps bill grow.
- Operational use by a state agency may need Earth Engine's commercial tier; confirm with Google before a pilot.
