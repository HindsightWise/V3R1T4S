# Octahedron Ramsey number: is R(K_{2,2,2}, K_{2,2,2}) 30 or 31?

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (a 30-vertex witness search, or an UNSAT proof on 30 vertices with symmetry breaking) · open as of 2026-10-30

## The problem

The octahedron K_{2,2,2} is the complete 3-partite graph with parts of size 2 (6 vertices, 12 edges). DS1 revision #18 (Apr 2026), item 5.13, gives 30 <= R(K_{2,2,2}, K_{2,2,2}) <= 31: the lower bound is from Harborth and Krause's distance colourings, the upper bound from Lidicky and Pfender's flag-algebra method (SIAM J. Discrete Math. 2021, arXiv:1704.03592). The value is one bit away: a 2-colouring of K_30 with no monochromatic octahedron gives 31, a proof that none exists gives 30. No 2026 paper found by an arXiv title search touches this cell.

## What counts as a win

Either (a) an explicit graph G on 30 vertices such that neither G nor its complement contains K_{2,2,2} as a subgraph, verified by two independent exact programs, proving R = 31; or (b) a proof that every graph on 30 vertices contains K_{2,2,2} in it or its complement, proving R = 30, certified by a DRAT/LRAT/FRAT UNSAT proof of a stated CNF (any symmetry breaking must be proved sound, e.g. via SAT modulo symmetries with a checkable certificate) that a referee regenerates and checks. Either settles the number (the current gap is 30-31, so both directions are strict improvements).

## Partial wins

- **p1:** A complete, certified classification showing that no circulant, 2-block or 3-block polycirculant graph on 30 vertices works (exhaustive search with a re-runnable script and an UNSAT certificate per symmetry class), not already reported by Harborth-Krause, Lidicky-Pfender, Lidicky-McKinley-Pfender-Van Overberghe or any newer paper.
- **p2:** A DRAT/LRAT-certified proof, on a CNF the verifier regenerates, that no graph on 30 vertices with G and its complement both octahedron-free has every degree in {14, 15} (so any witness for R = 31 must be irregular). An explicit such graph would instead be the full win.

## How a win is checked

K_{2,2,2}-freeness: G contains an octahedron as a subgraph iff some 6 vertices split into three disjoint pairs with all 12 cross-pair edges present (edges inside a pair are irrelevant). Implement once by brute force over all C(30,6) = 593,775 six-subsets and their 15 pairings into three pairs, and once as a SAT query that must be UNSAT. Run both on G and on its complement. UNSAT claims: regenerate the CNF, check the proof with drat-trim or cake_lpr, and audit any symmetry breaking for soundness.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://arxiv.org/abs/1704.03592>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The octahedron is not induced-forbidden: any 6 vertices with all 12 cross-part edges count, whatever happens inside the parts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/octahedron-ramsey-number.md
```

Already set up? Say `run V3R1T4S on octahedron-ramsey-number`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `octahedron-ramsey-number`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
