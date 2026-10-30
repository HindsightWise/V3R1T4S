# Langford's problem: the number of Langford pairings L(2,31) or L(2,32), or the next Nickerson-Skolem (V(2,32), V(2,33)) or planar (P(43), P(44)) counts

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (Godfrey-type inclusion-exclusion over about 2^62 sign vectors for n = 31; pruned planar searches may be laptop-days) · open as of 2026-10-30

## The problem

Langford's problem (C. Dudley Langford, 1958): arrange 1,1,2,2,...,n,n so that the two copies of k have exactly k numbers between them. L(2,n) counts solutions up to reversal (OEIS A014552). It is nonzero iff n = 0 or 3 mod 4. Known values: L(2,15), L(2,16) in the 1980s; L(2,19) 1999; L(2,20) 2002 (Godfrey's algebraic method); L(2,23) = 3,799,455,942,515,488 (Krajecki, Jaillet and Bui, 2004); L(2,24) 2005; L(2,27) = 111,683,611,098,764,903,232 and L(2,28) = 1,607,383,260,609,382,393,152 (Assarpour, Bar-Noy and Liu, arXiv:1507.00315, 2015). John E. Miller's Langford page (dialectrix.com) says that all n >= 31 are unknown. Zan Pan (2021) gave asymptotic estimates. Related tables: Nickerson's variant, where the two k's have k-1 numbers between them (Skolem-type, OEIS A059106, nonzero for n = 0, 1 mod 4), is listed through n = 31. The last nonzero terms, n = 28 and 29, come from Assarpour et al. (added in 2023), and a(30) = a(31) = 0, so V(2,32) and V(2,33) are next. Planar Langford sequences, where arcs joining equal numbers can be drawn without crossing (OEIS A125762), are known through n = 42. Knuth computed them through n = 28 (2007), Rory Molinari added n = 31 to 35 in 2018, and Edward Moody added n = 36 to 42 in April 2019. a(41) = a(42) = 0, so P(43) and P(44) are next. All three OEIS entries were re-fetched on 2026-10-30 and show these ranges.

## What counts as a win

The exact value of L(2,31) or L(2,32), the first unknown terms of OEIS A014552 at verification time. It must come with complete source code and a run log, and be confirmed by a second independent computation (different code, or a different method such as direct enumeration on a subrange plus the algebraic formula), with agreement on every digit. Any claimed value must also pass consistency checks: the method must reproduce L(2,n) exactly for all n <= 28, and the value must be of the size predicted by Zan Pan's asymptotic formula.

## Partial wins

- **p1:** The exact Nickerson-variant count V(2,32) or V(2,33) (the next nonzero terms of OEIS A059106, which is listed through n = 31), verified as in the success criterion, with the method reproducing all known terms.
- **p2:** The exact planar Langford count P(43) or P(44) (the next terms of OEIS A125762 beyond n = 42), verified as in the success criterion, with the method reproducing all known planar terms.
- **p3:** An independent recomputation of L(2,27) and L(2,28), with code independent of Assarpour-Bar-Noy-Liu, that matches the OEIS values exactly, together with measured timings that project the cost of n = 31.

## How a win is checked

Rerun the released code on small n and check every known term of A014552, A059106 or A125762. For a new term, require two independent computations to agree. Where the Godfrey formula is used (a signed sum over plus-or-minus-one vectors of products of polynomial sums), recompute modulo several large primes in a separate implementation and check against the exact big-integer value.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A014552>

## Sources

- <https://oeis.org/A014552>
- <http://dialectrix.com/langford.html>
- <https://arxiv.org/abs/1507.00315>
- <https://oeis.org/A059106>
- <https://oeis.org/A125762>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A014552 counts up to reversal. A176127 counts ordered arrangements, which is twice as many. Do not mix the two conventions.
- n = 29 and 30 are zero for L(2,n), since n must be 0 or 3 mod 4. The first unknown nonzero terms are n = 31 and 32.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/langford-skolem-pairings-next-counts.md
```

Already set up? Say `run V3R1T4S on langford-skolem-pairings-next-counts`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `langford-skolem-pairings-next-counts`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
