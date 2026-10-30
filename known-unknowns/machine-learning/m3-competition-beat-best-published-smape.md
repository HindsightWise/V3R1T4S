# M3 competition (3,003 series): an out-of-sample average sMAPE below the best published 12.37

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-hours (3,003 short series, a few MB) · open as of 2026-10-30

## The problem

The M3 competition (Spyros Makridakis and Michele Hibon, IJF 2000) has 3,003 series: 645 yearly (horizon 6), 756 quarterly (8), 1,428 monthly (18) and 174 other (8). The Theta method of Vassilios Assimakopoulos and Konstantinos Nikolopoulos won it with average sMAPE 13.01 (M3 definition, averaged over all series and horizons as in arXiv:1905.10437 equation 5). Later published results, as tabulated in arXiv:1905.10437 Table 14, are DOTM (Fiorucci et al. 2016) 12.90, EXP (Spiliotis et al. 2019) 12.71 and N-BEATS-I+G (Oreshkin, Carpov, Chapados, Bengio, ICLR 2020) 12.37. That is the lowest average this entry could pin to a primary source. Smyl, Bergmeir, Dokumentov, Long, Wibowo and Schmidt (arXiv:2309.13950, 2024) report {L,S}GT with a per-series mean sMAPE of 12.29. That is a different averaging (Theta scores 12.76 under it), and their subsets give about 12.76 under the horizon-weighted average used here. Their LGT holds the best yearly value, 15.18. The best listed values on the other subsets are Quarterly 8.84 and Monthly 13.11 (N-BEATS-I+G) and Other 4.19 (N-BEATS-G). The data with the held-out test values are distributed in Rob Hyndman's Mcomp R package on CRAN. Open task: beat 12.37 without touching the test values.

## What counts as a win

Saved forecasts for all 3,003 M3 series at the official horizons whose average sMAPE, computed with the M3 definition (200/H times the sum of |y - f| / (y + f)) averaged over all series and horizons as in arXiv:1905.10437 Appendix C.2, against the test values in the CRAN Mcomp package, is STRICTLY LOWER (direction: min) than 12.37 and than any lower credible published M3 average the skeptic finds. LEAK RULE: a frozen, hashed script rerun in a fresh environment that has only the training parts of the series (the $xx test component stripped); all choices fixed on holdouts carved from the training parts; no pretrained component whose documented training data include any M3 series.

## Partial wins

- **p1:** Under the full-win leak rule, an average sMAPE (horizon-weighted as in arXiv:1905.10437 equation 5) strictly below 12.71 (EXP) with a method containing no neural network.
- **p2:** Under the full-win leak rule, with all 3,003 series forecast, a subset sMAPE strictly below the best known value for Yearly (15.18, LGT, arXiv:2309.13950 Table 4), Quarterly (8.84), Monthly (13.11) or Other (4.19) (arXiv:1905.10437 Table 14).

## How a win is checked

Install Mcomp from CRAN, export M3 train and test parts, rerun the frozen script with test parts removed, score with an independent sMAPE script, and as a scorer check confirm it gives Theta's 13.01 (horizon-weighted, equation 5) on the original M3 THETA forecasts shipped in Mcomp's M3Forecast object. A fresh forecast::thetaf run is a different implementation and will not reproduce 13.01 exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1905.10437>

## Sources

- <https://arxiv.org/abs/1905.10437>
- <https://arxiv.org/abs/2309.13950>
- <https://cran.r-project.org/package=Mcomp>
- <https://github.com/robjhyndman/Mcomp>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Combinations of Theta variants, damped ETS and a small global network, with weights chosen on the last training horizon of each series.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- M3 full series, including test values, sit in Monash, LOTSA and many other pretraining corpora.
- The forecasters.org M3 page sat behind a bot check on 2026-10-30; use the CRAN package.
- No 2024-2026 literature sweep could be run on 2026-10-30; check for lower published averages first.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/m3-competition-beat-best-published-smape.md
```

Already set up? Say `run V3R1T4S on m3-competition-beat-best-published-smape`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `m3-competition-beat-best-published-smape`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
