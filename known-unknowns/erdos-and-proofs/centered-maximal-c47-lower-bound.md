# Centred Hardy-Littlewood maximal constant for squares in the plane (C_47): a measure beating Lin's 1.6855099933

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constant 47: c_2 is the optimal weak-type (1,1) constant of the centred maximal operator over axis-parallel squares in R^2. No best constant is known in any dimension d > 1 (Melas solved d = 1: (11+sqrt 61)/12). Bounds: upper 3.879 (Yongxi Lin 2026, Lean-formalised, improving the covering bound 4); lower bound Phi ~ 1.6855099933 (Lin 2026, Lean on Palomar), from a periodic measure with masses 1 and w = (17+4 sqrt 22)/9 on alternating columns, improving Aldaz's 1.6211915 (2000). Discretisation (Aldaz 2011) means sums of Dirac masses suffice. Target: an explicit (finite or periodic) measure giving a strictly larger certified lower bound.

## What counts as a win

Success means an explicit measure mu (finitely many point masses, or a periodic arrangement with a finite period cell) with exact algebraic or rational parameters, plus a proof-carrying computation showing alpha |{x : M mu(x) >= alpha}| / ||mu|| > L, where L is STRICTLY GREATER (direction: max) than the largest lower bound on the live page https://teorth.github.io/optimizationproblems/constants/47a.html and in any open pull request touching constants/47a.md at https://github.com/teorth/optimizationproblems/pulls, both re-fetched live immediately before claiming. The area of the super-level set must be computed exactly (polygonal regions bounded by lines where square averages equal alpha, which for point masses are piecewise axis-parallel/diagonal) or enclosed by interval arithmetic with a strictly positive margin, in two independent implementations. For periodic measures the reduction to a period cell must be stated and checked.

## Partial wins

- **p1:** A rigorous upper bound on the best ratio achievable within Lin's two-mass alternating-column family (all choices of the two masses, column spacing h and row spacing V), showing the family is exhausted (a computer-assisted proof).

## How a win is checked

For point masses at exact coordinates: the maximal function at x is a max over finitely many critical side lengths (where the square boundary hits a mass), so {M mu >= alpha} is a finite union of polygons computable exactly with rational/algebraic arithmetic (e.g. in Sage or with interval arithmetic on a fine adaptive grid with certified inclusion). Two implementations must agree; compare to the live record.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/47a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/47a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/47a.md>
- <https://github.com/CoolRmal/centered-maximal-constant>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Generalise Lin's lattice: three or more mass values, non-rectangular periodic lattices (sheared or rotated by 45 degrees), and optimise parameters by gradient-free search on the exact area functional.
- Lift Melas's one-dimensional extremisers: products and tensorised versions of the d = 1 extremal configurations, then perturb.
- Cross-domain import (crystallography / sphere packing): treat the period cell as a crystal and search space groups (wallpaper groups) for the mass arrangement, as packing records are found by symmetry-constrained search.
- Cross-domain import (topology optimisation in engineering): represent the measure as a density on a fine grid, optimise the smoothed ratio with adjoint gradients, then 'snap' the result to point masses and certify exactly.
- Use the Lean development in Lin's repository as a template for a formal certificate once a numeric improvement is found.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Wrong operator: the constant is for centred squares (l_inf balls), not Euclidean discs or uncentred squares; Lin's repository also has disc bounds that are a different constant.
- Normalisation: weak type (1,1) uses alpha |{M f >= alpha}| / ||f||_1; using > alpha vs >= alpha or forgetting to divide by the period-cell mass inflates the ratio.
- Grid estimates of the area: sampling the plane on a grid gives a number, not a bound; the area must be exact or rigorously enclosed.
- Periodic measures are infinite: the reduction to one period cell must be justified (as in Lin's construction) or a finite truncation with boundary loss accounted for.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/centered-maximal-c47-lower-bound.md
```

Already set up? Say `run V3R1T4S on centered-maximal-c47-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `centered-maximal-c47-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
