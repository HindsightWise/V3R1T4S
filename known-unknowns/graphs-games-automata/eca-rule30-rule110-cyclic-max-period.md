# Elementary CA on rings: the maximum cycle length of Rule 30 (A334497) and Rule 110 (A204371) on a cyclic width of 37

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (exhaustive over 2^37 states, reduced by rotation, the only symmetry that commutes with Rules 30 and 110; bitset memory of order 16 GB, or a disk-backed variant) · open as of 2026-10-30

## The problem

Run an elementary cellular automaton on a cyclic universe of n cells. Every start eventually enters a cycle. A334497(n) is the longest eventual period over all starts for Rule 30, and A204371(n) the same for Rule 110. Both are listed for n = 1..36. A334497(36) = 2,237,472. Credits for A334497: a(1..7) Bradley Klee, a(8..12) Jinyuan Wang, a(13..22) Pontus von Brömssen, and a(23..36) transcribed by Paolo Xausa in 2023 from Table 2 of Gage, Laub and McGarry (2005). That paper's full state-space census (its Table 1) covers widths 5..24 only, and it lists larger widths as further research, so a(25..36) may not come from an exhaustive search. Wolfram (1986, 'Random sequence generation by cellular automata') published maximum-cycle values for widths up to 54. Gage et al. found larger cycles than Wolfram at widths 22, 27 and 30 (the bold rows of their Table 2), so those 1986 values are not exhaustive and serve only as lower bounds; OEIS lists no term beyond 36. A204371(36) = 1584 (Ben Branman 2012, extended by Lars Blomberg 2015), and A204371(n) >= A180001(n), the eventual period of a single live cell, so A204371(37) >= 4403. Small brute-force checkers written for this check reproduced both sequences for n <= 18.

## What counts as a win

The exact value of A334497(37) or A204371(37) (or any later term), from an exhaustive search over all 2^n states, or over all rotation orbits with the rotation factor accounted for. It must be run by two independent implementations that agree. Both must reproduce A334497(1..24) and A204371(1..30) exactly, and both must report their values for A334497(25..30). Where these differ from the listed terms, the claim must also meet partial p1's correction rule. A value below a listed term means a bug, because every listed term comes from an observed cycle. A witness state on the maximal cycle must be given, so a skeptic can confirm the cycle length by direct iteration. Bit order must follow the Wolfram rule-number convention, which the small-n reproduction checks. The term must not already be in the live OEIS entry at claim time.

## Partial wins

- **p1:** An independent exhaustive recomputation of A334497(25..36). OEIS took a(23..36) from a 2005 conference table whose full census stopped at width 24. The recomputation either confirms every term or corrects one, and a correction must exhibit a cycle longer than the listed value, verified by iteration.
- **p2:** An independent exhaustive recomputation of A204371(31..36) by a second implementation, with the same confirm-or-correct rule.

## How a win is checked

Re-iterate the witness state for the claimed number of steps and check that it returns to itself with no shorter period, by testing the divisors of the claimed length. Re-run one implementation on a held-out width. Inspect the exhaustive code: it should mark visited states or orbits, take the eventual image, and walk each cycle once.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A334497>

## Sources

- <https://oeis.org/A334497>
- <https://oeis.org/A204371>
- <https://homes.luddy.indiana.edu/dgerman/2005midwestNKSconference/dgelbm.pdf>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A cycle found by random sampling is only a lower bound; the term needs exhaustive coverage. Wolfram's 1986 sampled values for widths 37..54 are lower bounds of this kind: a new term must be at least as large as Wolfram's value for that width, or the discrepancy must be explained. For Rule 110, A180001(37) = 4403 is a further floor.
- Rotation-orbit methods must convert an orbit cycle into the true period of the state (orbit length times the rotation offset needed to return).
- Reflection does not commute with Rule 30 or Rule 110 (their mirror images are Rules 86 and 124). Do not reduce by reflection.
- A334497 is the maximum eventual period, not the maximum transient or the number of cycles.
- A334497(25..36) may come from a non-exhaustive search (see statement), so a mismatch there is not by itself evidence of a bug in your exhaustive code. Resolve it with a witness cycle.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/eca-rule30-rule110-cyclic-max-period.md
```

Already set up? Say `run V3R1T4S on eca-rule30-rule110-cyclic-max-period`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `eca-rule30-rule110-cyclic-max-period`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
