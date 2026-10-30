# Still-life counts in other Life-like rules: HighLife a(14) (A175000), 2x2 a(11) (A166476), Move a(11) (A175001), Maze a(10) (A175002)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

OEIS lists the number of strict still lifes with n live cells, up to rotation and reflection, for several Life-like rules. Christian Schroeder (2010) and Nathaniel Johnston (2009) computed short initial runs that have not been extended since: HighLife B36/S23 (A175000) through n = 13 (218), 2x2 B36/S125 (A166476) through n = 10 (126), Move/Morley B368/S245 (A175001) through n = 10 (3), and Maze B3/S12345 (A175002) through n = 9 (669). Strict means the pattern is stable under the rule and cannot be split into two or more still lifes of that rule. Pseudo still lifes are excluded. HighLife and Life share S23, so a HighLife still life is a Life still life in which no dead cell has exactly 6 live neighbours. Strictness must still be re-decided under the HighLife rule.

## What counts as a win

A new exact term for any of the four sequences: A175000(14), A166476(11), A175001(11) or A175002(10). It must come from two independent enumerators that agree. Each must reproduce every listed term of that sequence, and one must be a general Life-like-rule enumerator, not a filter of a Life still-life list. Report the objects as RLE or apgcodes so a skeptic can re-check stability and strictness one by one. The term must not already be in the live OEIS entry at claim time.

## Partial wins

- **p1:** Any one new term as above (each sequence's next term counts once).
- **p2:** Three or more further consecutive terms of one sequence (e.g. A175000(14..16)), each meeting the same two-enumerator rule.

## How a win is checked

Re-step every reported object under the stated rule with an independent stepper (lifelib supports arbitrary outer-totalistic rules) and check stability. Check strictness by testing every partition of the live cells into still-life parts (or with Cook's skew-symmetric-graph method adapted to the rule). Canonicalise under the 8 symmetries and count. Compare small n with OEIS.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A175000>

## Sources

- <https://oeis.org/A175000>
- <https://oeis.org/A166476>
- <https://oeis.org/A175001>
- <https://oeis.org/A175002>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Strictness depends on the rule. A Life-strict object can be pseudo in another rule, and the reverse.
- Births can only happen in the one-cell ring around the pattern (no rule here has B0), but that ring must be checked under the rule's own birth set: B6 and B8 kill many Life still lifes in HighLife, 2x2 and Move.
- LifeWiki pages for these rules (Cloudflare-blocked here) may already list longer counts. A term already published there is a re-derivation, not a new result, so check before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/lifelike-rules-still-life-counts.md
```

Already set up? Say `run V3R1T4S on lifelike-rules-still-life-counts`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lifelike-rules-still-life-counts`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
