# Queen domination of the 26 x 26 board: 13 or 14 queens? (first open value of OEIS A075458)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

gamma(Q_n), the fewest queens that occupy or attack every square of the n x n board, is known through n = 25 (OEIS A075458; values to n = 24 from William Bird's 2017 thesis, a(25) = 13 from Dmitry Kamenetsky's file). It is known that gamma(Q_n) is ceil(n/2) or ceil(n/2)+1 for n <= 132 (Ostergard and Weakley), so gamma(Q_26) is 13 or 14; Kamenetsky's best-known file lists a(26) <= 14. William D. Weakley ('Queen Domination of Even Square Boards', Electron. J. Combin. 29(2) (2022) P50) showed that a dominating set of size n/2 on an even board is either monochromatic (all queens on squares of one colour, by parity of x+y) or bichromatic with colour classes differing in size by at most 2. Below 238, monochromatic sets of size n/2 exist only for n = 2, 4, 6, 10, 12, 18, 30, 130, which rules out a monochromatic 13-queen set for n = 26. He conjectures that bichromatic sets of size n/2 do not exist for n > 4. So a 13-queen solution would have to be bichromatic (6 and 7 queens on the two colours) and would refute Weakley's conjecture. Taha Rostami and Curtis Bright (arXiv 2508.11945, v2 29 Jul 2026) built proof-producing SAT for queen domination, corrected the n = 16 solution count and resolved the previously open n = 19 enumeration case, but A075458 still stops at n = 25. Open target: either a 13-queen dominating set of the 26 x 26 board, or a certified proof that none exists.

## What counts as a win

Success means either (a) 13 squares of the 26 x 26 board such that every square is occupied or attacked by a queen on one of them, verified by an exact checker, or (b) a proof that 13 queens cannot dominate the 26 x 26 board: an UNSAT result for a validated CNF/ILP encoding with a DRAT/LRAT proof checked by drat-trim or cake_lpr (or a VeriPB certificate), with a second independent encoding agreeing; in both cases OEIS A075458 (https://oeis.org/A075458) re-fetched live immediately before claiming must still lack a(26), and a literature search (arXiv, Ostergard/Weakley/Bird follow-ups) must find no earlier resolution.

## Partial wins

- **p1:** Independent queen domination: a(32) of OEIS A075324 (the independent domination number, known through n = 31 from Langlois-Remillard, Mussig and Roldan), determined with a construction and a certified lower bound.
- **p2:** A DRAT-certified proof that every 13-queen dominating set of the 26 x 26 board, if any exists, must have a stated structural property (e.g. occupies every row of one parity), proved for a sound case split covering all cases.

## How a win is checked

For (a): mark rows, columns, diagonals and anti-diagonals of the 13 queens and check all 676 squares are covered. For (b): independent CNF generation, CaDiCaL/kissat with proof output, drat-trim check; compare with Rostami-Bright's published encoding on n = 24, 25 known values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A075458>

## Sources

- <https://oeis.org/A075458>
- <https://oeis.org/A075458/a075458.txt>
- <https://oeis.org/A075324>
- <https://arxiv.org/abs/2508.11945>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v29i2p50>
- <https://doi.org/10.37236/1573>
- <https://dspace.library.uvic.ca/handle/1828/8634>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Weakley structure: by Weakley (EJC 2022) any 13-queen dominating set of the 26 x 26 board is bichromatic with 6 queens on one square colour and 7 on the other; add that cardinality split as a constraint (citing the theorem) and enumerate the remaining structure with SAT. Weakley's own analysis of the bichromatic case is the natural starting point.
- Reuse the Rostami-Bright encoding (auxiliary line-occupancy variables, literal ordering, cube-and-conquer) and add symmetry breaking for the 8 board symmetries; split cubes over which columns are empty.
- Import from radar coverage / art-gallery problems: queen domination is a line-cover problem; use an LP 'line-weight' relaxation (weights on rows, columns and diagonals that every queen can cover only a bounded amount of) to prune cubes before SAT.
- Import from error-correcting codes: dominating sets of queen graphs resemble covering codes; search for 13-sets with additive structure (subsets of cosets of a line mod 26) and repair locally.
- Independent domination side (p1): Langlois-Remillard et al. published Julia ILP code; run it with stronger symmetry breaking for n = 32.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Domination counts squares occupied by a queen as covered; independent domination additionally forbids queens attacking each other. Do not mix A075458 and A075324.
- Diagonals and anti-diagonals both count; board edges cut them (no wrap-around).
- An UNSAT run with unchecked symmetry breaking or without a proof certificate is not a proof that a(26) = 14.
- An UNSAT proof that adds Weakley's 6/7 colour-split constraint relies on his 2022 theorem; state that dependency explicitly, or prove the split inside the certified pipeline.
- Bird's 2017 thesis (https://dspace.library.uvic.ca/handle/1828/8634, reachable on 2026-10-28), Weakley's 2022 paper and later papers may contain more than A075458 shows; check them and any follow-ups before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/queens-domination-26.md
```

Already set up? Say `run V3R1T4S on queens-domination-26`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `queens-domination-26`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
