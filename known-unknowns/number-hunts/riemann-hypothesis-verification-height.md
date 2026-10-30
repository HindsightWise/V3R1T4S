# MOONSHOT - Riemann hypothesis verified beyond Platt-Trudgian's height 3.0001753328 x 10^12, or a rigorous window above it

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for a new height record (Platt-Trudgian used rigorous interval arithmetic over about 1.2 x 10^13 zeros); laptop-days for a rigorous window of 10^5-10^6 zeros at large height · open as of 2026-10-30

## The problem

Riemann hypothesis verification: show that all zeros of zeta(s) with 0 < Im(s) <= T lie on the critical line and are simple. Rigorous record: David Platt and Tim Trudgian, 'The Riemann hypothesis is true up to 3 x 10^12' (Bull. LMS 2021, arXiv:2004.09765), T = 3.0001753328 x 10^12, using interval arithmetic with Turing's method and an Odlyzko-Schönhage-type multi-evaluation. It also re-checked earlier work. Gourdon and Demichel (2004) computed the first 10^13 zeros, plus 2 x 10^9 zeros near the 10^13-th, ..., 10^24-th zero, but without rigorous error control. Odlyzko computed zeros near index 10^23. The Wikipedia RH page (edited October 2026) states the Platt-Trudgian height as the record. Many explicit results (zero-free regions, explicit prime-counting bounds, Mossinghoff-Trudgian-Yang 2024) start from this height, so a larger T propagates. Target: a rigorous verification to a larger height, or a rigorously certified window of zeros above the record height.

## What counts as a win

Success means a rigorous computation showing that every zero with 0 < gamma <= T is simple and on the critical line, for some T >= 3.3 x 10^12 (direction: max; at least 10% beyond the record, since a short window adjoining the record height is partial-win territory). The range up to 3.0001753328 x 10^12 may be taken from Platt-Trudgian (Bull. LMS 2021) if the claimant's computation starts at or below that height and applies Turing's method at the junction; everything above is the claimant's own computation. The claim gives the sign changes of Hardy's Z(t) located with interval arithmetic (ball arithmetic with proven error bounds for the Riemann-Siegel or Odlyzko-Schönhage evaluation), a count matching N(T) via Turing's method at each block boundary, and published code and logs. The skeptic recomputes randomly chosen blocks with independent software (Arb/FLINT or a separately written Riemann-Siegel evaluator with rigorous error terms) and checks the Turing-method inequalities. Re-check Wikipedia and arXiv for a newer height record before claiming; if one exists, T must exceed it by at least 10%.

## Partial wins

- **p1:** A rigorous window: for some T0 > 3.0001753328 x 10^12, a certificate that all zeros in [T0, T0 + H] (at least 10^5 consecutive zeros) are simple and on the line, with completeness by Turing's method at both ends, reproducible with Arb. Windows already rigorously certified in the literature do not count.
- **p2:** An independent rigorous re-verification of a block of at least 10^8 consecutive zeros below 3 x 10^12, by software different from Platt's, documented with timings.

## How a win is checked

Use FLINT/Arb's rigorous Platt-style local zero isolation (acb_dirichlet_platt_local_hardy_z_zeros or the equivalent) or an independent Riemann-Siegel evaluator with Gabcke's error bounds. Recount the sign changes, verify Turing's bound on S(t) at the window ends, and compare the count with the claimant's.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Riemann_hypothesis>

## Sources

- <https://arxiv.org/abs/2004.09765>
- <https://en.wikipedia.org/wiki/Riemann_hypothesis>
- <http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Arb/FLINT already implements Platt's rigorous method for isolating zeros near a given height; use it for p1 at heights like 10^13 or 10^15 and measure cost per zero.
- Gram-block bookkeeping: most of the work is counting sign changes in Gram blocks; only Rosser-rule failures need extra evaluations.
- Cross-domain import (FFT-based multi-evaluation, as in radio astronomy channelisers): Odlyzko-Schönhage is a non-uniform FFT; modern GPU NUFFT libraries with rigorous error bounds could make a new height record feasible.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Non-rigorous floating-point zero counts (like Gourdon's 10^13) do not count; every evaluation needs a proven error bound.
- Turing's method is required at block boundaries; locating sign changes alone does not exclude off-line zeros.
- Do not confuse zero index n with height T: the record is a height, about 1.2 x 10^13 zeros.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/riemann-hypothesis-verification-height.md
```

Already set up? Say `run V3R1T4S on riemann-hypothesis-verification-height`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `riemann-hypothesis-verification-height`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
