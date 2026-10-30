# Knuth's cubic graceful conjecture: extend the verification past 14 vertices (16, 18, 20, 22), or a connected cubic graph that is not graceful

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (16-20 vertices); laptop-days for the 7,319,447 graphs on 22 vertices · open as of 2026-10-30

## The problem

A graph with q edges is graceful if its vertices can be given distinct labels from {0,...,q} so that the edge differences |f(u)-f(v)| are exactly 1,...,q. Donald Knuth (The Art of Computer Programming, Vol. 4B) proved by computer search that every cubic graph on 4, 6, ..., 14 vertices is graceful except the disconnected 2K4 and 3K4 (Kotzig), and conjectured that every connected cubic graph is graceful. Joseph Gallian's Dynamic Survey of Graph Labeling (DS6, 28th edition, 30 October 2025, Section 2) still reports the verification only up to 14 vertices. The next orders are small by enumeration standards: 4,060 connected cubic graphs on 16 vertices, 41,301 on 18, 510,489 on 20 and 7,319,447 on 22 (OEIS A002851), each with q = 3n/2 edges, and modern backtracking finds graceful labelings of cubic graphs such as generalized Petersen graphs P(n,k) with n <= 75 in seconds (Shao, Deng, Li and Vese, cited in DS6). Credit: Knuth (conjecture and verification to 14), Kotzig (2K4, 3K4), Gallian (survey).

## What counts as a win

Success means EITHER (a) a certificate that every connected cubic graph on 16, 18, 20 and 22 vertices is graceful: one file per order giving each graph (graph6, as produced by nauty geng -c -d3 -D3 n or genreg) with a graceful labeling, where an independent checker regenerates the complete list, confirms the counts 4,060 / 41,301 / 510,489 / 7,319,447 (A002851), matches every generated graph to a certificate entry by canonical form, and checks that the labels are distinct integers in [0, 3n/2] and the edge differences are exactly {1,...,3n/2}; OR (b) a connected cubic graph with no graceful labeling, certified by two independent exhaustive methods (for example a SAT/CP encoding with a DRAT/LRAT proof checked by drat-trim or cake_lpr, plus an independent backtracking search). Before claiming, re-read the latest DS6 edition and Knuth's TAOCP errata/pre-fascicles for a newer verification bound; orders already covered there do not count.

## Partial wins

- **p1:** Certificate (as in (a)) that every connected cubic graph on 16 vertices (4,060 graphs) is graceful.
- **p2:** Certificate that every connected cubic graph on at most 18 vertices is graceful (adds the 41,301 graphs on 18 vertices).
- **p3:** Certificate that every connected cubic graph on at most 20 vertices is graceful (adds the 510,489 graphs on 20 vertices).

## How a win is checked

Regenerate the graphs with nauty (geng -c -d3 -D3, or genreg) and compare the count with A002851. Canonically label each certificate graph (pynauty or nauty) and check one-to-one coverage. For each labeling assert injectivity, range [0, q], and that the multiset of |f(u)-f(v)| over edges equals {1..q}. Seconds to minutes. For a counterexample, check the DRAT/LRAT proof and re-derive the CNF independently.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://oeis.org/A002851>
- <https://www-cs-faculty.stanford.edu/~knuth/taocp.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Edge-driven backtracking: the edge with difference q must join labels 0 and q, then place differences q-1, q-2, ... (Knuth-style dancing links / exact cover over edge differences).
- CP-SAT model with AllDifferent on vertex labels and on edge differences, warm-started from a labeling of a neighbouring graph under a single edge switch.
- Run order 16 first as a pipeline test; most graphs should fall in milliseconds, so time goes into the rare hard graphs, which are worth reporting.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Disconnected cubic graphs are excluded: 2K4 and 3K4 are not graceful.
- Labels come from {0..q} with q = 3n/2 edges, not from {1..n}.
- A file of labelings is not a certificate unless the checker proves it covers every isomorphism class (count must match A002851).
- The 14-vertex bound is taken from Gallian's survey (DS6, 28th ed.), which cites TAOCP 4B. Knuth's later Volume 4 Fascicle 7 (Constraint Satisfaction, 2025, section 7.2.2.3, exercise 93 and answer) treats graceful labelings of regular graphs; read it and the TAOCP errata for a newer cubic bound before claiming (Knuth's site refused connections when this entry was checked).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/cubic-graphs-graceful-knuth-beyond-14.md
```

Already set up? Say `run V3R1T4S on cubic-graphs-graceful-knuth-beyond-14`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cubic-graphs-graceful-knuth-beyond-14`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
