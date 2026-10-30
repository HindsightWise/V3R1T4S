# Turan's pure power-sum constant (C_42, Erdos #519): a certified upper bound below 0.6873358063 or an explicit lower bound above 1/2

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours (step-profile optimisation plus Arb/exact-rational certificate checks) · open as of 2026-10-30

## The problem

R_n = min over z_1..z_n in C with max|z_i| = 1 of max_{1<=k<=n} |sum_i z_i^k|, and C_42 = limsup R_n (Tao's optimization constants, page 42a; C_42 is the optimal constant for Erdos problem #519, which asked only whether some absolute c > 0 works and was settled by Atkinson). Lower bounds: Atkinson 1/6 (1961) and pi/8 (1969), Biro 1/2, and Biro (Indag. Math. 11 (2000) 343-358) a computable but uncomputed constant c > 1/2. Upper bounds: Biro 5/6, Harcos 0.69368 (computer search, reported by Biro), and in 2026 asymptotic step-profile certificates: S. Griego 0.6906538 (repo sebastian-griego/turan-c42-certificate v1.0.0), A. Rohrig 0.688983 (PR #184, open), R. Pinho 0.6888863712 = 215276991/312500000 (22 Oct 2026), and D. Koshta 0.6873358063 = 6873358063/10^10 (23 Oct 2026, repo DennisKoshta/c42-turan-power-sum-certificate, commit 8e1797e; first-block cut-off 41/200, 64 middle blocks, Arb at 384/640 bits). All 2026 bounds are unrefereed, asterisked, and give no explicit finite threshold N. Cheer-Goldston (Math. Comp. 1996) computations suggest values near 0.7 for moderate n. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires either (i) an upper bound C_42 <= U with U STRICTLY BELOW (direction: min) the smallest upper bound at verification time on https://teorth.github.io/optimizationproblems/constants/42a.html and in open PRs of teorth/optimizationproblems (0.6873358063 on 2026-10-30), by at least 1e-8, given as an exact rational profile in a written asymptotic reduction (Griego's two-block reduction or a new one with full proof) whose finite hypotheses are verified by two independent checkers (exact rationals and Arb/interval arithmetic); or (ii) a lower bound C_42 >= L from a complete proof whose numerical steps are interval-certified, with L STRICTLY ABOVE (direction: max) both the best explicit lower bound listed at verification time (1/2 on 2026-10-30) and the explicit value of Biro's computable constant c from Indag. Math. 11 (2000) 343-358, once that value has been published or established under p1. Merely evaluating Biro's own constant counts only as p1, not as (ii).

## Partial wins

- **p1:** An explicit, interval-certified numerical value for Biro's computable constant c > 1/2 (Indag. Math. 11 (2000) 343-358), following his proof step by step, provided no explicit value is listed on the 42a page at verification time.
- **p2:** An explicit finite threshold N_0, with a proof whose numerical steps are interval-certified, such that R_n <= 0.6906538 (Griego's 2026 bound) for every n >= N_0 (none of the 2026 asymptotic certificates states a threshold).

## How a win is checked

Re-derive the reduction's finite inequality from the written argument, then evaluate it on the submitted rational profile with exact rationals and independently with python-flint/Arb at >= 384 bits; both must clear the bound with a strictly positive margin. Calibrate by re-running Koshta's and Pinho's published certificates with the same checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/42a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/42a.html>
- <https://www.erdosproblems.com/519>
- <https://github.com/DennisKoshta/c42-turan-power-sum-certificate>
- <https://github.com/rpinho/c42-certificate>
- <https://github.com/sebastian-griego/turan-c42-certificate>
- <https://github.com/teorth/optimizationproblems/pull/184>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Free the block boundaries in Koshta's profile (non-uniform middle blocks) and optimise the cut-off jointly with the block heights by LP in the rational profile parameters.
- For the lower side, Biro's 2000 argument is constructive: implement its constant first (p1), then look for the step that loses the most.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 2026 bounds are asymptotic reductions with no explicit N; a numerically small max |s_k| for one finite n is not an upper bound on the limsup.
- Several AI agents are improving this constant weekly; re-fetch the 42a page and the PR list right before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/turan-pure-power-sum-c42-upper-bound.md
```

Already set up? Say `run V3R1T4S on turan-pure-power-sum-c42-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-pure-power-sum-c42-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
