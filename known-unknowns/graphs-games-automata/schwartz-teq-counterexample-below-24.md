# Schwartz's conjecture: a tournament on at most 23 alternatives with two minimal TEQ-retentive sets (the smallest known has 24)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for structured search; computing TEQ exactly with memoisation over dominator subsets takes about 0.1 s on Brandt-Seedig's 24-vertex tournament in plain Python · open as of 2026-10-30

## The problem

For a tournament T = (A, >), let D(x) be the set of alternatives that dominate x. A nonempty X subset of A is TEQ-retentive if TEQ(T[D(x)]) is contained in X for every x in X with D(x) nonempty. Schwartz (1990) defined the tournament equilibrium set TEQ recursively as the union of the inclusion-minimal TEQ-retentive sets, and conjectured that every tournament has exactly one minimal TEQ-retentive set. The conjecture is equivalent to TEQ being monotonic and satisfying independence of unchosen alternatives and the weak and strong superset properties. Brandt, Chudnovsky, Kim, Liu, Norin, Scott, Seymour and Thomassé (Soc. Choice Welf. 40, 2013) disproved it non-constructively, with about 10^136 alternatives. Brandt and Seedig (arXiv:1302.5592) gave an explicit 24-alternative tournament with two disjoint isomorphic minimal TEQ-retentive sets of order 12, and wrote 12 <= n_TEQ <= 23. Brandt, Fischer, Harrenstein and Mair (2010) had checked all tournaments up to order 12. Yang (arXiv:1611.03991) proved the conjecture for all tournaments of order <= 14, and posed Conjecture 1: a minimal TEQ-retentive set of size 3 is always the unique one. So the smallest counterexample has 15 to 24 alternatives. This lane's own checker reproduced the 24-vertex example.

## What counts as a win

An explicit tournament (adjacency matrix) on n <= 23 alternatives together with two distinct inclusion-minimal TEQ-retentive sets X != Y, both recomputed by the verifier with an exact TEQ recursion. Direction: smaller n is better; any n <= 23 is a full win, because no counterexample on fewer than 24 alternatives is published and Yang (arXiv:1611.03991) proved there is none on 14 or fewer. Counterexamples to other TEQ-related statements (for example Brandt's weakening of the conjecture, which the 24-vertex example does not refute) are not this target unless they also exhibit two minimal TEQ-retentive sets on at most 23 alternatives.

## Partial wins

- **p1:** A tournament of any order with two minimal TEQ-retentive sets whose orders (|X|, |Y|) differ from (12, 12), a pair outside Yang's Figure 1 non-existence region and different from Brandt-Seedig's.
- **p2:** A counterexample to Yang's Conjecture 1: a tournament with a minimal TEQ-retentive set of size 3 that is not its unique minimal TEQ-retentive set.

## How a win is checked

Write an independent memoised recursion on vertex bitmasks: TEQ(S) = S if |S| = 1. Otherwise compute T_x = TEQ(D_S(x)) for each x in S. The least retentive superset C(x) of {x} is the closure under adding T_y for y already in the set. The minimal TEQ-retentive sets are the inclusion-minimal sets among the C(x), and TEQ(S) is their union. Check that the matrix is a tournament (exactly one arc per pair). Negative control: rebuild the Brandt-Seedig tournament (dominator lists in arXiv:1302.5592; X1 > Y2, X2 > Y1, Y1 > X1, Y2 > X2) and confirm the twelve TEQ(D(x_i)) sets printed there and exactly two minimal retentive sets. Also confirm uniqueness on random tournaments of order <= 12. Cross-check with a second, independently written implementation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1611.03991>

## Sources

- <https://arxiv.org/abs/1302.5592>
- <https://arxiv.org/abs/1611.03991>
- <https://doi.org/10.1007/s00355-009-0419-z>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The 24-vertex example joins two copies of a 12-vertex tournament with a block pattern. Search the same two-block construction with smaller or unequal blocks (sizes 7-11), keeping the cross pattern and searching the internal tournaments.
- TEQ evaluation is cheap at these sizes, so a simulated-annealing search on arc flips with 'number of minimal retentive sets' and 'size of the second-best closure' as objectives is practical.
- Yang's Figure 1 lists which (|H1|,|H2|) pairs are ruled out; use it to prune.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- TEQ(empty set) and alternatives with no dominators (Condorcet winners) need explicit handling; a Condorcet winner makes the minimal retentive set unique.
- Do not use a heuristic TEQ. The recursion must be exact on every dominator subtournament.
- Yang proved there are no (T3, Tk)-retentive tournaments for k <= 12, so a p2 witness needs a second minimal set of size at least 13.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/schwartz-teq-counterexample-below-24.md
```

Already set up? Say `run V3R1T4S on schwartz-teq-counterexample-below-24`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `schwartz-teq-counterexample-below-24`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
