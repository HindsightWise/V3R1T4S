# Viswanath's random Fibonacci constant 1.1319882487943...: a rigorous enclosure to 17 or more decimals

🔢 **Number hunts** · standard · tractability ★★★★☆ · compute: laptop-days · open as of 2026-10-30

## The problem

For t_{n+1} = +-t_n +- t_{n-1} with independent fair random signs, Divakar Viswanath (Math. Comp. 69 (2000) 1131-1155) proved |t_n|^{1/n} -> 1.13198824... almost surely. His method uses Furstenberg's formula with an invariant measure built on the Stern-Brocot tree, evaluated in floating point with a rounding-error analysis. J. B. Oliveira and L. H. de Figueiredo (Reliable Computing 8 (2002) 131-138) gave an interval computation that left the 9th decimal as 7, 8 or 9, certifying 1.13198824. This is recorded in a 2006 OEIS comment by R. J. Mathar, removed from the entry in Oct 2017 but visible in its history. Zai-Qiao Bai (J. Phys. A 40 (2007), cycle expansion) gave further non-rigorous digits, and OEIS A078416 (keywords hard, more) lists 14 digits, 1.1319882487943. Jerome Raulin proposed three more (...061, from Viswanath's program with 2^32 subdivisions, 128-bit floats and Wynn-epsilon extrapolation) in Oct 2017; N. J. A. Sloane deleted them on 25 Feb 2018 'as there seems to be some doubt about them'. So only about 8 decimals are backed by a rigorous enclosure and the published non-rigorous record is 13 to 16 decimals. The constant is the top Lyapunov exponent of an i.i.d. product of two 2x2 matrices; after removing non-increasing segments the problem maps to products of nonnegative matrices (Bai 2011), a setting where Fredholm-determinant and cycle-expansion methods with explicit error bounds (Pollicott 2010, Jurga and Morris 2019) now certify dozens of digits for positive matrices.

## What counts as a win

Success means a rigorous interval enclosure of Viswanath's constant of radius below 10^-D with D >= 17 decimals (settling the disputed digits 061 of 1.1319882487943061), D STRICTLY GREATER (direction: max) than the number of decimals in OEIS A078416 re-fetched live and in any published value found by search immediately before claiming, and consistent with the 13 decimals 1.1319882487943 of A078416. The certificate is a program in rigorous arithmetic (Arb, python-flint, IntervalArithmetic.jl or exact rationals) plus a written proof of every truncation bound it uses (Stern-Brocot depth, cycle-expansion or Fredholm-determinant tail), which a skeptic reruns.

## Partial wins

- **p1:** A rigorous interval enclosure of Viswanath's constant contained in [1.1319882487943, 1.1319882487944], certifying all 13 decimals of OEIS A078416.
- **p2:** A rigorous interval enclosure of radius below 10^-10 (at least 10 certified decimals), beating the roughly 8 decimals of Viswanath (2000) and Oliveira-de Figueiredo (2002).

## How a win is checked

Skeptic: rerun the interval program at two working precisions and check that each truncation error bound is proved in the write-up or cited from a published theorem with matching hypotheses (in particular any reduction from signed to nonnegative matrices). Check that the final enclosure contains 1.1319882487943 and has the claimed radius. Sanity check by Monte Carlo (10^9 steps) that the growth rate agrees to about 4 decimals. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A078416>

## Sources

- <https://oeis.org/A078416>
- <https://oeis.org/history?seq=A078416&start=20>
- <https://doi.org/10.1090/S0025-5718-99-01145-X>
- <https://doi.org/10.1023/A:1014702122205>
- <https://doi.org/10.1088/1751-8113/40/29/008>
- <https://arxiv.org/abs/1901.10944>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Dynamical-zeta import: the Lyapunov exponent of an i.i.d. product of finitely many positive matrices has a Fredholm-determinant expansion with explicit error bounds (Pollicott 2010; Jurga and Morris 2019); first reduce the signed random Fibonacci product to nonnegative matrices by removing non-increasing segments (Bai 2011), then check the contraction hypotheses.
- Interval import: Viswanath's Stern-Brocot formula is already a convergent sum with explicit structure; redo it in ball arithmetic with a proved tail bound at deeper truncation, as Oliveira and de Figueiredo did at lower depth.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Monte Carlo growth rates converge like N^-1/2 and can only sanity-check digits, never supply them.
- Raulin's 16-decimal value was removed from OEIS for doubt; matching it is not verification.
- The Embree-Trefethen threshold 0.70258 (OEIS A118288) belongs to the generalised recurrence t_{n+1} = +-t_n +- x t_{n-1}; growth rates of that family were computed by Y. Lan (J. Stat. Phys. 142 (2011)) and Zhang-Lan (2013), behind a login wall at review time, so it is not part of this target.
- The reduction to nonnegative matrices changes the step count; convert the per-step exponent back correctly before comparing with 1.13198824.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/random-fibonacci-viswanath-embree-trefethen-digits.md
```

Already set up? Say `run V3R1T4S on random-fibonacci-viswanath-embree-trefethen-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `random-fibonacci-viswanath-embree-trefethen-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
