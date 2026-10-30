# MOONSHOT - Davenport constant in rank 3: a group C_n1 + C_n2 + C_n3 with D(G) > D*(G)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (a certificate checks in milliseconds) · open as of 2026-10-30

## The problem

The Davenport constant D(G) of a finite abelian group G = C_n1 + ... + C_nr (n1 | ... | nr) is the least l such that every sequence of l elements has a nonempty zero-sum subsequence, and D(G) >= D*(G) = 1 + sum(n_i - 1). Olson (1969) proved equality for rank <= 2 and for p-groups. Equality is also known for some rank-3 families: C_3+C_3+C_3d (Bhowmik-Schlage-Puchta), C_4+C_4+C_4d, C_6+C_6+C_6d, C_{3*2^t}+C_{3*2^u}+C_{3*2^v}, C_{2p^a}+C_{2p^b}+C_{2p^c}, C_2+C_2m+C_2mn for all m and n (Girard-Schmid, J. Number Theory 197 (2019), Theorem 2.7, completed by Reiher's proof of Property B), and G1 + C_{p^k n} with G1 a p-group and p^k >= D*(G1). Most of this list is in Agarwal-Chen-Garg (MIT PRIMES 2024, section 2), which still carries an older restriction for C_2+C_2n+C_2n (no prime p >= 11 dividing n). Biswas-Mazumdar (arXiv:2402.09999) treat C_p^(d-1)+C_pq, conditionally when gcd(p,q) = 1, and cite A. Sheikh's 2017 University of London thesis for C_p+C_p+C_2p. In rank >= 4 there are infinitely many groups with D(G) > D*(G) (Geroldinger-Schneider and later work). For rank 3 it is conjectured that D(G) = D*(G) always. Benjamin Girard and Alain Plagne (arXiv:2510.20412 v1, Oct 2025) call this conjecture 'wide open'. One zero-sum-free sequence of length D*(G) over any rank-3 group would refute it.

## What counts as a win

Success means an explicit sequence over a group G of rank exactly 3 (n1 | n2 | n3, n1 >= 2) of length D*(G) = n1+n2+n3-2 with no nonempty zero-sum subsequence, verified by two independent programs. This proves D(G) >= D*(G)+1, STRICTLY GREATER (direction: max) than D*(G). Before claiming, check G against every family where D(G) = D*(G) is proven: the PRIMES 2024 list, Girard-Schmid (arXiv:1806.07636, all C_2+C_2m+C_2mn), arXiv:2402.09999 and the Sheikh thesis it cites, the Gao-Geroldinger survey, and a fresh arXiv search. A hit on a proven family means the checker has a bug.

## Partial wins

- **p1:** A certified determination D(G) = D*(G) for a rank-3 group G that no published result covers at verification time (check the PRIMES 2024 list, Girard-Schmid arXiv:1806.07636, arXiv:2402.09999 and the Sheikh thesis it cites, the surveys and a fresh arXiv search; a candidate to examine first is C_5+C_5+C_10, after confirming that Sheikh's work on C_p+C_p+C_2p does not already cover it; C_2+C_2m+C_2mn groups such as C_2+C_22+C_22 are settled). This needs an exhaustive search, with independently re-runnable code and two implementations that agree, showing that no zero-sum-free sequence of length D*(G) exists.

## How a win is checked

Keep a bitset R over G of the sums of nonempty subsequences seen so far. For each term g, set R = R | (R + g) | {g}. The sequence is zero-sum-free if and only if 0 never enters R. The cost is O(L |G|). For the second implementation, use explicit subset enumeration for L <= 25, or a Smith-normal-form-independent encoding of G as Z_n1 x Z_n2 x Z_n3. Check that n1 | n2 | n3 (or convert to invariant factors), that the rank is 3, and that the length is exactly D*(G).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2510.20412>

## Sources

- <https://arxiv.org/abs/2510.20412>
- <https://math.mit.edu/research/highschool/primes/materials/2024/Agarwal-Chen-Garg.pdf>
- <https://arxiv.org/abs/1806.07636>
- <https://arxiv.org/abs/2402.09999>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p49/pdf/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The rank->=4 counterexamples (Geroldinger-Schneider) use groups C_n^{(k-1)n+rho} + C_kn whose rank grows with n. Look for a 'rank-compressed' analogue: groups with two coprime-mixed factors, such as C_m + C_mn + C_mnk with gcd conditions, where the projection argument could fail.
- Search groups of moderate order (<= 2000) not covered by known theorems with SAT or ILP plus lazy cuts: the variables are the sequence terms, and each zero-sum found adds a cut.
- Use the inverse structure: extremal zero-sum-free sequences in the known cases have a rigid form (Property B-like). Search for long zero-sum-free sequences that avoid that structure.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convert to invariant factors first. C_2+C_3+C_6 has rank 2 (it is C_6+C_6), and D* must use the n1 | n2 | n3 decomposition.
- Zero-sum-free means no NONEMPTY subsequence of any length sums to 0. The empty sequence does not count, and single terms equal to 0 are already zero-sums.
- Most small rank-3 groups are covered by theorems; check the list before spending compute.
- The PRIMES 2024 list is out of date for C_2+C_2n+C_2n: Girard-Schmid (2019, Theorem 2.7) settle every C_2+C_2m+C_2mn, including C_2+C_22+C_22.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/davenport-rank-3-above-dstar.md
```

Already set up? Say `run V3R1T4S on davenport-rank-3-above-dstar`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `davenport-rank-3-above-dstar`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
