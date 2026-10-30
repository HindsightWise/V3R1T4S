# Finite lattices: the next count of unlabeled lattices (A006966, n = 21), semimodular (A229202, n = 26), modular (A006981, n = 36) or distributive lattices (A006982, n = 61)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (distributive and modular terms likely laptop-hours to days with Kohonen's vertical 2-sum recurrence; general lattices at n = 21 likely needs cluster) · open as of 2026-10-30

## The problem

Unlabeled lattices on n elements (A006966; also semilattices of order n-1) are known to n = 20, with a(20) = 23,003,059,864,006. That term comes from Volker Gebhardt and Stephen Tawn's orderly layer-by-layer algorithm (J. Algebra 545 (2020) 213-236, arXiv 1609.08255); a(19) is Nathan Lawless's. Jukka Kohonen extended semimodular lattices (A229202) to n = 25 (2017) and modular lattices (A006981) to n = 35 (2021). He also extended distributive lattices (A006982 b-file) to n = 60, with a(60) = 758,556,959,660,012, by counting vertical 2-sums of vertically indecomposable lattices (Order 2021, arXiv 2007.03232). That work builds on Jipsen and Lawless (modular lattices, 2013) and Erne, Heitzig and Reinhold (distributive lattices to 49, EJC 2002). All four OEIS entries and their b-files, re-fetched 2026-10-30, stop at those n.

## What counts as a win

Success means the exact next term of A006966 (n = 21), A229202 (n = 26), A006981 (n = 36) or A006982 (n = 61), re-fetched live immediately before claiming. Two independent methods or codes must agree exactly, for example an orderly generation of indecomposables plus the vertical 2-sum recurrence against a direct orderly generation, or two different work partitions with independent kernels. The code must reproduce every published term of that sequence, and a literature search must find no earlier value.

## Partial wins

- **p1:** The number of vertically indecomposable modular lattices on 36 elements or distributive lattices on 61 elements, extending Kohonen's classification (to 35 and 60 elements) and reproducing his published counts.
- **p2:** An independent confirmation of A006966(20) = 23,003,059,864,006 by a different algorithm and code (the value rests on one published computation).

## How a win is checked

Rerun the claimant's code for small n against the b-files. Recompute the vertical 2-sum recurrence from independently generated indecomposables. Spot-check random work units of the orderly generation with independent code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006982/b006982.txt>

## Sources

- <https://oeis.org/A006966>
- <https://oeis.org/A229202>
- <https://oeis.org/A006981>
- <https://oeis.org/A006982>
- <https://oeis.org/A006982/b006982.txt>
- <https://arxiv.org/abs/1609.08255>
- <https://arxiv.org/abs/2007.03232>
- <https://arxiv.org/abs/1708.03750>
- <https://doi.org/10.37236/1641>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Birkhoff duality: distributive lattices with n elements correspond to posets with exactly n down-sets, so generate posets by down-set count rather than lattices.
- Kohonen's recurrence needs only the vertically indecomposable lattices; their growth rate (about 1.725^n for distributive) is far below the totals.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Unlabeled vs labeled lattices; A006966 counts lattices with top and bottom included in n.
- The vertical 2-sum has symmetry cases that create one or two lattices; mishandling them is the classic error (Kohonen corrected A006981(24) in 2017).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/finite-lattices-next-terms.md
```

Already set up? Say `run V3R1T4S on finite-lattices-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `finite-lattices-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
