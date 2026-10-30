# Robbins' problem (full-information expected rank): a certified bound beating 1.908 <= V <= 2.32614

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-days (dynamic programming over truncated-loss states with interval arithmetic, or rigorous evaluation of history-dependent stopping rules) · open as of 2026-10-30

## The problem

X_1, ..., X_n are i.i.d. Uniform[0,1], observed one at a time; you must stop on exactly one, with no recall, and you lose its absolute rank among all n. V(n) is the minimal expected rank over all stopping rules, V(n) is nondecreasing, and V = lim V(n) (Robbins' problem, the 'fourth secretary problem'). The optimal rule depends on the whole history (Bruss-Ferguson 1996; Gnedin 2007) and V is unknown. Lower bound 1.908: Bruss and Ferguson (J. Appl. Prob. 30 (1993) 616-626), from the loss truncated at rank 5 (V >= V_n(5)). Upper bounds come from explicit rules: memoryless threshold rules give 2.3318 (Assaf and Samuel-Cahn, Adv. Appl. Prob. 28 (1996)), Bruss and Swan (2009) 2.33183 in continuous time, and Meier and Sogner (J. Appl. Prob. 54 (2017) 331-336) state an expected rank of 2.32614 for a rank-plus-threshold rule in Gnedin's Poisson embedding, the smallest published value. Goldenshluger and Malinovsky (arXiv:2610.33701, 24 Oct 2026) report that rule's value as 2.33044, and Brice, Bruss, Majumdar and Raskin (arXiv:2608.27419, Aug 2026) still quote 2.3318 and 1.908. Exact V(n) is known only for n <= 4 (Dendievel and Swan 2016, V(4) ~ 1.4932). For 5 <= n <= 100 Brice et al. give MDP-abstraction upper approximations (V(5) about 1.57128), and Goldenshluger-Malinovsky give uncertified DP approximations for n <= 10 (V(5) ~ 1.5707); neither gives certified values or new limit bounds. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires either (i) a fully specified stopping rule (it may depend on the whole history) together with a rigorous enclosure, by interval arithmetic or exact computation plus a written error analysis, of lim sup_n of its expected rank (or of its value in Gnedin's Poisson embedding, with the transfer to V proved or cited), whose upper end is STRICTLY BELOW (direction: min) the smallest upper bound published at verification time (2.32614, Meier-Sogner 2017, on 2026-10-30, used as the bar even though Goldenshluger-Malinovsky 2026 report that rule's value as 2.33044) by at least 1e-4; or (ii) a rigorous lower bound V >= L with L STRICTLY ABOVE (direction: max) the best published lower bound at verification time (1.908 on 2026-10-30) by at least 1e-4, from a finite computation (e.g. V >= V(n) >= truncated-loss values) whose every rounding is in the safe direction and whose reduction is proved. Simulation estimates, and finite-n values that are not bounds on the limit, never count.

## Partial wins

- **p1:** A rigorous enclosure of V(5) of width at most 1e-4, both ends certified with directed rounding, together with the optimal rule's description, computed by two independent programs, provided no certified V(5) of that width is published at verification time (Brice et al., arXiv:2608.27419, report 1.57128 and Goldenshluger-Malinovsky, arXiv:2610.33701, report 1.5707, both uncertified).

## How a win is checked

For upper bounds, re-derive the expected-rank integral for the submitted rule from its definition, evaluate it with interval arithmetic (and spot-check by Monte Carlo at large n as a sanity test only), and check the n -> infinity limit argument. For lower bounds, re-run the truncated-loss DP with directed rounding and check the inequality chain V >= V(n) >= bound. Calibrate by reproducing Bruss-Ferguson's 1.908 and the memoryless value 2.3318.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33701>

## Sources

- <https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/new-strategy-for-robbins-problem-of-optimal-stopping/C17885B33CCB77023382F5DB1AFDBAA0>
- <https://arxiv.org/abs/2610.33701>
- <https://arxiv.org/abs/2608.27419>
- <https://doi.org/10.1239/jap/1110381374>
- <https://doi.org/10.1239/jap/1238592113>
- <https://doi.org/10.2307/1428183>
- <https://en.wikipedia.org/wiki/Robbins%27_problem>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Rules that depend on the current value and the number of earlier values below a moving threshold (one extra statistic beyond memoryless) can be evaluated by a two-dimensional integral recursion.
- Lower side: Bruss-Ferguson truncate the loss at a fixed rank; modern hardware allows larger truncation levels and larger n in the same DP, provided every step is interval-certified.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The published upper values disagree: Meier-Sogner's abstract says 2.32614, Goldenshluger-Malinovsky (2026) report the same rule as 2.33044, Brice-Bruss et al. (2026) quote only 2.3318, and Wikipedia quotes 2.329. The bar is the smallest, 2.32614; re-read Meier-Sogner's paper and check newer citations of it and of Bruss-Ferguson 1993 before claiming.
- The expected-rank value of a rule must be its n -> infinity limit (or a bound valid for all n); a value at one finite n is not an upper bound on V, while a certified lower bound on any V(n) is a lower bound on V.
- The 2026 MDP and DP tables (Brice et al., Goldenshluger-Malinovsky) are approximations without certified error bounds; reproducing them is calibration, not a win.
- Do not confuse with the Chow-Robbins S_n/n game or the no-information expected-rank problem (solved: 3.8695, Chow et al. 1964).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/robbins-problem-minimal-expected-rank-bounds.md
```

Already set up? Say `run V3R1T4S on robbins-problem-minimal-expected-rank-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `robbins-problem-minimal-expected-rank-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
