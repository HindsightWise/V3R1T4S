# Erdos #1055 (Erdos-Selfridge prime classes): determine a(20) of OEIS A005113, or find a class-20 prime below 764276710625653

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (recursive enumeration of high-class primes up to about 8e14 by p+1 = m*q with q of the previous class) · open as of 2026-10-30

## The problem

Erdos-Selfridge classification (Guy A18; Erdos #1055). A prime p is in class 1 if p+1 has no prime factor other than 2 and 3. Otherwise p's class is one more than the largest class of the prime factors of p+1 (the OEIS A005113 convention). Erdos asks how p_r^(1/r) behaves, where p_r is the least prime of class r. OEIS A005113 lists p_1..p_19 = 2, 13, 37, 73, 1021, ..., 3666349256113, 65994286610033. a(17)-a(19) are from Jud McCranie (May 2026). M. F. Hasler (2007) gave a(20) <= 764276710625653, and Alper Ferudun confirmed in the OEIS discussion (18 Oct 2026) that this number is a prime of class 20. A b-file for n = 1..396 by Sascha Fürstenberg (Oct 2026) was found to list non-minimal values, e.g. a(20) = 1055908585760527. The data line was cut back to a(19), so a(20) is open. Lower bound: a(20) >= 2*a(19) - 1.

## What counts as a win

CONFIRMED by either (A) an explicit prime p < 764276710625653 of class 20, with a recursive certificate: the full factorisation of p+1 and of q+1 for every prime q in the chain, with primality proofs, so an independent checker recomputes the class; or (B) the exact value of a(20), proved minimal by an exhaustive enumeration that two independently written programs reproduce. They must agree on the full list of class-19 primes below a(20)/2 used in the search.

## Partial wins

- **p1:** An explicit prime of class 21 smaller than 2111817171521053 (the non-minimal a(21) value in the withdrawn Oct 2026 b-file), with a recursive class certificate.
- **p2:** An explicit prime of class 22 smaller than 105590858576052649 (the withdrawn b-file value), with a recursive class certificate.

## How a win is checked

Recompute the class recursively from the supplied factorisations, checking every factorisation by multiplication and every prime with a deterministic test (BPSW plus an ECPP or Pocklington certificate for numbers above 2^64). For (B), rerun both enumerations and diff the class-19 prime lists and the final minimum.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005113>

## Sources

- <https://www.erdosproblems.com/1055>
- <https://oeis.org/A005113>
- <https://oeis.org/history?seq=A005113>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Any class-20 prime p < 7.65e14 has p+1 = m*q with q of class 19, q >= a(19) = 65994286610033 and m even, so m <= 11. Enumerate the class-19 primes below 3.83e14 recursively from class-18 primes below 1.92e14, and so on, rather than classifying all primes.
- Hasler's PARI 'someofnextclass' routine in the OEIS entry is a useful starting point, but rewrite it so minimality is exhaustive.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The OEIS b-file b005113.txt (n = 1..396) contains non-minimal values. Use the data line and the history page, not the b-file.
- The class of a prime depends on the classes of all prime factors of p+1, not only the largest.
- The site and OEIS phrase the class-1 convention slightly differently; use the OEIS convention stated above and say so.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1055-erdos-selfridge-class-a20.md
```

Already set up? Say `run V3R1T4S on erdos-1055-erdos-selfridge-class-a20`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1055-erdos-selfridge-class-a20`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
