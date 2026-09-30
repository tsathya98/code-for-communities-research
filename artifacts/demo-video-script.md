# ShadowCast demo video script (Team Argmax)

**Target length:** 4:56. The rules allow 3 to 5 minutes, and most of the video has to be the working site, not slides.
**Narration:** about 600 words, roughly 4:18 at 140 words a minute. The rest is screen time without narration: the stat cards, the replay playing, the live call, the CAP feed and the end card.
**Record at:** https://shadowcast-two.vercel.app in Chrome, full screen at 1920×1080, browser zoom 100%.
**Slides used:** the intro and end card from `artifacts/video/intro-and-endcard.html` (open it in Chrome, press F for full screen, Right arrow or Space to advance), and from the pitch deck, downloaded as PDF and shown full screen: slide 4 (the solution, with the Prioritise screenshot), slide 8 (validation), slide 10 (architecture) and slide 12 (the ask).

## Before recording

- Open the site a minute before you start. The geo service sleeps when nobody uses it, and the first load takes about 12 seconds.
- Select each of the four storms once and open Prove on Fani. Gemini's readings of the IMD bulletin and the satellite images are then cached and appear instantly.
- Read the **Live now · real feeds** card and adjust the line about it in the Brief to what it shows that day. On 30 September it showed GDACS's Tropical Cyclone ONE-26 (ended) and one NDMA warning for Odisha, a flood on the Mahanadi at Naraj in Cuttack.
- Allow the microphone for the site, and say the Hindi question aloud twice beforehand.
- For the live call, wear headphones (otherwise the analyst hears itself and stops talking) and set the screen recorder to capture system audio as well as your microphone, so the analyst's voice is in the video. A call lasts at most four minutes.
- Every approval is written to the audit log and published on the public CAP feed. Rehearse with **Reject**, and approve only in the take you keep.
- Gemini takes 5 to 10 seconds to answer a question and longer to draft an advisory. Keep recording through the wait and cut it in editing. Don't talk over it.
- Record the screen with Snipping Tool (Win+Shift+R) or OBS, and the voice separately if the room is noisy.
- Hide the bookmarks bar and turn on Do Not Disturb.
- Rehearse the intro slides with the narration once. Press Right as you start each sentence, so the text lands as you say it.

## 0:00 to 0:26 · Cold open

**Show:** the intro slides, full screen. Start recording on slide 0 (black), then press Right as you begin each sentence.
1. "3 May 2019 · Puri, Odisha / Cyclone Fani makes landfall."
2. "1.2 million people were evacuated in time."
3. "Eleven days later…"
4. "Puri still had no mains power."
5. "Nobody could say which sites would go dark." Let "go dark" turn orange.
6. The three stat cards (3,325 · 0.97 · 5). Say nothing and let them count up, about 3 seconds.
7. "Introducing ShadowCast", about 2 seconds, then switch to the deck.

**Say:**
> In May 2019, Cyclone Fani hit Puri. Odisha evacuated 1.2 million people in time. Eleven days later, Puri district still had no mains power for its hospitals, water works and shelters. The warnings gave the storm's track, but nobody could say which of those sites would go dark.

## 0:26 to 0:41 · The solution

**Show:**
1. Deck slide 4 for about 15 seconds: point at the Mot shelter card, then at the Prioritise screenshot beside it, then run the cursor along the four steps at the bottom.

**Say:**
> I'm Sathya from Team Argmax. ShadowCast tells a district officer which sites and roads a cyclone will knock out, and when, up to 68 hours ahead. Here, Mot shelter comes first out of 3,325 sites.

## 0:41 to 1:55 · The Brief, twenty hours out

**Show:**
1. Back to the site. The **Storm** menu (top left) shows **Fani 2019 · Odisha coast (Ganjam to Balasore)**, **Best track** is selected, and the side panel is on **Brief**. The line under the storm menu reads **No cyclone active now · past storms replayed as forecast at the time**.
2. Drag the timeline to **2 May, 13:00 IST**. Above the date it says **Replay · Fani 2019**, and under it "2 MAY 07:30 UTC · T−20 H".
3. Hold on the **IMD bulletin · read by Gemini** card for about 5 seconds, then on **Live now · real feeds**.
4. Scroll down past the tiles (**At risk 917**, **Next gales 3 h**) to **Recommended actions**. Scroll past the **Surge flood 0** tile without stopping. Pause on **District administration · in 3 h**, then **Public works · in 14 h**.
5. Click **What-if simulation** (under the readouts, top left). Drag **Storm intensity** to **+10%** and **High tide** to **+1.00 m**. Watch the **≥50% outage** readout and the ranked list change. Then click **Surge** on the map legend (bottom left) for about 3 seconds to show the coast flooding. Click **Reset**, then **Outage**.
6. Press **Play replay**. Let the alert cards stack up and the roads turn amber for about 7 seconds, then pause at **Landfall**.

**Say:**
> I'm replaying Fani from twenty hours before landfall. Gemini has read IMD's bulletin straight from the PDF. It says landfall near Puri, with a surge of one and a half metres over Ganjam, Khurda, Puri and Jagatsinghpur. The card below is live, and today it shows a flood warning on the Mahanadi. *(say what the card shows on the day)*
>
> Below that is what ShadowCast adds. 917 sites are likely to lose power. Each agency gets an action that's due before gales reach its first site. District administration has three hours for 254 sites. About 3,900 kilometres of arterial road are likely to be cut, and public works has fourteen hours to get crews onto them.
>
> *(open What-if)* And I can stress test the storm. Make Fani a tenth stronger and land it on a high tide. More sites go dark, the coast floods, and the list reorders at once, all from the model we trained.
>
> *(press Play and let it run for about 7 seconds without narration)*

## 1:55 to 3:04 · Prepare: asking Gemini, then issuing the alert

**Show:**
1. Go back to the Brief and click the **District administration** action. The side panel switches to **Prioritise** and opens **Mot shelter (Bramhagiri)**. Point at **Peak wind** (126 kt), **Gales arrive** (2 May 16:30 IST), **Storm rain** (175 mm, with "NASA GPM measured 119 mm" under it) and **Access road** (3 May 04:15 IST, NH316).
2. Click **← Priorities**: the ranked list of 3.3K assets with its category filters (Hospital, Cyclone shelter, Substation, …). Hold for 2 seconds.
3. Open the **Prepare** tab.
4. With headphones on, click **Live call** above the message box. When the card reads **Live call · speak any time**, ask in Hindi *"Mot shelter ko sabse pehle kyun rakha gaya hai?"* (why is Mot shelter first?). The analyst answers aloud in Hindi straight away, captioned under **You** and **Analyst**. Let it talk for about 8 seconds, then click **End call**.
5. Click the suggestion **"Draft an advisory for the five highest-priority assets in English, Hindi and Odia"**. Cut the wait until the advisory card appears.
6. Click the English, Hindi and Odia tabs on the card, then **Approve and issue**.
7. Click **CAP feed** in the card's footer. The feed opens in a new tab with the new alert at the top. Hold for 3 seconds, then close the tab.

**Say:**
> This is Mot shelter's own panel. Its access road, NH316, closes at a quarter past four on the morning of landfall.
>
> This is Prepare. With Gemini Live on Vertex AI, I can simply call the analyst and ask in Hindi. *(ask, then let it answer for about 8 seconds)* It answers aloud using numbers from our geo service, and I can cut in at any time.
>
> *(click the draft)* For the written alert, Gemini 3.8 Flash checks IMD's bulletin first. Then it drafts a CAP alert, which is the format India's SACHET system uses, in English, Hindi and Odia.
>
> Nothing goes out until an officer approves it. The approval is signed on the server and logged in Firestore. *(approve, then CAP feed)* And approving also sends it out. The alert is already on a standard CAP feed that SACHET can pick up.

## 3:04 to 3:57 · Prove: scoring the model against satellites

**Show:**
1. Close the tab so you're back on the console, and open the **Prove** tab (still Fani). Hold on **ROC AUC 0.97** and the **Spatial holdout** line, then on the **Median light loss by modelled wind** chart and its 100 to 130 kt bar.
2. Scroll to **Satellite evidence · read by Gemini**: the before and after images and the **Agrees with ShadowCast** tag.
3. Scroll to **Storm rain vs NASA GPM** (0.72), then **Storm surge vs IMD** (2.3 m against 1.5 m).
4. Cut to deck slide 8 for about 8 seconds: point at the Hudhud row, then the Amphan row.

**Say:**
> On the Prove tab, NASA's satellite pictures of night lights show which substations went dark. Above a hundred knots, they lost a median of 77 percent of their light. The outage model we trained scores 0.97, even when each stretch of coast is held out.
>
> Gemini reads the same images and finds that Khordha, Puri and Cuttack went dark, which agrees with the forecast. Rain matches NASA's GPM satellite with a rank correlation of 0.72. And the surge model gives 2.3 metres on the Puri coast, against IMD's 1.5.
>
> *(slide 8)* On Hudhud, a storm in Andhra the model never saw, it scores 0.79. *(Amphan row)* On Amphan it fails, and we publish that, so an officer knows to recalibrate before trusting it on a new grid.

## 3:57 to 4:21 · Real forecasts, as issued

**Show:**
1. In the **Storm** menu choose **Dana 2024 · Odisha coast**, and click **T−68h** straight away. (The best-track view's top bar shows a backtest AUC of 0.32, which means nothing with only five outages, so don't linger on it.)
2. Drag the timeline back to **22 Oct, 06:00 UTC**, so the screen shows what was known before any gales. The top bar reads **Members 36**, **Likely gales 685**. Let the member tracks show on the map for a few seconds.

**Say:**
> ShadowCast replays real storms using the forecasts exactly as they were issued, so you see what an officer would have known at each moment. This is Cyclone Dana with ECMWF's ensemble 68 hours out, and 685 sites are likely to get gales. The official warnings feed is live, and a new storm is one build away.

## 4:21 to 4:56 · Architecture and close

**Show:**
1. On the site, open the **Storm** menu for about 3 seconds: Fani and Dana on the Odisha coast, Hudhud on the north Andhra coast, Amphan on the West Bengal coast.
2. Deck slide 10 for about 10 seconds, then slide 12 for about 10 seconds.
3. End on the end card (slide 8 of the intro slides) for about 3 seconds after the last line.

**Say:**
> Three coasts are already built, with alerts in Odia, Telugu and Bengali. It all runs on Vercel and Google Cloud, with Gemini on Vertex AI, the geo service on Cloud Run and no stored keys. One Odisha cyclone season for thirty officers costs about 5,300 rupees a month.
>
> Our ask is one cyclone season running alongside OSDMA.
>
> ShadowCast. Know what the storm will break, before it breaks.

## Facts behind every line

| Line | Source |
|---|---|
| 1.2 million evacuated | NBC News, 3 May 2019 |
| Puri district without power 11 days later | Business Standard (PTI), 14 May 2019 |
| IMD: landfall near Puri; 1.5 m surge over Ganjam, Khurda, Puri, Jagatsinghpur | IMD National Bulletin No. 44, 05:30 IST 2 May 2019, as read by Gemini (`/api/bulletins/fani-2019`) |
| Live NDMA warnings for Odisha | `/live`, the feed archiver's newest run (checked 30 Sep 2026: one Mahanadi flood warning) |
| 3,325 sites; Mot shelter first, 126 kt, gales 2 May 16:30 IST (16.5 h before landfall) | Live geo API, `fani-2019` |
| Mot shelter: access road NH316 closes 3 May 04:15 IST; rain 175 mm modelled vs 119 mm NASA GPM | `fani-2019` assets: `access_road`, `access_closes`, `rain_mm`, `observed_rain_mm` |
| 917 sites likely to lose power; district administration 254 sites in 3 h; public works in 14 h | The live Brief at 2 May 13:00 IST |
| About 3,900 of 9,800 km of arterial road cut | `fani-2019` roads (`/scenarios/fani-2019/roads`), IMD damage classes (cut at 90 kt) |
| Live call: Gemini Live (`gemini-live-2.5-flash-native-audio`, Vertex AI us-central1) answering from `search_assets` | geo service `/scenarios/<id>/voice` |
| Approved alert published on the CAP feed | `/api/cap` (Atom), `/api/cap/<id>` (CAP 1.2) |
| 77% median light loss above 100 kt; AUC 0.97 in sample and in the spatial holdout; Hudhud 0.79; Amphan fails | [validation-results.md](validation-results.md), Prove tab |
| Gemini: Khordha, Puri, Cuttack went dark; agrees with ShadowCast | `/api/evidence/fani-2019` |
| Rain rank correlation 0.72 (Fani); surge 2.3 m modelled vs 1.5 m IMD | Prove tab, `fani-2019` rain and surge summaries |
| Dana: 36 members and 685 sites with likely gales at T−68 h; payout odds 0% | `dana-2024` forecasts (ECMWF open data), Dana's parametric card, [validation-results.md](validation-results.md) |
| About ₹5,300 a month for one Odisha season with 30 officers | [costing.md](costing.md) |
