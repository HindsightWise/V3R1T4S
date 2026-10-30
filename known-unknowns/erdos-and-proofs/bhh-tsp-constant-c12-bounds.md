# Beardwood-Halton-Hammersley TSP constant (C_12): a certified bound beating 0.6421 <= beta_2 <= 0.861715646305

✏️ **Erdős problems and proofs** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (the current record's integer computation takes about 76 minutes in C on 8 threads at k = 9) · open as of 2026-10-30

## The problem

For n uniform random points in the unit square, the shortest tour length L_n satisfies L_n/sqrt(n) -> beta_2 almost surely (Beardwood-Halton-Hammersley 1959); Held-Karp experiments suggest beta_2 is about 0.71 (Johnson-McGeoch-Rothberg 1996). Upper bounds: 0.92117 (BHH 1959), Steinerberger (2015) 0.92117 - (9/16)e-6, Carlsson-Yu (computer-aided; 2023 preprint < 0.90304, INFORMS J. Comput. 2025 version cited as 0.90380 by later papers), Gaudio-Guan (arXiv:2602.11250, Feb 2026) 0.90367 with band crossovers, Z. Dong and J. Cao (arXiv:2610.02809, 2 Oct 2026) 0.8810 with blocks of six consecutive points in strips, and D. O'Keefe (2026, github.com/devinokeefe/travelling-sales-person-constant-bounds, commit f5d1842; unrefereed) beta_2 <= 0.861715646305 = 5A/(6^10 2^32 9 11) with A = 4430997795015293889, from blocks of ten points in strips of height 2.2/sqrt(n) and the Edmundson-Madansky inequality, checked by Python, C and Rust programs. Lower bounds: 0.625 (BHH), 0.6277 (Gaudio-Jaillet, ORL 2020), and 0.6421 (Dong-Cao 2026, not yet on Tao's page 12a, which still lists 0.6277). Dong-Cao's importance-sampling bounds 0.6536 and 0.8749 hold only with probability 1 - 2e-4 and are not proofs. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires a rigorous bound on beta_2 strictly better than the best rigorous bound at verification time on that side (direction: upper min, lower max), over Tao's page https://teorth.github.io/optimizationproblems/constants/12a.html, its open PRs, arXiv:2610.02809 (latest version), O'Keefe's repository and any newer arXiv claim; on 2026-10-30 the bars are 0.861715646305 (upper) and 0.6421 (lower). The bound must come from a written proof whose final step is a deterministic computation (exact integer/rational arithmetic, or interval arithmetic rounded in the safe direction) that two independent programs reproduce. Bounds holding only with high probability over random sampling do not count.

## Partial wins

- **p1:** An exact, independent verification at k = 9 of the cell-sum identities that O'Keefe's README says were checked only for smaller k (or an explicit counterexample to one of them), with code that shares nothing with his checkers.
- **p2:** An independent, code-disjoint deterministic replay of Dong-Cao's lower bound beta_2 >= 0.6421 (arXiv:2610.02809), rebuilt from the paper's description with exact or safely rounded arithmetic and reproducing the printed value, or a concrete error in it, recorded with logs; credited only while no independent replay of that bound is listed on Tao's page 12a or in an open PR at verification time.

## How a win is checked

Re-derive the integer quantity from the paper's theorem, run two independent implementations (e.g. C and Python) on the published spec, and check that the bound is below the claimed rational threshold with no floating point in the final comparison. Calibrate by reproducing O'Keefe's k = 5..9 table (A_0 values) and Dong-Cao's 0.8810.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.02809>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/12a.html>
- <https://arxiv.org/abs/2610.02809>
- <https://github.com/devinokeefe/travelling-sales-person-constant-bounds>
- <https://arxiv.org/abs/1907.02390>
- <https://optimization-online.org/?p=23315>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run O'Keefe's construction at k = 10 or 11 with the strip height re-optimised; his README table drops by 0.003 to 0.006 per step in k.
- Lower side: combine nearest-neighbour and second-nearest-neighbour exclusion with a finite LP over local configurations, as Gaudio-Jaillet and Dong-Cao do, and certify the LP dual exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Tao's page 12a lagged on 2026-10-30: it listed 0.6277 as the lower bound although Dong-Cao claim 0.6421, and printed O'Keefe's bound as 0.8618 (exact value 0.861715646305).
- Dong-Cao's 0.6536 and 0.8749 are probabilistic; beating them with another sampled estimate proves nothing.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/bhh-tsp-constant-c12-bounds.md
```

Already set up? Say `run V3R1T4S on bhh-tsp-constant-c12-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bhh-tsp-constant-c12-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
