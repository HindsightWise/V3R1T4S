# Sloane's 1973 question: an extremal doubly-even self-dual binary [72,36,16] code

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for any serious search; verifying a claimed code takes laptop-minutes to laptop-hours (2^36 codewords, or Brouwer-Zimmermann) · open as of 2026-10-30

## The problem

A doubly-even self-dual binary code of length n has minimum weight d <= 4*floor(n/24)+4 (Mallows-Sloane; Rains for all self-dual codes). For n = 24m a self-dual code meeting the bound must be doubly even (Rains), and the codewords of each fixed weight hold 5-designs (Assmus-Mattson). At lengths 24m the only known extremal codes are the extended Golay code (24) and the extended quadratic residue code (48). N. J. A. Sloane asked in 1973 whether a [72,36,16] self-dual code exists. It is still open. A long series of papers restricts Aut(C) of such a code. Conway-Pless, Bouyuklieva, O'Brien-Willems and others treat prime orders. Feulner and Nebe (arXiv:1110.6012) exclude Z7, Z3xZ3 and D10. Borello, Dalla Volta and Nebe (arXiv:1303.4899) exclude S3, A4 and D8. Borello (arXiv:1304.7162) excludes the elementary abelian group of order 8, which gives |Aut(C)| <= 5. Yorgov and Yorgov (arXiv:1310.2570, IEEE Trans. Inf. Theory 60 (2014) 3302-3307) exclude Z4. So Aut(C) is trivial, C2, C3, C2xC2 or C5. Bouyuklieva, Willems and Yankov (2014) note that no extremal code of length 24m other than those of lengths 24 and 48 is known. The reviewer knows of no construction or non-existence proof since then. Re-check arXiv before claiming.

## What counts as a win

Success means a 36 x 72 binary generator matrix G with these properties, each checked by two independently written programs. (1) rank(G) = 36 over GF(2). (2) G G^T = 0 over GF(2), so the code is self-dual. (3) Every row of G has weight divisible by 4, which together with (2) makes the code doubly even. (4) There are no codewords of weight 4, 8 or 12, so the exact minimum weight is 16, shown by exhaustive enumeration of all 2^36 - 1 nonzero codewords or by an exact Brouwer-Zimmermann computation, never by sampling. (5) The weight distribution equals the unique extremal Gleason weight enumerator (A_16 = 249849). A non-existence proof is also a full win if it comes as an independently re-runnable certificate (exhaustive search with checkable proof logs) that a skeptic re-runs.

## Partial wins

- **p1:** A re-runnable non-existence certificate excluding, for an extremal [72,36,16] code, one automorphism case that the literature still allows at claim time. Examples are Aut(C) containing C2xC2, an automorphism of order 5, or an automorphism of order 3 of the cycle type still allowed. The certificate is published search code that a skeptic re-runs, or SAT runs with DRAT/LRAT proofs, together with a written reduction. A fresh literature search must show that the case was not already excluded.

## How a win is checked

Check rank, G G^T = 0 and row weights mod 4 with bit-packed GF(2) arithmetic. Enumerate all 2^36 codewords with a Gray-code walk over 72-bit words using XOR and popcount, a few minutes in C. Confirm that A_4 = A_8 = A_12 = 0 and that the distribution matches the extremal enumerator from Gleason's theorem. A second independent implementation (e.g. a Brouwer-Zimmermann minimum-distance routine) must agree. Then search arXiv for a newer claim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1310.2570>

## Sources

- <https://arxiv.org/abs/1310.2570>
- <https://arxiv.org/abs/1304.7162>
- <https://arxiv.org/abs/1303.4899>
- <https://arxiv.org/abs/1110.6012>
- <https://web.math.ovgu.de/willems/papers/Aut15n96_new_part.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Restrict to codes with an automorphism of order 3 or 5 of the cycle types still allowed: the code splits into a fixed subcode and an F2[x]/(Phi_p) module, which shrinks the search enormously.
- Use the 5-design structure on the minimum-weight words as a pruning test during search.
- Build from known [72,36,12]/[72,36,14] self-dual codes via neighbours, using exact low-weight counts as the fitness function.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Singly-even (Type I) [72,36,14] or [72,36,16] claims are not this problem. The code must be doubly even, and Type I codes cannot reach 16 at n = 72.
- The literature already excludes many automorphism groups. A search restricted to an excluded group can only rediscover non-existence.
- Minimum weight estimated by random codeword sampling proves nothing.
- Dougherty, Karadeniz and Yildiz (arXiv:1303.4920, 2013) claim that Aut(C) has no involution, which would leave only orders 1, 3 and 5. Later papers (Borello 2013, Yorgov-Yorgov 2014) still list C2 and C2xC2 as open, so a p1 claim for an involution case must say how it relates to that claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/extremal-doubly-even-self-dual-72.md
```

Already set up? Say `run V3R1T4S on extremal-doubly-even-self-dual-72`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `extremal-doubly-even-self-dual-72`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
