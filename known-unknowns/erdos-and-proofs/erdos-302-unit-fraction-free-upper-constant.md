# Erdős #302: a certified upper constant below 0.84617 for the largest set in [1,N] with no 1/a = 1/b + 1/c

✏️ **Erdős problems and proofs** · standard · tractability ★★★☆☆ · compute: laptop-hours (exact gadget optimisation plus density sums; Lean optional) · open as of 2026-10-30

## The problem

Let f(N) be the size of the largest A in {1,...,N} with no distinct a, b, c in A satisfying 1/a = 1/b + 1/c (Erdős-Graham). The conjecture f(N) = (1/2+o(1))N is false: Stijn Cambie showed f(N) >= (5/8+o(1))N (odd numbers <= N/4 plus [N/2, N]); SamKorsky (forum 2026-07-05) adds N/(log N)^{0.00415...+o(1)}; a proof claim of Dmitry Khanukov (2026-09-13, github.com/khanukov/erdos302, unrefereed) asserts 5/8 + delta via Della Pietra's #301 work, with an explicit but astronomically small delta = 1/(86400 commonL) in a Lean overlay. Upper bounds: Wouter van Doorn 9/10 (still the value on the problem page); Robert Schuh 373/420 ~ 0.888 (proof claim); Khanukov 140803024/163562355 ~ 0.86085 (proof claim with Lean); Kenta Kitamura (forum 2026-09-25, github.com/KitaKen1/erdos-302-upper-bound, Formal Conjectures PR #6580, merged 2026-09-27) a Lean-verified limsup f(N)/N <= C, an explicit rational C = 0.84617398279640096..., axioms propext, Classical.choice, Quot.sound only. Exact small values are OEIS A390395 (68 terms in the data section; the b-file by Sharvil Kesarwani, first 658 terms from Chai Wah Wu, runs to n = 731 with a(731) = 606 on 2026-10-30). The method: decompose [1,N] into disjoint dilated gadgets a*T, compute exactly the largest solution-free subset of each finite T, and sum densities.

## What counts as a win

CONFIRMED: a complete proof that f(N) <= (c+o(1))N with an explicit rational or exactly specified c strictly below Kitamura's exact constant C = 303298432907684665348375061155255053723893276661771828230864577892179469/358435072543067896655954874015956559321978063343228205466655134412800000 = 0.84617398279640096... (not merely below the rounded 0.8461739827964010 stated in his Lean theorem), and strictly below any smaller constant posted on the #302 thread or proof-claims page at verification time, where every finite optimisation used is supplied as a certificate (explicit gadget sets, exact maximum solution-free subsets with ILP optimality certificates or exhaustive search) and the density sum is computed in exact rational arithmetic. A Lean proof with a clean axiom audit (propext, Classical.choice, Quot.sound only) is accepted in place of the certificate.

## Partial wins

- **p1:** Exact values of A390395(n) for every n from 732 up to at least 800, beyond the OEIS b-file at verification time (n = 1..731 on 2026-10-30), each with a witness set and an optimality certificate (exhaustive branch-and-bound or ILP dual bound) that an independent solver reproduces.
- **p2:** A complete, explicit proof that f(N) >= (c+o(1))N for an explicitly computed rational c >= 5/8 + 1/10000 = 0.6251, strictly above every explicit constant posted on the #302 thread or proof-claims page at verification time (Khanukov's Lean overlay gives only 5/8 + 1/(86400 commonL), astronomically close to 5/8), checkable line by line or in Lean.

## How a win is checked

Recompute each gadget's maximum solution-free subset independently (brute force for small gadgets, a different ILP solver for large ones), check disjointness and coverage of the gadget family, and recompute the limiting density in exact rationals. For Lean, run lake build and #print axioms.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/302>

## Sources

- <https://www.erdosproblems.com/302>
- <https://www.erdosproblems.com/forum/thread/302>
- <https://www.erdosproblems.com/forum/thread/302/proof-claims>
- <https://github.com/KitaKen1/erdos-302-upper-bound>
- <https://oeis.org/A390395>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use gadgets from divisors of larger smooth numbers (Wang's #301 configuration uses divisors of 720); 1/a = 1/b + 1/c iff (b-a)(c-a) = a^2, so solutions in a*T are governed by divisor structure.
- Weight gadgets by the dilation density and solve a single LP over many overlapping gadget families.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The thread moves fast (0.86085 to 0.84617 in two weeks); re-check the record before claiming.
- 301 (sums of k unit fractions) and #327 are different problems.
- Non-distinct b = c changes the answer (2/3 threshold, Cambie); distinctness is required.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-302-unit-fraction-free-upper-constant.md
```

Already set up? Say `run V3R1T4S on erdos-302-unit-fraction-free-upper-constant`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-302-unit-fraction-free-upper-constant`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
