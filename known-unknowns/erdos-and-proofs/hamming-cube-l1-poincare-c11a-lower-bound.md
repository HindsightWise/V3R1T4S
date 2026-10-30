# MOONSHOT - L1 Poincare constant of the Hamming cube (C_11a): a function on {-1,1}^n with ratio above sqrt(pi/2)

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours per candidate, but only at large n: exact multinomial sums for functions of a few block sums with n in the hundreds to thousands. Tables over 2^n points cannot win, because ILvHV's per-dimension dual bound keeps every function on n variables at or below C_dual,n, which is about 1.06 for n <= 7 and is extrapolated to reach sqrt(pi/2) only near n = 60. · open as of 2026-10-30

## The problem

C_11a is the smallest constant with E|f - Ef| <= C E|grad f| for all n and all f: {-1,1}^n -> R, with D_j f(x) = (f(x) - f(x^(j)))/2 and |grad f| the Euclidean norm of (D_j f) under the uniform measure (Tao's page 11a). Ben Efraim and Lust-Piquard (PTRF 2008) proved C_11a <= pi/2; Ivanisvili, Li, van Handel and Volberg (arXiv:1811.05584) proved it is strictly smaller, and Ivanisvili-Stone (arXiv:2407.04835, 2024) made the gap explicit, about 1.3e-4. The lower bound sqrt(pi/2) = 1.2533141 comes from Pisier's sharp Gaussian inequality via the central limit theorem. ILvHV write that it is still not clear whether C_11a > sqrt(pi/2); their computations of a dual constant suggest low dimensions approach sqrt(pi/2) only slowly (perhaps near n = 60). A check on 2026-10-30 found symmetric functions g(sum x_i) of erf/tanh shape reaching only about 1.134 at n = 1001, so a win needs genuinely new structure. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires an explicit function f: {-1,1}^n -> Q (any n; given as a table, or as a formula in the coordinates that a checker can evaluate exactly, such as a function of a few block sums) for which E|f - Ef| / E|grad f| is STRICTLY GREATER (direction: max) than sqrt(pi/2) = 1.2533141373155..., computed with exact rationals and certified square-root enclosures (interval arithmetic with outward rounding) so that the certified lower end of the ratio exceeds sqrt(pi/2), and strictly greater than any larger lower bound listed on https://teorth.github.io/optimizationproblems/constants/11a.html at verification time. This would show C_11a > sqrt(pi/2).

## How a win is checked

Evaluate f on all 2^n points (or via exact multinomial sums for block-structured f), compute E|f - Ef| exactly in rationals, enclose each |grad f|(x) = sqrt(sum_j D_j f(x)^2) by outward-rounded intervals, sum, and compare the certified lower end of the ratio with sqrt(pi/2). Calibrate on n = 1 (f = x gives ratio 1) and on majority functions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/11a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/11a.html>
- <https://arxiv.org/abs/1811.05584>
- <https://arxiv.org/abs/2407.04835>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Functions of two or three block sums (e.g. g(S_A, S_B)) keep exact evaluation cheap at large n while leaving room for non-Gaussian behaviour; symmetric g(S/sqrt n) of erf shape approach sqrt(pi/2) only from below (about 1.039 at n=101, 1.134 at n=1001, 1.193 at n=10001).
- Use ILvHV's dual problem as a filter: ratio(f) <= C_dual,n = sup over |g| <= 1 of the sup-norm of the integral of grad P_t g, which in Fourier terms is sum over S containing j of g^(S)/|S| chi_S. Before searching for f at dimension n, look for a g whose dual value at n exceeds sqrt(pi/2); without one, no f at that n can win.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The gradient uses D_j f = (f(x) - f(x^(j)))/2, not the unhalved difference; a factor 2 error flips the comparison.
- Ratios computed in floating point near sqrt(pi/2) are not certificates; the comparison must be certified.
- Small n cannot win. ILvHV (arXiv:1811.05584, sections 2 and 12) show that E|f-Ef|/E|grad f| <= C_dual,n in each dimension. They find C_dual,n constant for n = 2..7 (optimizer min(x1,x2), value 3*sqrt(2)/4, about 1.0607) and growing slowly after that, reaching sqrt(pi/2) only near n = 60-70 by extrapolation. Exhaustive or gradient-free search over 2^n-point tables at n <= 26 is a dead end for the win.
- Two- and three-valued symmetric functions stay uniformly below sqrt(pi/2) (ILvHV sections 9-10), and Boolean-valued functions satisfy a sharp L1 Poincare inequality (Durcik-Ivanisvili-Roos-Xie, arXiv:2602.20462, 2026); a winning f must take many values.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/hamming-cube-l1-poincare-c11a-lower-bound.md
```

Already set up? Say `run V3R1T4S on hamming-cube-l1-poincare-c11a-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hamming-cube-l1-poincare-c11a-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
