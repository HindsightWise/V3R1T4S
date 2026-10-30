# Fewest transversals in a Latin square of odd order: beat 778 (n=11), 11744 (n=13), 165289 (n=15) or a larger-order record (OEIS A091323)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (exact transversal counts up to order 21) · open as of 2026-10-30

## The problem

For odd n, let t(n) be the minimum number of transversals in a Latin square of order n (OEIS A091323, indexed by (n-1)/2). Ryser conjectured t(n) >= 1. Exact values are known for n <= 9 (1, 3, 3, 3, 68; McKay, McLeod and Wanless 2006). The live upper bounds have moved repeatedly in 2024-2026: Vatutin (2024-2025), Dennis Yurichev (Sep 2025), and Richard Bean on 20 Sep 2026, giving order 11: 778 (Ian Wanless's square), 13: 11744, 15: 165289, 17: 4384292, 19: 118899160, 21: 3887083600 (Bean's examples in a091323_6.txt, partly from a coloured-block construction). Zur Luria (arXiv:2609.08624, Sep 2026) proves t(n) <= ((1+o(1)) 2n/(3e^2))^n for n = 3 mod 6, improving Dai-Divoux-Kelly, so small-order records are far from settled.

## What counts as a win

Success means an explicit Latin square of odd order n, 11 <= n <= 21, with STRICTLY FEWER transversals than the upper bound for that order in the live OEIS A091323 entry (comments and links, re-fetched immediately before claiming; values on 2026-10-30: 778, 11744, 165289, 4384292, 118899160, 3887083600). The count must agree between two independently written programs. A square with zero transversals would disprove Ryser's conjecture: it is claimed only after a third independent check and a fresh literature search.

## Partial wins

- **p1:** A Latin square of order 11 with exactly 778 transversals that is not in the same main class as Wanless's square, shown by canonical forms under paratopy.
- **p2:** An independent recount that fails to reproduce a count listed in A091323 or its example files (an error), with both programs and the square.

## How a win is checked

Check the square is Latin. Count transversals with two independent exact counters (DLX, and bitmask backtracking). Compare the count with the live A091323 bound for that order.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A091323>

## Sources

- <https://oeis.org/A091323>
- <https://oeis.org/A091323/a091323_6.txt>
- <https://users.monash.edu.au/~iwanless/data/transversals/>
- <https://arxiv.org/abs/2609.08624>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Luria's 3x3 block construction for n = 3 mod 6 (transversals confined to the diagonal blocks or avoiding them) and Bean's coloured construction are both explicit; optimise the blocks by local search at n = 15 and 21.
- Hill-climb with cycle switches, scoring by an exact or sampled transversal count.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Even orders are trivial (Z_2m has no transversals); only odd n counts.
- Diagonal Latin squares have their own sequence (A287645), covered by diagonal-latin-square-spectra-vatutin.
- The bounds moved in Sep 2026; always re-fetch A091323 before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/latin-min-transversals-odd-orders.md
```

Already set up? Say `run V3R1T4S on latin-min-transversals-odd-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-min-transversals-odd-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
