# Burnt pancake graph diameter g(18) (OEIS A078941): decide 29 or 30

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster for a full proof; laptop-hours for single-stack certificates · open as of 2026-10-30

## The problem

g(n) is the largest number of flips needed to sort any stack of n burnt pancakes (signed prefix reversals), the diameter of the burnt pancake graph, OEIS A078941. It differs from T(n) = A078942, the distance of the single stack -I_n = [-1,...,-n] (the bank's burnt-pancake-even-n-exact-flips entry): T(n) <= g(n), and they differ at n = 15, where Josef Cibulka found two stacks (J_15 and Y_15) needing 25 flips against T(15) = 24. A078941 (re-fetched 2026-10-30) lists g(1..17) = 1, 4, 6, 8, 10, 12, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 28. The values up to n = 10 are from Cohen and Blum (1995), g(11) and g(12) are credited to Korf (2008), and g(13)-g(17) are from Cibulka (2009, 2011), added to the entry by Pontus von Brömssen in August 2026. No value is listed for n = 18. The lower side is fixed by T(18) = 29 (A078942, and Cibulka's 2011 table citing Cohen and Blum), so g(18) >= 29, and g(n+1) <= g(n) + 2 (Cohen and Blum) gives g(18) <= 30. So g(18) is 29 or 30. Cibulka also checked that no J_n or Y_n with n <= 20 other than n = 15 beats -I_n, and Bruno Bouzy (SoCS 2016) grew hard stacks one pancake at a time (changing one orientation or adding +n or -n at the bottom, then solving exactly by IDA*) and found none at n = 18 needing more than 29 flips (his hardest were -I_18, Y_18, H_18,4 and J_18). So a stack needing 30 flips, if one exists, is not of these forms. Cibulka settled g(17) = 28 by the bound g(16) + 2 rather than by listing the 17-stacks that need 28 flips. Those stacks are the candidate base for n = 18 under his contraction method (Lemma 10). Deciding g(18) either way is new.

## What counts as a win

Either (a) an explicit signed stack of 18 burnt pancakes with a re-runnable exact-search certificate that it cannot be sorted in 29 flips (an admissible lower bound whose admissibility proof is given, and matching node counts on rerun), plus a 30-flip sorting sequence, which settles g(18) = 30; or (b) a complete, independently re-runnable certificate that every signed 18-stack sorts within 29 flips (for example Cibulka's candidate-set method extended from the 17-stacks needing 28 flips, with released code, logs and per-depth counts), which settles g(18) = 29. The value must be new versus the live OEIS A078941 entry and its references at claim time, and a novelty check must find no later publication giving g(18).

## Partial wins

- **p1:** An independent recomputation of g(16) = 26 (no signed 16-stack needs 27 flips) with released code different from Cibulka's, together with the exact number of 16-stacks needing 26 flips, which Cibulka's published tables (counts up to n = 15) do not give.
- **p2:** The complete set, with its size, of signed 17-stacks needing exactly 28 flips, each certified by an exact solver with a proved-admissible bound and released with code, if this set is not published at claim time.

## How a win is checked

Apply the claimed flips with a short checker that reverses the prefix and negates signs. Rerun the released exact solver (with an admissible heuristic whose admissibility proof is given) to confirm that no shorter sequence exists, comparing node counts. For an upper-bound claim, rerun the released exhaustive search and check its symmetry and inverse reductions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A078941>

## Sources

- <https://oeis.org/A078941>
- <https://oeis.org/A078942>
- <https://doi.org/10.1016/j.tcs.2010.11.028>
- <https://arxiv.org/abs/2601.09447>
- <https://ojs.aaai.org/index.php/SOCS/article/view/18398>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Cibulka's Lemma 10 lets adjacent pancakes be contracted, so every 18-stack needing 30 flips arises from a 17-stack needing at least 28 flips. Computing that set first is the natural route to either answer.
- Bidirectional search with a signed-gap heuristic decides the exact flip distance of a single 18-stack on a laptop; use it to screen structured candidates beyond those already tried (-I_18, J_18, Y_18 and Bouzy's H_18,M family and one-step extensions of hard 17-stacks).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- T(n) (A078942) and g(n) (A078941) are different sequences; a result about -I_18 belongs to the other bank entry, and T(18) = 29 is already known.
- A stack needing 29 flips is not a result: g(18) >= 29 is already known.
- Flip conventions (whether flipping the top pancake alone counts) change values; reproduce g(1..12) first.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/burnt-pancake-graph-diameter-n18.md
```

Already set up? Say `run V3R1T4S on burnt-pancake-graph-diameter-n18`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `burnt-pancake-graph-diameter-n18`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
