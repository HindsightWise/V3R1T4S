# Extremal doubly-even self-dual binary codes at lengths 96, 120 and 128 (beyond the famous 72)

📊 **Record tables** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster for a search; checking a claimed [96,48,20] code takes laptop-hours, and a [120,60,24] or [128,64,24] code laptop-days, with an exact Brouwer-Zimmermann minimum-weight routine · open as of 2026-10-30

## The problem

A doubly-even self-dual binary code of length n (8 | n) has d <= 4*floor(n/24)+4 and is extremal when it meets this bound, so d = 20 needs n >= 96. Harada (arXiv:1902.08739, Adv. Math. Commun. 14 (2020) 89-96) records the status. Existence of an extremal code is unknown at length 96 (d = 20) and at lengths 120 and 128 (d = 24). At 104 the extended quadratic residue code is the only known extremal code. At 112 the first extremal code was found by Harada (2008), and the 2019 note shows at least three inequivalent ones exist. Doubly-even self-dual codes with d = 20 are known at 120 and at 128, so the open step there is d = 24. At 120 the first was found by Gaborit, Nedeloaia and Wassermann (2005), 25 more by Yorgova and Wassermann (2008), and more by Harada. At 128 one comes from Gaborit's table of Type II codes, and Harada gave more. Automorphism restrictions are known. For a [96,48,20] code only the primes 2, 3 and 5 can divide |Aut(C)|, and Bouyuklieva, Willems and Yankov exclude an automorphism of order 15. De la Cruz (arXiv:1302.0033) shows that only 2, 3, 5, 7, 19, 23 and 29 can divide |Aut(C)| of a [120,60,24] code. Length 72 is a separate bank entry (extremal-doubly-even-self-dual-72). The reviewer knows of no construction at 96, 120 or 128. Re-check arXiv before claiming.

## What counts as a win

Success means a generator matrix of a binary doubly-even self-dual [96,48,20], [120,60,24] or [128,64,24] code. Two independent programs must confirm all of the following. (1) Full rank n/2 over GF(2). (2) G G^T = 0. (3) All row weights are divisible by 4. (4) The exact minimum weight equals the extremal value, with no codeword of any smaller weight divisible by 4, shown by an exact minimum-distance algorithm and never by sampling. (5) The length still has no published extremal code at claim time.

## Partial wins

- **p1:** A second extremal doubly-even self-dual [104,52,20] code, proved inequivalent to the extended quadratic residue code of length 104 by an invariant such as the automorphism group order or the number of codewords of weight 20 through a fixed coordinate set, provided that a fresh literature search shows no second [104,52,20] code has been published since Harada (arXiv:1902.08739).

## How a win is checked

Check rank, self-orthogonality and doubly-evenness with bit-packed GF(2) code. Compute the minimum weight with two independent exact implementations, for example a Brouwer-Zimmermann routine with several disjoint information sets plus a separate enumeration of low-weight codewords via the extremal weight enumerator (A_20 for 96 follows from Gleason's theorem), and require agreement. For p1, compute the inequivalence invariant independently.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1902.08739>

## Sources

- <https://arxiv.org/abs/1902.08739>
- <https://arxiv.org/abs/1302.0033>
- <https://web.math.ovgu.de/willems/papers/Aut15n96_new_part.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Quasi-cyclic and double-circulant searches with an allowed automorphism of prime order (19, 23 or 29 at length 120), as Harada and Gulliver did at 112.
- Neighbour walks from the known d = 20 codes at 120 and 128, scoring the exact count of weight-20 codewords and pushing it to zero.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A d = 20 code at length 120 or 128 is not extremal. Extremal there means d = 24.
- Singly-even codes do not count.
- Re-check the literature before claiming p1: Harada's 2019 note is the latest status statement found, and later double-circulant papers may have produced more [104,52,20] codes.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/extremal-doubly-even-self-dual-96-120-128.md
```

Already set up? Say `run V3R1T4S on extremal-doubly-even-self-dual-96-120-128`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `extremal-doubly-even-self-dual-96-120-128`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
