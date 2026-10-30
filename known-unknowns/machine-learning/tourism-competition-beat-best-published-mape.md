# Tourism forecasting competition (1,311 series): an out-of-sample average MAPE below N-BEATS-G's 18.47

🤖 **Machine learning** · standard · tractability ★★★☆☆ · compute: laptop-hours (1,311 series, under 1 MB) · open as of 2026-10-30

## The problem

The 2010 tourism forecasting competition (George Athanasopoulos, Rob Hyndman, Haiyan Song and Doris Wu, IJF 2011) has 1,311 series: 518 yearly (horizon 4), 427 quarterly (8) and 366 monthly (24). Its Kaggle follow-up (Athanasopoulos and Hyndman 2011) ran in two parts. Team SaliMali (Phil Brierley) won the quarterly/monthly part. Team LeeCBaker (Lee C. Baker; see Baker and Howard 2011) is the best Kaggle team with results on all three subsets: overall MAPE 19.35 in the comparison of arXiv:1905.10437 Table 15, where the best statistical benchmark is ForecastPro at 19.84. N-BEATS-G (Oreshkin, Carpov, Chapados, Bengio, ICLR 2020) reports 18.47, the lowest overall average (horizon-weighted, Table 15 equation 6) this entry could pin to a primary source. The best listed values per subset are Yearly 21.44 (N-BEATS-I+G), Quarterly 14.71 (N-BEATS-G) and Monthly 19.17 (N-BEATS-G). The data with test values are in Peter Ellis's Tcomp R package on CRAN. Open task: beat 18.47 without touching the test values.

## What counts as a win

Saved forecasts for all 1,311 series at the official horizons whose average MAPE over all series and horizons (as in arXiv:1905.10437 Appendix C.3) against the Tcomp test values is STRICTLY LOWER (direction: min) than 18.47 and than any lower credible published overall tourism MAPE the skeptic finds. LEAK RULE: a frozen, hashed script rerun in a fresh environment holding only the training parts (Tcomp's $xx stripped); all choices fixed on holdouts carved from the training parts; no pretrained component whose documented training data include tourism competition series.

## Partial wins

- **p1:** Under the full-win leak rule, an overall MAPE strictly below 19.35 (LeeCBaker, winner of the Kaggle yearly part and the best Kaggle team with results on all three subsets) with a method containing no neural network.
- **p2:** Under the full-win leak rule and with all 1,311 series forecast, a subset MAPE strictly below Yearly 21.44, Quarterly 14.71 or Monthly 19.17.

## How a win is checked

Install Tcomp from CRAN, export train and test parts, rerun the frozen script without the test parts, recompute MAPE independently (horizon-weighted, arXiv:1905.10437 equation 6), and as a scorer check reproduce the published SNaive average 21.25 with forecast::snaive (a fresh forecast::thetaf run should land near, not exactly on, the published Theta 20.88).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1905.10437>

## Sources

- <https://arxiv.org/abs/1905.10437>
- <https://cran.r-project.org/package=Tcomp>
- <https://github.com/ellisp/Tcomp-r-package>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The margin over the Kaggle winner is under one MAPE point, and yearly series dominate the series count: damped-trend combinations with shrinkage toward the cross-series mean trend are a cheap start.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Monash's tourism_yearly/quarterly/monthly files and LOTSA-type corpora contain the full series including the test horizon.
- The Kaggle competition itself was scored by MASE; this target uses the MAPE comparison of the N-BEATS paper, so do not mix the two.
- No 2024-2026 literature sweep could be run on 2026-10-30; check for lower published values first.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tourism-competition-beat-best-published-mape.md
```

Already set up? Say `run V3R1T4S on tourism-competition-beat-best-published-mape`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tourism-competition-beat-best-published-mape`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
