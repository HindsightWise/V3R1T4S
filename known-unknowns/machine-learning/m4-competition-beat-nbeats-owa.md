# M4 competition (100,000 series): an honestly out-of-sample point forecast with overall OWA below N-BEATS's 0.795

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-days (100,000 series; about 270 MB of CSV in Dataset/Train and Dataset/Test; deep ensembles benefit from a GPU, statistical combinations run on CPU) · open as of 2026-10-30

## The problem

The M4 competition (Spyros Makridakis, Evangelos Spiliotis and Vassilios Assimakopoulos, 2018; IJF 2020) asked for point forecasts and 95% prediction intervals for 100,000 series (23,000 yearly, 24,000 quarterly, 48,000 monthly, 359 weekly, 4,227 daily, 414 hourly) at fixed horizons 6/8/18/13/14/48. The organisers' repository Mcompetitions/M4-methods holds the train and test sets, M4-info.csv, the point forecasts of all 49 valid submissions and the R code that computes sMAPE, MASE and OWA (the mean of sMAPE and MASE, each divided by the Naive2 value, over all series). In its Evaluation and Ranks sheet the winner, Slawek Smyl's ES-RNN hybrid (Uber), scores sMAPE 11.374 and OWA 0.821, and Montero-Manso, Talagala, Hyndman and Athanasopoulos (FFORMA) score 0.838. After the competition, N-BEATS (Boris Oreshkin, Dmitri Carpov, Nicolas Chapados, Yoshua Bengio; ICLR 2020, arXiv:1905.10437 Table 1) reported OWA 0.795 (sMAPE 11.135) for its N-BEATS-I+G ensemble. That is the lowest overall M4 OWA this entry could pin to a primary source. By frequency, N-BEATS leads on Yearly, Quarterly and Monthly (Table 12). On the Others subset (weekly, daily and hourly combined), submission 237 (Pawlikowski, Chorowska and Yanchuk, ProLogistica Soft) scores about 0.742 when recomputed from the organisers' per-frequency sheet, below N-BEATS's 0.822. For intervals, the winner's overall MSIS is 12.23 (Montero-Manso et al. 14.334). Open task: a forecast pipeline that never sees the test set and scores an overall OWA below 0.795.

## What counts as a win

Saved point forecasts for all 100,000 M4 series at the official horizons whose overall OWA, computed with the organisers' evaluation code from https://github.com/Mcompetitions/M4-methods (Naive2 normaliser, MASE seasonal period from M4-info.csv), is STRICTLY LOWER (direction: min) than 0.795 (N-BEATS-I+G, arXiv:1905.10437 Table 1) and than any lower overall M4 OWA the skeptic finds in a credible post-2020 paper for a method with test-free training. LEAK RULE: forecasts come from a frozen, hashed script that the skeptic reruns in a fresh environment where only Dataset/Train and M4-info.csv exist (no test files on disk); every model, hyperparameter and ensemble choice is fixed on a holdout carved from the end of each training series; any pretrained component must have published training-data documentation excluding all M4 series (time-series foundation models trained on Monash/LOTSA-type corpora are excluded unless proven otherwise).

## Partial wins

- **p1:** Overall OWA strictly below 0.821 (Smyl, M4 winner) under the full-win leak rule, with a pipeline that the skeptic reruns end to end in under 24 hours on one 8-core CPU machine with no GPU.
- **p2:** Under the full-win leak rule, with forecasts submitted for all 100,000 series, an OWA on one frequency subset that is strictly below the lowest known value for that subset: Yearly 0.758, Quarterly 0.800 or Monthly 0.819 (N-BEATS, arXiv:1905.10437 Table 12), or Others (weekly, daily and hourly combined) below the value of submission 237 (ProLogistica Soft), about 0.742. For Others, the claimant recomputes submission 237's exact value with the organisers' code from its released point forecasts and must beat that value.
- **p3:** 95% prediction intervals for all 100,000 series under the full-win leak rule, with overall MSIS (organisers' code) strictly below Smyl's 12.23 and overall empirical coverage between 94% and 96%.

## How a win is checked

Clone Mcompetitions/M4-methods, hash the Train/Test CSVs, rerun the frozen script in a container without the Test folder, then score the saved forecasts with the organisers' R evaluation code; as a scorer check, score submission-118 (Smyl) and confirm OWA 0.821 and sMAPE 11.374. Read the script for any test-file access or test-informed constants, and check pretrained models' data cards. Re-read the record in arXiv:1905.10437 and search for later lower overall OWAs before accepting.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1905.10437>

## Sources

- <https://github.com/Mcompetitions/M4-methods>
- <https://raw.githubusercontent.com/Mcompetitions/M4-methods/master/README.md>
- <https://github.com/Mcompetitions/M4-methods/raw/master/Evaluation%20and%20Ranks.xlsx>
- <https://arxiv.org/abs/1905.10437>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Forecast combination in the FFORMA / Theta tradition, weighted by features learned on training-only holdouts, stacked with a global deep model.
- Per-frequency specialists: M4's yearly and quarterly subsets dominate the series count, so gains there move overall OWA most.
- Ensembling over loss functions and lookback lengths, the main source of N-BEATS's gain, is cheap to reproduce with smaller networks.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Test leakage through pretraining: many public time-series corpora contain the full M4 series, including the test horizon.
- OWA in M4 is computed from aggregate sMAPE and MASE relative to Naive2 over all series, not as a mean of per-series OWAs; use the organisers' code.
- N-BEATS's per-frequency table compares only four M4 entries; always check all 49 released submissions before claiming a subset win.
- The 2026-10-30 checks fetched the primary sources but could not complete a 2024-2026 literature search; a claimant must search for, and beat, any lower credible overall OWA before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/m4-competition-beat-nbeats-owa.md
```

Already set up? Say `run V3R1T4S on m4-competition-beat-nbeats-owa`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `m4-competition-beat-nbeats-owa`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
