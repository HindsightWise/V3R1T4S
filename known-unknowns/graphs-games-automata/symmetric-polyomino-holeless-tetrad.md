# Holeless tetrad from a symmetric polyomino with at most 33 cells (record: 34-ominoes, Rubin and Scherer)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT search over symmetric polyominoes of 12..33 cells) · open as of 2026-10-30

## The problem

A tetrad is a figure made of four congruent shapes, each sharing a boundary of positive length with each of the other three. Walter Trump studied polyomino tetrads from 1970-71 and presented his notebooks on trump.de in 2020. Michael R. W. Buckley named them in 1975. George Sicherman's 'Polyomino and Polynar Tetrads' page (revised 2020-01-14, file last modified 2025-12-11) records the minima. The smallest polyomino tetrads use octominoes. The smallest symmetric polyomino tetrad uses a 9-omino. The smallest tetrads for tiles with mirror or with birotary symmetry use 13-ominoes, and Juris Čerņenoks found the smallest for tiles with diagonal symmetry (19-ominoes). So any tetrad of a symmetric tile needs at least 13 cells. The smallest holeless tetrad (union with no hole) is Trump's 11-omino. For symmetric polyominoes, the smallest holeless tetrad known was found independently by Frank Rubin and Karl Scherer and uses 34-ominoes, improving Trump's and Scherer's earlier 48-omino. Sicherman calls it only the smallest known, and Trump's page lists symmetric tiles as a planned topic with no newer record. The range 13..33 cells is open.

## What counts as a win

Success means a polyomino P with at most 33 cells that has a non-trivial symmetry (mirror or rotation, as on Sicherman's page), and four copies of P (each congruent to P, reflections allowed) with disjoint interiors, such that every pair of copies shares a boundary segment of positive length (not only a corner) and the union of the four has no holes (its complement in the plane is connected). The live Sicherman tetrad page must be re-fetched before claiming and must still list 34 as the smallest known.

## Partial wins

- **p1:** An exhaustive, two-method (DLX or SAT with DRAT-checked UNSAT) proof that no symmetric polyomino with at most m cells forms a holeless tetrad, for some m >= 16, labelled as a bounded result.
- **p2:** A holeless tetrad from a polyomino with mirror symmetry and one from a polyomino with birotary symmetry, each with at most 34 cells and each different from the Rubin-Scherer example, so that both symmetry classes have a recorded holeless witness.

## How a win is checked

Check that P is edge-connected and equals one of its non-trivial isometric images. Check that each copy is an isometry of P, that copies are disjoint, that each pair shares at least one unit edge, and that the complement of the union is connected (flood fill on a padded grid). This takes milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://sicherman.net/tetrads/ntetrads.html>

## Sources

- <http://sicherman.net/tetrads/ntetrads.html>
- <http://sicherman.net/tetrads/tetrads.html>
- <https://www.trump.de/tetrads/contents.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- A holeless tetrad has one tile that touches the other three and one that is partly enclosed. Search over the 'central' configuration (three tiles around a fourth) with SAT on a bounded grid, with P symmetric by construction (variables only on a fundamental half).
- Start from Trump's asymmetric 11-omino holeless tetrad and from the 13-omino symmetric tetrads with holes. Try symmetrising or plugging the holes by growing P.
- Iterative deepening on cell count: for each size, SAT jointly over the shape of P (with symmetry constraints) and four placements.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Corner contact alone does not count as sharing a boundary.
- 'Holeless' refers to the union of the four tiles, not to P itself. Use the page's definition.
- Check the symmetry type the page counts as 'symmetric' (mirror or rotary). A P with only translational coincidences is not symmetric.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/symmetric-polyomino-holeless-tetrad.md
```

Already set up? Say `run V3R1T4S on symmetric-polyomino-holeless-tetrad`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `symmetric-polyomino-holeless-tetrad`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
