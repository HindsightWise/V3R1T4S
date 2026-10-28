# Knight covering (domination) of the n x n board: fewer knights than Frank Rubin's records for n = 22..50

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The knight domination number of the n x n board is the fewest knights that occupy or attack every square (OEIS A006075). Exact values are known up to n = 21 (a(20) = 62, verified optimal by Lee Morgenstern per the Contest Center; a(21) = 68 added by Andy Huchala in 2021). For larger boards the best known coverings are Frank Rubin's, mostly from 2000-2004, on his Contest Center pages: 22x22: 75, 23x23: 82, 24x24: 88, 25x25: 96, 26x26: 102, 27x27: 111, 28x28: 119, 29x29: 126, 30x30: 135, 31x32: 148, 35x35: 182, 40x40: 230, 45x45: 291, 50x50: 350. These were found with hand-designed patterns (tetrads, Monier's pattern, 'cup' patterns) and partial search. A web search on 2026-10-28 found no published SAT/MaxSAT/ILP or local-search improvement for these sizes. Open target: an explicit covering of some listed board with STRICTLY fewer knights.

## What counts as a win

Success means a list of knight squares on an n x n board (n among 22..30, 35, 40, 45, 50, or the 31x32 board) such that every square is occupied or attacked by a knight, checked by an independent exact checker, with STRICTLY fewer knights than the smallest of: Rubin's count for that board on https://www.contestcen.com/knight.htm and its linked board page (e.g. https://www.contestcen.com/kn27.htm), the upper bounds in OEIS A006075 (https://oeis.org/A006075), and any newer published covering found by a literature search, all re-fetched live immediately before claiming. For n = 22, a covering with 74 or fewer knights also settles that A006075's listed upper bound is not optimal.

## Partial wins

- **p1:** A certified optimality result: a(22) = 75 (or a smaller exact value with matching covering) proved by an ILP or SAT solver with a checkable certificate (DRAT/VeriPB proof, or an LP dual bound proof).
- **p2:** A strictly better covering for a rectangular m x n board with 20 <= m, n <= 50 that appears on Rubin's or Morgenstern's pages (archived), verified the same way.

## How a win is checked

Parse the knight list, mark each knight square and its up to 8 attacked squares, and confirm all n^2 squares are marked. Count knights. Fetch the Contest Center board page and OEIS A006075 live and compare. The check takes milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.contestcen.com/knight.htm>

## Sources

- <https://www.contestcen.com/knight.htm>
- <https://oeis.org/A006075>
- <https://oeis.org/A006076>
- <https://web.archive.org/web/20070102070601/http://home.earthlink.net/~morgenstern/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Set cover with CP-SAT or a MaxSAT solver, warm-started from a periodic tiling (Monier pattern interior) with free variables only in a border strip of width 4-6; the interior is near-optimal, the border is where Rubin's records leave slack.
- Large-neighbourhood search: repeatedly free a random k x k window (k ~ 8-12), re-solve it exactly with ILP given the fixed knights outside, accept improvements.
- Import from wireless sensor networks / facility location: knight covering is a minimum dominating set on a regular graph; apply the 'Lagrangian heuristic plus subgradient' methods from facility location and the dominating-set heuristics from ad-hoc network backbones.
- Import from crystallography: enumerate wallpaper-group-periodic patterns with density close to 1/8 (Monier) and stitch them with optimised boundary layers, like crystal-surface reconstructions.
- Lower-bound side: LP relaxation with the 3x3 'needs 4 knights' cut from Rubin's optimality proofs gives instant bounds to see which boards have the biggest gap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rubin's board pages draw each covering as an HTML table (one cell per square); parse it carefully and compare against the stated knight count in the page heading, not your own reading of the table.
- A covering of the torus or of an infinite pattern clipped to the board is not automatically a covering of the bounded board: knights near the edge attack fewer squares.
- Squares occupied by knights must also be counted as covered (domination), but do not confuse with 'total domination' where knights must be attacked too; the record is the ordinary domination version.
- Lee Morgenstern's or later authors' results may beat a Rubin number without being on the Contest Center page; search the archived Morgenstern site and recent literature before claiming.
- Some board pages show several coverings (e.g. 30x30: 136 then 135; 40x40: 232, 232, 230; 45x45: 292 and 291; 50x50: 360 down to 350); the record is the smallest count on the page.
- A 'covering' found by a heuristic that leaves a single uncovered corner square is the commonest false win; always run the exhaustive checker.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/knight-covering-large-boards.md
```

Already set up? Say `run V3R1T4S on knight-covering-large-boards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knight-covering-large-boards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
