# Reinhart's open problem: squarefree d = pq or 2pq with h(d) = 2 and d | y (orders with unusual sets of distances)

🔢 **Number hunts** · standard · tractability ★☆☆☆☆ · compute: needs cluster (Reinhart's exhaustive search of squarefree d <= 2.3e14 used well over a million core-hours; new examples are expected only above that) · open as of 2026-10-30

## The problem

Let d >= 2 be squarefree, K = Q(sqrt d), omega = sqrt d if d = 2,3 mod 4 and (1+sqrt d)/2 if d = 1 mod 4, and epsilon = x + y*omega the fundamental unit. Andreas Reinhart (Acta Arith. 211 (2023) 61-92, arXiv 2305.09267) characterised orders in real quadratic fields with min Delta(O) = 2 ('unusual' sets of distances), and in Acta Arith. 215 (2024) 85-95 (Prop. 2.4, Thm. 2.5) tied them to the condition d | y. In Section 4 of arXiv 2410.21864 (v3, 15 Dec 2025) he poses this open problem: find squarefree d with (a) d = pq, p = 5 mod 8, q = 3 mod 4, h(d) = 2, y odd, d | y; or (b) d = pq, p != q, p = q = 1 mod 4, d = 5 mod 8, h(d) = 2, N(epsilon) = -1, d | y; or (c) d = pq, p = 1 mod 8, q = 3 mod 4, h(d) = 2, y odd, d | y; or (d) d = 2pq, p != q, p = q = 3 mod 8, h(d) = 2, d | y. He writes that apart from d = 5374184665 he does not know whether any of these situations can occur. His searches covered every squarefree d <= 2.3e14 (not independently double-checked), and only 22 squarefree d with d | y are known in all, so any solution is expected above 2.3e14. The AAC counterexample 331914313984493 (prime) is the first known squarefree d = 5 mod 8 with d | y, and one of only two known with N(epsilon) = -1.

## What counts as a win

CONFIRMED (full win) for a squarefree d with an explicit factorisation into proven primes that satisfies all the conditions of one of (a), (b), (c) or (d) above, exactly as stated in Section 4 of arXiv 2410.21864. h(d) = 2 must be proven unconditionally (PARI bnfinit + bnfcertify, which also certifies the fundamental unit, or an equivalent proven computation in Magma). x and y of the certified fundamental unit (taken > 1) are computed modulo 2d from its compact representation, and the verifier checks d | y, the parity of y where required, and N(epsilon) where required. The result must not already appear in Reinhart's papers or later literature at verification time.

## Partial wins

- **p1:** A composite squarefree d = 5 mod 8 with d | y for the certified fundamental unit of Q(sqrt d), certified as in the full criterion. The only known squarefree d = 5 mod 8 with d | y is the prime 331914313984493.
- **p2:** A composite squarefree d other than 5374184665 with d | y and N(epsilon) = -1, certified as in the full criterion. Reinhart says 5374184665 and 331914313984493 are the only two known squarefree d with these properties.

## How a win is checked

PARI/GP: prove p and q prime; bnf = bnfinit(minpoly of omega, 1); bnfcertify(bnf) == 1; read the class number; reduce the compact fundamental unit modulo 2d in O_K to get x and y mod 2d; check the congruences and the sign of the norm. Cross-check y mod d with an independent continued-fraction or infrastructure computation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2410.21864>

## Sources

- <https://arxiv.org/abs/2410.21864>
- <https://arxiv.org/abs/2305.09267>
- <https://arxiv.org/abs/2404.03038>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Screen candidates fast: d | y is equivalent to the order Z + dO_K having the same regulator as O_K. Test it with infrastructure arithmetic modulo d before certifying the class number.
- Restrict the sieve to d whose genus theory forces the 2-rank of the class group to be exactly 1, so h(d) = 2 is likely.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Use O_K = Z[omega] with the omega given above. For d = 2,3 mod 4, y is the coefficient of sqrt d.
- A GRH-conditional class number or unit is not enough; certify it.
- d = 5374184665 = 5 * 1074836933 is 1 mod 8, so it does not satisfy (b); check each congruence literally.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/reinhart-unusual-orders-d-divides-y.md
```

Already set up? Say `run V3R1T4S on reinhart-unusual-orders-d-divides-y`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `reinhart-unusual-orders-d-divides-y`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
