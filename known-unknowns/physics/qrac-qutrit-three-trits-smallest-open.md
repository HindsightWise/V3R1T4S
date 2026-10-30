# Smallest unsolved quantum random access code: three trits into one qutrit (n = d = D = 3), best 0.69715 vs bounds 0.69853 (projective only) and about 0.699 (general POVMs, floating-point)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-hours (seesaw searches; exact-arithmetic SDP dual certificates for upper bounds) · open as of 2026-10-30

## The problem

In a quantum random access code (QRAC) with n variables over a d-letter alphabet encoded into a D-dimensional quantum system, Alice prepares rho_x for x in [d]^n, Bob receives i in [n] and measures a d-outcome POVM {M^i_a}; the average success probability is ASP = (1/(n d^n)) sum_x sum_i Tr(rho_x M^i_{x_i}). Exact optima are known only for a few cases, e.g. (n,d,D) = (2,d,d) with 1/2(1 + 1/sqrt d) and (3,2,2) with 1/2(1 + 1/sqrt3). Mate Farkas, Nikolai Miklin and Armin Tavakoli (Quantum 9, 1643 (2025), arXiv:2312.14142) state that the smallest unsolved case is n = d = D = 3 and that whether MUB measurements are optimal there is unresolved. Their best lower bound is 0.69715 (best of 100 seesaw runs; three MUB measurements with optimal states give about 0.6971), their analytic upper bound (Corollary 1) is 0.71823, and dimension-restricted SDP relaxations (QDimSum) give 0.69853 at level 2+MMM+rhoMM, but only under the assumption of projective measurements. The best numerical bound valid for general POVMs is the almost-qudit SDP of Jef Pauwels, Stefano Pironio, Erik Woodhead and Armin Tavakoli (PRL 129, 250504 (2022), arXiv:2208.07887), plotted but not tabulated in arXiv:2312.14142 Fig. 2 at about 0.699 for D = 3 (read off the plot; floating-point, no exact certificate). Table 2 of arXiv:2312.14142 also lists open seesaw-versus-bound gaps for other n = 3 cells, e.g. (d,D) = (3,4): 0.72567 vs 0.77778, (3,5): 0.76241 vs 0.83024, (4,4): 0.64434 vs 0.66667.

## What counts as a win

Success means EITHER (a) 27 density matrices on C^3 and three 3-outcome POVMs (positive semidefinite, summing to the identity, given exactly or to 30 digits and verified in exact or interval arithmetic) whose ASP for n = d = D = 3, computed by the formula above at 40 digits, is STRICTLY GREATER (direction: max) than 0.69715, the best value in arXiv:2312.14142 (re-fetched live before claiming, plus an arXiv check for newer results), by at least 1e-5 (ASP >= 0.69716); OR (b) a proven upper bound on the ASP valid for ALL states and POVMs in dimension 3 that is STRICTLY LESS (direction: min) than 0.69853, given as an exact (rational or algebraic) dual certificate or a machine-checked proof.

## Partial wins

- **p1:** A proven upper bound of at most 0.6990 on the ASP for n = d = D = 3, valid for general POVMs, given as an exactly verified certificate (a rational SDP dual whose feasibility and value are checked in exact arithmetic, for a relaxation that does not assume projective measurements) or as a machine-checked proof. This is the first rigorous POVM-valid bound at the level of the floating-point Pauwels et al. value.
- **p2:** For another n = 3 cell of the arXiv:2312.14142 table with (d,D) in {(3,4), (3,5), (4,4), (4,5), (2,3)}, an explicit strategy beating the tabulated seesaw value by at least 1e-5, verified as in (a).

## How a win is checked

(a) Check each rho_x has unit trace and eigenvalues >= 0 and each POVM element is PSD with sum I (exact or interval arithmetic after rationalising); compute ASP in mpmath. Sanity-check the formula on the known (2,3,3) optimum 1/2(1 + 1/sqrt3) = 0.78868 before comparing. (b) and p1: verify the dual certificate identity exactly (rational SDP dual feasibility and value), confirming that the relaxation used does not assume projective measurements, or re-run the machine-checked proof.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2312.14142>

## Sources

- <https://arxiv.org/abs/2312.14142>
- <https://quantum-journal.org/papers/q-2025-02-25-1643/>
- <https://arxiv.org/abs/2208.07887>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 0.69853 SDP value assumes projective measurements; using it as a general bound, or comparing a POVM-valid bound against it without saying so, is wrong.
- Normalisation: ASP averages over all d^n inputs and n questions.
- Seesaw runs stall in local optima (the paper notes this for some cells); the 1e-5 margin guards against rounding of the 5-decimal table, not against bugs.
- Do not confuse this with qubit QRACs or the n = 2 family, which are solved.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/qrac-qutrit-three-trits-smallest-open.md
```

Already set up? Say `run V3R1T4S on qrac-qutrit-three-trits-smallest-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qrac-qutrit-three-trits-smallest-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
