# Decisive stacked evidence for the (l=2, m=0) memory-carrying mode across all GWTC-4.0 and GWTC-5.0 binary black holes

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: needs cluster (about 190 events x 2 waveform models x 2 seeds of bilby/dynesty nested sampling with a time-domain waveform; each run takes hours to a day on many cores) or laptop-weeks; inputs are GWOSC strain and the LVK PE releases (PSDs, calibration envelopes) · open as of 2026-10-30

## The problem

Gravitational-wave memory, the permanent displacement left after a burst of radiation, is a nonlinear prediction of general relativity that has not been detected. It lives mainly in the (l=2, m=0) spherical-harmonic mode, which also has an oscillatory ringdown part. Rossello-Sastre, Husa, Xu, Valencia, Llobera-Querol and Ramos-Buades (arXiv:2607.04909, 2026-07-06) compared IMRPhenomTHM_20 (with the full (2,0) mode) against IMRPhenomTHM (without it) for the 84 GWTC-4.0 binary black holes plus 6 GWTC-5.0 events chosen for high SNR or spin. They used bilby/dynesty with nlive 1000, naccept 60, dlogz 0.05 and two seeds. The stacked sum of log10 Bayes factors over GWTC-4.0 is 1.38 +/- 0.79: strong on Jeffreys' scale but not decisive. The best single event is GW230814_230901 at 0.63 +/- 0.09. They estimate that decisive evidence needs about 166 (+82/-55) events, and they left the O4b events out of the stack because those were not chosen in an unbiased way. Mitman, Isi and Farr (arXiv:2605.27500) use hierarchical inference on GWTC-5.0 to constrain the memory enhancement factor to 0.26 (+4.09/-4.08), and warn that naively multiplying Bayes factors across events can mislead. GWTC-5.0 (arXiv:2605.27225) adds 104 O4b candidates with FAR < 1/yr and full PE releases. Open task: decisive (log10 B >= 2) evidence for the (2,0) mode from a complete, unbiased GWTC-4.0 + GWTC-5.0 stack, robust to waveform choice and calibrated against simulated memory-free data.

## What counts as a win

Saved per-event results (configuration files, priors, the PSDs and calibration envelopes used, evidences with sampling errors for both models and both seeds, and the code) for a pre-registered, complete event list: every binary black hole candidate with FAR < 1/yr and an LVK PE release from O4a (the 84 GWTC-4.0 BBHs analysed in arXiv:2607.04909; PE release Zenodo 17602505) and from O4b (the 104 GWTC-5.0 candidates; PE releases Zenodo 20348005 and 20348006), 188 events; O1-O3 events are not part of the list. No selection by SNR, spin or Bayes factor is allowed; an event may be dropped only by a data rule declared before any (2,0)-mode result is seen (for example, events the LVK analysed with glitch-mitigated data, Table 3 of arXiv:2508.18079 and Table 4 of arXiv:2605.27090, when that data is not public). The events are analysed on GWOSC strain with IMRPhenomTHM_20 vs IMRPhenomTHM (or a newer model pair that differs only by the (2,0) mode), at settings no looser than those of arXiv:2607.04909 (dynesty, nlive 1000, naccept 60, dlogz 0.05, two seeds), such that: (1) the stacked sum of per-event log10 B is at least 2.0 (direction: max), and its 1-sigma lower bound (the sum minus the quadrature sum of per-event errors) is at least 1.5; (2) for the 10 events contributing most, a second waveform family that contains the (2,0) mode, run with and without it (for example an NR surrogate or an effective-one-body model with m = 0 modes), gives a summed log10 B at least half of the first family's sum for those events; (3) null calibration: for each of the 5 largest contributors, at least 20 injections of the memory-free model at that event's maximum-likelihood parameters into GWOSC noise from nearby times, analysed identically, give log10 B values whose 95th percentile lies below that event's observed value; and (4) the stacked value exceeds every published stacked (2,0)-mode or memory Bayes factor for LVK data, with arXiv re-fetched live immediately before claiming.

## Partial wins

- **p1:** The complete, unbiased GWTC-4.0 + GWTC-5.0 stack (event-list and settings rules met) with stacked log10 B of at least 1.0 and null calibration (3) passed, published as a per-event table: the first unbiased stack to include O4b.
- **p2:** A single event with log10 B >= 1.0 for the (2,0) mode under both waveform families and null calibration (3) for that event; the current best single event is at 0.63 +/- 0.09.

## How a win is checked

Skeptic reruns the per-event analyses from the saved configurations with new seeds for 10 randomly chosen events plus the 5 largest contributors, checks each log10 B lies within 2 sigma of the saved value, recomputes the stacked sum from the saved table, checks the event list against the GWTC-4.0 and GWTC-5.0 tables and the pre-registration, and reruns 5 of the null injections. Days on a cluster or a large workstation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:memory+AND+abs:gravitational&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://arxiv.org/abs/2607.04909>
- <https://arxiv.org/abs/2605.27500>
- <https://arxiv.org/abs/2605.27225>
- <https://zenodo.org/records/17602505>
- <https://zenodo.org/records/20348005>
- <https://zenodo.org/records/20348006>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: rerun the published bilby setup on every O4b BBH with FAR < 1/yr, add the results to the 84 GWTC-4.0 runs, and reuse the LVK PSDs and calibration envelopes.
- Importance-reweight the released LVK posterior samples to the (2,0) model, as Hubner et al. did for memory in GWTC-1 and GWTC-2, to get cheap Bayes factors, and rerun full sampling only where the reweighting efficiency is low.
- Cross-domain import (medical meta-analysis): random-effects stacking and leave-one-out influence checks to show the evidence is not driven by one or two events.
- Hierarchical alternative (Mitman, Isi and Farr): report the memory-enhancement-factor posterior alongside the stacked Bayes factor.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Selecting events by SNR, spin or a first-pass Bayes factor biases the stack; freeze the event list before seeing any (2,0)-mode result.
- Waveform systematics in the dominant modes can masquerade as (2,0)-mode evidence at high SNR (GW250114_082203 has network SNR 76.9); criterion (2) exists for this.
- Nested-sampling evidence errors are often underestimated; use two seeds and the tighter dlogz, and report per-event errors.
- Mitman, Isi and Farr show that naive products of Bayes factors can favour wrong conclusions; the stacked number is one line of evidence, and the null calibration is the guard.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/gw-memory-20-mode-stacked-bayes-factor.md
```

Already set up? Say `run V3R1T4S on gw-memory-20-mode-stacked-bayes-factor`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gw-memory-20-mode-stacked-bayes-factor`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
