# Small 3-graph Turán and codegree-squared densities: beat a bound in the Lidický-Volec 2026 table (K6, K7, K5^-, K5^=, K5^ < , J4, J5, F4,2, F4^-,2)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for the lower-bound side (pattern and blow-up searches); upper-bound wins need 7-vertex flag programs, which took 145-440 GB RAM per cell with the Lidický-Volec solver (their Table 3), since 6-vertex programs only reproduce the prior bounds · open as of 2026-10-30

## The problem

Table 2 of Lidický and Volec, 'Solving Large SDPs from Flag Algebra Problems' (arXiv:2610.33850, 24 Oct 2026), lists for small 3-graphs F the best lower bound, the previous upper bound and a new certified upper bound for both the Turán density pi(F) and the codegree-squared density pi_l2(F) (the l2 setting of Balogh, Clemen and Lidický, arXiv:2108.10406 v3). Examples: K6 0.84 vs 0.849270 (l2 0.7348 vs 0.735792); K7 0.888888 vs 0.897843; K5^- 0.602673 (Liu-Schülke-Wang-Yang-Zhang, arXiv:2410.08921) vs 0.632498; K5^= 0.58656 vs 0.602768; K5^< 0.555555 vs 0.571371; J4 0.5 vs 0.502135; J5 9/14 vs min(0.64475, 0.652485); F4^-,2 86/175 vs 0.493024; F4,2 0.618782 vs 0.619154. Certificates and code: lidicky.name/pub/lpsdp/, github.com/BLL4/lpsdp. The authors stopped runs before optimality. Cells for K4, K4^-, K5 and C5 are separate bank targets and are excluded here, as are cells already exact (Fano plane, l2 of K4 and K5).

## What counts as a win

Success means, for some cell (F, pi or pi_l2) of arXiv:2610.33850 Table 2 other than K4, K4^-, K5, C5, the Fano plane and the l2 cells of K4 and K5, EITHER (a) a certified upper bound STRICTLY LESS (direction: min) than the smallest upper bound for that cell among Table 2's prior and new columns, the latest arXiv:2108.10406 version and any later paper found at claim time, delivered as a flag-algebra certificate with exact rational or rigorous interval PSD verification (or a compiling Lean 4 proof); OR (b) an explicit F-free construction (finite pattern, optional recursion with written proof) whose exactly computed limiting density (or normalised codegree-squared sum) is STRICTLY GREATER (direction: max) than the cell's lower bound. F must be exactly the 3-graph defined in arXiv:2610.33850 or arXiv:2108.10406.

## Partial wins

- **p1:** Two cells: wins under the main criterion in two different cells of the eligible table (counted once per cell).
- **p2:** A complete Lean 4 proof (no sorry, no new axioms) of one of the new Table 2 upper bounds for an eligible cell, formalised from the published Lidický-Volec certificate, provided no Lean formalisation of it is public at claim time.

## How a win is checked

For upper bounds: independently enumerate F-free 3-graphs on n vertices up to isomorphism, recompute densities (or the codegree-squared objective) and flag products, verify PSD matrices exactly or by interval Cholesky, and check the inequality on every graph. For constructions: brute-force F-freeness of the pattern under all vertex maps (a blow-up contains F iff some map of V(F) to parts sends every edge of F to an edge of the pattern), check the recursion argument, and compute the limiting density symbolically or by exact optimisation over part weights. Compare against the live arXiv:2610.33850 and arXiv:2108.10406 tables.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33850>

## Sources

- <https://arxiv.org/abs/2610.33850>
- <https://arxiv.org/html/2610.33850v1>
- <https://lidicky.name/pub/lpsdp/>
- <https://github.com/BLL4/lpsdp>
- <https://arxiv.org/abs/2108.10406>
- <https://arxiv.org/abs/2410.08921>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lower-bound side: K5^- (0.6027 vs 0.6325) and K7 (0.8889 vs 0.8978) have the widest gaps; search weighted blow-ups of small patterns and iterated constructions.
- Upper-bound side: rerun the lpsdp cutting-plane solver longer from the published checkpoints.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For J5 the 2026 new bound (0.652485) is weaker than the prior 0.64475; beat the smaller one.
- Several cells mix definitions (K5^=, K5^ < , J4): take the exact edge sets from the papers before computing.
- Numerical SDP values without rigorous rounding do not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/turan-3-graph-density-table-lidicky-volec.md
```

Already set up? Say `run V3R1T4S on turan-3-graph-density-table-lidicky-volec`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-3-graph-density-table-lidicky-volec`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
