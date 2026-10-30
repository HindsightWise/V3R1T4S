# New planetary-anomaly candidate in public KMTNet 2024-2025 microlensing light curves, absent from the KMTNet planet list and the archives

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (3,348 KMTNet 2025 events plus 3,441 from 2024; pySIS photometry is KB-MB per event; binary-lens grid searches take CPU-hours per anomalous event) · open as of 2026-10-30

## The problem

The Korea Microlensing Telescope Network (KASI; Kim et al. 2016, JKAS 49, 37) posts pySIS photometry of every event it finds from its three sites. Under its data policy the data become public on 1 July of the following year, so the 2024 season (3,441 events, public since 2025-07-01) and the 2025 season (3,348 events in listpage.dat, public since 2026-07-01) may now be analysed and published, with the requested acknowledgement. The KMTNet AnomalyFinder series (Zang et al. 2021, 2022; Hwang et al. 2022; Gould et al. 2022; Jung et al. 2022, 2023, and later papers up to paper XIII on the 2021 prime fields, arXiv:2605.17053) searched earlier seasons systematically; 2024-2025 planets so far appear only in individual and small-batch papers. The KMTNet list of microlensing planets (based on exoplanet.eu, updated 2026-04-13) counts 361 microlensing planets, 276 of them with KMTNet data. Open task: a planetary microlensing anomaly (binary lens with q < 0.03) in a 2024 or 2025 KMTNet event that no publication or list reports. A win is a candidate, never 'a planet'.

## What counts as a win

A saved bundle: the event name, the KMTNet pySIS files as downloaded (date and SHA-256), the fit code and the results, showing: (1) a 2L1S model with q < 0.03 beats the best 1L1S model (parallax and finite source allowed) by delta chi^2 > 100 after the errors of each site and field are rescaled to chi^2/dof = 1; (2) a 1L2S (binary-source) model is worse than the 2L1S model by delta chi^2 > 15; (3) the anomaly is covered by at least two KMTNet sites, or by at least 10 points from different nights or fields, and is not caused by flagged or outlying frames; (4) the event is in the KMTNet 2024 or 2025 public event list; (5) the event is absent from the KMTNet planet list PDF, the NASA Exoplanet Archive microlensing table and exoplanet.eu, and an ADS/arXiv search on its KMT, OGLE and MOA names finds no planetary interpretation. All of these are re-fetched immediately before claiming.

## Partial wins

- **p1:** A candidate meeting every criterion except that delta chi^2 is between 50 and 100, or the anomaly is covered by one site only.
- **p2:** A free-floating-planet candidate: a 1L1S event with tE < 0.5 d and the finite-source size rho measured at >= 3 sigma, not in any published free-floating-planet sample (KMTNet, MOA or OGLE) found by the search.
- **p3:** A complete anomaly scan of the 2025 season: every event fitted, residual-anomaly thresholds stated in advance, and the anomaly list released, with at least one anomaly absent from all publications.

## How a win is checked

Skeptic re-downloads the pySIS files for the event, checks the hashes, reruns the 1L1S, 1L2S and 2L1S fits with an independent code (MulensModel or VBMicrolensing), checks the coverage and frame flags, and repeats the list and literature checks. A few hours per event.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://kmtnet.kasi.re.kr/ulens/data/KMTNet_exoplanet_list.pdf>

## Sources

- <https://kmtnet.kasi.re.kr/ulens/>
- <https://kmtnet.kasi.re.kr/ulens/event/2025/listpage.dat>
- <https://kmtnet.kasi.re.kr/ulens/data/KMTNet_exoplanet_list.pdf>
- <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=ML>
- <https://arxiv.org/abs/1806.07545>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: an AnomalyFinder-style scan (Zang et al. 2021): fit 1L1S, then search the residuals with a grid of short Gaussian or Paczynski bumps and dips, then run full 2L1S grids on the survivors.
- Prioritise high-magnification events, where central caustics make planets most detectable.
- Cross-domain import (particle-physics trigger design): set anomaly thresholds by injecting simulated planetary anomalies into real KMTNet baselines and measuring the false-alarm rate on events with no injection.
- Cross-check against OGLE EWS and MOA alert photometry where the event has OGLE or MOA counterparts.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- pySIS online photometry has systematics (bad seeing, cosmic rays, field-edge effects) that mimic short anomalies; demand multi-site or multi-field confirmation.
- Binary-source events (1L2S) produce planet-like bumps; always fit them.
- The KMTNet team analyses these seasons too: check the latest arXiv listings, not only the April 2026 planet list.
- Policy item 5: data for events found only by other teams are not given out; only events in KMTNet's own public list qualify.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/kmtnet-2024-2025-planetary-anomaly-candidate.md
```

Already set up? Say `run V3R1T4S on kmtnet-2024-2025-planetary-anomaly-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kmtnet-2024-2025-planetary-anomaly-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
