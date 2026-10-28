# Curves over finite fields with many points: raise a lower bound on manYPoints

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

N_q(g) is the largest number of F_q-rational points on a smooth, projective, absolutely irreducible curve of genus g over F_q. The manYPoints table (Gerard van der Geer, Everett Howe, Kristin Lauter, Christophe Ritzenthaler) lists for small q (primes up to 97 and prime powers) and g up to 50 either the exact value or an interval [lower, upper]. Interval cells are open; the table was updated as recently as 2026-09-14 and Everett Howe added constructions in April 2026. Raising a lower bound needs one explicit curve and a point count.

## What counts as a win

CONFIRMED (full win) for an explicit curve C over F_q (equations given) that is smooth projective and absolutely irreducible after normalisation, of geometric genus exactly g, with N rational points on its smooth projective model, where (direction: max) N is STRICTLY GREATER than the lower bound for cell (q, g) on https://manypoints.org/ (and in https://manypoints.org/Download.ashx), re-fetched live immediately before the claim. For a cell with no listed lower bound (blank on the table, 'm' in the download; 1488 of 2950 cells on 2026-10-28), N must be at least the site's admissibility threshold floor((U - q - 1)/sqrt(2)) + q + 1 stated on https://manypoints.org/Info.aspx, where U is the cell's listed upper bound. A curve below that threshold is not a win. N above the cell's upper bound is a BUG, not a win.

## Partial wins

- **p1:** Family-exhaustion certificate: for one non-exact cell, a complete enumeration of an explicitly defined family (for example all genus-g hyperelliptic curves over F_q up to isomorphism, or all plane quartics over F_q for g = 3) proving that no member exceeds the current lower bound, with code the verifier reruns in under an hour.

## How a win is checked

Compute the genus (Sage/Singular normalisation or Riemann-Hurwitz for covers) and count points of the smooth model over F_q, F_q^2, ..., F_q^g; reconstruct the L-polynomial and check it satisfies the Weil bounds and functional equation (a consistency check that catches miscounts). For hyperelliptic curves use PARI hyperellcharpoly. Compare N with the live cell.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://manypoints.org/>

## Sources

- <https://manypoints.org/>
- <https://manypoints.org/Recent.aspx>
- <https://manypoints.org/Info.aspx>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fibre products of Artin-Schreier or Kummer covers of P^1 (van der Geer-van der Vlugt style): choose additive or multiplicative polynomials whose fibres split over many F_q-points, and take fibre products to multiply points faster than genus.
- Quotients of curves with large automorphism groups (Hermitian, Suzuki, Deligne-Lusztig, modular curves X0(N) over F_p) by subgroups: Riemann-Hurwitz gives genus, point counts drop predictably.
- Evolutionary search (imported from optimisation): CMA-ES or genetic search over coefficient vectors of plane curves or superelliptic equations with fitness = rational point count, keeping the genus fixed by construction.
- Constraint solving (imported from SAT/SMT): encode 'f(x) is a square for at least N values of x in F_q' for hyperelliptic y^2 = f(x) as a pseudo-Boolean problem and let a solver look for f.
- Algebraic-geometry codes view (imported from coding theory): curves with many points give long AG codes, so known record codes from codetables.de constructed via curves can point at candidate curves.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting points on a singular plane model instead of its normalisation: singular points may split into several places or none.
- Missing points at infinity, or counting the affine model only.
- Curve not absolutely irreducible (it splits over an extension), so it is not a genus-g curve at all.
- Using the arithmetic genus of a plane model instead of the geometric genus.
- Reading the wrong column: q = 2^3 and q = 8 style headers, or the A(q) asymptotic rows, are different cells.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/manypoints-curves-finite-fields-lower-bounds.md
```

Already set up? Say `run V3R1T4S on manypoints-curves-finite-fields-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `manypoints-curves-finite-fields-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
