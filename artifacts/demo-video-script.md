# ShadowCast demo video script (Team Argmax)

**Target length:** 4:50. The rules allow 3–5 minutes, and the video must show the working deployment, not only slides.
**Narration:** about 680 words at roughly 140 words a minute.
**Record at:** https://shadowcast-two.vercel.app, full screen at 1920×1080.
**Slides used:** from the ShadowCast pitch deck: the cover, slide 4 (the solution, with the live Prioritise screen), slide 8 (validation, with Gemini's satellite reading), slide 10 (architecture) and slide 12 (the ask).

Before recording:
- Open the site once so the Cloud Run geo service is warm. Open each storm once so Gemini's cached readings load instantly.
- Rehearse the Gemini calls. Vertex AI can take a few seconds to answer, so cut the waits in editing rather than talking over them.
- Allow the microphone in the browser for the voice question.
- On Windows 11, Snipping Tool records the screen (Win+Shift+R). Record the narration separately if the room is noisy.

---

## 0:00–0:20 · Cold open

**Show:** black, then fade into the console at Fani's landfall: full map, pulsing eye, alert cards, the blue surge band along the coast.

**Say:**
> In May 2019, Cyclone Fani hit Puri. Odisha evacuated 1.2 million people in time, and that was a triumph. But eleven days later, Puri district still had no power: hospitals, water works, shelters. The warnings said where the storm would go. Nobody said what it would break.

## 0:20–0:40 · The solution

**Show:** deck slide 1 (cover) for about 3 s, then slide 4 (the solution) for about 12 s: move the cursor from the Mot shelter card to the Prioritise screenshot beside it, then along the four steps at the bottom. Then back to the console.

**Say:**
> I'm Sathya, and this is Team Argmax. ShadowCast tells a district officer which hospitals, shelters, substations and roads a cyclone will knock out, and when, up to sixty-eight hours ahead: here, Mot shelter, first of 3,325 sites. It learns from real outages seen by satellite, runs on real forecasts, uses Gemini to read, hear and draft, and checks itself after every storm.

## 0:40–1:50 · The Brief: official and live, then what breaks

**Show:**
1. Storm select: **Fani 2019 · Odisha coast**, **Best track**; the panel opens on **Brief**.
2. Drag the timeline to 2 May, 13:00 IST (T−20 h). Hold on the **IMD bulletin · read by Gemini** card, then the **Live now** card.
3. Scroll to the tiles and the first action cards, then **Anticipatory finance**.
4. Press **Play**. Let the alert cards stack up and the arterial roads turn amber as they close. Pause at **Landfall**.

**Say:**
> This is the Odisha coast: 3,325 real sites. I'm replaying Fani from twenty hours out, and the console opens on the duty brief.
>
> First, the official picture. Gemini has read IMD's own bulletin straight from the PDF: landfall near Puri, a one-and-a-half-metre surge over Ganjam, Khurda, Puri and Jagatsinghpur. Our surge model is right beside it. And this card is live, today: the NDMA warnings in force for Odisha right now.
>
> Then what breaks. 917 sites are likely to lose power. Every agency gets an action with a deadline: the moment gales reach its first site, because after that, crews can't move safely. District administration has three hours for 254 shelters and schools. Public works: about 3,900 kilometres of arterial road will be cut, and the Bhubaneswar–Puri highway becomes unsafe four hours before landfall, which is the deadline for every shelter on it.
>
> And the money: Puri's parametric cover triggers four hours before landfall, and the districts that triggered really did lose power, as the satellites confirm.
>
> *(press Play)* As the storm closes in, alerts fire and the roads close one by one.

## 1:50–2:55 · Prepare: Gemini hears, explains and drafts

**Show:**
1. Click the first action to open **Mot shelter (Bramhagiri)**, then open **Prepare**.
2. Tap the **microphone** and ask aloud, in Hindi or Odia: *"Mot shelter ko sabse pehle kyun rakha gaya hai?"* (why is Mot shelter first?). Tap again to send. Let the answer stream, starting with "Heard: …".
3. Click **"Draft an advisory for the five highest-priority assets in English, Hindi and Odia"**.
4. Flip the language tabs, click **Approve and issue**, then **Listen in Odia** for about 4 s.

**Say:**
> Now, Prepare. This is Gemini 3.8 Flash on Vertex AI, and I can just ask it out loud, in Hindi. It hears the question directly and answers from live calls to our geo service: 126-knot winds, the storm passing nine kilometres away, gales sixteen hours before landfall.
>
> *(click draft)* It checks IMD's bulletin first, then drafts a Common Alerting Protocol message, the format India's SACHET system uses, in English, Hindi and Odia.
>
> Nothing goes out on its own: I approve or reject, the approval is signed on the server, and it's logged in Firestore. *(approve)* Gemini's text-to-speech then reads it in Odia, for radio and phone.

## 2:55–3:50 · Prove: the satellites check everything

**Show:**
1. Open **Prove** on Fani: the AUC tiles, then scroll to **Satellite evidence · read by Gemini** (before/after images), **Storm rain vs NASA GPM** and **Storm surge vs IMD**.
2. Cut to deck slide 8 (validation) for about 12 s: point at the Hudhud row, then the Amphan row. Back to the console for the next section.

**Say:**
> Here's the part most tools skip: was it right? NASA's night-light satellite shows which substations went dark. Above a hundred knots they lost a median seventy-seven percent of their light. Hide parts of the coast and refit, and the model still scores 0.97.
>
> Gemini looks at the same before and after images and calls it: Khordha, Puri and Cuttack went dark, which agrees with the forecast. Rain matches NASA's GPM satellite with a rank correlation of 0.72, and the surge lands in the range IMD reported.
>
> *(slide 8)* Every model, every storm, scored the same way. On Hudhud, a storm in Andhra the model never saw, it scores 0.79.
>
> *(Amphan row)* On Amphan it fails, and we publish that. That is what Prove is for: telling an officer to recalibrate before trusting the model on a new grid.

## 3:50–4:15 · Real forecasts

**Show:** storm select **Dana 2024**, click **T−68h**: the ensemble tracks fan out; step to **T−20h**. Show the parametric card's trigger odds.

**Say:**
> And it works on real forecasts. This is Cyclone Dana with ECMWF's ensemble exactly as issued, sixty-eight hours out. Every site gets the share of forecast tracks that bring it gales, and every district its odds of a payout, days before landfall.

## 4:15–4:50 · Architecture and close

**Show:** deck slide 10 (architecture), then slide 12 (the ask), and end on the live URL.

**Say:**
> It's all live. The console runs on Vercel. Gemini, its voice and the audit log run on Google Cloud; the geo service runs on Cloud Run with Earth Engine; every byte of data sits in Cloud Storage and Firestore, with no stored keys. Three coasts and three languages are already built.
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
| IMD: landfall near Puri; 1.5 m surge over Ganjam, Khurda, Puri, Jagatsinghpur | IMD National Bulletin No. 44, 05:30 IST 2 May 2019, as read by Gemini (`/api/bulletins/fani-2019`) |
| Live NDMA warnings for Odisha | `/live`, feed archiver's newest run |
| 3,325 sites; Mot shelter: 126 kt, 9 km, gales +16 h | Live geo API, `fani-2019` |
| 917 sites likely to lose power; district administration 254 sites due in 3 h | The live Brief at 2 May 13:00 IST |
| About 3,900 of 9,800 km of arterial road cut; NH316 (Bhubaneswar–Puri) unsafe from 3 May 04:45 IST | `fani-2019` roads (`/scenarios/fani-2019/roads`), IMD damage classes (cut at 90 kt) |
| Puri triggers 4 h before landfall; triggered districts lost power at 18% of lit substations vs 0% | `fani-2019` insurance summary |
| 77% median light loss above 100 kt; AUC 0.97 in sample and holdout; Hudhud 0.79; Amphan fails | [validation-results.md](validation-results.md) |
| Gemini: Khordha, Puri, Cuttack totally dark, agrees | `/api/evidence/fani-2019` |
| Rain rank correlation 0.72 (Fani); surge 2.3 m modelled vs 1.5 m IMD | `fani-2019` rain and surge summaries |
| Dana ensemble 68 → 20 h, 36–52 members | `dana-2024` forecasts (ECMWF open data) |
