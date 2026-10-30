# Cellular automata on graphs: the next maximum period for Life on simple graphs (A384209) and for totalistic or outer-totalistic rules on connected graphs (A357951-A357953)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (nauty geng enumerates the 12,005,168 graphs on 10 vertices for A384209(10), the 11,117 connected graphs on 8 vertices for A357951(8), or the 261,080 connected graphs on 9 vertices for A357952(9) and A357953(9); each graph needs all 2^n states, times all rules for the totalistic variants) · open as of 2026-10-30

## The problem

Put two-state automata on the vertices of a finite graph. A384209(n) (Pontus von Brömssen, 2025) is the longest cycle period of Conway's Life rule (a live vertex survives with 2 or 3 live neighbours; a dead vertex is born with exactly 3) over all simple graphs on n vertices and all starting states. It is known for n = 1..9: 1, 1, 1, 1, 2, 4, 8, 14, 27. Von Brömssen's 2022 sequences take the maximum over connected graphs on n nodes, all rules of a class and all starts: outer-totalistic rules A357951 (n <= 7, a(7) = 66), totalistic rules counting the node itself A357952 (n <= 8, a(8) = 112), and totalistic rules not counting the node A357953 (n <= 8, a(8) = 96). The OEIS entries give optimal examples: graph6 graphs for A384209, and graphs, rules and starts for the A35795x sequences. A checker written for this check reproduced A384209(1..7) from the networkx graph atlas.

## What counts as a win

A new exact term of any of the four sequences: A384209(10), A357951(8), A357952(9) or A357953(9), or a later term. It must come from exhaustive enumeration of all graphs of the class (nauty geng, connected graphs where required), all rules of the class and all 2^n states. Two independent implementations must agree and reproduce every listed term. The result must include a witness (graph6 string, rule, start state) whose cycle length equals the claimed value under direct simulation. The term must not already be in the live OEIS entry at claim time.

## Partial wins

- **p1:** Any one new term as above (each sequence's next term counts once).
- **p2:** Two or more further consecutive terms of one sequence (e.g. A384209(10) and A384209(11)), each meeting the full-win rules: exhaustive enumeration, two agreeing implementations and a simulated witness.

## How a win is checked

Simulate the witness from its graph6 string with an independent stepper and confirm the minimal period. Confirm the geng graph counts per n (OEIS A000088 for all graphs, A001349 for connected graphs). Re-run the enumerators on n <= 7 against the OEIS data.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A384209>

## Sources

- <https://oeis.org/A384209>
- <https://oeis.org/A357951>
- <https://oeis.org/A357952>
- <https://oeis.org/A357953>
- <https://houseofgraphs.org/graphs/21096>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A384209 ranges over all simple graphs, including disconnected ones, where the period is the lcm of the component periods. The A35795x sequences use connected graphs only.
- A357952 counts the node itself in the totalistic sum, and A357953 does not.
- For outer-totalistic rules, the birth and survival sets range over 0..n-1 neighbours. Pruning rules by the graph's actual degree set is allowed only if the pruning is shown to be complete.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/graph-automata-max-period.md
```

Already set up? Say `run V3R1T4S on graph-automata-max-period`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `graph-automata-max-period`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
