# Random sequential adsorption on the square lattice: more digits of the NN-exclusion jamming coverage 0.3641323(1), and the dimer value (0.906820 vs 0.906823)

⚛️ **Physics** · standard · tractability ★★★☆☆ · compute: laptop-days (exact time-series expansions by depth-first enumeration, plus event-driven Monte Carlo) · open as of 2026-10-30

## The problem

In random sequential adsorption (RSA) particles land irreversibly at random and stick if allowed, until a jammed state. With nearest-neighbour exclusion on the square lattice (equivalently the density of a random greedy maximal independent set of Z^2), the jamming coverage has no closed form, unlike Flory's 1D result. Chee Kwan Gan and Jian-Sheng Wang (J. Chem. Phys. 108 (1998) 3010, doi 10.1063/1.475687, arXiv cond-mat/9710340) computed exact time-series coefficients: 21 terms for NN-exclusion and 18 for dimers on the square lattice, 24 and 22 on the honeycomb lattice. Their depth-first algorithm ran in under 60 MB per machine, up to 120 hours each; the older algorithm needed 706 MB already at order 14. Pade analysis gave 0.3641323(1) (square NN-exclusion), 0.37913944(1) (honeycomb NN-exclusion) and 0.906823(2) for dimers on the square lattice. For dimers this compares with the Monte Carlo 0.906820(2) of Jian-Sheng Wang and Ras Pandey (PRL 77 (1996) 1773) and a biased earlier estimate 0.9068088(4). Asher Baram and Marshall Fixman gave 0.3641330(5) (J. Chem. Phys. 103 (1995) 1929). The Wikipedia 'Random sequential adsorption' tables (checked 2026-10-30) list nothing more precise. The 1998 series were limited by 1998 compute; today's multicore machines allow many more exact terms.

## What counts as a win

Success means either (A) the square-lattice NN-exclusion jamming coverage with stated uncertainty at most 2e-8 (5 times smaller than Gan-Wang's 1e-7), or (B) the square-lattice dimer jamming coverage with uncertainty at most 5e-7, such that (a) two methods agree within combined uncertainty (exact series longer than Gan-Wang's analysed with Pade or differential approximants, and event-driven Monte Carlo on large tori with finite-size checks), (b) the series coefficients are released as exact integers and reproduce all Gan-Wang Table I coefficients exactly, (c) for (B) the claim states its distance in combined sigma to both 0.906820(2) and 0.906823(2), and (d) a literature search before claiming (physics and probability literature on random greedy independent sets) finds no better published value. Direction: smaller uncertainty.

## Partial wins

- **p1:** Exact series for the vacancy probability of NN-exclusion RSA on the square lattice beyond order 21 (at least 26 terms), reproducing Gan-Wang's 21 coefficients exactly, checked by a second program.
- **p2:** Exact series for dimer RSA on the square lattice beyond order 18 (at least 23 terms), reproducing Gan-Wang's coefficients exactly.
- **p3:** A Monte Carlo jamming coverage for NN-exclusion RSA on the square lattice with uncertainty <= 5e-8 and an explicit finite-size study, consistent or inconsistent with 0.3641323(1) at 3 sigma.

## How a win is checked

Skeptic (< 1 hour): recompute the first 10-12 series coefficients by brute-force enumeration of local histories and compare exactly with the released list; rerun the approximant analysis; rerun the Monte Carlo at two sizes with fresh seeds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Random_sequential_adsorption>

## Sources

- <https://en.wikipedia.org/wiki/Random_sequential_adsorption>
- <https://arxiv.org/abs/cond-mat/9710340>
- <https://arxiv.org/abs/cond-mat/9605038>
- <https://doi.org/10.1063/1.469717>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- NN-exclusion RSA jamming is a local function of i.i.d. arrival times (a site is occupied iff no earlier-arriving neighbour is occupied), so the coverage is an exact integral over decreasing paths; this gives an independent expansion and a fast Monte Carlo with no time stepping.
- Modular arithmetic and memoised local configurations (Gan-Wang's depth-first tree) parallelise well across cores.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Wikipedia RSA page has had no content edits since 2023; probability papers on greedy independent sets of Z^2 may hold newer numbers not listed there. Search them before claiming.
- Series are in t, in y = 1 - e^-t or in u = e^-t - 1 depending on the paper; convert before comparing coefficients.
- Continuum RSA of disks (0.547...) is a different problem and not covered here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/lattice-rsa-jamming-coverage-square-lattice.md
```

Already set up? Say `run V3R1T4S on lattice-rsa-jamming-coverage-square-lattice`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lattice-rsa-jamming-coverage-square-lattice`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
