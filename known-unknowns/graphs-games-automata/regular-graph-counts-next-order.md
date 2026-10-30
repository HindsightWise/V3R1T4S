# Unlabeled regular graph counts: the next unknown term for cubic, quintic, sextic or 7-regular graphs (A002851, A006821, A006822, A014377), or quartic beyond order 50

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (Burnside over vertex permutations: count labeled k-regular graphs fixed by each cycle type; exp(O(sqrt n)) per degree) · open as of 2026-10-30

## The problem

Counts of connected unlabeled k-regular graphs rose in two steps. Generation came first: Meringer's GENREG, run by Jason Kimberley for processor-years at Newcastle (2009-2011). Counting without generation followed: Andrew Howroyd, Mar-May 2020, gave quartic to n = 28, quintic to 28, sextic to 24 and 7-regular to 24. Cubic connected graphs A002851 are known to 40 vertices (Robinson and Wormald, 'Numbers of cubic graphs', J. Graph Theory 1983). In September 2026 Yue Cheng and Zhipeng Xu (arXiv 2609.31407, 'Exact counting of unlabeled quartic graphs by permutation-cycle aggregation', code on Zenodo) gave quartic counts for orders 29..50. They checked them only via the identity-permutation (labeled) part, and they report no counts for degrees 3, 5, 6 or 7. OEIS checked live 2026-10-30: A002851 ends at 2n = 40, A006820 at n = 28 (Cheng-Xu not yet in the b-file), A006821 at 2n = 28, A006822 at n = 24, A014377 at 2n = 24. No pending drafts.

## What counts as a win

Success means a new exact term of A002851, A006821, A006822 or A014377 at the first order beyond the live b-file, or a connected quartic count at order 51 or more (beyond Cheng-Xu's published table). The term must be computed by two independent methods or implementations that agree exactly, for example a Burnside/cycle-index count and Howroyd-style labeled counting fixed by permutations implemented separately. The same code must reproduce every published term of that sequence and the disconnected version (A005638, A033301, ...) via the inverse Euler transform.

## Partial wins

- **p1:** An independent recomputation of Cheng and Xu's connected quartic counts at orders 29..50, including the nonidentity-permutation contributions they did not cross-check, with a second implementation agreeing. Any disagreement with their table must be resolved and reported.

## How a win is checked

Skeptic: rerun the claimant's code for all published orders and compare; check the identity-permutation contribution against independently computed labeled regular graph counts (A002829 cubic, A005815 quartic, ...); recompute the new term modulo a fresh prime if the method is modular.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A002851>

## Sources

- <https://oeis.org/A002851>
- <https://oeis.org/A006820>
- <https://oeis.org/A006821>
- <https://oeis.org/A006822>
- <https://oeis.org/A014377>
- <https://arxiv.org/abs/2609.31407>
- <https://oeis.org/A033301>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Cheng-Xu's quartic orders 29..50 are already published (arXiv 2609.31407) though not yet in OEIS; claiming them is not a win, only p1 if independently recomputed.
- Cubic, quintic and 7-regular sequences are indexed by 2n (half the order); quartic and sextic by n.
- Connected vs all graphs: convert with the inverse Euler transform and check both against OEIS.
- Cheng-Xu's recurrence and their PARI/GP code (Zenodo doi:10.5281/zenodo.22961966) work for any fixed degree. Running their code for degree 3, 5, 6 or 7 gives one method only; the second method must be implemented separately.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/regular-graph-counts-next-order.md
```

Already set up? Say `run V3R1T4S on regular-graph-counts-next-order`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `regular-graph-counts-next-order`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
