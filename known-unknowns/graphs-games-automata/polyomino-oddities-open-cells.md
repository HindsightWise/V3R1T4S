# Polyomino oddities (Sillke figures): settle a '?' or 'Unsolved' cell, or beat a minimal known tile count on George Sicherman's oddity tables

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (SAT/DLX over symmetric figures) · open as of 2026-10-30

## The problem

A polyomino oddity is a figure with binary symmetry or better made from an odd number of congruent copies of one polyomino (rotations and reflections allowed). Oddities are also called Sillke figures after Torsten Sillke, with early work by Livio Zucca. George Sicherman's Polyform Curiosities pages keep the minimal known oddities per polyomino and per symmetry type, with many entries by Mike Reid and one improved by Roger Phillips. The hexomino table (35 hexominoes x 7 symmetries: lateral on cell or edge, diagonal, rotary, double lateral on cell or edge, double diagonal on vertex; page 'last revised 2017-09-20', file modified 2026-03-18) gives counts from 1 to 49 tiles, 'None' for cells proven impossible by colouring and 13 cells still marked '?'. The heptomino page (revised 2024-10-02) has 'Unsolved' lists for lateral, diagonal and birotary symmetry. The pentomino page (revised 2026-09-20) lists minimal known counts up to 73 tiles and leaves 8 cells blank because no oddity is known: T and U for double diagonal, double rotary and full symmetry, and V for double lateral and full symmetry. (Composite solutions using pairs of pentominoes do not count.) The large counts (e.g. 27, 33 and 49 tiles for some hexominoes) are probably not optimal. This target is distinct from the bank's compatibility target: it concerns one polyomino and a symmetric figure, not common figures of two polyforms.

## What counts as a win

Success means a polyomino P and a symmetry class S taken from one of Sicherman's single-polyomino oddity tables (Polyomino Oddities http://sicherman.net/oddities/index.html, Pentomino Oddities, Hexomino Oddities or Heptomino Oddities; not the one-sided, pair, composite, semi-oddity or polyking tables), plus an explicit figure F (set of grid cells) with symmetry S exactly as Sicherman defines it (e.g. lateral on cell = a mirror axis through cell centres) and an explicit tiling of F by k copies of P (reflections allowed), with k odd. One of three must hold on the live page: it shows '?' or 'Unsolved' for (P, S); the (P, S) cell of the pentomino table is blank (no known oddity; as of 2026-10-30 these are T and U for double diagonal, double rotary and full symmetry, and V for double lateral and full symmetry); or k is STRICTLY less than the listed minimal known count. Holeless-variant tables count separately and require F to be holeless. The pages must be re-fetched before claiming. Cells marked 'None' or 'Impossible' are excluded.

## Partial wins

- **p1:** A smaller holeless variant: a holeless oddity with strictly fewer tiles than the listed holeless minimum for some (P, S) in a holeless-variant table.
- **p2:** For a '?' or 'Unsolved' cell, a SAT/DLX proof (with DRAT certificate) that no oddity with symmetry S exists using at most k tiles inside a bounding box of side L, for stated k >= 15 and L, labelled as a bounded result.

## How a win is checked

Canonicalise each tile of the tiling under the 8 grid isometries and check that it equals P, that tiles are disjoint and cover F exactly, and that k is odd. Check that F equals its image under the symmetry S (with the right axis or centre type) and that the complement is connected for holeless variants. Compare k with the live table. This takes milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://sicherman.net/6ominodd/index.html>

## Sources

- <http://sicherman.net/noddities.html>
- <http://sicherman.net/6ominodd/index.html>
- <http://sicherman.net/7ominodd/index.html>
- <http://sicherman.net/oddities/index.html>
- <http://sicherman.net/pentodd/index.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Model a symmetric figure as its fundamental domain: tiles either lie in an orbit of size |G| or are fixed by part of the group, so an odd total forces tiles that sit on axes. Enumerate those first, then SAT-pack the orbits.
- Grow from the known minimal rectangles and from oddities of related polyominoes (sub- and super-shapes) as seeds for local search.
- Colouring arguments from the page's impossibility proofs work as fast filters: only search (P, S) pairs that pass every parity test.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The symmetry types are subtle: axis through cell centres versus along edges, rotation centre on a cell, edge or vertex. A figure with the wrong axis type does not count for that column.
- Each hexomino row is identified by a picture. Match P's exact shape from the page image, and do not rely on row order.
- 'None' means proven impossible by colouring. A claimed solution there is a checker bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/polyomino-oddities-open-cells.md
```

Already set up? Say `run V3R1T4S on polyomino-oddities-open-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `polyomino-oddities-open-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
