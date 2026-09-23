# Website and public API verification

**Inspected:** 22 September 2026 (Asia/Kolkata)  
**Rendered page:** `https://hack2skill.com/event/codeforcommunities2`  
**Public JSON endpoint:** `https://hack2skill.com/api/v1/event/codeforcommunities2/event-details`

## Browser inspection performed

I opened the landing page in a live browser, dismissed only the cookie notice, and inspected every page section. The page has 11 section-navigation controls:

1. Overview
2. Why participate
3. Who can participate
4. Problem statements
5. What to build & what to submit
6. Timeline
7. In-person demo day
8. Mentorship & support
9. Attend a GDG
10. Rules & Guidelines
11. FAQs

I also opened each of the five problem-statement accordions and all eight FAQ accordions. Full-page and section screenshots were captured during the browser session (overview/full page; tracks 2–5; submission requirements; timeline; FAQ). The source browser tool exposes screenshots inline to the session but not as writable local files; the API snapshot and all facts used below are persisted here.

## API-to-rendered-page comparison

| Item | Rendered page | Public API | Result |
|---|---|---|---|
| Event title | “Build with AI: Code for Communities — Second Edition” | Same | Match |
| Mode / cost / team size | Hybrid; Free; 1–4 | `HYBRID`; `FREE`; min 1, max 4 | Match |
| Registration window | 11 Aug–30 Sep 2026; registration card says Wed 30 Sep | `2026-08-11T09:09:00Z` to `2026-09-30T18:29:00Z` | Match; API gives the precise close instant (23:59 IST) |
| Submission window | Page timeline says 10 Aug–30 Sep | API says 11 Aug–30 Sep | **Conflict** — treat 30 Sep as the deadline; obtain organizer clarification on whether work could begin on 10 or 11 Aug. |
| Five tracks | All present, rendered as accordions | Same HTML content carried in the public API's “Problem statements” section | Match |
| Requirements, tools, scoring | All visible | Same custom HTML in “What to build & what to submit” | Match |
| Timeline / demo days / FAQs | Visible | Same custom HTML in sections 15–20 | Match |
| Contact email | `build-with-ai-india@googlegroups.com` | Same | Match |

### Publicly exposed but hidden metadata

The API marks the following fields as hidden for the normal page, yet returns them publicly:

- `impressions`: **128,715**
- `registrations`: **14,531**
- configured age range: **16–65**
- CMS flags, internal object identifiers, markup, and event-section ordering.

These are not required for an entry. They are useful only as a rough competition signal: this is a high-volume contest, so a thin dashboard or chat wrapper will not stand out.

## Important wording correction

The user-supplied initial brief calls tracks 1–4 “BRICS” and describes BRICS-wide systems. The official page instead frames the primary deployment as **India**: Indian cities, states, PHCs, and communities. The rules add that entries should have **cross-border applicability** and be scalable to other BRICS nations. Build and pitch an India-first pilot with portable interfaces/data contracts; do not claim access to BRICS government data.

## Items still unconfirmed on the official page

- Exact submission-form fields and whether a link to the GitHub repository must be public or merely access-granted.
- Whether Google AI Studio / Vertex credits are available to every registrant or only top teams. The page says organizers should confirm this; the FAQ only promises credits to top teams.
- In-person demo-day date and venue (both are explicitly TBA).
- City-wise GDG workshop schedule (the page says it will be published later).
- The 10-August versus 11-August submission-start discrepancy noted above.

Use `build-with-ai-india@googlegroups.com` for the deadline/credit/submission questions; do not assume an answer from the marketing page.

