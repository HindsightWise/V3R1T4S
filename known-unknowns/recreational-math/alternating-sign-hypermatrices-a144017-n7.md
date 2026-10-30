# Alternating sign hypermatrices: the number of 7 x 7 x 7 ASHMs, A144017(7) (a(6) found in Feb 2026)

🎲 **Recreational math** · standard · tractability ★★★★☆ · compute: laptop-days (compiled meet-in-the-middle DP over 6.9e7 partial-sum states per middle layer; each step adds one of the 218,348 ASMs of order 7 compatible with the state, generated row by row rather than looped over; modular arithmetic) · open as of 2026-10-30

## The problem

An alternating sign hypermatrix (ASHM) of order n is an n x n x n array over {0,1,-1} whose nonzero entries alternate in sign, starting and ending with +1, along every line in all three directions (Brualdi and Dahl, Adv. Appl. Math. 2018). Those with no -1 entries correspond to the n x n Latin squares. A144017 was entered by Samuel Zbarsky (2008). Cian O'Brien corrected a(4) and added a(5) = 852960 (2023), and Ludovic Schwob reached a(6) = 27729279360 on 11 Feb 2026. a(7) is open (keyword 'hard,more', re-fetched 2026-10-30). Schwob also entered A389236 (ASHM Latin-like squares, after O'Brien 2020), known to a(5) = 848320. Each horizontal slice of an ASHM is an ASM, and the partial sums of the slices along the vertical lines must stay in {0,1}. A DP over these 0/1 partial-sum matrices, whose row and column sums equal the layer index, reproduces a(1)..a(5) exactly (written independently by the drafter, the skeptic and the auditor). For n = 7 the two middle layers each have 68,938,800 states (7 x 7 binary matrices with all line sums 3, or 4; A001501). There are 218,348 ASMs of order 7 (A005130; 7436 is the order-6 count), so the ASMs compatible with each state should be generated row by row, not by looping over all of them. Meet in the middle at layer 3 or 4 therefore makes a(7) a workstation computation in compiled code.

## What counts as a win

The exact integer A144017(7), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, using different methods (for example the partial-sum DP vs a corner-sum or meet-in-the-middle count, or the same DP under a different layer order). The same code must reproduce a(0)..a(6).

## Partial wins

- **p1:** A389236(6), the number of ASHM Latin-like squares of order 6, with code reproducing A389236(1..5), under the same two-run rule.

## How a win is checked

Skeptic: run an independent brute force for n <= 5 and the claimant's DP for n = 6 (minutes). Recompute a(7) modulo a fresh prime, or recompute the forward and backward counts of a random sample of middle-layer states and check the meet-in-the-middle sum.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A144017>

## Sources

- <https://oeis.org/A144017>
- <https://oeis.org/A389236>
- <https://doi.org/10.1016/j.aam.2017.11.005>
- <https://doi.org/10.1016/j.aam.2020.102097>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Meet in the middle: a(7) = sum over 0/1 matrices S with all line sums 3 of f3(S) * f4(J - S), where f_k counts k-slice prefixes reaching that partial sum (reversing the vertical axis turns suffixes into prefixes of J - S). Both layers have 68,938,800 states. The dihedral symmetry of the square acting on all slices at once cuts work and memory by up to 8x.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Lines in all three directions must alternate. Checking only the vertical lines over arbitrary slices overcounts, so each slice must itself be an ASM.
- a(n) grows much faster than the Latin square count; use exact or multi-prime arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/alternating-sign-hypermatrices-a144017-n7.md
```

Already set up? Say `run V3R1T4S on alternating-sign-hypermatrices-a144017-n7`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `alternating-sign-hypermatrices-a144017-n7`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
