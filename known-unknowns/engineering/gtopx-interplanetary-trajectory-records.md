# ESA GTOP / GTOPX interplanetary trajectory benchmarks: beat a best-known Delta-v, mass or mission time (Messenger full 1.9579 km/s, Cassini2 8.3830 km/s, Rosetta 1.34334 km/s, GTOC1, Sagas) by 0.1%

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (millions to billions of objective evaluations; each about 10 microseconds in C) · open as of 2026-10-30

## The problem

ESA's Advanced Concepts Team built the GTOP database (2005-2014: Izzo, Vinko, Biscani and others). It poses multiple-gravity-assist spacecraft trajectory design as box-constrained black-box problems (MGA and MGA-1DSM). Martin Schlueter, Neshat, Wahib, Munetomo and Wagner extended it as GTOPX (arXiv 2010.07517; SoftwareX 2021), with one GPL C/C++ source file, gtopx.cpp, and posted best solution vectors. The GTOP pages carry the record histories and have no entry after 2014. Best-known values (GTOPX page and solution files, fetched 2026-10-30, and the GTOPX paper): - Cassini1: 4.9307 km/s (Stickel) - Cassini2: 8.382998066 km/s (Schlueter, Fiala, Gerdts 2009, MIDACO; Danoy et al.'s 2012 8.383091 is higher) - Messenger reduced: 8.629944278 km/s (Biscani, Rucinski, Izzo) - Messenger full: 1.957873052 km/s (Schlueter, Wahib, Maruyama 2014, MXHPC/MIDACO; GTOP rounds to 1.959) - GTOC1: -1,581,950.1318 (Schlueter, Gerdts) - Rosetta: 1.34334419 km/s (GTOPX paper Table 13, local search, refining Vasile and Minisci 2008; the posted rosetta.txt still lists the older 1.343367) - Sagas: 18.187747 years (Vinko, Izzo) - Cassini1-MINLP: 3.5007 (Schlueter, Munetomo) The GTOPX authors believe all values are 'essentially converged', and note that GTOP improvements traditionally need at least 0.1% to count as significant. Neither GTOP nor GTOPX proves any of them optimal. No improvement on these GTOPX values since 2021 was found (a fresh literature search could not be repeated on 2026-10-30).

## What counts as a win

A decision vector x within the instance's box bounds (and satisfying g(x) >= 0 for constrained instances: Cassini1, GTOC1, Sagas, Cassini1-MINLP), evaluated with gtopx.cpp compiled from the GTOPX source, whose objective f(x) is STRICTLY LOWER (direction: min) than the best-known value by at least 0.1% relative. The values are 4.9307, 8.382998066, 8.629944278, 1.957873052, -1581950.1318, 1.34334419, 18.187747 and 3.5007 for instances 1-8; for GTOC1 (negative objective) the requirement is f(x) < -1581950.1318 x 1.001. In the same build, the record vector must reproduce its value: the posted solutions/ < instance > .txt vector for every instance except Rosetta, and for Rosetta the local-search vector of GTOPX paper Table 13 (f = 1.34334419 to the digits shown).

## Partial wins

- **p1:** A strict improvement of at least 1e-5 relative (but under 0.1%) on any of instances 2-8 over the values in the success criterion (Rosetta: 1.34334419), checked the same way.
- **p2:** For Cassini1-MO or Cassini1-MO-MINLP (GTOPX instances 9 and 10), a feasible point that strictly dominates at least one point of the posted paretofront.txt, evaluated with gtopx.cpp.
- **p3:** A from-scratch solve of Messenger full to below 2.0 km/s by code a skeptic reruns from the stated seed, reproducing the vector, where the code reads no record vector and is initialised only from random samples within the bounds.

## How a win is checked

Download gtopx.cpp, main.cpp and the makefile from the GTOPX page, compile, and evaluate the record vector: the posted solutions/ < instance > .txt vector (for example 1.957873051874192 for Messenger full) or, for Rosetta, the GTOPX paper Table 13 local-search vector (1.34334419). Then evaluate the claimed vector, check the bounds from main.cpp and the constraint signs, and compute the relative improvement. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.midaco-solver.com/index.php/about/benchmarks/gtopx>

## Sources

- <http://www.midaco-solver.com/index.php/about/benchmarks/gtopx>
- <https://arxiv.org/abs/2010.07517>
- <https://www.esa.int/gsp/ACT/projects/gtop/>
- <https://www.esa.int/gsp/ACT/projects/gtop/messenger_full>
- <https://www.esa.int/gsp/ACT/projects/gtop/cassini2>
- <https://www.esa.int/gsp/ACT/projects/gtop/rosetta>
- <https://www.midaco-solver.com/data/pub/PDPTA20_Messenger.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Monotonic basin hopping with problem-aware perturbations (resonance-aware time-of-flight jumps for the Mercury legs of Messenger full).
- Pruning by sequential leg decomposition: grid the departure epoch and first legs, then prune with partial Delta-v bounds before full optimisation.
- Massively parallel island-model differential evolution or CMA-ES with restarts (the MXHPC recipe), then a local SQP polish.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- pykep and pygmo 'gym' versions of these missions use different ephemerides or models. Values from them are not comparable: evaluate only with gtopx.cpp.
- The GTOP pages round values (1.959 vs 1.9579 for Messenger full). Compare against the GTOPX solution files.
- Cassini1 and Sagas are considered easy and very likely at their global optima. A 0.1% improvement there almost surely means a bug or a bound violation.
- The TandEM instances are not in GTOPX and their record vectors are mostly not posted (N/A), so they are out of scope here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/gtopx-interplanetary-trajectory-records.md
```

Already set up? Say `run V3R1T4S on gtopx-interplanetary-trajectory-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gtopx-interplanetary-trajectory-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
