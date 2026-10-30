# Knot mosaics: the first mosaic, or a 7-mosaic, for one of the 854 11- and 12-crossing knots with no known mosaic in KnotInfo

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

A knot mosaic (Lomonaco-Kauffman) is an n x n grid of tiles from 11 standard square tiles (blank, arcs and crossings) whose arcs join into a knot diagram. The mosaic number of K is the smallest n with an n-mosaic of K, and the tile number is the fewest non-blank tiles. KnotInfo (Livingston and Moore) stores the pair [mosaic number, tile number] from Aaron Heap and coauthors (Heap-Knowles, Heap-LaCourt, and 'Tabulating knot mosaics: crossing number 10 or less', in preparation) and from Lee, Hong, Lee and Oh. Heap's Knot Mosaic Space site (geneseo.edu/knotmosaics) tabulates mosaics through 10 crossings. In database_knotinfo 2026.10.5, every knot through 10 crossings and most 11-12 crossing knots have exact pairs, mostly [7,31] or [7,29]. But 29 eleven-crossing knots (e.g. 11a_17, 11a_101, 11n_119, 11n_184) and 825 twelve-crossing knots (e.g. 12a_1, 12a_2) are listed [[7,infty), [32,infty)]: no mosaic is recorded at all. Can an explicit mosaic give them a finite value, or close the mosaic number at 7?

## What counts as a win

For a knot K listed '[ [7,infty) , [32,infty) ]' in KnotInfo's mosaic_tile_number field (live site or the database_knotinfo mirror when not older), re-fetched immediately before claiming, and not shown with a mosaic on Heap's Knot Mosaic Space site (https://www.geneseo.edu/knotmosaics): a 7 x 7 mosaic, given as a matrix of the 11 standard tile codes. It must be suitably connected, with every arc endpoint matched on each tile edge, and its diagram, converted to a PD code, must be identified as K (mirror allowed) by SnapPy and Regina. This closes the mosaic number at 7.

## Partial wins

- **p1:** An 8 x 8 mosaic, checked as in the main criterion (tile-edge matching, a single closed component, SnapPy/Regina identification of the PD code), verified as one of the 854 knots. This bounds its mosaic number by 8 and gives its first finite tile-number upper bound.
- **p2:** A mosaic of any size verified as one of the 854 knots with exactly 32 non-blank tiles, which closes the tile number at its listed lower bound 32.

## How a win is checked

Skeptic checks tile-edge matching and that the arcs form a single closed component, converts the mosaic to a PD code, and identifies it with SnapPy/Regina. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/mosaic_tile_number.html>

## Sources

- <https://knotinfo.org/descriptions/mosaic_tile_number.html>
- <https://www.geneseo.edu/knotmosaics>
- <https://www.geneseo.edu/knotmosaics/knot-table/>
- <https://github.com/amheap/knot-mosaics>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: convert KnotInfo grid diagrams (arc index 11-14) into mosaics and compress them with mosaic moves.
- Conventional: enumerate space-efficient 7-mosaics (Heap-LaCourt) with fast HOMFLY filtering, keeping those that match a target knot.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not run the code from Heap's GitHub repository. It is for reading the published method only; write your own checker.
- Heap's pipeline defines 7-mosaic layouts with 27, 29, 31, 32, 34, 36, 37, 39 and 41 non-blank tiles, and KnotInfo's [32,infty) tile bound reflects that the 27-, 29- and 31-tile layouts did not produce these knots. A 7-mosaic for one of them must use at least 32 non-blank tiles. Some may need 8 or more; report 8-mosaics under p1.
- KnotInfo stores mosaic and tile numbers as a pair, not as an interval. Read the field format carefully.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-mosaic-number-twelve-crossing.md
```

Already set up? Say `run V3R1T4S on knotinfo-mosaic-number-twelve-crossing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-mosaic-number-twelve-crossing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
