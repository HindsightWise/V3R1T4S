# Grassmannian packings: N subspaces of R^m (m <= 16) with larger minimal squared chordal distance than Cohn's table

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Choose N n-dimensional subspaces of R^m that maximise the minimal squared chordal distance d^2 = n - ||U_i^T U_j||_F^2, which is the sum of the squared sines of the principal angles. The table was started by J. H. Conway, R. H. Hardin and N. J. A. Sloane (Experiment. Math. 5 (1996), 139-159) and Sloane's 1997 web table. Henry Cohn now maintains it at cohn.mit.edu/grassmannian with 10-decimal distances rounded DOWN, upper bounds (simplex/orthoplex, rounded up), notes crediting each construction, and all configurations in the data set hdl.handle.net/1721.1/147005 (files m-n-N.txt). On 2026-10-30 it had 3,511 rows for m = 3..16 and n = 1..6, 1,163 of them starred (the bound is met, so they cannot be improved). Another 15 unstarred rows are noted 'optimal packing' with a proof of optimality (e.g. (3,1,8), Mixon-Parshall), so they cannot be improved either. It is actively contested: the notes credit 'Henry Cohn' with 15 rows in 2023, 75 in 2024, 528 in 2025 and 50 in 2026, plus constructions by Fickus, Jasper, Mixon, Ganzhinov and others. 1,562 unstarred rows still cite only the original Conway-Hardin-Sloane paper [9] or Sloane's 1997 table [29]. Eight rows are flagged 'unclear whether bound is tight', e.g. (6,3,17): 1.5937499963 vs bound 1.59375. The n = 1 rows are real projective line packings. Complex line packings are a separate bank target (game-of-sloanes-complex-line-packings).

## What counts as a win

Success means N matrices U_i (m x n, >= 20 significant digits) for an UNSTARRED (m, n, N) row of the live table at https://cohn.mit.edu/grassmannian (re-fetched immediately before claiming) whose note does not say 'optimal packing' or 'proof of optimality', such that after orthonormalising each U_i in mpmath at 50 digits, the minimum over i < j of n - ||U_i^T U_j||_F^2 is STRICTLY GREATER (direction: max) than the table's squared chordal distance for (m, n, N) by at least 1e-9. It must also not exceed the row's listed bound by more than 1e-10 (a larger value means a bug). And no value for (m, n, N) published after the table's last change, found in an arXiv search (Grassmannian / line packing / fusion frame with m, n, N), is larger.

## Partial wins

- **p1:** An improvement by at least 1e-9 (same checker and exclusions) on an unstarred row whose note cites only [9] (Conway-Hardin-Sloane 1996) or [29] (Sloane's 1997 table), i.e. a value never improved since the 1990s (1,562 such rows on 2026-10-30).
- **p2:** For one of the eight rows marked 'unclear whether bound is tight' ((6,3,17), (7,2,18), (7,3,23), (10,2,28), (10,5,56), (11,4,69), (12,2,35), (15,2,46)), a packing attaining the bound with a rigorous certificate: exact algebraic coordinates, or an interval Newton proof that an exact solution lies within 1e-30 of the given point.

## How a win is checked

Checker (seconds): parse the vectors (the first n lines span subspace 1, and so on), orthonormalise each block by QR in mpmath, compute all pairwise n - ||U_i^T U_j||_F^2, and take the minimum. Compare it with the live row (10 decimals, rounded down) and its bound. Reproduce the posted file for the row first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/grassmannian>

## Sources

- <https://cohn.mit.edu/grassmannian>
- <https://hdl.handle.net/1721.1/147005>
- <https://projecteuclid.org/euclid.em/1047565645>
- <https://neilsloane.com/grass/index.html>
- <https://arxiv.org/abs/1707.01858>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Rows with empty notes in m = 11..16 were often run only once in 1996 (Sloane's page says so). Run multistart alternating projection (Dhillon-Heath-Strohmer-Tropp) followed by a smooth max-min polish (log-sum-exp of the distances, then an active-set Newton step).
- For n >= 2, build candidates from complex or quaternionic line packings (Game of Sloanes, Hoggar) viewed as real planes, which the table already credits for several tight rows.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Starred rows meet the bound. No improvement is possible there.
- The distance is the squared chordal distance (n minus the sum of squared cosines), not the chordal distance or the smallest principal angle. Mixing them up gives meaningless 'records'.
- MIT DSpace returned HTTP 429 to scripted requests on 2026-10-30. Download the tar file once, slowly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/cohn-grassmannian-packings-table.md
```

Already set up? Say `run V3R1T4S on cohn-grassmannian-packings-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cohn-grassmannian-packings-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
