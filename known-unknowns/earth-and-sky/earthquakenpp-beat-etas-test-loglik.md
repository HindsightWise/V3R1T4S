# EarthquakeNPP: beat the ETAS benchmark's per-event test log-likelihood on a real California catalog

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-hours (catalogs of 10^4 to 10^5 events ship pre-processed in the repo; ETAS inversion with the etas package and small NPPs both train on CPU) · open as of 2026-10-30

## The problem

EarthquakeNPP (Samuel Stockman, Daniel Lawson, Maximilian Werner, Univ. Bristol; TMLR 2026, arXiv 2410.08226v3) standardises earthquake forecasting as spatio-temporal point-process modelling on 7 real California catalogs with fixed chronological burn-in/train/val/test periods: ComCat_25 (M2.5+), SCEDC_20/25/30, QTM SanJac_10 and SaltonSea_10 (Ross et al. 2019 template-matching catalog) and WHITE_06 (White et al. 2019). Its ETAS baseline (Leila Mizrahi's etas package, fitted on train+val) gives these mean per-event test log-likelihoods (temporal + spatial = total = -nll, nats/event; Experiments/ETAS/output_data_*/ll_scores.json): ComCat_25 1.4343 + -8.6898 = -7.2554; SCEDC_20 2.5410 + -7.5342 = -4.9932; SCEDC_25 2.1394 + -7.5380 = -5.3986; SCEDC_30 1.8403 + -7.6206 = -5.7803; SanJac_10 1.1325 + -5.3981 = -4.2656; SaltonSea_10 2.3320 + -2.3151 = +0.0170; WHITE_06 2.0211 + -4.2611 = -2.2400. The paper finds that none of the five NPPs it tested beats ETAS. Of the three with a likelihood (NSTPP, DeepSTPP, AutoSTPP; SMASH and DSTPP are generative and were scored by CSEP consistency tests, which also favour ETAS), the best mean total per dataset in Experiments/out_metrics.csv is AutoSTPP's, 1.06 to 1.41 nats/event below ETAS, mostly in the spatial term (e.g. WHITE_06 -3.391, SaltonSea_10 -1.286). One DeepSTPP seed edges ETAS's temporal term on SaltonSea_10 (2.340 vs 2.332), so temporal-only gains are not wins. Open task: any model, neural or a better classical one, with a higher total test log-likelihood than ETAS on a real dataset.

## What counts as a win

Saved, runnable code (fixed seeds, weights or fitted parameters) that, for one of the 7 real datasets (not the synthetic ETAS_25 or ETAS_incomplete_25, where ETAS is the generating model), is fitted only on events before the dataset's test start (burn-in, train and validation periods as defined in the repo's dataset notebooks) and evaluated on the official test period with the paper's metric: mean log-likelihood per test event of the temporal plus spatial terms, each event conditioned on the full history including auxiliary events, with the temporal integral term included. The total must be strictly greater (direction: max) than the ETAS total for that dataset in Experiments/ETAS/output_data_ < dataset > /ll_scores.json at https://github.com/ss15859/EarthquakeNPP re-fetched live immediately before claiming, by at least 0.02 nats/event, for the mean over 3 seeds with every seed above ETAS; and greater than any total test log-likelihood for the same dataset and split reported in a paper from the last 24 months (search 'EarthquakeNPP'). The spatial density must integrate to 1 over the dataset's region (checked numerically to within 1e-3).

## Partial wins

- **p1:** Re-run the repo's ETAS (invert_etas.py, predict_etas.py) and reproduce ll_scores.json totals to within 0.005 on 3 datasets, then beat the best NPP total in out_metrics.csv (AutoSTPP 3-seed mean) by at least 0.3 nats/event on those 3 datasets.
- **p2:** A higher spatial test log-likelihood than ETAS (by at least 0.02 nats/event, 3-seed mean) on any real dataset, with a temporal term no more than 0.05 below ETAS's.
- **p3:** A model that beats ETAS's total test log-likelihood on any real dataset by at least 0.02 nats/event for the 3-seed mean, with every seed above ETAS, meeting every rule of the success criterion except the 24-month literature condition.

## How a win is checked

Skeptic clones the repo, runs the claimed code from the repo's pre-processed CSVs with the documented splits, recomputes per-event temporal and spatial log-likelihoods with an independent script (numerical integration of the intensity over the test window and of the spatial density over the region polygon), reruns the ETAS scripts for the comparator, and checks that no test-period event enters fitting (code reading plus refitting with test events deleted gives identical parameters). About 1-3 hours on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ss15859/EarthquakeNPP>

## Sources

- <https://github.com/ss15859/EarthquakeNPP>
- <https://arxiv.org/abs/2410.08226>
- <https://raw.githubusercontent.com/ss15859/EarthquakeNPP/main/Experiments/out_metrics.csv>
- <https://github.com/lmizrahi/etas>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: better ETAS variants: anisotropic or finite-fault spatial kernels for large events, spatially varying background from smoothed seismicity, magnitude-dependent productivity fitted per region.
- Conventional: hybrid ETAS + neural background (ETAS triggering kept, NPP models only the non-stationary background, where the paper finds NPPs help).
- Cross-domain import (epidemiology): Hawkes models with covariate-driven reproduction numbers, as in COVID-19 nowcasting.
- Cross-domain import (crime forecasting): self-exciting point processes with learned anisotropic kernels (Mohler et al.) carried over to fault-aligned aftershock zones.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Temporal-only gains do not count: DeepSTPP already edges ETAS's temporal term on SaltonSea_10 in one seed while losing more than 1.8 nats/event spatially.
- The synthetic ETAS datasets are generated by ETAS; beating it there is not possible in expectation and is excluded. Japan_Deprecated is not one of the 7 real datasets.
- Leakage: fitting the background rate or kernels on the full catalog (including the test period) inflates the score; refit with test events deleted.
- Spatial densities that do not integrate to 1 over the region (truncated flows, unnormalised kernels) produce spuriously high spatial log-likelihoods.
- ETAS was fitted on train+val in the repo; Appendix C shows train-only fitting changes little, so compare against the published file, not a weaker re-fit.
- No 2024-2026 literature search could be run when this entry was drafted or audited (search budget exhausted on 2026-10-30); before claiming, look for papers citing arXiv 2410.08226 that report EarthquakeNPP test log-likelihoods.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/earthquakenpp-beat-etas-test-loglik.md
```

Already set up? Say `run V3R1T4S on earthquakenpp-beat-etas-test-loglik`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `earthquakenpp-beat-etas-test-loglik`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
