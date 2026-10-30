# Erdos #1204 (Elliott): a narrower admissible k-tuple than Sutherland's table for some 343 <= k <= 5000, or exact minimal sums B(k) beyond k = 147

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (local search over sieved tuples; exact branch and bound for p1) · open as of 2026-10-30

## The problem

A sequence 0 <= a_1 < ... < a_k is admissible if it misses at least one residue class modulo every prime. Erdos #1204 (attributed to Elliott) asks for A(k) = min a_k (the minimal diameter, OEIS A008407) and B(k) = min (a_1+...+a_k)/k. It is known that (1/2+o(1)) k log k <= A(k) <= (1+o(1)) k log k. The best known admissible tuples for k <= 5000 are in Andrew Sutherland's table 'Narrow admissible tuples' (math.mit.edu/~primegaps, Polymath8). Entries are by Engelsma, Sutherland and Xiao-Feng Xie; the last updates are from 2016 and 2019. Optimality is proven only for k <= 342 (Engelsma). Sample entries: k=343: 2340; k=500: 3594; k=1000: 7802; k=2000: 16978; k=3000: 26606; k=5000: 46806. The page says submissions are no longer taken there and directs improvements to Sutherland by email; that is a human action, not part of the win. For B(k), Leandre Jack (forum, 5 Sep 2026) computed exact S(k) = k*B(k) for all k <= 147 by two independent searches; for example S(93) = 22474, and the greedy sequence stops being optimal at k = 93.

## What counts as a win

CONFIRMED: an explicit integer k-tuple, for some 343 <= k <= 5000, that is admissible and has diameter a_k - a_1 strictly smaller than the Sutherland table entry for that k at verification time.

## Partial wins

- **p1:** Exact S(k) = min sum over admissible k-tuples, with an optimal tuple, for every k from 148 up to some K >= 160. Values come from two independent exact searches, and the k <= 147 values must reproduce Leandre Jack's table.
- **p2:** A reproducible exhaustive proof that the k = 343 table entry (diameter 2340) is optimal, or an admissible 343-tuple of smaller diameter (which is then the full win).

## How a win is checked

Admissibility: for every prime p <= k, compute the set of residues a_i mod p and confirm it is not all of Z/pZ; primes p > k are automatic. Diameter: a_k - a_1. Compare with the table row fetched from math.mit.edu/~primegaps on the day. For p1/p2, re-run the exact searches with an independent implementation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://math.mit.edu/~primegaps/>

## Sources

- <https://www.erdosproblems.com/1204>
- <https://www.erdosproblems.com/forum/thread/1204>
- <https://math.mit.edu/~primegaps/>
- <https://oeis.org/A008407>
- <https://github.com/leandrejack-afk/erdos-computations>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Polymath8 methods: Schinzel sieve and shifted greedy sieve, then local 'adjustment' search that swaps elements while keeping admissibility. xfxie's 2016/2019 improvements came from long runs of this kind.
- Most rows still date from June-July 2013. The only later improvements are scattered 2014 rows, xfxie/Engelsma rows of Aug-Sep 2016 spread over k = 1573..4957, and k = 1976-1979 (Feb 2019). Rows untouched since 2013, especially between the improved clusters, may still be soft.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ties do not count: the diameter must be strictly smaller.
- Do not email or submit anything; record the improvement for the human operator.
- Rows for k <= 342 are proven optimal and cannot be beaten.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1204-narrow-admissible-tuples.md
```

Already set up? Say `run V3R1T4S on erdos-1204-narrow-admissible-tuples`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1204-narrow-admissible-tuples`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
