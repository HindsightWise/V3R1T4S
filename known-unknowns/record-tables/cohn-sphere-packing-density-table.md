# MOONSHOT - denser sphere packing than Cohn's table in some dimension 10..48

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Henry Cohn maintains a table of the best known sphere packing densities (center density, number of translates, density, upper bound, ratio) in dimensions 1-48, with archived data and explicit coordinates. Only dimensions 1, 2, 3, 8, 24 are proven optimal. Improvements in mid dimensions (e.g. 10, 11, 13, 18-23) came from non-lattice periodic packings and new lattices, and the table is still moving: Chen, Hu, Li, Wang and Wu (arXiv:2505.02394, antipode construction, 2025) hold the records in dimensions 19, 20, 21, 23, 44, 45 and 47, and Dorofeev, Sun and Wang (arXiv:2607.20359, v4 29 Aug 2026) hold them in every dimension from 38 to 43. Any denser packing in a listed dimension is a famous result but is checkable from a periodic packing description.

## What counts as a win

Success means a periodic packing in R^n, 10 <= n <= 48 (lattice basis L plus k translates t_i, all with exact rational or algebraic coordinates), such that an independent script computes exactly the minimal distance 2r between distinct centers (min over lattice vectors and translate differences, by exact Fincke-Pohst enumeration in rational arithmetic) and the resulting center density k*r^n/covol(L) is STRICTLY GREATER (direction: max) than the center density for dimension n on https://cohn.mit.edu/sphere-packing/ re-fetched live immediately before claiming.

## Partial wins

- **p1:** A new non-isometric packing matching the best known density in some dimension 10-31 (different kissing configuration), certified exactly.
- **p2:** A lattice (not just periodic packing) matching a non-lattice record density in some dimension, certified exactly.

## How a win is checked

Exact rational lattice arithmetic (fpylll for enumeration with rational Gram, cross-checked with PARI qfminim); compute packing radius and covolume; compare with the table's center density. Under an hour for n <= 32.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/sphere-packing/>

## Sources

- <https://cohn.mit.edu/sphere-packing/>
- <https://arxiv.org/abs/2607.20359>
- <https://arxiv.org/abs/2505.02394>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Codes-to-lattices: Construction A/B/D from the best binary/ternary codes in codetables.de and Brouwer's tables, including newly found codes from the other coding-theory entries.
- Non-lattice periodic packings: start from the record lattice, add a coset (glue vector) at deep holes and optimise the scaling exactly (the method behind several mid-dimension records).
- Cross-domain import (materials science / crystal structure prediction): apply random-structure search (AIRSS-like) in R^n with soft repulsive potentials and periodic cells, then snap to exact rational coordinates.
- Cross-domain import (machine learning / AlphaEvolve-style program search): evolve programs that output Gram matrices, with exact density as fitness.
- Cross-domain import (algebraic number theory): ideal lattices of number fields with small discriminant (Craig-type and Mordell-Weil lattices) evaluated exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Center density vs density vs kissing number confusion (the table's 'center density' is the number of unit-radius spheres per unit volume, i.e. k*r^n/covolume with r half the minimal distance).
- Floating-point minimal-norm computation can miss a short vector; use exact enumeration.
- A periodic packing's density must account for all k translates and their mutual distances, not only lattice vectors.
- The kissing-number tables (already in the bank) are a different record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/cohn-sphere-packing-density-table.md
```

Already set up? Say `run V3R1T4S on cohn-sphere-packing-density-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cohn-sphere-packing-density-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
