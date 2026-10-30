# MOONSHOT - Ore's harmonic numbers: an odd one (Ore's conjecture), or a counterexample to the practical, Mersenne-factor or completeness conjectures recorded in OEIS A001599

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (structured search over smooth numbers; the odd case is a moonshot) · open as of 2026-10-30

## The problem

n is harmonic (an Ore number) when the harmonic mean of its divisors, n*tau(n)/sigma(n), is an integer (OEIS A001599, last edited 30 May 2026). Ore (1948) showed every perfect number is harmonic and conjectured that 1 is the only odd harmonic number, which would rule out odd perfect numbers. Graeme L. Cohen and Ronald M. Sorli ('Odd harmonic numbers exceed 10^24', Math. Comp. 2010) gave the current lower bound for an odd one. Takeshi Goto listed all 937 harmonic numbers below 10^14 (b-file by Robert G. Wilson v; Goto's own page was unreachable on 2026-10-30), and Ivan Borysiuk's file a001599_1.txt gives 10000 numbers 'conjectured to be the 10000 smallest Ore numbers', the largest 64555935231675888000. OEIS comments record conjectures that a single number would refute: every harmonic number is practical (Jaycob Coleman, 2013, checked below 10^14) and every harmonic number > 1 has a Mersenne prime factor (Ivan Borysiuk, 2024). Our own check on 2026-10-30 found all 10000 numbers in Borysiuk's file harmonic and practical, and every entry above 1 even and divisible by a Mersenne prime.

## What counts as a win

CONFIRMED (full win): an odd integer n > 1, given with its complete proven factorisation, such that n*tau(n) is divisible by sigma(n), refuting Ore's conjecture (by Cohen-Sorli it must exceed 10^24).

## Partial wins

- **p1:** A harmonic number that is not practical (it fails Stewart's criterion: with primes p_1 < p_2 < ... of n, p_1 = 2 and each p_(i+1) <= 1 + sigma(p_1^e_1 ... p_i^e_i)), refuting Coleman's conjecture.
- **p2:** A harmonic number n > 1 with no Mersenne prime (2^q - 1 prime) among its prime factors, refuting Borysiuk's conjecture.
- **p3:** Completeness gap: a harmonic number below 64555935231675888000 that is absent from Borysiuk's file https://oeis.org/A001599/a001599_1.txt and from the A001599 b-file at verification time.

## How a win is checked

Factor n (it is expected to be smooth) and prove the factors, compute tau(n) and sigma(n) exactly and check n*tau(n) % sigma(n) == 0; apply Stewart's criterion for practicality; test membership of Mersenne primes among the factors; diff n against the OEIS b-file and Borysiuk's file.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001599>

## Sources

- <https://oeis.org/A001599>
- <https://oeis.org/A001599/a001599_1.txt>
- <https://oeis.org/A001599/b001599.txt>
- <https://doi.org/10.1090/S0025-5718-10-02337-9>
- <https://doi.org/10.1090/S0025-5718-03-01554-0>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Goto-Shibata enumeration by harmonic mean H = n*tau(n)/sigma(n): fix H and build n prime power by prime power so that the partial ratio stays consistent, extending their H <= 300 completeness to larger H.
- Harmonic seeds (Cohen-Sorli): many harmonic numbers arise from small seeds by multiplying in prime powers whose tau and sigma cancel; search seed closures for members missing from Borysiuk's list or lacking 3, 7, 31 and 127.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Harmonic here means the harmonic mean of divisors, not the partial sums H_n of the harmonic series.
- 1 is harmonic and odd; the conjecture concerns n > 1.
- Borysiuk's list is only conjectured complete; a missing term must be checked against the b-file too.
- Floating-point ratios mislead for 20-digit n: use exact integers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/ore-harmonic-number-conjectures.md
```

Already set up? Say `run V3R1T4S on ore-harmonic-number-conjectures`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ore-harmonic-number-conjectures`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
