# Connected maximum-density still lifes: close a gap in Mahajan's n = 26..50 table (OEIS A398723), starting with 349 <= a(26) <= 352

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (CP-SAT / MaxSAT on 26x26..50x50 boards for lower bounds; certified upper bounds may take laptop-days) · open as of 2026-10-30

## The problem

Place live cells in an n x n square so that the whole plane, with every cell outside the square dead, is a still life under Conway's Life (B3/S23). Every live cell has 2 or 3 live neighbours, and no dead cell (inside the square or in the ring just outside it) has exactly 3. All live cells must also form one component under king-move (8-neighbour) adjacency. Maximise the population. This is the Connected Maximum-density Still Life benchmark of the Fourth ASP Competition (2013). Chu and Stuckey (2012) solved the unconnected version (A055397) for all n. Siddhartha Mahajan (2026, OEIS A398723, GitHub release v1.0.1) proved exact values for n = 1..25 and n = 31, 32, 33, 39, each with a witness and an upper-bound proof (row-DP enumeration, Chu-Stuckey's unconnected maxima, or his bound C(n) <= floor((4n^2+5n-d[n mod 8])/8) for n >= 14). The problem was also used in the CAISc 2026 verifiable-problems track, which ended in July 2026. His live table docs/RESULTS.md (repository last updated 2026-10-28; unchanged on 2026-10-30) gives these open bounds as (lower, upper): 26 (349,352), 27 (375,378), 28 (406,407), 29 (433,435), 30 (462,465), 34 (594,597), 35 (625,631), 36 (665,668), 37 (701,704), 38 (738,742), 40 (815,821), 41 (858,863), 42 (902,906), 43 (940,948), 44 (989,993), 45 (1034,1037), 46 (1077,1083), 47 (1126,1132), 48 (1174,1178), 49 (1223,1228), 50 (1276,1279). a(26) is the first unresolved OEIS term.

## What counts as a win

Full win: the exact value of a(26). This needs (1) a 26 x 26 board that passes the checks below, with population P, and (2) a proof that no connected still life in the 26 x 26 square has population P+1 or more. The proof is either (a) a DRAT/LRAT UNSAT certificate checked by drat-trim or cake_lpr, or a VeriPB certificate checked by veripb, or (b) an exhaustive enumeration or dynamic-programming bound. Either way it must be produced by two independently written programs or encodings that agree. Board checks: run one Life step on the (n+4) x (n+4) zero-padded board and get the identical board back; confirm by BFS that the live cells form one 8-connected component; count the cells. Before claiming, re-fetch the live RESULTS.md and OEIS A398723 and confirm the value is still open there. A solver's 'optimal' status without a checked certificate or independent reproduction is not a proof.

## Partial wins

- **p1:** For any open n in 26..50, a board that passes the checks, with population STRICTLY greater than the Lower value in the live RESULTS.md at verification time.
- **p2:** For any open n in 26..50, a proof meeting the full-win proof standard that no connected still life in the n x n square has population U or more, where U is at most the live Upper value, so the table's upper bound drops. The same encoding or program must reproduce the known exact values for n = 10..16 (feasible at the optimum, infeasible at optimum+1).
- **p3:** Any other open n in 26..50 closed exactly (a matching board and an upper bound to the same standard).

## How a win is checked

Write an independent numpy Life stepper and an 8-connectivity BFS, and run them on the claimed board JSON or RLE. For upper bounds, check the proof file with drat-trim / cake_lpr (or veripb), and inspect the encoding: cells outside the square must be forced dead and must stay dead, and connectivity must be encoded soundly (e.g. flow or spanning-tree constraints). Re-run the encoder on n <= 25 against Mahajan's proof index. Fetch RESULTS.md and A398723 live.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/Siddhartha-Mahajan/connected-still-life/blob/main/docs/RESULTS.md>

## Sources

- <https://oeis.org/A398723>
- <https://github.com/Siddhartha-Mahajan/connected-still-life>
- <https://raw.githubusercontent.com/Siddhartha-Mahajan/connected-still-life/main/docs/RESULTS.md>
- <https://oeis.org/A055397>
- <https://doi.org/10.1016/j.artint.2012.02.001>
- <https://www.mat.unical.it/aspcomp2013/ConnectedMaximumDensityStillLife>
- <https://caisc2026.github.io/verifiable-problems/?problem=connected-still-life>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed from Mahajan's own n26..n50 constructions and from Chu-Stuckey optimal unconnected patterns. Then run large-neighbourhood search with CP-SAT: free a window, re-solve it, and keep connectivity with a flow formulation.
- Upper bounds: adapt Chu-Stuckey's relaxation (per-cell wastage accounting over 3x3 windows) and add connectivity cuts. The gaps of 1-3 at n = 26..30 are the natural first attacks.
- Sizes with gap 1 (n = 28) are the cheapest exact closures.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A055397 values are for unconnected still lifes. Several of Mahajan's upper bounds (e.g. n = 28, 36, 44, 47) already equal them, so they are not new upper bounds you can claim.
- Connectivity is by king moves (8-neighbour), not rook moves.
- Births in the ring just outside the square are forbidden; a board that is stable only on a bounded grid fails.
- The table moves (repository last updated 2026-10-28). Re-fetch it before claiming.
- CAISc 2026 accepted several connected-still-life papers: V. P. T. Menta (cited in A055397), A. S. Jaswal ('... up to n = 32'), T. Sodha, P. Sridhar, A. A. Rushdi, Collier-Derfer and Reddy et al. The track's accepted sizes were 8-21 (subset), 31 and 32, and Menta's public repo (github.com/praxelhq/connected-still-life) is below Mahajan's values (n = 31: 485, n = 32: 515). OpenReview showed a bot check here (BLOCKED), so check those papers, especially Jaswal's, for n = 26..30 values before any claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/connected-still-life-max-population.md
```

Already set up? Say `run V3R1T4S on connected-still-life-max-population`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `connected-still-life-max-population`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
