# Source register

All web claims in `hackathon-intelligence.md` should be read alongside the official hackathon page and public event API. Accessed 22 September 2026.

| Source | Why it matters |
|---|---|
| [Hack2Skill event page](https://hack2skill.com/event/codeforcommunities2) | Primary source for all contest content, rules, FAQs, scoring, and dates. |
| [Public event-details API](https://hack2skill.com/api/v1/event/codeforcommunities2/event-details) | Raw event CMS content used to validate rendered content and exact registration/submission timestamps. |
| [Gemini 3.7 Flash model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash) | Confirms the exact model named in Track 5. Inputs: text, image, video, audio, PDF; supports structured outputs, function calling, code execution, caching, Maps grounding, and thinking. |
| [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog) | Confirms `gemini-3.7-flash` reached GA on 13 August 2026. |
| [Google Earth Engine overview](https://developers.google.com/earth-engine/guides) | Track 5's named geospatial analysis environment; appropriate for satellite-derived features and mapping rather than pretending it is a real-time forecast feed. |
| [CPCB air-quality portal](https://airquality.cpcb.gov.in/) | India baseline for station-level AQ data. The CPCB annual-report description says it publishes real-time AQI and pollutant subindices and exposes CAAQMS data publicly. |
| [CPCB report on CAAQMS / Sameer](https://cpcb.nic.in/openpdffile.php?id=UmVwb3J0RmlsZXMvMTczM18xNzQ0MDg4NjgzX21lZGlhcGhvdG8yMDM0Ny5wZGY%3D) | Supports a Track 2 prototype framing: public complaints can include photos and geocoordinates and be routed to an implementing agency. |
| [Soil Health Card API-integration guidelines](https://soilhealth.dac.gov.in/files/SHC_API_Integration_Guidelines.pdf) | Strongest named data/interop reference for Track 4; documents structured soil, plot, farmer, crop, test-result, and geospatial concepts. |
| [Soil Health Card: 12 parameters](https://support.soilhealth.dac.gov.in/kb/faq.php?id=38) | Specifies N, P, K, S, Zn, Fe, Cu, Mn, B plus pH, EC and organic carbon; useful for a realistic demo data model. |
| [IMD Regional Specialised Meteorological Centre, New Delhi](https://rsmcnewdelhi.imd.gov.in/) | Authoritative Indian tropical-cyclone warning context for Track 5. Use it as a source for warnings/tracks where available; do not fabricate a real-time feed. |
| [data.gov.in](https://www.data.gov.in/) | Government open-data catalogue referenced by the contest. A prototype should cite the exact dataset and license rather than claim generic “government data.” |

## Data-use rule of thumb

For a hackathon demo, use public, licensed data plus transparent synthetic records for the operational layer (complaints, inventory movements, PHC attendance). Label synthetic data clearly. Never collect Aadhaar, personal health records, or precise household data just to make the demo feel realistic.

