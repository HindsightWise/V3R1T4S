# MOONSHOT - A hyperoval in PG(2,128) not equivalent to any known hyperoval

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days for search; equivalence testing laptop-hours · open as of 2026-10-30

## The problem

A hyperoval in PG(2,q), q = 2^h, is a set of q+2 points with no three collinear. Up to equivalence, hyperovals correspond to o-polynomials. The known infinite families are: hyperconic, translation x^(2^i) with gcd(i,h) = 1, Segre x^6 (h odd), Glynn I and II (h odd), Payne (h odd), Cherowitzo (h odd), Subiaco (all h) and Adelaide (h even), plus the sporadic O'Keefe-Penttila hyperoval for q = 32. Classifications: q <= 16 (Hall; O'Keefe-Penttila), q = 32 by computer, six classes (Penttila-Royle, J. Geom. 1994), and q = 64, exactly four classes, all known (Vandendriessche, EJC 26(2) P2.35, 2019). q = 128 is the smallest open case: no classification exists, and finding a hyperoval outside the families listed above would be a major discovery. Credit for the families goes to Segre, Glynn, Payne, Cherowitzo, Cherowitzo-Penttila-Pinneri-Royle (Subiaco) and Cherowitzo-O'Keefe-Penttila (Adelaide).

## What counts as a win

Give 130 points of PG(2,128) as normalised 3-vectors over GF(128) = GF(2)[x]/(x^7+x+1), or as an o-polynomial f with the standard hyperoval {(1,t,f(t))} + {(0,1,0),(0,0,1)}. No three points may be collinear (checked exhaustively). The set must be PROJECTIVELY INEQUIVALENT under PGammaL(3,128) to every hyperoval in PG(2,128) from the known families (regular, translation, Segre, Glynn I, Glynn II, Payne, Cherowitzo, Subiaco). This is shown by an equivalence test the skeptic reruns, for example an invariant such as the stabiliser order that differs from every known class, plus a full frame-mapping test. It also must not appear in any later publication. Direction: settle, open on 2026-10-30.

## Partial wins

- **p1:** A rerunnable computer proof that every hyperoval of PG(2,128) admitting a nontrivial collineation of a stated prime order p, where p divides |PGammaL(3,128)| (so p is one of 2, 3, 7, 43, 127, 337), is equivalent to a known one. This partial classification must not already be published or implied by a published theorem (check Penttila-Royle, J. Geom. 54 (1995), and the literature on hyperovals with transitive or large stabilisers before claiming).

## How a win is checked

Check no-three-collinear over all C(130,3) triples, or via line counts: every line meets the set in 0 or 2 points. For inequivalence, compute the stabiliser in PGammaL(3,128): map every ordered 4-subset to the standard frame and test whether the image equals the set (frames x 7 Frobenius powers, with an early-abort hash). Compare the order and orbit structure with each known family's representative, and run the same frame test between the candidate and each representative.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i2p35>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i2p35>
- <https://en.wikipedia.org/wiki/Oval_(projective_plane)>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search o-polynomials of restricted shape (sums of a few monomials x^a with exponents in cyclotomic classes mod 127), which is how most families were found. The o-polynomial condition is checkable fast.
- Vandendriessche's method for q = 64 (point sets with 0 or 2 points per line in symmetric incidence structures) may scale to sub-cases of q = 128 with a prescribed automorphism.
- Use the Cherowitzo-Penttila-Pinneri-Royle flock and q-clan correspondence (Subiaco) to search for new herds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many monomial or binomial candidates are equivalent to known hyperovals under the 'magic action'. Always run the full equivalence test.
- Ovals (q+1 points) and hyperovals (q+2) differ: the claim must be a 130-point hyperoval.
- Wikipedia lags: it still calls PG(2,64) unclassified, but Vandendriessche (2019) classified it. Use the EJC paper.
- Penttila and Royle (J. Geom. 54 (1995) 91-104) already searched all hyperovals of PG(2,128) with GF(2) o-polynomials, so o-polynomials with coefficients in GF(2) will not give a new class; also, a prescribed prime order that does not divide |PGammaL(3,128)| makes a partial claim vacuous.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/pg2-128-new-hyperoval.md
```

Already set up? Say `run V3R1T4S on pg2-128-new-hyperoval`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pg2-128-new-hyperoval`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
