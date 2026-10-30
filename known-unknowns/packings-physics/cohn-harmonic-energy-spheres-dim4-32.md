# Harmonic energy on spheres in 4 to 32 dimensions: lower the best known energy in the Ballinger-Blekherman-Cohn-Giansiracusa-Kelly-Schurmann table

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Place N points on the unit sphere S^{n-1} in R^n to minimise the harmonic energy sum_{i < j} |x_i - x_j|^{-(n-2)}. For n = 3 this is the Thomson problem (a separate bank target, excluded here). Henry Cohn's live table (cohn.mit.edu/harmonic-energy) lists the best energies known for 3 <= n <= 32 and n+1 <= N <= 64, plus larger cases up to N = 336 (1,682 rows, 10 decimals). Each row also gives the minimal-angle cosine, the design strength and the number of distinct distances. The data come from Brandon Ballinger, Grigoriy Blekherman, Henry Cohn, Noah Giansiracusa, Elizabeth Kelly and Achill Schurmann (Experiment. Math. 18 (2009), 257-283, arXiv:math/0611451) and their 2021 update with coordinates (hdl.handle.net/1721.1/130937). The page asks for improvements. A companion page (cohn.mit.edu/harmonic-optima) lists the proven universal optima, which cannot be beaten (e.g. 24 points in R^4 are not among them, but 120 in R^4, 16 in R^5 and 27 in R^6 are), and conjectured optima such as 40 points in R^10 and 64 in R^14. Sanity checks on 2026-10-30 reproduced (n,N) = (4,10): 22.5, (4,24): 167 and (5,12): 23.6035593670 with plain BFGS multistart. Rows for n >= 4 with large N and irregular structure (many distinct distances, design strength 0) are the natural targets.

## What counts as a win

Success means N unit vectors in R^n (n in 4..32; >= 20 significant digits) for an (N, n) pair listed at https://cohn.mit.edu/harmonic-energy (re-fetched immediately before claiming), whose energy E* = sum_{i < j} |x_i - x_j|^{-(n-2)}, computed in mpmath at 40 digits after normalisation, is STRICTLY LOWER (direction: min) than the SMALLEST table energy for that (N, n) by at least max(1e-9, 1e-12 * E). The (N, n) must not be a proven optimum: not a simplex (N = n+1), not a cross polytope (N = 2n), not a universal optimum listed on https://cohn.mit.edu/harmonic-optima, and not proven optimal for harmonic energy in any paper found in an arXiv check. It must be a different basin: polishing the 2021 data set's coordinates for (N, n) with the same routine stays above E* + max(1e-9, 1e-12 * E). And no lower published value is found in an arXiv search.

## Partial wins

- **p1:** An improvement (same rules) for a row with n >= 4 and N >= 65 (the 'larger cases' beyond the full grid).
- **p2:** An audit of the 2021 data set: (N, n) rows where the posted coordinates do not reproduce the table energy to 1e-9, or polish more than 1e-9 lower (under-converged, reported as such, not a record).

## How a win is checked

Checker (seconds to minutes): normalise in mpmath, compute E* exactly, and compare with the live table minimum for (N, n). Polish the data-set configuration and the claim with the same L-BFGS plus mpmath Newton routine, and compare the basins. Check the harmonic-optima page for proven rows.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/harmonic-energy>

## Sources

- <https://cohn.mit.edu/harmonic-energy>
- <https://cohn.mit.edu/harmonic-optima>
- <https://arxiv.org/abs/math/0611451>
- <https://hdl.handle.net/1721.1/130937>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Large-N rows in moderate dimensions (n = 4..8, N = 65..256) were run with limited restarts in 2009. Use symmetry-seeded starts (orbits of root systems, the 600-cell and E8 subsets) and basin hopping.
- Rows with 'Distances' in the hundreds or thousands are unstructured local minima, likely far from optimal. Rows with few distances are probably sharp.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The exponent is n - 2, which depends on the dimension. Using 1/r in higher dimensions is a different problem.
- Some (N, n) pairs appear twice in the table with equal energies (different configurations). Use the minimum.
- n = 3 rows are the Thomson problem: they belong to thomson-problem-live-tables and do not count here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/cohn-harmonic-energy-spheres-dim4-32.md
```

Already set up? Say `run V3R1T4S on cohn-harmonic-energy-spheres-dim4-32`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cohn-harmonic-energy-spheres-dim4-32`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
