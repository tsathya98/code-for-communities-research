# Outage model validation (26 Sep 2026)

**Model:** P(outage | peak wind) = logistic(−26.85 + 0.2515 × wind_kt), fitted on Fani 2019. P = 0.5 at about 107 kt.
**Label:** VIIRS VNP46A2 night-light loss of at least 50% around a lit substation, from quality-masked medians: about two weeks before the storm against the seven nights after landfall.

## 1. Spatial holdout on Fani: passes

The model was refitted five times, each time hiding one contiguous south-to-north fifth of the coast (40 substations per block).

| Block (latitude) | n | Went dark | Held-out AUC |
|---|---|---|---|
| 19.10–20.23 | 40 | 43% | 0.94 |
| 20.24–20.51 | 40 | 58% | 0.91 |
| 20.51–20.83 | 40 | ~10% | 0.85 |
| 20.83–21.02 | 40 | 0% | n/a |
| 21.03–21.69 | 40 | 0% | n/a |

- **Pooled out-of-fold:** AUC **0.969**, Brier **0.050** (in sample: 0.973 and 0.049).
- **Meaning:** a two-parameter model does not overfit the Odisha coast. It discriminates within held-out stretches, not only "near the track vs far away".

## 2. Amphan 2020, a held-out strong storm in West Bengal: fails

2,227 assets; 156 lit substations; 28% went dark.

| Metric | Value |
|---|---|
| AUC | **0.44** (chance) |
| Brier | 0.278 (the model predicts 1–4%) |
| Spearman (wind vs loss) | −0.02 |
| Median loss by modelled wind | 0–60 kt: 27%; 60–80 kt: 50%; 80–100 kt: 41% |

### Diagnosis

The pipeline checks out: track, landfall and windows are all correct. What fails is the transfer.

1. **The hazard saturates over land.**
   - The JTWC best track keeps 95 kt at 12Z on 20 May, after landfall over the Sundarbans and Kolkata. It only decays to 83 kt at 15Z.
   - Holland's profile has no inland friction or decay, so 80% of substations sit at 80–95 kt (median 86). Kolkata, where observed gusts were about 60–70 kt, is modelled at 89 kt.
   - With almost no spread in modelled wind, the model can't rank anything.
2. **Outage depends on the grid, not only local wind.**
   - Rural substations (WBSEDCL) went dark more often (36%) than Kolkata's (CESC, 14%), despite lower modelled wind.
   - Rural losses also occurred 40–70 km from the track.
3. **Dim substations are noisy.**
   - Percentage loss from pre-storm radiance around 5 nW/cm²/sr is noisy.
   - *Post hoc, not a claim:* among substations with pre-storm radiance ≥ 20 (n=45, mostly urban), wind AUC is 0.93. For radiance ≥ 5 it is 0.38.

## What this means

- **Claims we can make:** the wind→outage model generalises across the reference coast (spatial holdout 0.97), and it raised no false alarms on Dana.
- **Claim we cannot make:** that it transfers to another state's grid. Amphan says it does not, at least without inland wind decay and grid-specific calibration.
- **Pitch framing:** "Prove" is the product feature that catches exactly this. The satellite check shows when a model calibrated on one grid is wrong on another, which tells officials to recalibrate before relying on it.

## Options (awaiting decision)

1. **Physics fix, then an untouched test storm.**
   - Add a standard inland decay (Kaplan–DeMaria 1995) and a land-roughness reduction to the wind model. Both come from the literature and are not tuned on Amphan.
   - Re-score Amphan with the same Fani-fitted model.
   - Add a third storm not yet examined (Hudhud 2014 over Visakhapatnam, or Yaas 2021) as the clean test.
2. **Show Amphan as it is.** Publish the scenario with its failing score and the diagnosis. This is honest, and it demonstrates that "Prove" works.
3. **Keep Amphan in the docs only.**
