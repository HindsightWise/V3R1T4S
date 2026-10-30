# Bernstein's constant beta = lim 2n E_2n(|x|): more than the 50 decimals of Varga and Carpenter (1985)

🔢 **Number hunts** · standard · tractability ★★★☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Let E_m(|x|) be the error of the best uniform approximation of |x| on [-1,1] by real polynomials of degree at most m. Bernstein (Acta Math. 1913/14) proved that beta = lim_{n -> inf} 2n E_{2n}(|x|) exists, showed 0.278 < beta < 0.286, and conjectured beta = 1/(2 sqrt(pi)) = 0.28209.... Richard S. Varga and Amos J. Carpenter (Constr. Approx. 1 (1985) 333-348; Mat. Sb. 1986, English Math. USSR Sb. 57 (1987)) disproved the conjecture with high-precision Remez computations and Richardson extrapolation. Their value 0.2801694990238691330364364912306720000424821398... is the source of the 50 decimals in OEIS A073001 (keyword 'more'; b-file n = 0..49). For the value, MathWorld cites only Varga-Carpenter (1987) and Varga's SIAM book (1990), and Wikipedia quotes 12 digits. An unexplained OEIS extension to a(106) was proposed in Aug 2026 and reverted by the editors within a week, so the published record is still 50 decimals. No closed form is known. Because E_{2n}(|x|) = E_n(sqrt t) on [0,1] and 2n E_{2n} has an asymptotic expansion in 1/n^2 (exploited by Varga-Carpenter), today's multiprecision Remez codes should reach far larger n and many more digits on a laptop.

## What counts as a win

Success means a decimal value of beta with D decimals, D >= 60 and STRICTLY GREATER (direction: max) than the digit count of OEIS A073001 re-fetched live and of any published value found by a literature search re-run immediately before claiming. Conditions: (a) two independent determinations agree on all D decimals (for example Richardson or Levin-type extrapolation from two disjoint ranges of n, or two different Remez implementations); (b) the first 50 decimals match A073001, or any disagreement is confined to its last few decimals and is explained in the write-up and backed by the certified E_{2n} brackets; (c) the digits are stable when the largest n used is increased by at least 20%. Each E_{2n} used must be certified to the working precision by an equioscillation (de la Vallee Poussin) bracket.

## Partial wins

- **p1:** A table of E_{2n}(|x|) for all n <= 200, each with a certified two-sided de la Vallee Poussin bracket of relative width below 10^-60, posted with the alternation points and coefficients so that every row can be rechecked independently.

## How a win is checked

Skeptic: for 10 random rows, recheck the de la Vallee Poussin lower bound (alternating signs and sizes at the stated points) and the upper bound (the maximum of |p(x) - |x|| over [-1,1], by interval subdivision) in multiprecision interval arithmetic. Rerun both extrapolations and compare digits. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A073001>

## Sources

- <https://oeis.org/A073001>
- <https://mathworld.wolfram.com/BernsteinsConstant.html>
- <https://en.wikipedia.org/wiki/Bernstein%27s_constant>
- <https://doi.org/10.1007/BF01890040>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Work with sqrt(t) on [0,1] (half the degree) and a barycentric Remez in Chebfun-style multiprecision; reuse the previous n's alternation set as the starting guess.
- Sequence-acceleration import: fit the known 1/n^2 expansion by least squares with many terms and validate on held-out n, as in high-precision extrapolation of lattice series.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Agreement of two extrapolations from overlapping n ranges is not independent; use disjoint ranges.
- Remez iterates that have not equioscillated to full precision inflate E_{2n}; certify each value with an equioscillation bracket.
- E_n for odd n equals E_{n-1} for the even function |x|; indexing slips shift the limit by a factor of 2.
- The A073001 history shows digits a(50)-a(106) proposed in Aug 2026 without a method and then reverted. Matching them is not verification, and OEIS editors reject unexplained machine-computed digits, so a claim must include its method and certificates.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/bernstein-constant-digits.md
```

Already set up? Say `run V3R1T4S on bernstein-constant-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bernstein-constant-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
