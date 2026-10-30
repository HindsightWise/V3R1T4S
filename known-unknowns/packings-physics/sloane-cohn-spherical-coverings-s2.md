# Spherical coverings: N points on the sphere with a smaller covering radius than the Hardin-Sloane-Smith table (N = 4..130, kept by Henry Cohn)

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Place N points on the unit sphere S^2 so that the covering radius (the largest angular distance from any point of the sphere to the nearest of the N points) is as small as possible. R. H. Hardin, N. J. A. Sloane and W. D. Smith computed putatively optimal coverings for N = 4..130 in 1994 (neilsloane.com/coverings, page last modified 2015, point files cover.3. < N > .txt) and coverings with icosahedral symmetry for N = 2+10(i^2+ij+j^2) from 72 up to 78032 (1994-2000, 267 rows). Henry Cohn now maintains these tables (cohn.mit.edu/sloane, radii rounded UP to 7 decimals, so his last digit can be 1e-7 above Sloane's; files cov3-N.txt in data set hdl.handle.net/1721.1/147004) and asks for improvements. The general table carries no credited change since 1994. Recomputing the posted files for N = 20, 77, 100 and 130 on 2026-10-30 reproduced the table (e.g. N = 130: 11.3165625 degrees). Only a few small N are proven optimal: at least N <= 7 and N = 12 (L. Fejes Toth, Schutte), and survey literature also reports small cases such as N = 10 and 14 as settled, so this target counts only N >= 15. Tarnai and Gaspar studied rigidity; Rathbun (arXiv:2008.04441) gave algebraic forms for some putatively optimal N. The AlphaEvolve survey (Georgiev, Gomez-Serrano, Tao, Wagner, arXiv:2511.02864) did not try coverings. Minimax objectives are non-smooth, and the 1994 searches for N near 100-130 were short, so the upper rows are plausible targets.

## What counts as a win

Success means N unit vectors ( > = 20 significant digits) for some N in 15..130 listed in the live general table at https://cohn.mit.edu/sloane (re-fetched immediately before claiming), whose covering radius R*, computed exactly as stated in verification_method, is STRICTLY SMALLER (direction: min) than the table's covering radius for N by at least 1e-7 degrees (Cohn's values are rounded up; Sloane's page https://neilsloane.com/coverings/ rounds to nearest and can be 1e-7 lower, so compare against the smaller of the two). Also, no published value for N found in an arXiv / Google Scholar check ('covering' 'sphere' 'equal circles' / 'spherical caps' plus N) is lower than R*. N <= 14 is excluded because several small cases are proven optimal.

## Partial wins

- **p1:** A configuration of any symmetry with covering radius at least 1e-7 degrees smaller than the SMALLEST icosahedral-table value listed for that N (cohn.mit.edu/sloane, icov3 rows) for some listed N with 132 <= N <= 2000 (66 such rows covering 60 distinct N on 2026-10-30; N = 492, 912, 1332, 1472, 1692 and 1962 each have two rows with different (i, j), and the smaller radius is the bar), same exact checker. Rows with N <= 130 do not count, because the general table already matches or beats the icosahedral rows there (e.g. N = 92: 13.4878634 vs 13.6762972).
- **p2:** A table-integrity finding: at least one N in 4..130 where the posted cover.3.N.txt (or Cohn's cov3-N.txt), run through the exact checker, does not reproduce the tabulated radius to within 1e-7 degrees, reported with both values.

## How a win is checked

Checker (seconds per N): normalise the points in mpmath (50 digits). Take the convex hull (scipy for the combinatorics). Assert the origin is strictly inside. For each facet, compute the unit outward normal and the angular circumradius arccos(n . a). Assert the empty-cap (Delaunay) property: every other point p satisfies n . p <= n . a + 1e-30. R* is the maximum angular circumradius. Run the same checker on Sloane's posted cover.3.N.txt to reproduce the table first (verified 2026-10-30 for N = 20, 77, 100, 130). Compare R* with the live table value minus 1e-7.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/sloane>

## Sources

- <https://cohn.mit.edu/sloane>
- <https://neilsloane.com/coverings/index.html>
- <https://neilsloane.com/coverings/dim3/cover.3.130.txt>
- <https://hdl.handle.net/1721.1/147004>
- <https://arxiv.org/abs/2008.04441>
- <https://arxiv.org/abs/2511.02864>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Smooth the minimax objective: minimise the log-sum-exp of the facet circumradii (or an L_p norm with p rising to infinity), then finish with an exact active-set Newton step on the equal-radius facets, as done for Tammes polishing.
- Seed from Tammes and Thomson optima at the same N (spherical-codes.org, Deeter tables). Good coverings are often near-uniform minimum-energy configurations with defect motifs moved around.
- Use the icosahedral rows as seeds for N slightly above or below 2+10(i^2+ij+j^2) by inserting or deleting points near the 12 disclinations and re-optimising without symmetry.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Directions: the table gives covering radii in degrees, rounded UP. Smaller wins. Do not confuse it with the packing (Tammes) table, where larger minimal angles win.
- A wrong hull (degenerate co-circular facets) gives a wrong radius. Always run the empty-cap check in high precision.
- neilsloane.com serves point files only to a browser-like User-Agent (plain curl gets HTTP 403). MIT DSpace returned HTTP 429 to scripted requests on 2026-10-30, so fetch the data set slowly or use the Sloane files.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/sloane-cohn-spherical-coverings-s2.md
```

Already set up? Say `run V3R1T4S on sloane-cohn-spherical-coverings-s2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sloane-cohn-spherical-coverings-s2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
