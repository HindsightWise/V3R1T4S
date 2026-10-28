# Multiply perfect numbers: find a new 9-, 10- or 11-perfect number

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

n is k-perfect when sigma(n) = k*n. Achim Flammenkamp's Multiply Perfect Numbers page (built on Richard Schroeppel's archive; page last updated 2026-02-20) lists 5932 known MPNs in its database snapshot of 2022-12-31 (its yearly table counts 5933 for 2024 and 2025, adding the 2024 perfect number credited on the page to 'Lurant&Woltman&Kurowski et al.'): 1136 8-perfect (estimated about 1140; the page answers 'probably yes' to whether all are discovered), 2164 9-perfect (estimated about 2200), 1710 10-perfect (estimated about 4500) and only 2 11-perfect (estimated about 10000; the first found 2001-03-13 by G. F. Woltman, the second 2022-09-07). George Woltman is credited with 2416 discoveries (1997-2013, 2021-2022). The claims file mpn_current.txt lists 0 claimed-but-unmerged numbers since 2023-01-12. Verification is cheap: given the factorisation of n, sigma(n) needs no further factoring.

## What counts as a win

CONFIRMED (full win) for a positive integer n given as a product of proven primes with exponents, such that sigma(n) = k*n exactly with k >= 10, and n absent from the database file mpn.gz and the claims file mpn_current.txt linked from https://wwwhomes.uni-bielefeld.de/achim/mpn.html (both re-fetched immediately before the claim) and from OEIS A007691 (multiply-perfect numbers) and its b-file.

## Partial wins

- **p1:** New 9-perfect number: sigma(n) = 9n exactly, n absent from mpn.gz and mpn_current.txt at verification time.
- **p2:** New 8-perfect number (the page calls the 8-perfect list 'probably' complete, so this would be surprising): same checks; double-check before claiming.

## How a win is checked

Prove each prime (BPSW + PARI isprime/ECPP). Compute sigma(n) = prod (p^(e+1)-1)/(p-1) exactly with Python big integers; check sigma(n) mod n == 0 and k = sigma(n)/n. Compute ln(ln(n)) to 7 decimals and the factorisation string and search both in mpn.gz and mpn_current.txt.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wwwhomes.uni-bielefeld.de/achim/mpn.html>

## Sources

- <https://wwwhomes.uni-bielefeld.de/achim/mpn.html>
- <https://wwwhomes.uni-bielefeld.de/achim/mpn.gz>
- <https://wwwhomes.uni-bielefeld.de/achim/mpn_current.txt>
- <https://oeis.org/A007691>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Systematic substitution: the page lists 'substitution pairs' (X, Y) with equal fractional abundancy; apply every pair to every known MPN containing X, and compose substitutions. Check which combinations are absent from the database.
- Term rewriting (imported from programming-language theory): treat substitutions as rewrite rules on factorisation strings and search the closure of the known set under the rules with deduplication by ln(ln(n)).
- Best-first search with an admissible heuristic (imported from AI planning, A*): state = partial factorisation with an unbalanced sigma; heuristic = how far the remaining abundancy is from the target; expand by adding the largest unresolved prime from sigma(p^e).
- Use Cunningham-table factorisations of p^e - 1 (Wagstaff's tables) as a free oracle so the search never stalls on factoring sigma(p^e).
- Times-k trick from the page: if n is k-perfect, k is prime and k does not divide n, then k*n is worth testing for (k+1)-perfection; scan the 10-perfect list for 11-perfect candidates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Duplicates written with a different factor order or exponent layout; dedupe by the full integer or ln(ln(n)).
- A factor that is only a probable prime makes the claim unproven.
- Numbers known on forums or in OEIS but not yet merged into Flammenkamp's file; check OEIS and the claims file too.
- Abundancy miscounted when sigma(n)/n is not an integer (a 'near' MPN).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/multiperfect-new-k-perfect.md
```

Already set up? Say `run V3R1T4S on multiperfect-new-k-perfect`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `multiperfect-new-k-perfect`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
