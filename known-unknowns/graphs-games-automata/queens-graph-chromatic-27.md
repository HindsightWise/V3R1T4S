# Is the 27 x 27 queens graph 27-colourable? (first open chromatic number of the queens graph)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The n x n queens graph has the squares as vertices, adjacent when a queen on one attacks the other. Its chromatic number is at least n; it equals n whenever n mod 6 is 1 or 5 (Gardner/Iyer-Menon construction), and Michel Vasquez and Gunter Stertenbrink found n-colourings for many other n by computer search (Vasquez found a 26-colouring of the 26 x 26 board). OEIS A088202 records the values through n = 26 (a(26) = 26 added 2016 from Chvatal's site) and states that a(27) is the first open case; Vasek Chvatal's page poses 'Problem 1. Is the 27 x 27 queen graph 27-colourable?'. A 27-colouring is the same as a partition of the 27 x 27 board into 27 disjoint non-attacking 27-queen solutions. Bernardo Subercaseaux, Przybocki and Marijn Heule (arXiv 2609.27674) benchmarked 1584 SAT encodings of queen colouring but did not report settling n = 27.

## What counts as a win

Success means an explicit 27 x 27 array of colours 0..26 such that no two squares in the same row, column, diagonal or anti-diagonal share a colour, verified by an independent checker, while OEIS A088202 (https://oeis.org/A088202), re-fetched live immediately before claiming, still says a(27) is open (also check Chvatal's page http://www.cs.concordia.ca/~chvatal/queengraphs.html if it is reachable, and a literature search); OR a certified proof that no 27-colouring exists (an UNSAT result for a validated encoding with a DRAT/LRAT proof checked by drat-trim or cake_lpr, plus a second independent encoding agreeing).

## Partial wins

- **p1:** An n-colouring of the n x n queens graph for some n > 27 that OEIS A088202 or Chvatal's page lists as open at verification time (check the page for which n are known via compositions).
- **p2:** A 27-colouring of the 27 x 27 queens graph with exactly one row, column or diagonal relaxed (e.g. the 27 x 27 board with one wrapped diagonal family, i.e. a partial-torus variant), stated clearly as a relaxation, together with a reproducible search showing how close a full solution is (number of violated pairs), as a benchmark rather than a record.

## How a win is checked

Read the 27 x 27 array; for each row, column, each of the 53 diagonals and each of the 53 anti-diagonals check colours are distinct. Milliseconds. For an impossibility claim, check the DRAT proof and re-derive the CNF independently.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A088202>

## Sources

- <https://oeis.org/A088202>
- <http://www.cs.concordia.ca/~chvatal/queengraphs.html>
- <https://arxiv.org/abs/2609.27674>
- <https://arxiv.org/abs/1606.07918>
- <https://www.johndcook.com/blog/2024/01/30/coloring-the-queens-graph/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Two-stage exact cover: enumerate many 27-queen solutions with strong symmetry (e.g. invariant under 180-degree rotation, or 'linear-like' solutions j = a*i + b mod p perturbed), then solve the exact-cover problem of choosing 27 disjoint ones with DLX or SAT.
- Use the best encodings from Subercaseaux-Przybocki-Heule (symmetry-breaking choice, clique hints, blocked-clause exactly-one) and add a 3-fold or 9-fold symmetry assumption because 27 = 3^3; symmetric solutions shrink the search by orders of magnitude.
- Import from Latin-square and Sudoku generation: a 27-colouring is a Latin square whose colour classes also avoid repeated colours on every straight diagonal; reuse simulated annealing and Jacobson-Matthews style Markov moves from Latin-square sampling, with diagonal conflicts as the energy.
- Import from frequency assignment (radio channels): tabu-search colouring algorithms like Vasquez's own (which found the 26-colouring) with modern partial-assignment crossover (hybrid evolutionary 'HEA' of Galinier and Hao).
- Composition: Chvatal's page explains composing r- and s-colourings into rs-colourings; look for 'near-composition' ideas such as a 3 x 3 block of 9 x 9 boards with twisted offsets, repaired by local search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Diagonals must include ALL diagonals of the square board (not wrapped/toroidal ones, which would be a harder problem, and not only the two main diagonals).
- A colouring of the 27 x 27 torus is impossible in general for n divisible by 3; do not confuse torus and board results.
- Partial colourings with a few conflicts left are not solutions, however close.
- An UNSAT result from an encoding with a symmetry-breaking assumption only excludes symmetric solutions; it proves nothing about chi(Q_27) unless the symmetry breaking is proven sound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/queens-graph-chromatic-27.md
```

Already set up? Say `run V3R1T4S on queens-graph-chromatic-27`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `queens-graph-chromatic-27`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
