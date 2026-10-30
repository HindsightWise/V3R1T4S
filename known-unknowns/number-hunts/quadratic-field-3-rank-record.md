# Class groups of quadratic fields with record 3-rank: an imaginary quadratic field of 3-rank 9 (record 8, Elkies), or a real one of 3-rank 8

🔢 **Number hunts** · standard · tractability ★☆☆☆☆ · compute: laptop-days (Mestre-Nagao or Diaz y Diaz style searches; certificate checking takes seconds) · open as of 2026-10-30

## The problem

Large 3-ranks of class groups of quadratic fields are very rare: under Cohen-Lenstra the chance that an imaginary quadratic field has 3-rank r decays like 3^(-r^2), about 3^-64 for r = 8. Quer (1987) found three imaginary quadratic fields of 3-rank 6 from Mordell curves of rank 12, and Bagshaw, Jacobson, Rollick and Scheidler (CMS Winter Meeting 2021) still cite that as the record for fields found by the Diaz y Diaz construction. Noam Elkies (ANTS XVI, 2024, 'Rank of an elliptic curve and 3-rank of a quadratic field via the Burgess bounds') proved unconditionally that Q(sqrt(-3D)), with D = 72513834653847828539450325493 = 41 * 1768630113508483622913422573, has class group of 3-rank 8, 'the current record for the class group of a quadratic number field'. The mirror real field Q(sqrt D) has 3-rank 7, which is unconditional as a lower bound and exact under GRH. Both come from the Mordell curve y^2 = x^3 + 16D of rank 16. Elkies also reports the record rank 17 for Mordell curves y^2 = x^3 + k, with k = -908800736629952526116772283648363 (announced 2016, exhibited on MathOverflow in 2023), whose fields again have 3-ranks 8 and 7 under GRH.

## What counts as a win

CONFIRMED (full win) for a fundamental discriminant Delta < 0, proven fundamental by factorisation, together with nine primitive positive-definite binary quadratic forms f_1..f_9 of discriminant Delta. Each f_i^3 must reduce to the principal form, and every product f_1^e_1 ... f_9^e_9 with e in {0,1,2}^9 \ {0} (19,682 products) must reduce to a non-principal reduced form. This proves 3-rank >= 9 > 8 (direction: max). The verifier composes and reduces the forms with independent code (exact integer arithmetic; PARI qfbcomp/qfbred as a cross-check). The field must not appear with 3-rank >= 9 in the literature at verification time.

## Partial wins

- **p1:** A real quadratic field Q(sqrt D), D > 0 fundamental, with 3-rank of the class group >= 8 (record 7). Certificate: (3^8 - 1)/2 = 3280 cubic polynomials whose fields all have discriminant exactly D (by Hasse, these are the unramified cyclic cubic extensions), proven pairwise non-isomorphic by Frobenius cycle types at small primes or nfisisom, and each field's discriminant proven equal to D (nfdisc with complete factorisation).
- **p2:** A Mordell curve y^2 = x^3 + k over Q with 18 or more points whose Neron-Tate height matrix has positive determinant (computed at 100 and at 200 digits, agreeing), beating Elkies' rank 17.

## How a win is checked

Full win: check that Delta is fundamental, check the discriminant of every form, cube each form and reduce, then enumerate all 3^9 - 1 exponent vectors with independent composition code. p1: nfdisc on each cubic, pairwise isomorphism tests, and confirmation that the count 3280 is reached. p2: PARI ellinit, ellisoncurve and ellheightmatrix at two precisions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://antsmath.org/ANTSXVI/papers/Elkies.pdf>

## Sources

- <https://antsmath.org/ANTSXVI/papers/Elkies.pdf>
- <https://mathoverflow.net/questions/442468/mordell-curves-with-large-rank>
- <https://www2.cms.math.ca/Events/winter21/res/pdf/ant-rs.pdf>
- <https://arxiv.org/abs/1910.12276>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Follow Elkies: rank(E_k) is at most 1 plus the 3-ranks of Q(sqrt k) and Q(sqrt(-3k)), so Mordell curves of rank >= 18 force large 3-ranks. Search with Mestre-Nagao sieves over k.
- Diaz y Diaz / Quer / Bagshaw-Jacobson-Rollick-Scheidler: build discriminants as norms from cubic fields with many small cubic units, then sieve by 3-rank heuristics.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The forms must be primitive and of the exact discriminant Delta; a non-fundamental Delta describes an order, not the field.
- Rank 17 for Mordell curves is a lower bound from explicit points; only explicit independent points count for p2, never analytic rank.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/quadratic-field-3-rank-record.md
```

Already set up? Say `run V3R1T4S on quadratic-field-3-rank-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quadratic-field-3-rank-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
