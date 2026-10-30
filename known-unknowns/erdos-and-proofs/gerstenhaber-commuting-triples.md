# MOONSHOT - Gerstenhaber problem: three commuting d x d matrices generating an algebra of dimension > d (or reducibility of C(3,d) for some 11 <= d <= 28)

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours (checking a candidate is exact linear algebra on d^2-dimensional vectors; the search space is the hard part) · open as of 2026-10-30

## The problem

Gerstenhaber (Annals of Math. 1961) proved that two commuting d x d matrices over a field generate a unital algebra of dimension at most d. Whether the same holds for three pairwise commuting matrices has been open for over 60 years (the Gerstenhaber problem). It fails for four or more: E13, E14, E23, E24 in M_4 generate a 5-dimensional algebra. Known positive cases, as summarised by R. Cherny, M. Satriano and Y. Song (arXiv:2402.16334, 2024): the variety C(3,d) of commuting triples is irreducible for d <= 10 (K. Sivic 2012), so the bound holds there. The bound also holds when one matrix has nullity at most 3 (Guralnick-Sethuraman, Sivic), when one matrix squares to zero (Holbrook-Omladic 2001), for one-generated modules, and for several combinatorial gluing classes (Rajchgot-Satriano; Cherny-Satriano-Song). C(3,d) is reducible for d >= 29 (Holbrook-Omladic 2001; Ngo-Sivic 2014), so the generic-point argument breaks there, but no counterexample is known. Holbrook and O'Meara (arXiv:2006.08588) published a computing strategy aimed at finding one. The formal-conjectures file Other/GerstenhaberThreeMatrices.lean tags the triple case research open (last changed 2026-10-14).

## What counts as a win

Success means three explicit d x d matrices A, B, C with entries in Q or in a stated prime field F_p, such that AB = BA, AC = CA and BC = CB hold exactly, and the unital algebra K[A,B,C] they generate has dimension STRICTLY GREATER (direction: max) than d. The dimension is computed by two independent exact programs as the rank of the span of all monomials A^i B^j C^k, iterating the degree until the span stops growing. The problem must still be open, i.e. the formal-conjectures file is still tagged research open and no newer paper settles it, re-checked before claiming.

## Partial wins

- **p1:** A certificate that C(3,d) is reducible for some d with 11 <= d <= 28: an explicit polynomial parametrisation (over Q) of a family of pairwise commuting triples, verified to commute identically by symbolic expansion, whose Jacobian matrix has exact rank greater than d^2 + 2d (the dimension of the component of simultaneously diagonalisable triples) at a stated rational point. The claim must also show, by a check of the literature cited in arXiv:2402.16334 and newer papers, that reducibility at that d was not already published.

## How a win is checked

Load the matrices exactly (Fractions or integers mod p) and check the three commutators are zero. Vectorise I and every monomial of degree <= t, compute the rank exactly (fraction-free elimination over Q, or Gaussian elimination mod p), and increase t until the rank stabilises; a second independent implementation, for example sympy against a hand-written modular rank, must agree. For p1, expand the commutators of the parametrised family symbolically to confirm they vanish identically, then compute the exact rank of the Jacobian at the stated point.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Other/GerstenhaberThreeMatrices.lean>

## Sources

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Other/GerstenhaberThreeMatrices.lean>
- <https://arxiv.org/abs/2402.16334>
- <https://arxiv.org/abs/2006.08588>
- <https://doi.org/10.2307/1970336>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search only where the known theorems leave room: d >= 11, all three matrices nilpotent (reduction to the local case), each of nullity >= 4, none squaring to zero, and modules needing at least two generators.
- Use the combinatorial model of Cherny-Satriano-Song and Rajchgot-Satriano: glue monomial quotients S/I and S/J along an isomorphism of submodules and compute the dimension of the resulting algebra combinatorially. Enumerate gluing data far beyond the classes they settle.
- Use the dimension count as a guide: components of C(3,d) other than the main one (known to exist for d >= 29) are where a counterexample could live. Constructions of extra components (Holbrook-Omladic, Ngo-Sivic) give explicit families to test at their generic points.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For d <= 10 the bound is a theorem (irreducibility of C(3,d)), so do not search there.
- The dimension is that of the unital algebra (include I), computed over the field of the entries. Mixing fields or floating-point ranks gives false counts.
- Generic (diagonalisable) triples always satisfy the bound. Random rational triples will never be counterexamples, so the search must be structured.
- Four commuting matrices are known to violate the bound and do not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/gerstenhaber-commuting-triples.md
```

Already set up? Say `run V3R1T4S on gerstenhaber-commuting-triples`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gerstenhaber-commuting-triples`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
