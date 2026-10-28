# Gavin Theobald's Geometric Dissections: a dissection with fewer pieces than the catalogue's best

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Gavin Theobald's site catalogues 786 geometric dissections (regular polygons, stars, Greek crosses, etc., 2D and 3D) with the fewest pieces known, last updated 11 June 2026; the History page shows steady improvements (e.g. 'Improved dissection of {4} to 2×{7}', 7 Dec 2025; new {4}→rotated {6}, 30 Mar 2026). Target: a valid dissection between two shapes listed in the catalogue using strictly fewer pieces than the catalogue's entry (same rules: free / hinged / turn-over-allowed as on that page), or the same count without turning pieces over where the catalogue needs a turnover.

## What counts as a win

Scope: plane (2D) polygon dissections on the catalogue whose record is an ordinary free dissection. 3D, spherical, hinged and locked dissections are excluded because the verification method does not check them. Success means explicit pieces (vertex coordinates in exact form: rationals or explicit algebraic numbers in Q(sqrt2, sqrt3, sqrt5, ...) as sympy expressions) together with two rigid-motion placements, such that an exact checker confirms two things. First, each placement tiles the respective target polygon exactly (union equals target up to measure zero; pairwise interiors disjoint; total area equal). Second, the shapes have the catalogue's normalisation (equal area). The piece count must be STRICTLY LESS (direction: min) than the count on the relevant catalogue page on https://www.gavin-theobald.uk/, re-fetched live immediately before claiming, with turnover allowed only if that page's record allows it. Alternatively, an equal count with no piece turned over counts where the live record requires a turnover. The dissection must not be previously published (check Frederickson's books and the site's History).

## Partial wins

- **p1:** Matching a catalogue piece count with a genuinely different dissection (non-congruent piece set), exactly verified.
- **p2:** A turnover-free dissection where the catalogue's best of the same count needs a turnover.

## How a win is checked

Exact polygon geometry in sympy (or exact algebraic-number Shapely-free code): verify each placed piece is a rigid motion (orientation-preserving unless turnover allowed) of the piece polygon, check pairwise interior-disjointness via exact segment intersection, and check union area = target area plus every target boundary point covered (vertex/edge-matching). Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.gavin-theobald.uk/HTML/Home.html>

## Sources

- <https://www.gavin-theobald.uk/HTML/Home.html>
- <https://www.gavin-theobald.uk/Index.html>
- <https://www.gavin-theobald.uk/HTML/History.html>
- <https://www.gavin-theobald.uk/HTML/Contents.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Classic strip and tessellation superposition (Frederickson's T-strip/P-strip methods): automate overlaying two strips at varying offsets/angles and count resulting pieces.
- Target the families the History shows as still moving (polygon-to-2×polygon, rotated copies, stars {n/k}) where the record is recent and seldom minimal.
- Cross-domain import (image registration in medical imaging): treat the two tessellations as images and optimise the overlay transform to maximise boundary coincidence, which minimises piece count.
- Cross-domain import (garment/sheet-metal nesting): nesting heuristics (no-fit polygons) to place pieces of the first shape into the second.
- Exhaustive search over small hinged-dissection combinatorics for 4-5 piece targets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point coordinates that 'almost' fit are the classic false dissection; only exact arithmetic counts.
- Turnover rules: reflected pieces are not allowed when the record is turnover-free.
- Area normalisation: dissections are between shapes of EQUAL area; a scaled target is invalid.
- Frederickson's books and Theobald's site may contain the dissection already under a different shape name; check both.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/theobald-geometric-dissections-fewer-pieces.md
```

Already set up? Say `run V3R1T4S on theobald-geometric-dissections-fewer-pieces`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `theobald-geometric-dissections-fewer-pieces`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
