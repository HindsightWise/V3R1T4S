# Skewes numbers for prime k-tuples: A210439(10), A332493(9), or the sexy-prime (p, p+6) Skewes number

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for the sexy-prime search (primesieve-style counting with a running Hardy-Littlewood comparison); laptop-minutes to test A210439(10) against Luhn's public 10-tuplet lists up to 10^20 (a win only if a crossing occurs there); needs cluster for 9-tuplets beyond 2^64 and 10-tuplets beyond 10^20 · open as of 2026-10-30

## The problem

Tóth (CMST 2019, arXiv:1910.02636) defined the Skewes number of an admissible prime k-tuple pattern P as the first prime p at which the count pi_P(p) exceeds the Hardy-Littlewood prediction C_P Li_P(p), with Li_P(x) = int_2^x dt/(log t)^k. Known values: twins 1369391 (Marek Wolf 2011), cousins 5206837, triplets, quadruplets, quintuplets and the 6-tuplet 251331775687 (Tóth 2019), 7-tuplets 7572964186421 and 214159878489239 (Hugo Pfoertner 2020), the three 8-tuplet patterns (Pfoertner and Norman Luhn 2021, up to 750247439134737983). OEIS A210439 (minimal Skewes number over the n-tuplet patterns) got a(9) = 3658988336628289781 from Karl Desfontaines and Hugo Pfoertner on 2026-06-03, using Desfontaines' enumeration of all four 9-tuplet patterns up to 2^64; a(10) is open. A332493 (the latest first sign change among the n-tuplet types) stops at a(8) = 750247439134737983 (2021), so a(9) is open. Wikipedia's Skewes number page (edited 2026-10-28) states that the Skewes number for sexy primes (p, p+6), if it exists, is still unknown. A check for this entry found pi_6(x) < C Li_2(x) at every sexy pair up to 10^10 (deficit about 4,500 there and growing), with C = 4 C_2 = 2.6406. Hardy-Littlewood constants for every pattern are tabulated by Tony Forbes and Norman Luhn. Luhn's public database of the smallest prime k-tuplets (updated 2026-09-27) lists the four 9-tuplet patterns only up to 10^18, below A210439(9), so Desfontaines' 2^64 run is not in it. It lists both 10-tuplet patterns up to 10^20 (about 5.12 million of each). Target: a new Skewes number in any of these three cells.

## What counts as a win

Success means a prime p and a pattern P such that (1) p starts an instance of P; (2) an exhaustive enumeration of all instances of P up to p (code and counts given) shows pi_P(q) <= C_P Li_P(q) at every instance q < p and pi_P(p) > C_P Li_P(p), with Li_P evaluated by rigorous quadrature (mpmath or Arb) and C_P computed to at least 15 digits; and (3) the value fills a cell absent on the day of claiming: A210439(10), A332493(9), or the (p, p+6) Skewes number, re-checked on OEIS (A210439, A332493) and on Wikipedia/OEIS for the sexy case. The skeptic recounts the instances with an independent sieve: all of them for the sexy case. For 9- and 10-tuplets the recount is cross-checked against Luhn's smallest k-tuplet database where it reaches (9-tuplets to 10^18, 10-tuplets to 10^20), plus random-window recounts beyond it. The skeptic also re-evaluates the comparison near p. A full win for A332493(9) also requires the first crossings of all four 9-tuplet types.

## Partial wins

- **p1:** A certified lower bound: an exhaustive verification that no sexy-prime Skewes number exists below 10^14 (pi_6(x) <= C Li_2(x) at every sexy pair up to 10^14), with counts at each power of 10 checked by an independent run.
- **p2:** The first crossing for one of the 9-tuplet types other than p + [0, 2, 6, 8, 12, 18, 20, 26, 30] (the one giving A210439(9)), not recorded in OEIS A210439 or A332493 on the day of claiming, with full enumeration up to it, independently re-verified (a step toward A332493(9)).

## How a win is checked

Recount with a separately written segmented sieve (primesieve for pairs; a wheel sieve over admissible residues mod 2*3*5*7*11*13*17*19*23 for 9- and 10-tuplets). Compute C_P with an independent Euler-product evaluation, and Li_P with mpmath.quad. Compare the running count against the prediction at each instance near the claimed crossing.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A210439>

## Sources

- <https://oeis.org/A210439>
- <https://oeis.org/A332493>
- <https://arxiv.org/abs/1910.02636>
- <https://en.wikipedia.org/wiki/Skewes%27s_number>
- <https://pzktupel.de/ktpatt_hl.php>
- <https://pzktupel.de/smarchive.php>
- <https://arxiv.org/abs/1107.2809>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sexy pairs: run primesieve's segmented counting and track D(x) = pi_6(x) - C Li_2(x) at every pair; D drifts like -sqrt(x)/log x with fluctuations, so watch for upward excursions. If none occurs by 10^15 or so, report p1.
- For 9- and 10-tuplets, the minimal-span patterns are few (four 9-tuplet types of span 30, two 10-tuplet types of span 32); one wheel sieve over the union of admissible residue classes serves all of them at once.
- Use Kourbatov's PARI code (linked from A210439) as an independent reference for the Li_n integral and constants.
- Cross-domain import (sequential change detection): D(x) is a slowly drifting random-walk-like process; bound how far ahead a crossing can be from the current value and the local variance, to schedule compute.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Li_P integrates from 2, not 0 or the first instance; the constant C_P must include the correct local factors for each pattern (sexy pairs: 2 C_2 times 2 for the prime 3).
- The Skewes number is the FIRST crossing; a crossing found in a window without a complete count from 2 is not a Skewes number.
- Patterns versus consecutive-prime tuples: A333586/A333587 use consecutive primes of minimal span. For pairs (p, p+6) Tóth's definition does not require consecutiveness; state which definition is used.
- Floating-point Li_P near 10^20 loses digits; use mpmath with at least 30 digits.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/prime-ktuple-skewes-numbers-next.md
```

Already set up? Say `run V3R1T4S on prime-ktuple-skewes-numbers-next`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `prime-ktuple-skewes-numbers-next`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
