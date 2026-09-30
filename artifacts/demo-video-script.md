# ShadowCast demo video script (Team Argmax)

**Length:** about 3:30 as written. With clicks and Gemini waits a real take runs about 4:10, under the 5:00 limit.
**Site:** https://shadowcast-two.vercel.app, Chrome full screen, zoom 100%.
**Slides:** `video/intro-and-endcard.html` (F = full screen, Right = next), and deck slides 10 and 12 from `pitch-deck/ShadowCast-deck.pdf` (open it in Chrome, press F11 for full screen, arrow keys to change page).
**Narration:** "..." means pause. The fillers are optional.

## Before recording

- Open the site a minute early (the first load takes about 12 s). Click each storm once and open Prove on Fani.
- Headphones on. Record system audio and your mic, so the analyst's voice is in the video.
- Rehearse with **Reject**. Approve only in the final take.
- Gemini waits: keep recording and cut them later.
- Do Not Disturb on, bookmarks bar hidden.

## 0:00 to 0:26 · Cold open

**Show:** intro slides. Start on black, then press Right at each sentence. Let the three stat tiles count up (about 3 s), then show the ShadowCast reveal (about 2 s). **Leave this tab on the reveal slide.** You come back to it at the end.

**Say:**
> In May 2019, Cyclone Fani hit Puri. ... Odisha evacuated 1.2 million people in time. ... Eleven days later, Puri district still had no mains power for its hospitals, water works and shelters. ... The warnings gave the storm's track. But nobody could say which of those sites would go dark.

## 0:26 to 0:53 · The solution

**Show:** stay on the reveal slide, then switch to the site tab.

**Say:**
> Hi, I'm Sathya from Team Argmax. ShadowCast tells a district officer which sites and roads a cyclone will knock out, and when, up to 68 hours ahead.
>
> And none of what you'll see is synthetic. Real cyclone tracks from NOAA and ECMWF, 3,325 real sites from OpenStreetMap, and an outage model we trained on NASA satellite data, pulled through Google Earth Engine.

## 0:53 to 1:34 · The Brief

**Show:**
1. Fani 2019, **Best track**, **Brief** tab. Drag the timeline to **2 May, 13:00 IST**.
2. Point at the **At risk 917** tile, then the **District administration** card (in 3 h, 254 sites).
3. **What-if simulation**: slowly drag Intensity to **+10%** and High tide to **+1.00 m**. Click **Surge** (3 s), then **Reset** and **Outage**.
4. **Play replay** for about 6 s, then pause.

**Say:**
> Here's Fani, twenty hours before landfall. 917 sites are likely to lose power. ... Every agency gets a deadline. District administration has three hours, for 254 sites.
>
> *(open What-if)* And I can stress test it. A tenth stronger, on a high tide... *(drag, no talking)* That's our trained model rerunning live.
>
> *(press Play)* Watch the roads turn amber as they close.

## 1:34 to 2:31 · Prepare

**Show:**
1. Click the **District administration** card. Mot shelter opens. Point at **99%**, then **Access road 3 May 04:15**.
2. **Prepare** tab, then **Live call**. Ask the question below in English. Let it answer for about 10 s, then **End call**.
3. Click **"Draft an advisory…"**. Cut the wait.
4. Click the English, Hindi and Odia tabs, then **Approve and issue**.
5. Click **CAP feed** (3 s), then close that tab.

**Live call question:**
> *"Which hospital loses power first, and when do the gales reach it?"*

**Say:**
> Mot shelter has a 99 percent chance of losing power, and its road closes at a quarter past four, the morning of landfall.
>
> Now I'll just call the analyst. It's multilingual, so an officer can ask in Hindi or Odia too. *(ask, let it answer about 10 s, no talking)*
>
> *(click the draft)* Gemini drafts the alert in English, Hindi and Odia. ... *(approve)* Once an officer approves, it's live on a CAP feed that SACHET can read.

## 2:31 to 2:54 · Prove

**Show:**
1. **Prove** tab. Point at **AUC 0.97**.
2. Scroll to **Satellite evidence** and hold on the before and after images (4 s).

**Say:**
> Did it work? NASA's night lights show which substations actually went dark. The outage model we trained on that scores 0.97... and 0.79 on Hudhud, a storm it never saw. *(satellite images)* Gemini reads the same images, and agrees.

## 2:54 to 3:05 · Dana forecast

**Show:** Storm menu, **Dana 2024**, then click **T−68h** straight away. Let the forecast tracks sit on the map (4 s).

**Say:**
> And this is Cyclone Dana, with the forecast exactly as it was issued, 68 hours out.

## 3:05 to 3:34 · Close

**Show:** deck page 10 (6 s), then page 12 (5 s). For the last line, switch to the intro tab and press Right once for the end card. Hold 3 s, then stop recording.

**Say:**
> Three coasts are built, with alerts in Odia, Telugu and Bengali, all on Google Cloud with Gemini on Vertex AI. One Odisha season for thirty officers costs about 5,300 rupees a month.
>
> Our ask is one cyclone season alongside OSDMA.
>
> *(end card)* ShadowCast. Know what the storm will break, before it breaks.

## Sources

| Line | Source |
|---|---|
| Tracks from NOAA (IBTrACS) and ECMWF open data, 3,325 OSM sites, model trained on NASA VIIRS night lights via Google Earth Engine | Live geo API, README data sources, [validation-results.md](validation-results.md) |
| 1.2 million evacuated | NBC News, 3 May 2019 |
| Puri without power 11 days later | Business Standard (PTI), 14 May 2019 |
| 917 sites, 254 in 3 h | Live Brief at 2 May 13:00 IST |
| Mot shelter 99%, road closes 04:15 | Mot shelter panel, `fani-2019` assets |
| AUC 0.97, Hudhud 0.79 | [validation-results.md](validation-results.md) |
| Dana at T−68 h | `dana-2024` forecasts (ECMWF open data) |
| ₹5,300 a month | [costing.md](costing.md) |
