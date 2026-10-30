# Toads and Frogs: values of T^a [ ]^b F^a beyond Thanatipanonda's table, or a counterexample to Erickson's Conjecture 5

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days per cell (boards of length 2a + b from 20 to 30; canonical-form evaluation with memoisation) · open as of 2026-10-30

## The problem

Toads and Frogs (Richard Guy, Winning Ways) is played on a strip. Left's toads T move one square right into an empty square or jump one frog; Right's frogs F move left in the same way; the player unable to move loses. Jeff Erickson (Games of No Chance, 1996) made six conjectures. Jesse Hull proved the sixth (NP-hardness, 2000), and Doron Zeilberger and Thotsaporn Thanatipanonda proved 1-3 and refuted 4 (T^7 [ ]^7 F^6 > 2). Conjecture 5 says that T^a [ ]^b F^a (a toads, b empty squares, a frogs) is infinitesimal for every (a, b) except (3, 2), whose value is +-1/8; Wikipedia (re-read 2026-10-30) calls it 'the last one still open'. Thanatipanonda tabulated T^a [ ]^b F^a in Figure 2 of arXiv:0804.0640 (v1, 2008) and in Table 3.1 of the published version (Electron. J. Combin. 18 (2011) P67). Rows a <= 4 are given for b <= 20 and are 0 or *, apart from (3,2) and the b = 2 column (an unspecified infinitesimal for a >= 4). Row 5 is known to b = 13 in the arXiv figure (to b = 12 in the published table), row 6 to b = 7, row 7 to b = 5, and rows 8-10 only to b = 5 or 4. The cells (5,11), (6,8), (7,6) and (7,7) are marked only as non-zero in the arXiv figure and left blank in the published table. He adds that T^2 [ ]^b F^2 = 0 for 21 <= b <= 103 except b = 25, 31, ..., 103 (which are *), and that T^3 [ ]^b F^3 = 0 for 21 <= b <= 53 except b = 29 (which is *). He conjectures that T^a [ ]^b F^a = * for a > b > 0 (b not 2), and that it is 0 or * for b >= a > 0. No later table was found (2026 arXiv math.CO titles checked).

## What counts as a win

CONFIRMED: a position T^a [ ]^b F^a, with a >= 1, b >= 0 and (a, b) not (3, 2), whose value is not infinitesimal (its Left stop or Right stop is non-zero), refuting Erickson's Conjecture 5. The canonical form (or both stops, with a certified game-tree evaluation) must be computed by two independent programs, for example CGSuite and one written by the claimant. The counterexample must not be published at verification time (Wikipedia's Toads and Frogs article, arXiv, Electron. J. Combin.).

## Partial wins

- **p1:** The exact canonical value, computed by two independent programs, of one of the four cells that the arXiv v1 Figure 2 marks only as non-zero and the published Table 3.1 leaves blank, (a, b) = (5, 11), (6, 8), (7, 6) or (7, 7), or of any other cell with a <= 10 and b <= 20 that both versions leave blank.
- **p2:** A counterexample to Thanatipanonda's stronger conjectures, computed by two independent programs: a cell T^a [ ]^b F^a with a > b > 0 and b not 2 whose value is not *, or with b >= a > 0 whose value is neither 0 nor *.

## How a win is checked

Implement Toads and Frogs from the rules (moves: one step into an empty square, or a jump over exactly one opposing piece into an empty square) together with a canonical-form engine. Calibrate on Winning Ways values (T[ ][ ]F = 0, TF[ ][ ] = 1, T[ ]F[ ] = 1/2, TFT[ ]F = *, T[ ]TFF = up) and on Figure 2 cells such as (3,2) = +-1/8 and the rows a <= 4. Recompute the claimed cell with a second program (CGSuite has a Toads and Frogs ruleset) and compare the canonical forms, or at least both stops.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Toads_and_Frogs>

## Sources

- <https://en.wikipedia.org/wiki/Toads_and_Frogs>
- <https://arxiv.org/abs/0804.0640>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v18i1p67>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The four non-zero cells are the cheapest: boards of length 20 to 23. Thanatipanonda's Java program only compared sums; a full canonical-form evaluation with a transposition table keyed by the strip is the obvious upgrade.
- Positions split into independent pieces once toads and frogs are blocked against each other. Evaluate the pieces separately and add their canonical forms.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Thanatipanonda's 'N' in column b = 2 means an infinitesimal he did not write out, not 'unknown'.
- 'Not equal to 0' in the table is consistent with *. Computing only the outcome class cannot refute Conjecture 5; the stops are needed.
- Check the convention: Left owns the toads and moves right; swapping the sides negates every value.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/toads-and-frogs-erickson-conjecture-5.md
```

Already set up? Say `run V3R1T4S on toads-and-frogs-erickson-conjecture-5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `toads-and-frogs-erickson-conjecture-5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
