# Brun's constant (C_81): an unconditional upper bound below Platt-Trudgian's 2.288513

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: pure thought (explicit sieve estimates), plus laptop-hours of certified numerics · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 81: Brun's constant B is the sum of the reciprocals of the twin primes. Unconditional bounds on the live page: 1.840503 < B < 2.288513 (Dave Platt and Tim Trudgian, arXiv 1803.01925, 'Improved bounds on Brun's constant'; their abstract calls this about a 13% improvement on the previous best published result, the upper side moving from the Crandall-Pomerance bound 2.347). Lower bounds are partial sums from twin-prime enumeration; Thomas Nicely's enumerations gave 1.8318... (the much-quoted B ~ 1.902 is an extrapolation, not a bound). Under GRH, Dominic Klyve's unpublished thesis bound of 2.1754 was superseded by Lachlan Dunn (Bull. Aust. Math. Soc. 113 (2025), arXiv 2504.15658): B < 2.1594. The README carries the unconditional 2.288513. An unconditional upper bound needs an explicit sieve upper bound for twin primes up to x, with fully explicit constants, combined with computed twin-prime counts up to a large height. Both ingredients have improved since 2018 (explicit Brun-Titchmarsh and Selberg-sieve constants, larger verified twin-prime counts), but the bound has not been updated.

## What counts as a win

Main win: an unconditional upper bound B < U with U STRICTLY LESS (direction: min) than the smallest unconditional upper bound on https://teorth.github.io/optimizationproblems/constants/81a.html and in any open pull request touching constants/81a.md (currently 2.288513), both re-fetched immediately before claiming. It needs a complete written proof citing each explicit input by its exact published statement (refereed sieve inequalities, published twin-prime counts or a supplied re-verifiable enumeration), and a supplied interval-arithmetic program that evaluates every numerical step (integrals, sums, optimisation of the sieve parameter) with outward rounding. Conditional results (GRH) do not count for the main win.

## Partial wins

- **p1:** Under GRH, a bound B < U' with U' strictly below Dunn's 2.1594, at the same proof and certification standard.
- **p2:** An interval-arithmetic replay that reproduces Platt-Trudgian's 2.288513 from their published inputs and parameters, as a rerunnable bundle, or locates an error in their numerics.

## How a win is checked

Skeptic: check each cited explicit inequality against its source (statement, range of validity, constants). Rerun the interval program at two precisions. Spot-check any twin-prime counts used against published tables and, for heights up to 1e12, by an independent segmented-sieve count. Expected: hours to read, minutes to rerun.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/81a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/81a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/81a.md>
- <https://arxiv.org/abs/1803.01925>
- <https://arxiv.org/abs/2504.15658>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Replace the Brun-type sieve in the Crandall-Pomerance and Platt-Trudgian argument with the explicit Selberg-sieve upper bound for twin primes (Riesel-Vaughan style constants), optimised in the switching height.
- Use the largest published twin-prime counts (pi_2(x) to 1e18 or beyond, from Oliveira e Silva's computations) for the head of the sum, so the sieve only bounds a shorter tail.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Mixing conditional (GRH) and unconditional bounds: 2.1594 is conditional and does not count as the unconditional record.
- The 1.902 'value' of B is an extrapolation; using it anywhere in a proof invalidates the proof.
- Nicely's original twin-prime pages return 404 (the trnicely.net domain was taken over by an unrelated site); cite archived or published counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/brun-constant-unconditional-upper-bound.md
```

Already set up? Say `run V3R1T4S on brun-constant-unconditional-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brun-constant-unconditional-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
