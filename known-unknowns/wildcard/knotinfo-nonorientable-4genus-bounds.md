# KnotInfo smooth 4D crosscap numbers: a nonorientable band certificate beating an upper bound for an 11-13 crossing knot (3,525 intervals)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The smooth 4D crosscap number gamma_4(K), the nonorientable 4-genus, is the smallest first Betti number of a smooth nonorientable surface in B^4 bounded by K (gamma_4 = 1 for slice knots). KnotInfo (Livingston and Moore) gives upper bounds from nonorientable band moves to slice knots, immersed disks and crossing changes. Lower bounds come from Yasuhara's Arf/signature criterion, Gilmer-Livingston and Ozsvath-Stipsicz-Szabo's unoriented knot Floer upsilon. Values are complete through 10 crossings (Jabuka-Kelly for 8-9, Ghanbarian arXiv:2011.03480 for 10). Fairchild treated non-alternating 11-crossing knots (arXiv:2403.00996). Lee and Sabloff extended the data to 11-crossing alternating knots and to 12 and 13 crossings, with an algorithmic Mobius-band search through 14 crossings ('An algorithmic search for knots bounding Mobius bands in B^4', arXiv:2607.23582, July 2026). In database_knotinfo 2026.10.5, 3,525 entries are intervals: 59 at 11 crossings, 455 at 12 and 3,011 at 13. Most are [2,3] (1,751), [1,2] (991) or [1,3] (773).

## What counts as a win

For a knot K whose smooth_4d_crosscap_number is an interval [a,b] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a PD code D verified as K by SnapPy/Regina and a sequence of k band moves D = K_0 -> K_1 -> ... -> K_k. Each move must be a nonorientable (one-component to one-component) band move, the final knot K_k must be certified smoothly slice, and k must be STRICTLY LESS than b (direction: min). K_k counts as slice when Regina certifies the unknot, KnotInfo lists smooth_four_genus 0, or a ribbon certificate is given as band moves to a Regina-certified unlink. k = a closes the interval; for [1,2] entries this means one band to a slice knot, i.e. K bounds a Mobius band.

## Partial wins

- **p1:** For a prime knot with 14 crossings that Lee-Sabloff (arXiv:2607.23582) do not list as bounding a Mobius band in B^4, and that is not obstructed by Yasuhara's criterion or any other obstruction they report: a certified Mobius band, i.e. one nonorientable band move from a diagram identified as the knot by SnapPy/Regina to a knot certified smoothly slice as in the main criterion.
- **p2:** A demonstrated KnotInfo inconsistency: a certificate with k below a listed lower bound, with every intermediate knot identified and inputs saved.

## How a win is checked

Skeptic replays each band move on the PD code, checks that every step stays a knot (one component), identifies K_0 and K_k with SnapPy/Regina, and checks the slice certificate for K_k. Under 30 minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/smooth_4d_crosscap_number.html>

## Sources

- <https://knotinfo.org/descriptions/smooth_4d_crosscap_number.html>
- <https://arxiv.org/abs/2607.23582>
- <https://arxiv.org/abs/2403.00996>
- <https://arxiv.org/abs/2011.03480>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: exhaustive short nonorientable bands between arcs of many diagrams of K, keeping only results whose HOMFLY matches a slice knot, then identifying them.
- Conventional: crossing changes to knots of known gamma_4 combined with the immersed-disk construction KnotInfo describes.
- Cross-domain import (reaction-network search): breadth-first search over band moves with canonical PD hashing.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- An oriented (coherent) band produces a 2-component link. Only one-component bands add a crosscap; mixing the two needs separate bookkeeping, so this criterion uses only nonorientable bands.
- Lee-Sabloff's July 2026 search is the frontier. The remaining [1,2] knots survived it, so check their data before claiming.
- Yasuhara's criterion rules out gamma_4 = 1 for some knots. A claimed Mobius band for one of them signals a bookkeeping error.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-nonorientable-4genus-bounds.md
```

Already set up? Say `run V3R1T4S on knotinfo-nonorientable-4genus-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-nonorientable-4genus-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
