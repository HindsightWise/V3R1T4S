# 2018 WFIRST/Roman Microlensing Data Challenge: one automated pipeline that recovers more planetary (s, q) solutions than all four entries

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-days (293 two-band light curves, about 100 MB; binary-lens fits with public codes such as MulensModel, pyLIMA or VBMicrolensing take minutes to hours per event) · open as of 2026-10-30

## The problem

The 2018 Microlensing Data Challenge (coordinated by Rachel Street, simulations by Matthew Penny; panel Rachel Akeson, Scott Gaudi, Hyungsuk Tak, Eamonn Kerins) released 293 simulated Roman bulge-survey light curves in W149 and Z087: 93 cataclysmic variables, 74 single lenses (free-floating planets included), 83 stellar binary lenses and 43 bound-planet lenses (github microlensing-data-challenge/data-challenge-1; Zenodo 18041245). The full simulation parameters were released in 2019 (Answers/master_file.txt; Jennifer Yee's summary). Four teams entered (contacts Etienne Bachelet for teams 1 and 2, Geoffrey Bryden for team 3, Clement Ranc and Arnaud Cassan for team 4); the entries were released on Zenodo 21235143 (Street et al., July 2026), and the panel graded them qualitatively, noting that classification of subtle anomalies stayed hard. Scoring the released entries against the truth on 2026-10-30 (low-q set = the 51 events with true q < 0.03; recovered = some listed binary-lens model with |dlog10 q| <= 0.3 and |dlog10 s| <= 0.1, the close/wide s <-> 1/s degeneracy allowed, a listed q > 1 read as 1/q), team 1 recovers 41/51, team 2 32, team 4 12 and team 3 2 (one of them, event 267, listed with q = 3162). Team 1 also lists a q < 0.03 model for 9 events whose truth is not low-q (team 2: 5), recovers 1 of the 3 planets with log10 q < -5 (events 47, 131, 152) and 6 of the 10 low-q events with s > 2, and its first-listed models classify 268/293 events correctly in three classes (variable or flat, single lens, binary lens). The organisers' evaluation code is still being written (commits to June 2026), and no published quantitative ranking exists. Open task: beat every entry with a single frozen pipeline.

## What counts as a win

A saved bundle: a fully automated, frozen pipeline (no per-event human choices; every threshold and prior fixed beforehand and tuned only on light curves the claimant simulated independently) that the skeptic runs on the 293 light curves of Zenodo 18041245. It outputs exactly one model per event: a class, plus s and q (q <= 1, the lighter lens over the heavier) for binary lenses. The pipeline never reads the Answers folder or any team entry. Scoring uses master_file.txt (0-based whitespace columns 46 = q, 47 = s, event-type token, last column = light-curve number) and the rules in the statement. Win, direction max for counts: (a) more than 41 of the 51 low-q events recovered by the single output model; (b) at most 9 events with an output q < 0.03 whose truth is not q < 0.03; (c) three-class accuracy of at least 268/293. All three must hold, and the result must also beat any later quantitative results the organisers publish on the same events (github microlensing-data-challenge/evaluation_code and an ADS/arXiv search for the 2018 Microlensing Data Challenge, re-fetched before claiming).

## Partial wins

- **p1:** Condition (a) alone (more than 41 of 51 low-q events recovered with one output model per event), with at most 15 false low-q outputs.
- **p2:** Three-class accuracy strictly above 268/293 with one output model per event.
- **p3:** Recover at least 2 of the 3 planets with true log10 q < -5 (events 47, 131, 152) within the tolerances; the best entry recovers 1.
- **p4:** Recover at least 8 of the 10 low-q events with true s > 2 (wide planets); the best entry recovers 6.

## How a win is checked

Skeptic downloads the light curves and master_file.txt, checks that the pipeline never opens Answers/ or the entries (sandboxed run), runs it end to end, and scores it and the four Zenodo entries with an independent implementation of the rules. About a day of CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/microlensing-data-challenge/evaluation_code>

## Sources

- <https://github.com/microlensing-data-challenge/data-challenge-1>
- <https://zenodo.org/records/18041245>
- <https://zenodo.org/records/21235143>
- <https://www.microlensing-source.org/resources/data-challenge-2018/>
- <https://www.microlensing-source.org/assets/files/2018_microlensing_data_challenge.pdf>
- <https://github.com/microlensing-data-challenge/evaluation_code>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a PSPL fit with parallax first, then a residual-anomaly detector that seeds a dense (log s, log q, alpha) grid of binary-lens fits, with finite-source magnification from VBMicrolensing.
- Simulation-based inference: train a neural posterior estimator on light curves simulated with the same cadence and noise model, then refine the top modes with chi^2 minimisation.
- Cross-domain import (gravitational-wave template banks): build a stochastic template bank in (s, q, alpha, rho) with a mismatch metric to guarantee coverage of caustic-crossing morphologies.
- Handle the s <-> 1/s and offset degeneracies explicitly: fit both branches and report the lower-chi^2 one.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The truth file is public: tuning thresholds on the challenge events themselves is test-set contamination; tune on independent simulations.
- Team entries list several models per event; the bar counts them generously (any listed model), while the claimant gets one model per event.
- In the simulation the binary frame's x-axis points from the centre of mass to the less massive lens at t0 (data-challenge README); alpha conventions differ between codes.
- About 8 low-q events are stellar-binary simulations with brown-dwarf companions (ombin, q < 0.03); they count in the low-q set.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/roman-microlensing-data-challenge-2018-planet-recovery.md
```

Already set up? Say `run V3R1T4S on roman-microlensing-data-challenge-2018-planet-recovery`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `roman-microlensing-data-challenge-2018-planet-recovery`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
