# A number that is a sum of two fourth powers in three different ways (Taxicab(4,2,3))

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (sorted-sums enumeration beyond 1e28) · open as of 2026-10-30

## The problem

Euler knew 635318657 = 59^4+158^4 = 133^4+134^4, and Leech (1957) proved it is the smallest number that is a sum of two positive fourth powers in two ways (OEIS A003824). No number is known that is a sum of two fourth powers in three ways. Guy (UPINT D1, quoted in OEIS A230561) writes that no one knows of three such equal sums. Search frontiers: Donovan Johnson found none <= 1e21 (OEIS A230561, 2014). Bill Butler lists all 1,413 primitive two-way solutions below 1e28, and Martin Fuller built the A003824 b-file from that list. Butler reports that his search to 1e28 found no three-way solution (unreviewed; he notes the program could be faulty). D. J. Bernstein's sorted-sums method (Math. Comp. 70 (2001)) produced the first 516 primitive solutions. Target: a three-way representation. Credit: Euler, Leech, Bernstein, Butler, D. Johnson, M. Fuller, D. W. Wilson, and the A003824/A230561 editors.

## What counts as a win

CONFIRMED for a positive integer N and three pairwise distinct unordered pairs {a,b} of positive integers with a^4 + b^4 = N for each pair, checked exactly with Python big integers. The win also needs that OEIS A230561, A003824 and MathWorld's 4th-powers page list no such N at verification time. Since none is known, any such N, primitive or not, is the first known example. Representations that use zero or negative fourth powers or differences do not count.

## Partial wins

- **p1:** Frontier extension: an exhaustive enumeration of ALL N = a^4+b^4 <= B (primitive or not) with at least two representations as a sum of two positive fourth powers. The verifier independently reimplements it on sampled windows, with identical per-window lists and hashed logs. It must certify that no N <= B has three or more representations, for a B strictly greater than 1e28 (Butler's bound, the largest claimed on 2026-10-30) and than any larger bound published at verification time. Its primitive sublist below 1e28 must agree with the A003824 b-file (1,413 terms), or the verifier must confirm any disagreement.

## How a win is checked

Three exact big-integer evaluations and a check that the pairs are distinct, under 1 second. For p1, the verifier reruns sampled windows with an independent sorted-sums or hash-join implementation in exact integer arithmetic, compares the lists with the A003824 b-file and audits coverage.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A230561>

## Sources

- <https://oeis.org/A230561>
- <https://oeis.org/A003824>
- <https://www.durangobill.com/RamanujanPics/Rama4thPower.html>
- <https://www.durangobill.com/Ramanujan.html>
- <https://mathworld.wolfram.com/DiophantineEquation4thPowers.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For gcd(a,b) = 1, every odd prime factor of a^4+b^4 is 1 mod 8 (because -1 is then a fourth power mod p), and a^4+b^4 is 1 or 2 mod 16 (Fuller's note on A003824). A three-way N is g^4 times numbers of this shape, so build candidates multiplicatively from primes 1 mod 8 and test them, instead of scanning all sums.
- Euler's and Gerardin's parametric 4.2.2 families: look for a parameter value where two different parametric families give the same N, using resultants and rational-point searches on the resulting curves instead of brute force.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Multiples g^4*N of a two-way N are not new two-way solutions. They give a third pair only if g^4*N also has an unrelated representation, so check every candidate exactly and do not filter non-primitive N away.
- Floating-point sums lose exactness above about 1e16 for doubles (2^53) and about 1e19 for x87 long doubles. Use exact integers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/fourth-powers-three-ways-taxicab-4-2-3.md
```

Already set up? Say `run V3R1T4S on fourth-powers-three-ways-taxicab-4-2-3`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fourth-powers-three-ways-taxicab-4-2-3`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
