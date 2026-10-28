# Domatic, idomatic and total domatic numbers of the n x n queens graph for n = 10..12 (close Lauri's gaps)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The domatic number dom(Q_n) is the largest k such that the squares of the n x n chessboard split into k disjoint sets, each dominating the queens graph (every square holds a queen of the set or is attacked by one). idom requires each set to also be independent; tdom requires total domination. Juho Lauri settled many small cases by SAT (Discrete Math. Lett. 16 (2025) 94-99). His Corrigendum (Discrete Math. Lett. 18 (2026) 34-35, published 26 Aug 2026, doi 10.47443/dml.2026.195) fixes a programming error and gives the current table: dom(Q_9) = 15, dom(Q_10) = 17, dom(Q_11) in {18, 19, 20}, dom(Q_12) in {20, 21}; idom(Q_9) = 15, idom(Q_10) = 16, idom(Q_11) = 18, idom(Q_12) in {18, 19, 20}; tdom(Q_9) = 14, tdom(Q_10) in {15, 16}, tdom(Q_11) in {16, 17}, tdom(Q_12) in {18, 19, 20}. Six (invariant, n) pairs are still open. OEIS A292192 (dom(Q_n)) still shows the pre-corrigendum a(9) = 13 and a(10) = 16 as of 2026-10-28. Each open value can be settled from below by an explicit partition (checkable in milliseconds) or from above by an UNSAT proof.

## What counts as a win

Success means settling or narrowing one of the six intervals still open in Table 1 of Lauri's Corrigendum, Discrete Math. Lett. 18 (2026) 34-35 (https://doi.org/10.47443/dml.2026.195): dom(Q_11) in {18,19,20}, dom(Q_12) in {20,21}, idom(Q_12) in {18,19,20}, tdom(Q_10) in {15,16}, tdom(Q_11) in {16,17}, tdom(Q_12) in {18,19,20}. The interval must still be open in any later erratum or paper found by a search and in the live OEIS entries (A292192 and related), all re-fetched immediately before claiming. A raised lower bound requires an explicit partition of all n^2 squares into k classes, each class dominating (resp. independent dominating, total dominating) Q_n, with k above the current lower bound. A lowered upper bound requires a CNF encoding of 'a partition into k classes exists' that a solver reports UNSAT, with a DRAT/LRAT proof checked by drat-trim or cake_lpr, and the encoding cross-checked by finding the known (k-1)-partitions as SAT. Determining dom(Q_11) or dom(Q_12) exactly also extends A292192.

## Partial wins

- **p1:** Any single raised lower bound (an explicit partition beating the Corrigendum's lower bound for one of the 6 open (invariant, n) pairs).
- **p2:** A DRAT-certified upper bound improvement for one of the open pairs, with two independently written encodings agreeing.
- **p3:** Exact values for n = 13 for any of the three invariants, with a constructive lower bound and a certified upper bound, if not already published.

## How a win is checked

For a partition: check it covers each square exactly once; for each class, check every square is in the class or shares a row, column or diagonal with a class member (for tdom, every square including members must be attacked by a different member; for idom, no two members attack each other). For an upper bound: rerun the CNF through CaDiCaL/kissat with proof output and check with drat-trim; separately regenerate the CNF from an independent script and compare satisfiability on k-1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.dmlett.com/archive/v18/DML26_v18_pp34-35.pdf>

## Sources

- <https://doi.org/10.47443/dml.2026.195>
- <https://www.dmlett.com/archive/v18/DML26_v18_pp34-35.pdf>
- <https://doi.org/10.47443/dml.2025.112>
- <https://www.dmlett.com/archive/v16/DML25_v16_pp94-99.pdf>
- <https://oeis.org/A292192>
- <https://oeis.org/A075458>
- <https://oeis.org/A075324>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Symmetry-aware SAT: impose that the partition is invariant under a subgroup of the board's dihedral group (classes mapped to classes), which shrinks the search hugely for constructive lower bounds.
- Upper bounds by counting: as in the Corrigendum's proofs, enumerate all minimum dominating sets (e.g. Q_11 has exactly two of size 5, Q_12 eight of size 6) and use size-distribution counting plus set-packing SAT; add clique hints (as in Subercaseaux, Przybocki and Heule's queen-colouring encodings).
- Import from frequency assignment in cellular networks: domatic partitions are 'cluster-head rotations'; graph-colouring-style tabu search (TabuCol) adapted to the domatic objective finds partitions fast.
- Import from coding theory: a domatic partition of a vertex-transitive graph often comes from a perfect-code-like lattice; try cosets of sublattices of Z^2 mod n as candidate classes and repair with SAT.
- Cube-and-conquer on the UNSAT side, splitting on which class occupies the 4 corners and the centre.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- dom, idom and tdom are three different invariants; a partition valid for dom may not be independent (idom) or total (tdom). Check the exact definition for the claimed one.
- Total domination requires every square, including those in the class, to be attacked by another member of the same class.
- An UNSAT result without a checked proof, or from an encoding never validated on known SAT cases, is not a certified upper bound.
- The original 2025 paper had a programming error; several of its values (dom(Q_9), dom(Q_10), idom(Q_9), idom(Q_10), idom(Q_11)) were corrected in the 2026 Corrigendum, and OEIS A292192 had not caught up as of 2026-10-28. Use the Corrigendum's table, and search for any later erratum before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/queens-graph-domatic-numbers.md
```

Already set up? Say `run V3R1T4S on queens-graph-domatic-numbers`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `queens-graph-domatic-numbers`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
