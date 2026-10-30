# Superbridge index: a polygon realising superbridge index 3 for one of Jeon-Jin's nine candidates (5_2, 6_1, ..., 8_9), or 4 for a 9-10 crossing knot listed [4,5]

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

For a knot embedding K in R^3 and a direction v, b_v counts the local maxima of the height v.x on K. The superbridge index sb(K) is the minimum over embeddings of the maximum of b_v over all v (Kuiper, 1987). KnotInfo (Livingston and Moore) lists sb, with bounds from Randell (sb <= stick/2), Kuiper's torus-knot values, and Clayton Shonkwiler's computations (arXiv:2009.13648, 2112.10902, 2206.06950) and Eddy-Shonkwiler (arXiv:1909.00917). Jeon and Jin showed there are only finitely many 3-superbridge knots and narrowed the candidates (JKTR 2001, 2002). Shonkwiler (arXiv:2009.13648) removed 8_7 from their list, and Jeon and Jin conjecture that only 3_1 and 4_1 have sb = 3. In database_knotinfo 2026.10.5, nine knots are still listed [3,4]: 5_2, 6_1, 6_2, 6_3, 7_2, 7_3, 7_4, 8_4 and 8_9. Twelve 9-crossing knots (e.g. 9_2, 9_10, 9_38) and 164 of the 165 10-crossing knots are [4,5]. Shonkwiler proved that every prime knot through 10 crossings has sb <= 5. Lower bounds come from sb > bridge index (Kuiper) and from Jeon-Jin (sb >= 4 for every knot other than 3_1, 4_1 and the nine). Adams et al. (arXiv:2008.06483) proved sb <= 3b - 1, so every 2-bridge knot has sb <= 5 even where KnotInfo shows no entry. Is any of the nine a 3-superbridge knot, or does any [4,5] knot have a 4-superbridge polygon?

## What counts as a win

For a knot K whose super_bridge_index is an interval [a,b] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a closed polygon with exact rational coordinates, in general position (checked exactly), whose knot type SnapPy and Regina identify as K. Its superbridge number max_v b_v must be computed exactly and equal a. For a [3,4] knot, every direction v must have at most 3 local maxima. To compute it, enumerate the cells of the arrangement of great circles {v : v.e_i = 0} over the edge vectors e_i, and count, at a rational interior point of each cell, the vertices that are strict local maxima.

## Partial wins

- **p1:** For a prime 11- or 12-crossing knot with no KnotInfo super_bridge_index entry, a polygon verified as above (exact general position, SnapPy/Regina identification) whose superbridge number, computed exactly by cell enumeration, is at most 5 (direction: min). The knot must also satisfy three conditions. Its KnotInfo bridge_index is at least 3, since for 2-bridge knots sb <= 5 already follows from Adams et al.'s sb <= 3b - 1. Its KnotInfo polygon_index upper bound is 12, so Randell's sb <= stick/2 gives only 6. It has no value in the appendices of arXiv:2206.06950. In database_knotinfo 2026.10.5 that leaves 737 knots: 12 at 11 crossings and 725 at 12. For a 4-bridge knot this pins sb = 5.
- **p2:** For an 11- or 12-crossing knot with no KnotInfo superbridge entry, a verified polygon whose superbridge number, computed exactly by cell enumeration, is 4. This pins sb = 4, because Jeon and Jin's theorem gives sb >= 4 for every knot other than 3_1, 4_1 and the nine candidates. By Kuiper (sb > b), such a knot must have bridge index 2 or 3.

## How a win is checked

Skeptic checks general position exactly, identifies the knot type with SnapPy/Regina, and independently computes max_v b_v by exact cell enumeration of the great-circle arrangement, counting local maxima at one rational interior point per 2-cell. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/super_bridge_index.html>

## Sources

- <https://knotinfo.org/descriptions/super_bridge_index.html>
- <https://arxiv.org/abs/2009.13648>
- <https://arxiv.org/abs/2112.10902>
- <https://arxiv.org/abs/2206.06950>
- <https://arxiv.org/abs/1909.00917>
- <https://arxiv.org/abs/2008.06483>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: optimise many-stick polygons (not minimal-stick ones) with the objective max_v b_v, as in Shonkwiler's non-minimal realisations (arXiv:2206.06950).
- Cross-domain import (computational geometry / robust optimisation): minimise the worst case over the sphere of directions with a minimax solver over the arrangement cells.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- b_v must be maximised over ALL directions, including near-degenerate ones. Sampling random v underestimates sb, so enumerate cells exactly.
- Jeon and Jin's finiteness work constrains 3-superbridge knots heavily. The nine [3,4] cases may all be 4, so record negative runs honestly.
- Only the knot type matters, but identify it with a verified tool, never by matching invariants alone.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/superbridge-index-jeon-jin-candidates.md
```

Already set up? Say `run V3R1T4S on superbridge-index-jeon-jin-candidates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `superbridge-index-jeon-jin-candidates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
