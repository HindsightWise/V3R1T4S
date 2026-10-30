# Busy Beaver for Wang tiles: exact BBWT(5), or n Wang tiles that tile a larger largest square than the n = 5..10 records

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (SAT on d x d grids; exhaustive n = 5 enumeration up to colour renaming) · open as of 2026-10-30

## The problem

For a finite set of Wang tiles (unit squares with coloured edges, no rotation or reflection, touching edges must match), its score is the largest d such that the set tiles a d x d square, or 0 if there is no largest d (so every set that tiles the plane scores 0). BBWT(n) is the largest score over all sets of n tiles. The bbchallenge wiki's Wang Tiles page (last edited 2026-10-03) lists BBWT(1..4) = 1, 2, 3, 4 and only lower bounds above: BBWT(5) >= 6, BBWT(6) >= 8, BBWT(7) >= 11, BBWT(8) >= 14, BBWT(9) >= 17, BBWT(10) >= 212 (no tile set given for n = 10). The n = 5 champion is [1,0,2,0] [2,0,3,0] [3,0,4,0] [4,6,1,5] [4,5,2,6] (notation [top,right,bottom,left]). Exact values are finite computations up to n = 10 because Jeandel and Rao proved that every set of at most 10 Wang tiles that tiles the plane also tiles it periodically, so every set either has a periodic (torus) tiling or fails at some finite square size.

## What counts as a win

Success means (a) a set of n Wang tiles, 5 <= n <= 10, with a score STRICTLY greater than the lower bound listed for n on https://wiki.bbchallenge.org/wiki/Wang_Tiles, re-fetched live before claiming, certified by an explicit d x d tiling and a DRAT (or LRAT) proof, checked by drat-trim or cake_lpr, that no (d+1) x (d+1) tiling exists (free boundary, matching only between adjacent tiles); or (b) an exact BBWT(5) (or BBWT(6)) while the page lists ' > =': an enumeration of all n-tile sets up to colour renaming and tile order in which each set gets either a periodic tiling certificate (a k x l torus tiling) or an UNSAT certificate at its score + 1, the maximum matching the reported value.

## Partial wins

- **p1:** Exact BBWT(5) with all certificates (expected 6 if the listed champion is optimal).
- **p2:** A tile set beating the listed bound for one n in 6..9 (criterion (a)).
- **p3:** A 10-tile set with a certified score STRICTLY greater than 212 (criterion (a) for n = 10; the page lists 212 without a tile set), with the explicit tiling and the DRAT/LRAT certificate published.

## How a win is checked

Check the d x d tiling edge by edge. Encode (d+1) x (d+1) as SAT (one tile per cell, horizontal and vertical edge matching) with independent code and check the UNSAT proof with drat-trim; a tiling of a larger square restricts to every smaller one, so UNSAT at d+1 bounds the score. For exhaustive claims, re-generate canonical tile sets independently, confirm the count, and re-check each torus tiling and UNSAT certificate. Calibration: the listed n = 5 champion tiles 6 x 6 and not 7 x 7 (reproduced by backtracking).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Wang_Tiles>

## Sources

- <https://wiki.bbchallenge.org/wiki/Wang_Tiles>
- <https://arxiv.org/abs/1506.06492>
- <https://en.wikipedia.org/wiki/Wang_tile>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The listed champions are counters: a column of 'clock' tiles plus a few tiles that force a contradiction after a fixed number of rows. Search for counter gadgets with longer forced periods.
- For n = 10, encode tile sets from small Turing machines or the Jeandel-Rao construction pruned to 10 tiles, which tile large but finite regions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The page does not define the boundary condition; this target assumes free boundary (outer edges unconstrained). State the convention used.
- A set that tiles the plane scores 0, not infinity; long-tiling sets must be shown NOT to tile the plane (UNSAT at d+1).
- Tile sets are unordered and colours are names: count canonical forms in exhaustive claims.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/wang-tiles-busy-beaver-bbwt.md
```

Already set up? Say `run V3R1T4S on wang-tiles-busy-beaver-bbwt`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wang-tiles-busy-beaver-bbwt`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
