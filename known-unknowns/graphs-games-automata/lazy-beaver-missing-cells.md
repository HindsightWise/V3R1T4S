# Lazy Beaver: compute a missing LB(n, m) value (LB(7,2), LB(5,3), LB(4,4), LB(3,5) or LB(2,7))

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (all tree-normal-form machines of the domain run to the answer's step count) · open as of 2026-10-30

## The problem

The Lazy Beaver LB(n, m), defined by Scott Aaronson in his 2020 survey, is the smallest k > 0 such that no n-state, m-symbol Turing machine halts in exactly k steps from a blank tape. Unlike the Busy Beaver it is computable: deciding it only needs every machine simulated for k steps. The bbchallenge wiki's Lazy Beaver page (last edited 2026-10-09) lists values computed by Terry and Shawn Ligocki in 2021: LB(2..6, 2) = 7, 22, 72, 427, 8,407; LB(2,3) = 23, LB(3,3) = 351, LB(4,3) = 189,270; LB(2,4) = 93, LB(3,4) = 242,789; LB(2,5) = 956; LB(2,6) = 33,851. OEIS A337805 (Zachary Vance, 2020; a(6) added by Tijn Caspar de Leeuw, 2026-02-04) has LB(n,2) through n = 6. The cells LB(7,2), LB(5,3), LB(4,4), LB(3,5) and LB(2,7) are empty.

## What counts as a win

Success means an exact value for one cell that is empty on https://wiki.bbchallenge.org/wiki/Lazy_Beaver and in OEIS A337805 when re-fetched before claiming: a number k, a list of witness machines halting in exactly j steps for every j < k, and a complete tree-normal-form enumeration of the domain, run by code that can be audited, showing that no machine halts in exactly k steps (every machine either halts at some other step count or is still running after k steps). The step convention must match the listed values, and the enumeration must reproduce at least one listed value in a neighbouring cell.

## Partial wins

- **p1:** An independent re-computation of LB(6,2) = 8,407 or LB(2,6) = 33,851 with published code, or a demonstration that a listed value is wrong.

## How a win is checked

Re-run every witness machine and confirm it halts in exactly the stated number of steps. Re-run the enumeration with an independently written tree-normal-form generator, check the machine counts per depth, and confirm that no machine halts at step k. Calibrate on small cells (LB(2,2) = 7, LB(3,2) = 22, LB(2,3) = 23).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Lazy_Beaver>

## Sources

- <https://wiki.bbchallenge.org/wiki/Lazy_Beaver>
- <https://oeis.org/A337805>
- <https://www.scottaaronson.com/papers/bb.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Enumerate in tree normal form with a step cap equal to the current candidate k. Most branches halt or are pruned early, and machines still running at k need no further work.
- Grow the witness set incrementally. A sorted bitmap of achieved halting times, updated as the enumeration runs, gives the answer as its first gap.
- Cells with n*m = 14 (LB(7,2) and LB(2,7)) have the smallest raw machine domains among the empty cells. LB(5,3) and LB(3,5) have 15 transitions and LB(4,4) has 16.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Halting-step conventions differ (whether the halting transition counts), so calibrate on the listed values first.
- Checked 2026-10-30: no value beyond the wiki table turned up on Shawn Ligocki's blog (sligocki.com) or in web search. The googology wiki page was unreadable (HTTP 402) and the Busy Beaver Discord needs a login, so neither was checked. Re-check both, the second as a human step, before claiming.
- Tree normal form must not drop machines that halt in exactly k steps through symmetric variants. Prove that the reduction preserves halting times.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/lazy-beaver-missing-cells.md
```

Already set up? Say `run V3R1T4S on lazy-beaver-missing-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lazy-beaver-missing-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
