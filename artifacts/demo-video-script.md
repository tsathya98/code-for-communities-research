# ShadowCast demo video script (Team Argmax)

**Target length:** 4:25. The rules allow 3–5 minutes, and the video must show the working deployment, not only slides.
**Narration:** about 630 words at roughly 140 words a minute.
**Record at:** https://shadowcast-two.vercel.app, full screen at 1920×1080.
**Slides used:** the ShadowCast pitch deck, for the cover, the solution slide and the closing architecture.

Before recording:
- Open the site once so the Cloud Run geo service is warm.
- Rehearse the Gemini calls. Vertex AI can take a few seconds to answer, so cut the waits in editing rather than talking over them.
- On Windows 11, Snipping Tool records the screen (Win+Shift+R). Record the narration separately if the room is noisy.

---

## 0:00–0:20 · Cold open

**Show:** black, then fade into the console at Fani's landfall: full map, pulsing eye, alert cards.

**Say:**
> In May 2019, Cyclone Fani hit Puri. Odisha evacuated 1.2 million people in time, and that was a triumph. But eleven days later, Puri district still had no power: hospitals, water works, shelters. The warnings said where the storm would go. Nobody said what it would break.

## 0:20–0:40 · The solution

**Show:** deck slide 1 (cover) for about 3 s, then slide 4 (the solution) for about 12 s, then back to the console.

**Say:**
> I'm Sathya, and this is Team Argmax. ShadowCast tells a district officer which hospitals, shelters and substations a cyclone will knock out, and when, up to sixty-eight hours ahead. It learns from real outages seen by satellite, drafts the alert with Gemini, and checks itself after every storm.

## 0:40–1:50 · Brief, Predict and Prioritise

**Show:**
1. Storm select: **Fani 2019 · Odisha coast**. The replay strip is on **Best track**, and the side panel opens on **Brief**.
2. Drag the timeline to 2 May, 13:00 IST (T−20 h). Hold on the Brief: the summary, the three tiles, then the first action card (**District administration · in 3 h**).
3. Press **Play**. Let the alert cards stack up and the action deadlines turn to "Gales … ago". Pause at **Landfall**.
4. Click the **District administration** action. It opens **Mot shelter (Bramhagiri)** with its reasons.

**Say:**
> This is the Odisha coast: 3,325 real sites. I'm replaying Fani from twenty hours out, and the console opens on the duty brief.
>
> Fani is twenty hours from landfall, and 917 sites are likely to lose power. Every agency gets its action with a deadline: the moment gales reach its first site, because after that, crews and generators can't move safely. District administration has three hours to open and stock 254 shelters and schools. Health has three hours to get back-up generators to 515 sites.
>
> *(press Play)* As the storm closes in, alerts fire: gales now at these shelters, hurricane-force winds reaching this hospital in one hour. Each dot's colour is its chance of losing power, from a model fitted on where the lights actually went out.
>
> *(click the action)* And every item drills down. Mot shelter: modelled peak wind 126 knots, the storm passing nine kilometres away, gales sixteen hours before landfall, eight thousand people nearby.

## 1:50–2:55 · Prepare

**Show:**
1. With Mot shelter selected, open the **Prepare** tab and click the suggestion **"Why is Mot shelter (Bramhagiri) ranked #1?"**. Let the answer stream.
2. Click **"Draft an advisory for the five highest-priority assets in English, Hindi and Odia"**.
3. On the advisory card, flip the language tabs: English → Hindi → Odia.
4. Click **Approve and issue**. Show the line "Approved and issued … logged in the audit trail".
5. Click **Listen in Odia** and let about 4 s of audio play.

**Say:**
> Now, Prepare. This is a Gemini 3.8 Flash agent on Vertex AI. It doesn't guess. It calls our geo service as a tool and explains the rank from the actual numbers.
>
> *(click draft)* I ask for an advisory for the five highest-priority sites. Gemini drafts a Common Alerting Protocol message, the format India's SACHET system already uses, in English, Hindi and Odia.
>
> Nothing goes out on its own. The tool is gated: I, the officer, approve or reject, and the approval is signed on the server.
>
> *(approve)* Approved. It's written to an append-only audit log in Firestore, and Gemini's text-to-speech reads it in Odia for radio and phone broadcasts.
>
> *(let the audio play)*

## 2:55–3:35 · Prove

**Show:**
1. Open the **Prove** tab on Fani: the AUC tile and the night-light loss by wind band chart.
2. Storm select **Hudhud 2014**, then Prove.
3. Storm select **Amphan 2020**, then Prove.

**Say:**
> Here's the part most tools skip: was it right? After landfall, NASA's night-light satellite shows which substations went dark.
>
> On Fani, substations above a hundred knots lost a median seventy-seven percent of their light. Below eighty knots, almost none. Hide parts of the coast and refit, and it still scores 0.97.
>
> *(Hudhud)* On Hudhud, a storm in Andhra the model never saw, it scores 0.79.
>
> *(Amphan)* On Amphan in Bengal it fails, at 0.44, and we publish that. That's what Prove is for: it tells an officer to recalibrate before trusting the model on a new grid.

## 3:35–4:00 · Real forecasts

**Show:**
1. Storm select **Dana 2024**. On the replay strip, click **T−68h**: the ensemble tracks fan out.
2. Step through to **T−20h** and watch them tighten.

**Say:**
> And it works with real forecasts. This is Cyclone Dana with ECMWF's ensemble, exactly as it was issued, sixty-eight hours before landfall. Instead of one line, every site gets the share of forecast tracks that bring it gales. As the issue times advance, you watch the uncertainty tighten.

## 4:00–4:25 · Architecture and close

**Show:** deck slide 10 (architecture), then slide 12 (the ask), and end on the live URL.

**Say:**
> It's all live. The console runs on Vercel. Gemini, the voice and the audit log run on Google Cloud, and the geo service runs on Cloud Run with Earth Engine. There are no stored keys anywhere. Three coasts and three languages are already built.
>
> Our ask: one cyclone season running alongside OSDMA.
>
> ShadowCast: know what the storm will break, before it breaks.

---

## Facts behind every line

| Line | Source |
|---|---|
| 1.2 million evacuated | NBC News, 3 May 2019 |
| Puri district without power 11 days later | Business Standard (PTI), 14 May 2019 |
| 3,325 sites; Mot shelter: 126 kt, 9 km, gales +16 h, about 8,219 people | Live geo API, `fani-2019` |
| 917 sites likely to lose power; district administration 254 sites due in 3 h; health 515 sites due in 3 h | The live Brief at 2 May 13:00 IST, `fani-2019` best track |
| 77% median light loss above 100 kt; about 0 below 80 kt | `fani-2019` `loss_by_band` |
| AUC 0.97 in sample and in the spatial holdout; Hudhud 0.79; Amphan 0.44 | [validation-results.md](validation-results.md) |
| Dana ensemble 68 → 20 h, 36–52 members | `dana-2024` forecasts (ECMWF open data) |
