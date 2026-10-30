# Finite point sets with record-low L-infinity star discrepancy in [0,1]^2 (n = 22..1020) or [0,1]^3 (n = 9..5000)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (exact 2D evaluation is O(n^2); 3D up to a few thousand points is feasible) · open as of 2026-10-30

## The problem

The star discrepancy D*(P) of n points is the largest gap between the fraction of points in an anchored box [0,q) (or [0,q]) and its volume. Optimal sets are known only for n <= 21 in 2D and n <= 8 in 3D (Clement, Doerr, Klamroth, Paquete, arXiv:2311.17463). Beyond that, the best published values are spread over several recent papers. Clement-Doerr-Klamroth-Paquete's permutation-based sets (arXiv:2407.11533, PNAS 2025; point files at github.com/frclement/LowDiscPermu): Table 1 gives 2D n = 180: 0.00901, n = 260: 0.00640, n = 420: 0.00412. The text reports 0.02709 (Fig. 3 caption 0.027088) for n = 50, 0.014444 for n = 100, '0.01' for n = 150 and 0.007718 for n = 200. Table 2 covers 3D up to n = 50. Rusch, Kirk, Bronstein, Lemieux and Rus's Message-Passing Monte Carlo (arXiv:2405.15059): 2D n = 20..1020 in steps of 40, e.g. n = 1020: 0.00303. Sadikov's OpenEvolve sets (arXiv:2510.03650 and its repository): 2D n = 500: 0.00509, n = 1020: 0.00245; 3D n = 9..16. Chen, Clement, Doerr and Kirk's L2 subset selection (arXiv:2511.02706): 3D and 2D tables for n = 50..2000. Clement et al.'s projected gradient descent post-processing (arXiv:2511.10496): 2D and 3D tables, not records at its tabulated 2D sizes. FlowBoost (Berczi, Hashemi, Kluver, arXiv:2601.18005): 2D n = 60: 0.029440, not a record. Ait Abderrahim, Doerr, Durand (arXiv:2604.00786 v2): 3D n = 20..5000, e.g. n = 50: 0.04979 after post-processing, n = 500: 0.01115, n = 5000: 0.00210. Several 'new best' claims are beaten by other papers (e.g. Sadikov's 2D n = 100 value 0.01504 versus 0.014444), so the record for a size is the minimum over all sources. The ALGO lab benchmark page cited by FlowBoost (algo.dei.uc.pt/star) did not resolve on 2026-10-30.

## What counts as a win

Success means n explicit points in [0,1)^d, d in {2,3}, with coordinates given as exact decimals or rationals, whose star discrepancy D*, computed exactly in rational arithmetic by two independent implementations, is STRICTLY SMALLER (direction: min) than the smallest value published for that exact (d,n) in any paper, preprint or public results repository of any date, by more than half a unit in the last printed digit of that value. A value printed with fewer than four significant digits (e.g. the '0.01' for 2D n = 150 in arXiv:2407.11533) is read as if padded with zeros to four significant digits (0.01000, so the bar is 0.009995). A posted point file counts at its exact D* as computed by the verifier, if that is lower. Sources include at least arXiv:2407.11533 (including values stated in its text, and its PNAS 2025 version), github.com/frclement/LowDiscPermu, arXiv:2405.15059, 2510.03650 and its repository, 2511.02706, 2511.10496, 2601.18005, 2604.00786, and anything newer. Here 22 <= n <= 1020 for d = 2 and 9 <= n <= 5000 for d = 3, and some source must give a value for that (d,n). Sizes with a proven optimum (n <= 21 in 2D, n <= 8 in 3D) do not count.

## Partial wins

- **p1:** A new proven optimum: the exact optimal star discrepancy for 2D with n = 22 or for 3D with n = 9, with an optimal point set and an optimality certificate (the Clement et al. MILP model solved to proven optimality and re-solved to the same optimum by a second, independent solver), extending the known optimal range.

## How a win is checked

2D: sort the points and evaluate, for every grid corner q built from the point coordinates and 1, both the open-box excess vol(q) - |P in [0,q)|/n and the closed-box excess |P in [0,q]|/n - vol(q), in exact fractions; D* is the maximum. 3D: use the Dobkin-Eppstein-Mitchell algorithm or an O(n^3 log n) sweep, cross-checked against a brute-force O(n^4) evaluation for n <= 200. Then look up the minimum published value for (d,n) across all listed sources and newer arXiv papers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2407.11533>

## Sources

- <https://arxiv.org/abs/2407.11533>
- <https://arxiv.org/abs/2311.17463>
- <https://github.com/frclement/LowDiscPermu>
- <https://arxiv.org/abs/2405.15059>
- <https://arxiv.org/abs/2604.00786>
- <https://arxiv.org/abs/2510.03650>
- <https://github.com/hockeyguy123/openevolve-star-discrepancy>
- <https://arxiv.org/abs/2511.02706>
- <https://arxiv.org/abs/2511.10496>
- <https://arxiv.org/abs/2601.18005>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Clement et al.'s permutation trick: fix the relative order of a good set and solve the LP for the optimal coordinates; apply it to the best sets of the other papers.
- Local search on the exact discrepancy with moves that only touch the critical boxes, followed by the permutation LP as a final polish.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many papers compare only with a subset of the others; take the minimum over all sources for each n.
- Floating-point discrepancy codes misreport ties at critical boxes; final numbers must come from exact arithmetic.
- Records exist only at the sizes the papers tabulate; a size with no published value is not a record.
- Posted point files are not the whole record: arXiv:2407.11533 states lower values in its text (n = 50: 0.027088, n = 100: 0.014444) than in its Table 1 or its posted files.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/star-discrepancy-finite-point-sets-2d-3d.md
```

Already set up? Say `run V3R1T4S on star-discrepancy-finite-point-sets-2d-3d`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `star-discrepancy-finite-point-sets-2d-3d`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
