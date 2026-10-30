# Rhombic tilings of the 2n-gon (primitive sorting networks, A006245): the count for n = 17, or the next term of a higher-dimensional zonotopal-tiling column A060595-A060601

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (n = 17 rhombic tilings); laptop-hours to laptop-days for several zonotope cells · open as of 2026-10-30

## The problem

A006245(n) counts rhombic tilings of a 2n-gon. The same number counts primitive sorting networks on n elements, commutation classes of reduced words of the longest permutation, simple Euclidean arrangements of n pseudolines and rank-3 signotopes. No formula is known, only asymptotic bounds: Felsner-Valtr, with lower bounds improved by Dumitrescu-Mandal and Cortés Kühnast, Dallant, Felsner and Scheucher (arXiv:2402.13107, 2024). Terms: a(10) Felsner 1996, a(11) Yamanaka 2009, a(12) Samuel 2011, a(13) Toshiki Saitoh 2011 (PiDDs), a(14)-a(15) Yuma Tanaka 2013, and a(16) = 76413073725772593230461936736 by Gunter Rote (Dec 2021). a(17) is open: re-fetched 2026-10-30, and the 2024 table of Cortés Kühnast et al. also stops at n = 16. The higher-dimensional analogues count tilings of the zonotope Z(D,d) (higher Bruhat orders, signotopes of rank d+1); they are the columns of A060637. Known ranges: A060595 (d=3) D <= 10, A060596 (d=4) D <= 10, A060599 (d=5) D <= 11, A060597 (d=6) D <= 11, A060598 (d=7) D <= 12, A060600 (d=8) D <= 13, A060601 (d=9) D <= 13. Manfred Scheucher computed the recent terms (2021-2023), and his C++ program for enumeration is linked from A006245.

## What counts as a win

The exact integer A006245(17), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly: two different algorithms, or one algorithm under two different state encodings with exact or multi-prime arithmetic. The same code must reproduce a(1)..a(16).

## Partial wins

- **p1:** The next term of A060595 (D = 11) or A060596 (D = 11), with the code reproducing all published terms of that column, under the same two-run rule.
- **p2:** The next term of A060599 (D = 12), A060597 (D = 12), A060598 (D = 13), A060600 (D = 14) or A060601 (D = 14). The code must reproduce all published terms of that column and the D = d+3 values of A060602, under the same two-run rule.

## How a win is checked

Skeptic: run Scheucher's published C programs or the claimant's code for small n and D and compare with the OEIS terms. Then rerun the claimed value modulo a fresh prime, or with a second algorithm (for A006245, a sweep-line DP over wiring-diagram cuts vs a signotope DP).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006245>

## Sources

- <https://oeis.org/A006245>
- <https://oeis.org/A060637>
- <https://oeis.org/A060595>
- <https://oeis.org/A060596>
- <https://oeis.org/A060599>
- <https://arxiv.org/abs/2503.02336>
- <https://arxiv.org/abs/2402.13107>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Count, do not list: a(16) is 7.6e28, so a(17) needs a DP over sweep states (cuts of the wiring diagram) or signotope prefixes, never one-by-one enumeration.
- For higher signotopes, a DP that adds one element at a time over the extension structure (Bergold-Felsner-Scheucher) is a natural route.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A006245 is the Euclidean (labelled) count; A006246 and A006248 are projective or up-to-symmetry order-type counts and are not this target.
- Offsets differ by column (A060595 starts at D = 3, A060601 at D = 9).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/rhombic-zonotopal-tilings-a006245-n17.md
```

Already set up? Say `run V3R1T4S on rhombic-zonotopal-tilings-a006245-n17`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rhombic-zonotopal-tilings-a006245-n17`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
