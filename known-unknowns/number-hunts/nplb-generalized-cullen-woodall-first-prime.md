# Generalized Cullen and Woodall primes: first prime for a base with none known

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Generalized Cullen numbers are n*b^n+1 and generalized Woodall numbers are n*b^n-1. Gary Barnes's tables (No Prime Left Behind, started 2025-08-09; the bases <= 1000 Cullen page was last updated 2026-10-25, the bases <= 1000 Woodall page 2026-05-11) list, for every base b up to and beyond 10000, the n giving primes and the contiguous test limit; Gunter Loh's older status page and Norman Luhn's pzktupel tables are the history. In the bases 9001-10000 page (unchanged since 2025-08-09), every base is tested only to n = 10K and 365 of the 1000 bases had no known Cullen prime on 2026-10-28; the bases <= 1000 Cullen page has 258 bases with no known prime (205 of them tested only to 10K) and the Woodall page 64. Candidates near n = 10K, b ~ 9000 have about 40 000 digits; Cullen primes are provable by an N-1 test because N-1 = n*b^n is fully factored.

## What counts as a win

CONFIRMED (full win) for a base b marked as having no known primes (zero primes listed) on the live NPLB Generalized Cullen or Woodall page for its range (index at http://www.noprimeleftbehind.net/Generalized-Cullen-primes-1000.htm), re-fetched immediately before the claim, and an n STRICTLY GREATER than that base's listed test limit such that n*b^n+1 (Cullen) or n*b^n-1 (Woodall) is PROVEN prime (N-1 or N+1 proof). Each such base leaving the no-prime list counts (direction: min on the count of bases with no known prime).

## Partial wins

- **p1:** New prime for a base that already has primes: proven prime n*b^n+-1 with n greater than the listed contiguous test limit and not listed (including not inside a '(...)' missing-range note) at verification time.
- **p2:** Test-limit extension certificate: one unreserved base tested with no prime from the listed limit to at least twice that limit, with sieve file and residues saved for a 2% random retest by the verifier.

## How a win is checked

Check the base row on the live page (zero primes, limit). Recompute N exactly. Cullen: N-1 = n*b^n, factor n and b, run a Pocklington/Proth-style proof (PFGW -tp/-tm, PRST, or PARI isprime(N,1) where feasible). Woodall: N+1 = n*b^n, N+1 proof with PFGW -tp or LLR/PRST. Confirm no trivial factor from parity (b odd and n odd makes n*b^n+1 even) or from b being a perfect power that maps to a different listed form.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.noprimeleftbehind.net/Generalized-Cullen-primes-1000.htm>

## Sources

- <http://www.noprimeleftbehind.net/Generalized-Cullen-primes-1000.htm>
- <http://www.noprimeleftbehind.net/Generalized-Cullen-primes-9001-10000.htm>
- <http://www.noprimeleftbehind.net/Generalized-Woodall-primes-1000.htm>
- <http://guenter.loeh.name/gc/status.html>
- <https://pzktupel.de/Primetables/TableCullenGen.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sieve all no-prime bases of one page together (gcwsieve / MultiSieve handle many bases at once) from n = 10K to 20K, then PRP in increasing n so the first hit per base ends work on that base.
- Scheduling theory (imported from operations research): candidate test time grows like (n log b)^2 log(n log b); order the queue by expected primes per second (sieve survivors times 1/ln N) rather than by base number.
- Heuristic prime-count models (Wagstaff-style, imported from probabilistic modelling): estimate each base's expected number of primes in a range from its sieve density and spend effort where the posterior chance of a first prime is highest.
- Covering-set analysis: for a stubborn base, look for a finite covering set or algebraic factorisation that makes every n*b^n+1 composite on some residue class; proving such a class is barren is a different but checkable result.
- Error-checked big-integer arithmetic (Gerbicz checks in PRST) so a single bit flip never produces a false prime at 40 000 digits.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- PRP is not proof; Cullen needs an N-1 proof and Woodall an N+1 proof.
- Odd b with odd n gives an even Cullen number: trivial compositeness; similar parity traps for Woodall.
- Exponents already shown in the '(...)' missing-range notation or above the contiguous limit may already be known.
- Bases that are perfect powers can be the same numbers as another base's form; check the page notes.
- Reserved bases (yellow or green) are being worked by others; claims there may duplicate unreported work.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/nplb-generalized-cullen-woodall-first-prime.md
```

Already set up? Say `run V3R1T4S on nplb-generalized-cullen-woodall-first-prime`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nplb-generalized-cullen-woodall-first-prime`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
