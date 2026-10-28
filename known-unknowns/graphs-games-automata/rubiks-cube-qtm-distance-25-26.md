# MOONSHOT - Rubik's Cube in the quarter-turn metric: a new position at distance 26, or a third distance-25 position

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

God's number for the 3x3x3 Rubik's Cube in the quarter-turn metric (QTM) is 26 (Tomas Rokicki and Morley Davidson, 2014, about 29 CPU-years). Yet only ONE position is known to need 26 quarter turns (superflip composed with fourspot, proven by Michael Reid in 1998, with its two rotations), and at distance 25 only two positions (and their rotations) are known; about 150,000 positions are estimated at distance 24. Rokicki's cube20.org states that despite significant effort no additional distance-26 positions have been found. cube20.org/symmetry also gives the optimal QTM distance of EVERY position with a nontrivial symmetry or antisymmetry: 78,820 such positions at distance 24, 36 at distance 25 and 3 at distance 26. So all known 25s and 26s are symmetric, and any new one must have trivial symmetry. Open target: a new antipode at distance 26, or a third distance-25 position, inequivalent under the 48 cube symmetries and inversion to the known ones.

## What counts as a win

Success means a cube position, given as a scramble and a facelet string, that two independently written optimal QTM solvers (e.g. Rokicki's and Kociemba's or an independent IDA* with verified pattern databases) both prove requires exactly 25 (or 26) quarter turns, and that is not equivalent under the 48 spatial symmetries combined with inversion to any position listed as known at that distance on https://www.cube20.org/qtm/ re-fetched live immediately before claiming (and not reported in later literature or the cube forums found by search).

## Partial wins

- **p1:** A distance-24 QTM position with trivial stabiliser under the 96-element symmetry/antisymmetry group (so not among the symmetric positions tabulated at https://cube20.org/symmetry/sum2-q.html), proved distance-24 by two independent optimal solvers and not listed on cube20.org or its linked Cube-Lovers/cubeman posts, with a search log showing how its quarter-turn neighbours were screened for distance 25.

## How a win is checked

Run both optimal solvers on the position; each must return a 25- (or 26-) move solution and exhaust depth 23 (resp. 24) without a solution (parity fixes odd/even). Check the solution by applying it to the scramble. Canonicalise the position under the 96-element symmetry/antisymmetry group and compare with the known positions (superflip*fourspot and the two distance-25 positions from the cube20 page and its linked Cube-Lovers/cubeman posts). A depth-25 optimal proof can take hours per position on a laptop, so budget accordingly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.cube20.org/qtm/>

## Sources

- <https://www.cube20.org/qtm/>
- <https://www.cube20.org/>
- <https://kociemba.org/>
- <http://forum.cubeman.org/?q=node/view/138>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Symmetric positions are exhausted (cube20.org/symmetry), so target asymmetric positions. Every distance-25 position is one quarter turn from some distance-24 position, so screen the asymmetric quarter-turn neighbours of the 78,820 symmetric distance-24 positions (and of newly found asymmetric 24s) with a fast suboptimal solver, then run optimal solvers on survivors.
- Perturb the known antipodes: apply short asymmetric move sequences or conjugations to superflip*fourspot and the two known 25s, and screen the results for positions whose best suboptimal solution stays at 24+ before optimal solving.
- Import from cryptanalysis (meet-in-the-middle): screen candidates by checking whether they are within distance 12 of a large table of distance-13 positions from both sides; positions that fail are distance-25/26 candidates.
- Import from extreme-value search in large graphs: run a random walk or simulated annealing biased towards positions with high pattern-database lower bounds (heuristic 'deepness'), using the admissible heuristic itself as the energy, and send only high-scoring positions to the optimal solvers.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Half-turn metric (HTM) distance-20 positions are plentiful; claims must be in the quarter-turn metric, where a half turn counts as 2.
- Positions related by one of the 48 symmetries or by inversion are the same for this purpose; canonicalise before claiming novelty.
- Every position with any nontrivial symmetry or antisymmetry has already been solved optimally on cube20.org/symmetry; a 'new' symmetric distance-25/26 position means a canonicalisation or solver bug.
- A suboptimal solver failing to find a short solution is not a lower bound; only an exhaustive optimal search proves distance.
- QTM parity: odd-parity positions have odd distance; a solver reporting an even distance for an odd position has a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/rubiks-cube-qtm-distance-25-26.md
```

Already set up? Say `run V3R1T4S on rubiks-cube-qtm-distance-25-26`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rubiks-cube-qtm-distance-25-26`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
