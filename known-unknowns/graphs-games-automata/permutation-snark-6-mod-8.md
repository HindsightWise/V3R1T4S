# Permutation snarks: a first one of order 6 mod 8 (at least 54 vertices) or a first one of girth at least 6

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days for cycle-permutation searches with SAT colouring tests; a certificate check takes seconds · open as of 2026-10-30

## The problem

A cycle permutation graph is a cubic graph with a 2-factor of two chordless cycles (each of length n/2); a permutation snark is one that is not 3-edge-colourable. Such snarks have order 2 mod 4, and Macajova and Skoviera showed that they exist for every n = 2 mod 8 with n >= 10 (cyclically 5-edge-connected ones for n >= 34). No permutation snark of order 6 mod 8 is known. This was posed by Brinkmann, Goedgebeur, Hagglund and Markstrom (JCTB 2013, Problem 1) and revisited in Macajova and Skoviera, 'Are there any permutation snarks on 6 (mod 8) vertices?' (Procedia Comput. Sci. 273, 2025). Jan Goedgebeur, Jarne Renders and Steven Van Overberghe ('Generation of Cycle Permutation Graphs and Permutation Snarks', arXiv:2411.12606, v4 May 2026; conference version SOFSEM 2025, LNCS 15538) generated all permutation snarks up to order 46. They proved that a smallest one of order 6 mod 8, if it exists, has at least 54 vertices and (Macajova-Skoviera) is cyclically 5-edge-connected. Although cycle permutation graphs can have arbitrarily large girth (Shawe-Taylor and Pisanski), no permutation snark of girth >= 6 is known. A smallest one has at least 50 vertices, at least 56 for girth 7, 62 for girth 8 and 72 for girth 9. Target: a permutation snark of order n = 6 mod 8.

## What counts as a win

An explicit simple cubic graph G on n vertices, n = 6 (mod 8), together with an explicit 2-factor consisting of two induced (chordless) cycles of length n/2 each, such that G has no proper 3-edge-colouring, proved by a DRAT/LRAT-checked UNSAT proof of an independently generated CNF. It must be the first such graph: a fresh arXiv/Scholar search ('permutation snark') at claim time must show no earlier published example. n < 54 means the checker is wrong.

## Partial wins

- **p1:** A permutation snark (any order) of girth at least 6, with the two-chordless-cycle 2-factor given explicitly, girth computed exactly and non-3-edge-colourability certified by a checked UNSAT proof (none known; at least 50 vertices).

## How a win is checked

Check cubicity and simplicity; check that the two given cycles are vertex-disjoint, cover all vertices, have length n/2, and that each induces a cycle (no chords). Check n mod 8. Compute girth by BFS. Encode 3-edge-colouring independently, break symmetry at one vertex, solve with proof logging and verify with drat-trim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2411.12606>

## Sources

- <https://arxiv.org/abs/2411.12606>
- <https://arxiv.org/abs/1206.6690>
- <http://www.dcs.fmph.uniba.sk/~macajova/publications.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- A cycle permutation graph is determined by a permutation of Z_{n/2}; search structured permutations (affine maps, products of rotations) for n = 54, 62, 70 with a fast parity pre-filter and a SAT test.
- Use the Goedgebeur-Renders-Van Overberghe generator and filter code (GitHub, cited in the paper) to explore beyond order 46 restricted to cyclically 5-edge-connected candidates.
- For p1, start from girth-6 cycle permutation graphs with large automorphism groups.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Permutation snarks cannot have order 0 mod 4; an order-0-mod-4 non-colourable claim is a bug.
- The two cycles must be chordless and of equal length; a hamiltonian or other 2-factor does not make G a cycle permutation graph.
- Many experts suspect order-6-mod-8 permutation snarks may not exist; budget accordingly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/permutation-snark-6-mod-8.md
```

Already set up? Say `run V3R1T4S on permutation-snark-6-mod-8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `permutation-snark-6-mod-8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
