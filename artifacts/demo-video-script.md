# ShadowCast demo video script (Team Argmax)

**Length:** about 4:20 (limit 5:00), so you have 40 seconds spare.
**Site:** https://shadowcast-two.vercel.app, Chrome full screen, zoom 100%.
**Slides:** `video/intro-and-endcard.html` (F = full screen, Right = next), and deck slides 10 and 12 from `pitch-deck/ShadowCast-deck.pdf` (open it in Chrome, press F11 for full screen, arrow keys to change page).
**Narration:** "..." means pause. The fillers are optional.

## Before recording

- Open the site a minute early (the first load takes about 12 s). Click each storm once and open Prove on Fani.
- Headphones on. Record system audio and your mic.
- Rehearse with **Reject**. Approve only in the final take.
- Gemini waits: keep recording and cut them later.
- Do Not Disturb on, bookmarks bar hidden.

## 0:00 to 0:26 · Cold open

**Show:** intro slides. Start on black, then press Right at each sentence. Let the three stat tiles count up (about 3 s), then show the ShadowCast reveal (about 2 s). **Leave this tab open on the reveal slide.** You come back to it at the very end.

**Say:**
> In May 2019, Cyclone Fani hit Puri. ... Odisha evacuated 1.2 million people in time. ... Eleven days later, Puri district still had no mains power for its hospitals, water works and shelters. ... The warnings gave the storm's track. But nobody could say which of those sites would go dark.

## 0:26 to 0:39 · The solution

**Show:** stay on the ShadowCast reveal slide while you say this, then switch to the site tab.

**Say:**
> Hi, I'm Sathya from Team Argmax. So, ShadowCast tells a district officer which sites and roads a cyclone is going to knock out, and when, up to 68 hours ahead.

## 0:39 to 1:49 · The Brief

**Show:**
1. Site: Fani 2019, **Best track**, **Brief** tab.
2. Drag the timeline to **2 May, 13:00 IST**.
3. Hold on the **IMD bulletin** card (5 s).
4. Scroll to **Recommended actions**: District administration (3 h), Public works (14 h).
5. **What-if simulation**: Intensity **+10%**, High tide **+1.00 m**. Click **Surge** (3 s), then **Reset** and **Outage**.
6. **Play replay** for 5 s, then pause.

**Say:**
> Okay, so I'm replaying Fani from twenty hours before landfall. Up here, Gemini has read IMD's bulletin straight from the PDF. It says landfall near Puri, and a surge of one and a half metres over Ganjam, Khurda, Puri and Jagatsinghpur.
>
> And below that is where ShadowCast comes in. 917 sites are likely to lose power. Each agency gets an action, due before gales reach its first site. So district administration has three hours, for 254 sites. And about 3,900 kilometres of arterial road are likely to be cut... public works has fourteen hours to get crews onto them.
>
> *(open What-if)* Now, I can also stress test this. Say Fani comes in a tenth stronger, um, and lands on a high tide. ... You can see more sites go dark, the coast floods, and the list reorders straight away. That's our trained model running again on the new winds.
>
> *(Play, 5 s, no talking)*

## 1:49 to 2:56 · Prepare

**Show:**
1. Click the **District administration** action. It opens Mot shelter. Point at **Access road** (NH316, 04:15).
2. **Prepare** tab, then **Live call**. Ask in Hindi *"Mot shelter ko sabse pehle kyun rakha gaya hai?"*. Let it answer for 6 s, then **End call**.
3. Click **"Draft an advisory…"**. Cut the wait.
4. Click the English, Hindi and Odia tabs, then **Approve and issue**.
5. Click **CAP feed** (3 s), then close the tab.

**Say:**
> This is Mot shelter's own panel. Its access road, NH316, closes at a quarter past four... on the morning of landfall.
>
> Okay, now Prepare. With Gemini Live on Vertex AI, I can just call the analyst... and ask in Hindi. *(ask, let it answer 6 s)* ... So it answers out loud, using numbers from our geo service, and I can interrupt it whenever I want.
>
> *(click the draft)* For the written alert, Gemini 3.8 Flash checks IMD's bulletin first. ... Then it drafts a CAP alert, that's the format India's SACHET system uses, in English, Hindi and Odia.
>
> Nothing goes out until an officer approves it. The approval is signed on the server and logged in Firestore. *(approve, then CAP feed)* And once I approve, it's sent. It's already on a standard CAP feed that SACHET can pick up.

## 2:56 to 3:38 · Prove

**Show:**
1. **Prove** tab: **AUC 0.97**, then the light-loss chart.
2. Scroll to **Satellite evidence**, then **Storm surge vs IMD**.

**Say:**
> So how do we know it's right? On the Prove tab, NASA's night light pictures show which substations actually went dark. Above a hundred knots, they lost a median of 77 percent of their light. The outage model we trained scores 0.97... even when each stretch of coast is held out.
>
> Gemini reads the same images and, um, finds that Khordha, Puri and Cuttack went dark, which agrees with the forecast. And the surge model gives 2.3 metres on the Puri coast, against IMD's 1.5.
>
> On Hudhud, a storm in Andhra the model never saw, it scores 0.79.

## 3:38 to 3:48 · Dana forecast

**Show:** Storm menu, **Dana 2024**, then click **T−68h** straight away. Drag the timeline back to **22 Oct, 06:00 UTC**.

**Say:**
> And this is Cyclone Dana, replayed with ECMWF's forecast exactly as it was issued, 68 hours out... 685 sites are likely to get gales.

## 3:48 to 4:20 · Close

**Show:** open the Storm menu (3 s), then deck slide 10 (8 s), then deck slide 12 (6 s). For the last line, switch to the intro tab and press Right once to bring up the end card (or open `intro-and-endcard.html#8`). Say the last line over it, hold 3 s, then stop recording.

**Say:**
> We've already built three coasts, with alerts in Odia, Telugu and Bengali. It all runs on Google Cloud and Vercel, with Gemini on Vertex AI and no stored keys. One Odisha cyclone season for thirty officers costs about 5,300 rupees a month.
>
> Our ask is one cyclone season running alongside OSDMA.
>
> *(end card)* ShadowCast. Know what the storm will break, before it breaks.

## Sources

| Line | Source |
|---|---|
| 1.2 million evacuated | NBC News, 3 May 2019 |
| Puri without power 11 days later | Business Standard (PTI), 14 May 2019 |
| IMD: landfall near Puri, 1.5 m surge | IMD National Bulletin No. 44, 2 May 2019 |
| 917 sites, 254 in 3 h, public works 14 h, 3,900 km of road | Live Brief at 2 May 13:00 IST |
| NH316 closes 04:15 | `fani-2019` assets |
| 77% light loss, AUC 0.97, Hudhud 0.79 | [validation-results.md](validation-results.md) |
| Surge 2.3 m vs IMD 1.5 m | Prove tab |
| Dana: 685 sites at T−68 h | `dana-2024` forecasts |
| ₹5,300 a month | [costing.md](costing.md) |
