# ShadowCast demo video script (Team Argmax)

**Target length:** 4:45. The rules allow 3 to 5 minutes, and most of the video has to be the working site, not slides.
**Narration:** about 630 words, roughly 4:31 at 140 words a minute. The rest is silent screen time: the replay playing, the Odia audio and the CAP feed.
**Record at:** https://shadowcast-two.vercel.app in Chrome, full screen at 1920×1080, browser zoom 100%.
**Slides used:** from the pitch deck, downloaded as PDF and shown full screen: slide 1 (cover), slide 4 (the solution, with the Prioritise screenshot), slide 8 (validation), slide 10 (architecture) and slide 12 (the ask).

## Before recording

- Open the site a minute before you start. The geo service sleeps when nobody uses it, and the first load takes about 12 seconds.
- Select each of the four storms once and open Prove on Fani. Gemini's readings of the IMD bulletin and the satellite images are then cached and appear instantly.
- Read the **Live now · real feeds** card and adjust the line about it at 0:40 to what it shows that day. On 30 September it showed GDACS's Tropical Cyclone ONE-26 (ended) and one NDMA warning for Odisha, a flood on the Mahanadi at Naraj in Cuttack.
- Allow the microphone for the site, and say the Hindi question aloud twice beforehand.
- Every approval is written to the audit log and published on the public CAP feed. Rehearse with **Reject**, and approve only in the take you keep.
- Gemini takes 5 to 10 seconds to answer a question and longer to draft an advisory. Keep recording through the wait and cut it in editing; don't talk over it.
- Record the screen with Snipping Tool (Win+Shift+R) or OBS, and the voice separately if the room is noisy.
- Hide the bookmarks bar and turn on Do Not Disturb.

---

## 0:00 to 0:20 · Cold open

**Show:**
1. Two seconds of black.
2. Fade in on the console with Fani selected and the timeline dragged to the **Landfall** mark (3 May, 09:00 IST): the storm eye over Puri, alert cards on the map, amber roads and the blue surge band along the coast. Don't touch anything.

**Say:**
> In May 2019, Cyclone Fani hit Puri. Odisha evacuated 1.2 million people in time. Eleven days later, Puri district still had no mains power for its hospitals, water works and shelters. The warnings gave the storm's track; nobody could say which of those sites would go dark.

## 0:20 to 0:40 · The solution

**Show:**
1. Deck slide 1 (cover) for 3 seconds.
2. Deck slide 4 for about 15 seconds: point at the Mot shelter card, then at the Prioritise screenshot beside it, then run the cursor along the four steps at the bottom.

**Say:**
> I'm Sathya, from Team Argmax. ShadowCast tells a district officer which sites and roads a cyclone will knock out, and when, up to sixty-eight hours ahead: here, Mot shelter, first of 3,325 sites. Its outage odds come from satellite records of real blackouts, and every storm is scored afterwards.

## 0:40 to 1:50 · The Brief, twenty hours out

**Show:**
1. Back to the site. The **Storm** menu (top left) shows **Fani 2019 · Odisha coast (Ganjam to Balasore)**, **Best track** is selected, and the side panel is on **Brief**.
2. Drag the timeline to **2 May, 13:00 IST**. The label under it reads "2 MAY 07:30 UTC · T−20 H".
3. Hold on the **IMD bulletin · read by Gemini** card for about 5 seconds, then on **Live now · real feeds**.
4. Scroll down past the tiles (**At risk 917**, **Next gales 3 h**) to **Recommended actions**. Scroll past the **Surge flood 0** tile without stopping. Pause on **District administration · in 3 h**, then **Public works · in 14 h**.
5. Scroll to **Anticipatory finance · parametric cover**: Puri at "3 May 04:45 IST · T−4 H, 100%".
6. Press **Play replay**. Let the alert cards stack up and the roads turn amber for about 7 seconds, then pause at **Landfall**.

**Say:**
> I'm replaying Fani from twenty hours before landfall, and the console opens on the duty brief. Gemini has read IMD's bulletin straight from the PDF: landfall near Puri, and a one-and-a-half-metre surge over Ganjam, Khurda, Puri and Jagatsinghpur. The card below is live. It shows the NDMA warnings in force for Odisha today, which right now is a flood on the Mahanadi. *(say what the card shows on the day)*
>
> Below that is what ShadowCast adds. 917 sites are likely to lose power. Each agency gets an action due before gales reach its first site, since crews can't work safely after that. District administration has three hours for 254 sites. About 3,900 kilometres of arterial road are likely to be cut, and public works has fourteen hours to get crews onto them.
>
> The parametric cover triggers in Puri four hours before landfall, and the satellites later showed that the districts where it triggered did lose power.
>
> *(press Play and let it run for about 7 seconds without narration)*

## 1:50 to 2:55 · Prepare: asking Gemini, then issuing the alert

**Show:**
1. Go back to the Brief and click the **District administration** action. The map moves to **Mot shelter (Bramhagiri)** and its panel opens. Point at **Access road**: 3 May 04:15 IST, NH316.
2. Open the **Prepare** tab.
3. Click **Ask by voice** (the microphone), say in Hindi *"Mot shelter ko sabse pehle kyun rakha gaya hai?"* (why is Mot shelter first?), and click it again to send. The answer starts with "Heard: …" and comes back in Hindi. Cut the wait.
4. Click the suggestion **"Draft an advisory for the five highest-priority assets in English, Hindi and Odia"**. Cut the wait until the advisory card appears.
5. Click the English, Hindi and Odia tabs on the card, then **Approve and issue**.
6. On the Odia tab, click the speaker button (**Listen in ଓଡ଼ିଆ**) and let it play for about 4 seconds.
7. Click **CAP feed** in the card's footer. The feed opens in a new tab with the new alert at the top. Hold for 3 seconds, then close the tab.

**Say:**
> Mot shelter tops the list, and its access road, NH316, closes at a quarter past four on the morning of landfall.
>
> This is Prepare, with Gemini 3.8 Flash on Vertex AI. I can ask it out loud, in Hindi. It hears the audio itself and answers in Hindi, with numbers from our geo service: here, 126-knot winds and gales sixteen hours before landfall. *(if the answer quotes other figures, say those)*
>
> *(click the draft)* It checks IMD's bulletin first, then drafts a CAP alert, the format India's SACHET system uses, in English, Hindi and Odia.
>
> Nothing goes out until an officer approves it. The approval is signed on the server and logged in Firestore. *(approve)* Gemini's text-to-speech reads it in Odia, for radio and phone. *(CAP feed)* Approving also dispatches it: the alert is already on a standard CAP feed that SACHET can pick up.

## 2:55 to 3:45 · Prove: scoring the model against satellites

**Show:**
1. Close the tab so you're back on the console, and open the **Prove** tab (still Fani). Hold on **ROC AUC 0.97** and the **Spatial holdout** line, then on the **Median light loss by modelled wind** chart and its 100 to 130 kt bar.
2. Scroll to **Satellite evidence · read by Gemini**: the before and after images and the **Agrees with ShadowCast** tag.
3. Scroll to **Storm rain vs NASA GPM** (0.72), then **Storm surge vs IMD** (2.3 m against 1.5 m).
4. Cut to deck slide 8 for about 12 seconds: point at the Hudhud row, then the Amphan row.

**Say:**
> On the Prove tab, NASA's night-light satellite shows which substations went dark, and above a hundred knots they lost a median seventy-seven percent of their light. The model scores 0.97, and still 0.97 when each stretch of coast is held out.
>
> Gemini reads the same before and after images and finds that Khordha, Puri and Cuttack went dark, which agrees with the forecast. Rain matches NASA's GPM satellite with a rank correlation of 0.72, and the surge model gives 2.3 metres on the Puri coast against IMD's 1.5.
>
> *(slide 8)* On Hudhud, a storm in Andhra the model never saw, it scores 0.79. *(Amphan row)* On Amphan it fails, and we publish that, so an officer knows to recalibrate before trusting it on a new grid.

## 3:45 to 4:15 · Real forecasts, as issued

**Show:**
1. In the **Storm** menu choose **Dana 2024 · Odisha coast**, and click **T−68h** straight away. (The best-track view's top bar shows a backtest AUC of 0.32, which means nothing with only five outages, so don't linger on it.)
2. Drag the timeline back to **22 Oct, 06:00 UTC**, so the screen shows what was known before any gales. The top bar reads **Members 36**, **Likely gales 685**. Let the member tracks show on the map for a few seconds.
3. Scroll to **Anticipatory finance**: every district at 0% trigger.

**Say:**
> ShadowCast replays real storms using the forecasts exactly as they were issued, so you see what an officer would have known at each moment. This is Cyclone Dana with ECMWF's ensemble sixty-eight hours out: 685 sites likely to get gales. No forecast member brings a district to the cover's 64-knot trigger, so the payout odds stay at zero. The official warnings feed is live, and a new storm is one build away.

## 4:15 to 4:45 · Architecture and close

**Show:** deck slide 10 for about 12 seconds, then slide 12 for about 12 seconds, and end on the live URL in the slide's footer.

**Say:**
> It all runs today on Vercel and Google Cloud: Gemini on Vertex AI, the geo service on Cloud Run with Earth Engine, and all the data in Cloud Storage and Firestore, with no stored keys. One Odisha cyclone season for thirty officers costs about 5,300 rupees a month.
>
> Our ask is one cyclone season running alongside OSDMA.
>
> ShadowCast: know what the storm will break, before it breaks.

---

## Facts behind every line

| Line | Source |
|---|---|
| 1.2 million evacuated | NBC News, 3 May 2019 |
| Puri district without power 11 days later | Business Standard (PTI), 14 May 2019 |
| IMD: landfall near Puri; 1.5 m surge over Ganjam, Khurda, Puri, Jagatsinghpur | IMD National Bulletin No. 44, 05:30 IST 2 May 2019, as read by Gemini (`/api/bulletins/fani-2019`) |
| Live NDMA warnings for Odisha | `/live`, the feed archiver's newest run (checked 30 Sep 2026: one Mahanadi flood warning) |
| 3,325 sites; Mot shelter first, 126 kt, gales 2 May 16:30 IST (16.5 h before landfall) | Live geo API, `fani-2019` |
| Mot shelter's access road NH316 closes 3 May 04:15 IST | `fani-2019` assets: `access_road`, `access_closes` |
| 917 sites likely to lose power; district administration 254 sites in 3 h; public works in 14 h | The live Brief at 2 May 13:00 IST |
| About 3,900 of 9,800 km of arterial road cut | `fani-2019` roads (`/scenarios/fani-2019/roads`), IMD damage classes (cut at 90 kt) |
| Puri triggers 4 h before landfall; triggered districts lost power at 18% of lit substations, others 0% | `fani-2019` insurance summary, on the Brief's parametric card |
| Approved alert published on the CAP feed | `/api/cap` (Atom), `/api/cap/<id>` (CAP 1.2) |
| 77% median light loss above 100 kt; AUC 0.97 in sample and in the spatial holdout; Hudhud 0.79; Amphan fails | [validation-results.md](validation-results.md), Prove tab |
| Gemini: Khordha, Puri, Cuttack went dark; agrees with ShadowCast | `/api/evidence/fani-2019` |
| Rain rank correlation 0.72 (Fani); surge 2.3 m modelled vs 1.5 m IMD | Prove tab, `fani-2019` rain and surge summaries |
| Dana: 36 members and 685 sites with likely gales at T−68 h; payout odds 0% | `dana-2024` forecasts (ECMWF open data), Dana's parametric card, [validation-results.md](validation-results.md) |
| About ₹5,300 a month for one Odisha season with 30 officers | [costing.md](costing.md) |
