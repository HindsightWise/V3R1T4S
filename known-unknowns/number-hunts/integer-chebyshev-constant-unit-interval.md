# Integer Chebyshev constant of [0,1]: a certified bound beating Niedbala Giraudin's 2026 bracket 0.422228600019 <= t_Z([0,1]) <= 0.422684697505

🔢 **Number hunts** · standard · tractability ★★★☆☆ · compute: laptop-hours (LP over a polynomial library plus interval-arithmetic bisection; the published certificates re-check in seconds to minutes) · open as of 2026-10-30

## The problem

The integer Chebyshev constant (integer transfinite diameter) of I = [0,1] is t_Z(I) = lim_n (min over nonzero P in Z[x], deg P <= n, of ||P||_I)^(1/n). By Fekete it is an infimum, so one explicit integer polynomial P gives the upper bound ||P||_[0,1]^(1/deg P). Gelfond and Schnirelman observed that the value 1/e would give an elementary proof of the prime number theorem; the true value is larger. Successive upper bounds came from Borwein-Erdelyi, Habsieger-Salvy, Pritsker (2005), Flammang (2009), Meichsner (2009) and Flammang (2014, 0.422685). The lower bound 0.4213 is Pritsker's (2005). That bracket was the state of the art in Flammang's 2019 survey. David Niedbala Giraudin, 'New bounds for the integer Chebyshev constant of [0,1]', arXiv:2610.00386 (v3, 12 Oct 2026, unrefereed, computations done with Claude), proves 0.422228600019 <= t_Z([0,1]) <= 0.422684697505 (Corollary 3: 0.4222286000 and 0.4226846976). The upper certificate is a product of 92 integer factors with integer exponents. Most come from the Hare-Hodges 23 factors, Hare's Gorshkov-Wirsing tower and Flammang's Table 1. The lower certificate is a discrete measure on 947 cells plus 206 irreducible polynomials, through a new inequality (Theorem 7) that charges for divisibility. Both certificates ship with ancillary verifier scripts. The author claims saturation on neither side: the lower bound still grew when the library went from 70 to 206 polynomials, and no finite library is optimal for the upper one. Qu and Yang (arXiv:2609.39505) independently proved Montgomery's conjecture relating t_Z to leading coefficients of totally real polynomials; this gives no numbers. Push either side of the bracket.

## What counts as a win

Either of the following. (A) An explicit integer polynomial P (or a list of integer factors Q_j with positive integer exponents e_j, P = prod Q_j^e_j) with ||P||_[0,1]^(1/deg P) STRICTLY BELOW 0.422684697505 (direction: min), proved by rigorous interval arithmetic: a bisection of [0,1] (or of w = x(1-x) in [0,1/4] for factors symmetric under x -> 1-x) in which every subinterval carries an outward-rounded upper bound on sum_j e_j log|Q_j| / deg P. (B) A certified lower bound STRICTLY ABOVE 0.422228600019 (direction: max): a measure and polynomial library satisfying the hypotheses of Theorem 7 of arXiv:2610.00386 (pairwise distinct, primitive, irreducible Q_j; budget B <= 1; inf A, the leading-coefficient term and every G_i bounded rigorously), or a certificate for Pritsker's (2005) method. In both cases the value is compared with the best bound on either side published at verification time (re-read the abstract page, its version history and the 2026 literature). For (B) the skeptic must also re-derive Theorem 7 from the paper, since it is new and unrefereed. Floating-point maxima without rigorous enclosures do not count.

## Partial wins

- **p1:** An independent rigorous re-verification of Niedbala Giraudin's shipped upper certificate (0.422684697505) or lower certificate (0.422228600019). It must use interval or exact arithmetic written from the paper's description, not the ancillary scripts. Report a confirmation or a located error. A located error counts as a win only if the skeptic reproduces it.

## How a win is checked

The verifier writes an independent checker with mpmath interval arithmetic (mpmath.iv) or python-flint arb. Upper bound: expand or factor P, confirm integrality and degree, then bisect [0,1] until every subinterval's rigorous enclosure of (1/deg P) * sum e_j log|Q_j(x)| is below log(claimed value). Calibrate on x(1-x), which must give exactly 0.5, and on Giraudin's certificate, which must give <= 0.422684697505. Lower bound: check irreducibility and primitivity (sympy factor_list), that the library is pairwise distinct, the budget B <= 1, and the three quantities of Theorem 7 with outward rounding. Then compare against the live arXiv abstract page for 2610.00386 and any newer paper.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.00386>

## Sources

- <https://arxiv.org/abs/2610.00386>
- <https://arxiv.org/html/2610.00386>
- <https://arxiv.org/abs/1804.05985>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Upper side: enlarge the factor library with new low-height irreducible polynomials with all roots in [0,1] (Gorshkov-Wirsing tower members, transported auxiliary-function factors à la Proposition 6, and greedy LP column generation), then re-solve the semi-infinite LP for the weights and round to integer exponents.
- Lower side: column generation on the 206-polynomial library (the paper reports that its value still grew from 70 to 206 polynomials) and adaptive refinement of the 947 cells.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The upper-bound margin over Flammang is only 3e-7: double-precision suprema are not proofs.
- Weights c_j must become integer exponents (or rationals with a common denominator) before the result is a single integer polynomial.
- A lower bound from one polynomial with all roots in [0,1] proves nothing (Remark 8 of the paper): divisibility must be paid for by the G_i terms.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/integer-chebyshev-constant-unit-interval.md
```

Already set up? Say `run V3R1T4S on integer-chebyshev-constant-unit-interval`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `integer-chebyshev-constant-unit-interval`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
