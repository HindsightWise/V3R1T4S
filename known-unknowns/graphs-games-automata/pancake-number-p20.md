# Pancake numbers: settle P(20), the diameter of the 20-pancake graph (OEIS A058986), now known to lie in {22, 23, 24}

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (exhaustive proof); laptop-hours for a single-stack lower-bound certificate · open as of 2026-10-30

## The problem

The pancake number P(n) is the largest number of prefix reversals (flips) needed to sort any stack of n distinct pancakes; equivalently the diameter of the pancake graph on S_n. OEIS A058986 (re-fetched 2026-10-30, revision 185, edited 2026-09-16) lists exact values only for n = 1..19, ending P(18) = 20 and P(19) = 22. Both were proved by Josef Cibulka (arXiv 2009, Theoret. Comput. Sci. 2011), who extended the method of Kounoike, Kaneko and Shinano (n = 14, 15, 2005) and Asai, Kounoike, Shinano and Kaneko (n = 16, 17, PC cluster, 2006): he showed that no 18-stack needs 21 flips, and the two Heydari-Sudborough (1997) stacks of order 19 give P(19) >= 22. His code and data are public. Simon Singh's 2013 blog post later stated the two values, which is how they entered the OEIS entry, and Gerold Jäger and Marcin Peczarski re-confirmed P(19) by branch and bound (OEIS comment, 2020). For n = 20 nothing is listed. J. K. McLean's argument in the entry gives P(20) <= P(19) + 2 = 24, and putting a largest pancake under a hard 19-stack gives P(20) >= 22, so P(20) is 22, 23 or 24. Kazuyuki Amano (IEICE Trans. Inf. & Syst. E108-D(3), 2025) showed that Heydari and Sudborough's stack, built for the (15/14)n lower bound, can be sorted in ceil((15/14)n + 2) flips, so that construction is essentially tight and is not a known source of 20-stacks needing 23 flips. Cibulka's page lists at least 410 stacks of 19 pancakes needing 22 flips (OEIS A067607), but a Cibulka-style proof for n = 20 would have to start from all 19-stacks needing 21 or 22 flips, a set nobody has computed. Deciding P(20), or even showing that one 20-stack needs 23 flips, is new.

## What counts as a win

Either (a) P(20) = 22: a complete, independently re-runnable certificate that every permutation of 20 elements can be sorted in at most 22 prefix reversals (for example a symmetry- and inverse-reduced exhaustive search with released code, logs and per-class counts); or (b) P(20) >= 23: an explicit 20-element stack together with an exhaustive-search certificate (re-runnable within a stated time budget, admissible pruning only) that it cannot be sorted in 22 flips, plus a sorting sequence showing its exact distance; if its distance is 24 that settles P(20) = 24. The value or bound must be strictly new versus the live OEIS A058986 entry and its references re-fetched immediately before claiming, and a novelty check must find no later publication giving P(20).

## Partial wins

- **p1:** The exact value of A067607(18), the number of 18-pancake stacks needing exactly 20 flips (the live entry gives only a(18) >= 12,357,059, from Cibulka's webpage), with a reproducible enumeration and released code, provided the live entry still lists no exact a(18) at claim time.
- **p2:** The exact value of A067607(19), the number of 19-pancake stacks needing exactly 22 flips (the live entry gives only a(19) >= 410), with the complete list released and every listed stack's distance certified by an exact solver with a proved-admissible bound, provided the live entry still lists no exact a(19) at claim time.

## How a win is checked

For a stack claim: apply the flips with a ten-line checker; rerun the released exact solver (IDA* or bidirectional search with a gap-type heuristic proved admissible) and confirm it exhausts depth 22 with no solution, matching node counts. For an upper-bound certificate: rerun the released exhaustive search on a sample of classes and check the reduction argument (inverse and symmetry classes) on paper.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A058986>

## Sources

- <https://oeis.org/A058986>
- <https://oeis.org/A067607>
- <https://doi.org/10.1587/transinf.2024FCL0002>
- <https://doi.org/10.1007/11823285_117>
- <https://doi.org/10.1016/j.tcs.2010.11.028>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Heydari and Sudborough's hard stacks and Amano's 2024 analysis; search their 20-element extensions for one whose exact distance is 23.
- The gap heuristic (number of non-adjacent neighbours) is admissible and very strong on random stacks; hard stacks are the ones with few gaps, so target that region with exact search.
- For the upper bound, combine the inverse map (a stack and its inverse have equal distance) with the reduction that only stacks needing many flips after the largest pancake is placed need deep search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not confuse P(n) with the burnt pancake numbers (A078941, A078942) or with sorting by unrestricted reversals.
- A heuristic that is not proved admissible makes any 'needs 23' claim worthless.
- Credit P(18) = 20 and P(19) = 22 to Cibulka (2011), not to Simon Singh's blog post, which gave no proof.
- When this entry was checked no literature search beyond the OEIS entries, Cibulka's paper and his webpage could be run; re-check arXiv and the live A058986 for 2024-2026 work on P(20) before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/pancake-number-p20.md
```

Already set up? Say `run V3R1T4S on pancake-number-p20`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pancake-number-p20`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
