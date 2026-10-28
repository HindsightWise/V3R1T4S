# Polyform compatibility: solve an open ('?') pair or shrink a smallest-known common figure on George Sicherman's tables

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Two polyforms are compatible if some figure can be tiled by copies of each. George Sicherman's Polyform Curiosities maintains tables of the smallest known compatibility figures, in number of tiles, for every pair in many families: heptiamonds (with and without holes), hexiamonds, holeless hexominoes, holeless pentomino-hexomino pairs, pentahexes and more, continuing work by Andris Cibulis, Andy Liu, Bob Wainwright, Uldis Barbans, Gilbert Lee, Giovanni Resta and Erich Friedman. Cells marked '?' are pairs with no known compatibility figure but no impossibility proof; '×' marks pairs believed impossible. The heptiamond table (revised 2012-01-04) and holeless hexomino table (2020-06-18) still contain many '?' cells. Open target: a figure for a '?' pair, or a figure with fewer tiles than listed for a solved pair.

## What counts as a win

Success means, for a pair of polyforms (P, Q) in a table linked under the Polyominoes, Polyiamonds or Polyhexes headings of http://sicherman.net/pairwise.html (square, triangular or hexagonal lattice). Tables under 'Other Plane Polyforms' and 'Solid Polyforms' are excluded because the verification method does not cover their grids. A win needs a figure F (a set of lattice cells) together with an explicit tiling of F by copies of P (rotations and reflections allowed unless the page says otherwise) and an explicit tiling of F by copies of Q. Both must satisfy the page's side conditions (e.g. 'holeless', connected), verified by an exact checker. AND either the pair's cell on the live page is '?', or F uses STRICTLY fewer tiles than the page's listed minimum for that pair. Use the page's own count convention: the number of tiles of each kind, i.e. area / order for equal-order pairs, or the pair of counts shown for mixed-order tables. The page must be re-fetched live immediately before claiming, and Friedman's Math Magic and Resta's Polypolyominoes checked for an existing smaller figure.

## Partial wins

- **p1:** Any '?' cell resolved by an explicit compatibility figure on any of the tables (heptiamond, hexiamond, holeless hexomino, holeless pentomino-hexomino, pentahex).
- **p2:** A smaller figure for a pair whose listed minimum is at least 10 tiles.
- **p3:** A computer-certified impossibility (SAT/DLX exhaustive, with checkable proof) up to a stated figure size for a '?' pair, clearly labelled as bounded.

## How a win is checked

Represent cells on the square, triangular or hexagonal lattice with integer coordinates. Check that tiling 1 uses only congruent copies of P (canonicalise each piece under the allowed symmetry group), tiling 2 only copies of Q, that both cover F exactly with no overlaps, that F satisfies the page's conditions (holeless: complement connected to infinity; connected). Compare tile counts with the live page. Milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://sicherman.net/pairwise.html>

## Sources

- <http://sicherman.net/pairwise.html>
- <http://sicherman.net/7mond/7compat.html>
- <http://sicherman.net/6mond/6compat.html>
- <http://sicherman.net/n6com/n6comh.html>
- <http://sicherman.net/n56com/n56comh.html>
- <http://sicherman.net/compatibility.html>
- <https://erich-friedman.github.io/mathmagic/0904.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Joint SAT model: variables for which cells are in F (bounded box), plus placement variables for P-copies and Q-copies; constrain both tilings to cover exactly F. Increase the tile count k until SAT. Symmetric F (mirror or rotational) shrinks the search a lot.
- Grow from known 'euphoric' polyforms: Sicherman lists polyforms compatible with every member of a family; chaining P -> euphoric -> Q does not directly give a figure, but their common figures are good seeds for local search.
- Import from crystallography: look for F as a fundamental domain of a periodic tiling shared by P and Q (find a common lattice of periods first, then cut a finite patch), as is done for co-tiling in quasicrystal studies.
- Import from VLSI placement: use rectangle-packing style simulated annealing over the boundary of F, alternating 'P-tile F' and 'Q-tile F' feasibility checks via DLX.
- Triage by staleness: the heptiamond page is from 2012, so modern SAT solvers have likely not been run across all its '?' cells.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Check whether reflections are allowed for the specific table; most allow them, but some variants (e.g. 'odd pairs', 'holeless') add constraints.
- 'Holeless' variants forbid holes; a figure with an enclosed hole does not count for the holeless table, but may count for the unrestricted one.
- Tile counts: compare like with like (number of P-tiles, number of Q-tiles, or area) as the page states; mixed-order tables use different conventions.
- Many 'smaller' figures already exist in Erich Friedman's Math Magic (Sept 2004) or Giovanni Resta's pages without being on Sicherman's page; check them before claiming.
- A '×' cell means 'almost surely no solution'; a claimed solution there is more likely a checker bug (wrong piece shape) than a discovery.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/polyform-compatibility-open-pairs.md
```

Already set up? Say `run V3R1T4S on polyform-compatibility-open-pairs`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `polyform-compatibility-open-pairs`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
