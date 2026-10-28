# Erdős distinct subset sums: an n-element set with distinct subset sums and smaller maximum than the best known

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Erdős Problem #1 asks how small the largest element of an n-element set of positive integers with all subset sums distinct can be. Its asymptotic form (is max(S) >> 2^n?) is now marked disproved on erdosproblems.com/1 (last edited 2026-09-03), by a construction from an OpenAI model ('GPT-6 Astra') giving max(S) <= eps*2^n for arbitrarily large n; that does not settle any small-n value. OEIS A276661 gives the exact minimum a(n) for n <= 10 (Lunnon a(0..8), J. P. Grossman a(9), Paul W. Dyson a(10) = 309 in 2025). For n >= 11 only bounds are known: the Conway-Guy sequence (A005318) gives a(11) <= 594, and Bohman showed it is not always optimal; Dubroff, Fox and Xu give a(n) >= A001405(n) = C(n, floor(n/2)), which Hasratyan and Ruszinkó (arXiv:2610.32580, 23 Oct 2026) improve for odd n to a(n) >= 2*C(n-1,(n-1)/2) (504 for n = 11). As of 2026-10-28, A276661 records sets below Conway-Guy: Ven Popov (Nov 2025) a(12) <= 1157 and a(13) <= 2249; Zachary Sharp (Oct 20 2026, witness sets in the a-file) a(14) <= 4403, a(15) <= 8635, a(16) <= 16946, a(17) <= 33280, a(18) <= 65412, a(19) <= 129517, a(20) <= 256715. Find, for some n >= 11, a set of n positive integers with distinct subset sums whose largest element is strictly smaller than the best known upper bound.

## What counts as a win

Success means an explicit set S of n >= 11 distinct positive integers whose 2^n subset sums are pairwise distinct, verified by two independent programs, with max(S) STRICTLY SMALLER (direction: min) than the best known upper bound for a(n) at verification time: the minimum over https://oeis.org/A276661 (data, comments and a-files, including Sharp's n = 14..20 witnesses) re-fetched live immediately before claiming, the Conway-Guy value A005318(n), Bohman's constructions, https://www.erdosproblems.com/1 and a fresh arXiv search for distinct-subset-sum constructions. Sets that are just a scaling or the {1} U 2S doubling of a known set do not count unless they beat the bound.

## Partial wins

- **p1:** Determine a(11) exactly: an exhaustive search with a reproducible, independently re-runnable enumeration (or a checkable certificate) proving that no 11-element distinct-subset-sum set has maximum below some value, matched by an explicit set attaining it.
- **p2:** A certified lower bound for a(11) above every published one (currently 2*C(10,5) = 504 from Hasratyan-Ruszinkó, arXiv:2610.32580, improving A001405(11) = 462 of Dubroff-Fox-Xu; plus any exhaustive-search bound in A276661 or a fresh arXiv search): an independently re-runnable exhaustive search proving that no 11-element distinct-subset-sum set has maximum <= M, for a stated M larger than the best published lower bound.

## How a win is checked

Compute all 2^n subset sums (n <= 40 with meet-in-the-middle: sort the 2^(n/2) half-sums and check that no two differences coincide, or use a bitset of size sum(S) for n <= 25) and check there are no repeats. Two implementations must agree. Equivalently, verify that no nonzero vector in {-1,0,1}^n gives a zero signed sum. Then compare max(S) with the live OEIS entry and Erdős problems page.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A276661>

## Sources

- <https://oeis.org/A276661>
- <https://oeis.org/A005318>
- <https://www.erdosproblems.com/1>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Popov's n = 12, 13 sets cluster near the maximum with a few small elements, like Conway-Guy sets. Local search: start from the Conway-Guy or Popov set, lower the maximum by 1, and repair by moving 1-3 elements, using a fast incremental test of signed-sum collisions.
- From coding theory: distinct subset sums means the integer vector is a 'detecting matrix' for the coin-weighing problem. Borrow constructions of small-entry detecting matrices and Lindström-type sequences, and convert.
- From lattice reduction: write the condition as 'no nonzero {-1,0,1} vector is orthogonal to S'. Use LLL/BKZ on a lattice built from a candidate S to find short orthogonal vectors quickly, as a fast rejection filter inside a search.
- SAT/ILP over the binary representations of the elements with a pseudo-Boolean constraint per signed combination is too large, but cube-and-conquer on the top few elements with a dynamic-programming check below is feasible for n = 11.
- Recursive improvements: if a smaller set is found at n, the {1} U 2S rule and Bohman's recursions give bounds at n+1, n+2; check whether a direct search beats those propagated bounds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Off-by-one in indexing: A276661 starts at n = 0 (a(0) = 0). Check that the set has exactly n elements.
- Allowing 0 or repeated elements: S must be a set of distinct positive integers.
- Distinct subset sums is not the same as distinct sums of pairs (Sidon) or distinct subset products. Check all 2^n subsets.
- Popov's n = 12, 13 and Sharp's n = 14..20 sets already beat Conway-Guy; beating Conway-Guy alone is not a record. Compare against the best value in the OEIS comments and a-files.
- The 2026 asymptotic disproof on erdosproblems.com/1 is about large n; it gives no small-n record by itself. Compare per n, and check whether any explicit set from that construction or its expositions beats a small-n bound.
- Overflow in subset-sum computation for large n: use 64-bit or big integers and test the checker on a known collision.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/distinct-subset-sums-small-n.md
```

Already set up? Say `run V3R1T4S on distinct-subset-sums-small-n`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `distinct-subset-sums-small-n`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
