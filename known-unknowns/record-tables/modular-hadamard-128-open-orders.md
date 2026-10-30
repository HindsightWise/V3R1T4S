# 128-modular Hadamard matrix at an order with no known Hadamard matrix (smallest 2396), or a first explicit 64-modular one there

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (modular Golay quadruple searches of length ~600; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

An m-modular Hadamard matrix of order n (Marrero and Butson) is an n x n +-1 matrix with H H^T = nI mod m. Any m-modular Hadamard matrix of order n < m is a true Hadamard matrix, so the Hadamard conjecture is equivalent to the m-modular conjecture for infinitely many m. The m-modular conjecture is settled for m = 5 (Lee and Szollosi), 12 (Marrero-Butson) and 32 (Eliahou and Kervaire, 2001, via modular Golay quadruples in the Goethals-Seidel array), and asymptotically for m = 7, 11 (Kuperberg). S. Eliahou (A 64-modular Hadamard matrix of order 668, Australas. J. Combin. 93(2) (2025) 422-427) reached m = 64 at 668 and announced the classes l = 1, 3, 5 mod 16 and l = 7 mod 32. His published follow-up (An update on modular Hadamard matrices, J. Algebraic Combin. 64 (2026), article 1, 12 June 2026) constructs 64-modular Hadamard matrices at all orders 4l with l = 3 mod 16 or l = 7 mod 32 and names 892 as the smallest open 64-modular order. The 2026 survey of Egan, Kotsireas, London and O Cathain (arXiv:2610.27175, Section 5.4) reports that he announced m = 64 at all orders (personal communication) and poses Problem 10: does a 128-modular Hadamard matrix exist at every order divisible by 4? At orders with a known Hadamard matrix the answer is trivially yes. Doubling (H -> [[H, H], [H, -H]]) turns a 64-modular matrix of order n into a 128-modular one of order 2n, and a 32-modular one into a 64-modular one. So the open cases are the 86 orders up to 10000 with no known Hadamard matrix on the Hadamard Matrix Explorer (math74.com), smallest 2396 = 4*599, then 2676, 2876, 2956, 3004, minus 5912 = 2*2956, which doubling settles because 2956 = 4*739 has l = 3 mod 16. For 2396, l = 599 (7 mod 16, 23 mod 32) is in neither published class.

## What counts as a win

Success means an explicit n x n +-1 matrix H (or a 128-modular Golay quadruple of length n/4 that the verifier expands through the Goethals-Seidel array) with every off-diagonal entry of H H^T divisible by 128, checked exactly by two independent programs, for an order n listed on the live page https://www.math74.com/Hadamard/unknown.html (re-fetched immediately before claiming), not settled as a true Hadamard order by any public source at claim time, and not twice an order with a published 64-modular Hadamard matrix (this excludes 5912 = 2*2956), with no 128-modular (or stronger) Hadamard matrix of that order found by a same-day arXiv search (direction: none; existence target).

## Partial wins

- **p1:** An explicit 64-modular Hadamard matrix (or 64-modular Golay quadruple) of an order n = 4l on the live unknown-orders list with l odd, l not 3 mod 16 and l not 7 mod 32 (the classes published in Eliahou's J. Algebraic Combin. 2026 paper; for example 2396, 2676, 2876, 3004, or 4676 and 5892 with l = 1 or 5 mod 16, which were announced but not published), provided no explicit 64-modular matrix of that order is public at claim time, checked as in the main criterion with modulus 64. Orders 8p (l even, such as 4792, 5752, 5912) do not count: doubling a 32-modular matrix of order 4p already gives one.

## How a win is checked

Compute all pairwise row inner products of H in integer arithmetic and check each off-diagonal value is 0 mod 128 (mod 64 for p1). If a quadruple (A, B, C, D) is given, check sum of aperiodic (or periodic) autocorrelations at every shift 1..l-1 is 0 mod m, then build the Goethals-Seidel array with the verifier's own code and check H H^T directly. Two independent programs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.27175>

## Sources

- <https://arxiv.org/abs/2610.27175>
- <https://ajc.maths.uq.edu.au/pdf/93/ajc_v93_p422.pdf>
- <https://doi.org/10.1007/s10801-026-01544-5>
- <https://www.math74.com/Hadamard/unknown.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Modular Golay quadruples: four +-1 sequences of length l whose autocorrelation sums vanish mod m at every shift (Eliahou-Kervaire); local search with an exact mod-m objective is cheaper than exact Golay quadruples.
- Periodic version: four circulants with periodic autocorrelation sums = 0 mod 128 also feed the Goethals-Seidel array; multiplier-orbit restrictions shrink the space for prime l = 599.
- Combine a 64-modular base with corrections on a few positions to clear the remaining residues mod 128.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- At any order where a true Hadamard matrix is known the problem is trivial; check the order is on the live unknown list, which shrinks as orders fall.
- HH^T = nI mod m requires off-diagonal inner products divisible by m; inner products of +-1 rows of even length are even, so do not count parity as progress.
- Eliahou's published 64-modular classes are l = 3 mod 16 and l = 7 mod 32 (J. Algebraic Combin. 2026); his l = 1 and 5 mod 16 classes (announced in the 2025 AJC note) and his all-orders result (personal communication in arXiv:2610.27175) are not public as matrices. Cite only what is published when claiming p1, and check for a newer Eliahou paper first.
- Doubling: [[H, H], [H, -H]] maps an m-modular matrix of order n to a 2m-modular one of order 2n. A 128-modular matrix at 2n is not new when a 64-modular one of order n is published (5912 = 2*2956), and a 64-modular one at an order 8p is not new because 32-modular matrices exist at every order 4p.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/modular-hadamard-128-open-orders.md
```

Already set up? Say `run V3R1T4S on modular-hadamard-128-open-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `modular-hadamard-128-open-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
