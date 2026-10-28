# High-rank elliptic curves over Q with prescribed torsion: beat a cell of Dujella's table

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

For each of Mazur's 15 torsion groups T, Andrej Dujella's table gives the best known lower bound B(T) for the rank of an elliptic curve over Q whose torsion subgroup is exactly T. On 2026-10-28 the table reads: trivial 32 (Elkies-Klagsbrun-Li, October 2026; the rank history page lists rank >= 30 and >= 31 by Alpoge-Howell, August 2026, before it), Z/2 22 (Li 2026), Z/3 15 and Z/4 13 (Elkies-Klagsbrun 2020; Li 2026), Z/5 9 (Klagsbrun 2020), Z/6 9 (Klagsbrun 2020, Voznyy 2020, Dujella-Peral 2026), Z/7 6 (Klagsbrun 2020), Z/8 6 (Elkies 2006, Dujella-MacLeod-Peral 2013, Voznyy 2021), Z/9 4 (Fisher 2009, van Beek 2015, Dujella-Petricevic 2021, Dujella-Petricevic-Rathbun 2022, Voznyy 2026), Z/10 4 (Dujella 2005, 2008; Elkies 2006; Fisher 2016), Z/12 4 (Fisher 2008), Z/2xZ/2 15 (Elkies 2009, Li 2026), Z/2xZ/4 9 (Dujella-Peral 2012, 2019; Klagsbrun 2020), Z/2xZ/6 6 (Elkies 2006; Dujella-Peral-Tadic 2015; Dujella-Peral 2020), Z/2xZ/8 3 (Connell 2000 and many later authors, most recently AttarBashi, Fisher, Rathbun and Voznyy 2022). The trivial-torsion and Z/2 cells are being pushed by large 2026 campaigns and are not laptop targets; the small-family cells (Z/7 through Z/12, Z/2xZ/6, Z/2xZ/8) are searched by Mestre-Nagao sieving over one- or two-parameter Kubert families, which is laptop-scale. A rank-4 curve with torsion Z/2xZ/8 would settle a question asked in print since 2000.

## What counts as a win

CONFIRMED (full win) for an elliptic curve E over Q, given by integral Weierstrass coefficients, whose torsion subgroup computed exactly (PARI elltors) is isomorphic to T, together with r explicit rational points whose Neron-Tate height-pairing matrix has determinant > 0 (computed at 100 and again at 200 decimal digits, agreeing, and bounded away from 0 by at least 10^-20 relative to the product of the diagonal), where r is STRICTLY GREATER (direction: max) than the value of B(T) shown for that T on https://web.math.pmf.unizg.hr/~duje/tors/tors.html, re-fetched live immediately before the claim, and greater than any higher value found in a same-day literature check (arXiv, Dujella's history page). Rank lower bounds only: analytic-rank, Nagao-sum or parity arguments never count.

## Partial wins

- **p1:** Record tie with a new curve: torsion exactly T for T in {Z/7, Z/8, Z/9, Z/10, Z/12, Z/2xZ/6, Z/2xZ/8}, r independent points with r equal to the live B(T), and the curve not isomorphic over Q (different minimal model after ellminimalmodel and not related by ellisomat) to any curve on Dujella's page for T at verification time.
- **p2:** Family record: an elliptic curve over Q(t) with torsion T and r independent Q(t)-points, r STRICTLY GREATER than G(T) on https://web.math.pmf.unizg.hr/~duje/tors/generic.html at verification time; independence certified by specializing at one rational t0 where the torsion is still T and the r specialized points have positive regulator.

## How a win is checked

PARI/GP: E=ellinit(a); check discriminant != 0; elltors(E) gives T exactly; ellisoncurve for every point; M=ellheightmatrix(E,P) at \p100 and \p200; matdet(M) > 0 with the stated margin and stable between precisions. Compare ellminimalmodel(E) and j-invariant against every curve scraped from the T page (z7.html, z8.html, ...). For p2 substitute t0, re-run the same checks, and verify the points satisfy the generic equation symbolically.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~duje/tors/tors.html>

## Sources

- <https://web.math.pmf.unizg.hr/~duje/tors/tors.html>
- <https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html>
- <https://web.math.pmf.unizg.hr/~duje/tors/generic.html>
- <https://web.math.pmf.unizg.hr/~duje/tors/z2z8.html>
- <https://web.math.pmf.unizg.hr/~duje/tors/z7.html>
- <http://web.math.pmf.unizg.hr/~duje/pdf/highranktorsion.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Mestre-Nagao sieve: run the Kubert parametrization for T over millions of small-height parameters, rank by Nagao sums S(N) = sum over p<N of (1 - (p-1)/#E(F_p)) * log p, then run 2-descent (PARI ellrank) only on the top 0.01%.
- Ranking as a learning problem (imported from machine learning): train a gradient-boosted model or small transformer on the first few hundred a_p of curves with known rank (the murmurations work of He, Lee, Oliver and Pozdnyakov shows a_p sequences carry rank signal) and use it to reorder the sieve queue.
- Bayesian optimisation / bandits over the parameter plane (imported from experimental design): treat the Nagao sum as a noisy objective, fit a Gaussian process over (u, v) parameters in two-parameter families, and spend sieve budget where the posterior upper bound is highest.
- Fibre in a richer family: for Z/2xZ/6 and Z/2xZ/8 use Dujella-Peral style sub-families with forced extra points (Diophantine triples, Heron triangles), so the generic rank starts higher before sieving.
- Signal-processing view of the sieve: Nagao sums are matched filters; replace them by a weighted sum tuned on known record curves (learned weights per p) and check whether it separates rank-r from rank-(r-1) curves better.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The torsion is larger than T (e.g. a Z/8 curve that actually has Z/2xZ/8): it then belongs to a different row and is not a record for T.
- Points that are dependent (multiples, sums with torsion) give a singular height matrix; low-precision determinants can look positive. Require two precisions and a margin.
- Rank 'found' by analytic rank, Nagao sums, root number/parity or BSD heuristics is not a lower bound. Only explicit independent points count.
- A change of Weierstrass model or a twist that is actually isomorphic over Q re-presents a listed curve; always compare minimal models.
- The trivial and Z/2 cells move monthly in 2026 (large GPU campaigns); a claim there must be checked against the live page and the rank history page the same day.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/dujella-torsion-rank-records-q.md
```

Already set up? Say `run V3R1T4S on dujella-torsion-rank-records-q`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dujella-torsion-rank-records-q`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
