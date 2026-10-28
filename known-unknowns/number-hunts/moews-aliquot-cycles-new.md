# Sociable numbers: find an aliquot cycle not on Moews' list

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

An aliquot cycle of length L >= 3 (sociable numbers) is a cycle of the map s(n) = sigma(n) - n. David Moews' list (updated 11-IX-2026) has 5446 cycles: 5433 of length 4, one of length 5, five of length 6, five of length 8, one of length 9 and one of length 28. Exhaustive searches: all cycles whose number before the largest member is below 10^14 (Dmitry Bodyagin, 2016), and all cycles with odd smallest member up to 10^16 (a mersenneforum.org group using Bodyagin's program, 2016). Most of the 4-cycles are of Borho's form (cycles 121-5446 among them); the list credits the bulk of these to Robert Gerbicz, with many by Karsten Blankenagel and Wieland Borho, Andreas vom Stein, Ren Yuanhua and others, so new large 4-cycles keep appearing.

## What counts as a win

CONFIRMED (full win) for a list of L >= 3 distinct positive integers n_1..n_L, each with a complete factorisation into proven primes, such that s(n_i) = n_{i+1} and s(n_L) = n_1 exactly, and such that no member appears anywhere in https://djm.cc/sociable.txt re-fetched immediately before the claim (direction: max on the count of known cycles).

## Partial wins

- **p1:** A new cycle of length other than 4 (5, 6, 8, 9, 28 or any new length), absent from the list; report as the headline result.
- **p2:** A new cycle whose smallest member is below 10^20, which would expose a gap in the region the list is closest to complete; label it separately and double-check against the exhaustive-search statements in the list header.

## How a win is checked

Multiply out each factorisation, prove every prime factor (BPSW below 2^64, PARI isprime or ECPP above), compute sigma exactly from the factorisation, check the cycle closes, check all members distinct and not perfect/amicable, and grep every member against the live list.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://djm.cc/sociable.txt>

## Sources

- <https://djm.cc/sociable.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Borho's rule for 4-cycles (the analogue of Euler's rule for amicable pairs): fix a common part a and solve for the prime structure of the other part; Gerbicz's large harvest came from systematically running such rules.
- Cycle detection on functional graphs (imported from algorithm design): run Brent's cycle finder on s(n) from structured seeds (products of a known-cycle common part with new primes) rather than from random n.
- Constraint solving (imported from SMT): encode the prime-exponent pattern of each member and the sigma equations modulo many small primes as constraints; let a solver propose patterns, then confirm with exact arithmetic.
- Meet-in-the-middle (imported from cryptanalysis): split each member into a fixed smooth part and an unknown part; tabulate sigma-ratios of candidate unknown parts and look for matches across the four members.
- Mine the 'breeders' and near-misses of amicable searches (Chernykh's database) as seeds for 4-cycles.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Amicable pairs (length 2) and perfect numbers (length 1) do not count.
- A rotation of a known cycle is the same cycle; check every member, not just the smallest.
- Incomplete factorisation gives a wrong sigma; every factor must be proven prime.
- Floating-point or truncated arithmetic in sigma for 30+ digit members.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/moews-aliquot-cycles-new.md
```

Already set up? Say `run V3R1T4S on moews-aliquot-cycles-new`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `moews-aliquot-cycles-new`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
