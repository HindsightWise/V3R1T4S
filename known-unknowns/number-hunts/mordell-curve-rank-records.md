# Mordell curves y^2 = x^3 + k: a smaller |k| of given rank 7..16 than the OEIS upper bounds, or rank >= 18

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (descent and point search per candidate k); needs cluster for rank >= 18 · open as of 2026-10-30

## The problem

OEIS A031507 (k > 0), A031508 (curves y^2 = x^3 - k) and A373795 (smallest |k|) give the smallest k for which y^2 = x^3 + k has rank n. Exact values are known only for n <= 6 (A031507: 1, 2, 15, 113, 2089, 66265, 1358556; Gebel-Petho-Zimmer 1998, Womack 2003). Upper bounds from Tom Womack's thesis (2003, Table 3.3) are: A031507 a(7) <= 47550317, a(8) <= 1632201497, a(9) <= 185418133372, a(10) <= 68513487607153; A031508 a(7) <= 56877643, a(8) <= 2520963512, a(9) <= 463066403167, a(10) <= 56736325657288, a(11) <= 46111487743732324, a(12) <= 6533891544658786928. Noam Elkies (ANTS-XVI, 2024) gave a(16) <= 1160221354461565256631205207888 (recorded in both A031507 and A031508) and showed that some k has rank >= 17, the largest Mordell-curve rank recorded in these OEIS entries. The entries carry the keyword 'more'; their latest dated comments are from June-July 2024. Curves for k and -27k are 3-isogenous and have the same rank (Elkies). Target: beat a listed bound, or reach rank 18. Credit: Gebel, Petho, Zimmer, Quer, Womack, Elkies, Klagsbrun, Cremona, and the OEIS editors (Hasler, Aranda, Sloane, Sondow).

## What counts as a win

CONFIRMED for a nonzero integer k and a rank r of one of two kinds. (A) 7 <= r <= 16, a rank-r upper bound is listed for k's sign in OEIS A031507 (k > 0) or A031508 (k < 0, as |k|) at verification time, and |k| is STRICTLY SMALLER (direction: min) than that bound and than any rank-r example of the same sign found in a same-day literature check (Womack 2003 Table 3.3, Elkies ANTS-XVI 2024, and later work). (B) r >= 18, any k, provided OEIS A031507, A031508 and A373795 and a same-day literature check show no Mordell curve of rank >= 18. In both cases the rank needs r points on y^2 = x^3 + k with nonzero canonical-height regulator (PARI ellheightmatrix, determinant > 0 at >= 38 digits, stable at 2x precision). For (A) it also needs an upper bound rank <= r from a 2-descent or 3-isogeny Selmer computation (PARI ellrank, or Magma TwoDescent/ThreeIsogenyDescent) that the verifier reproduces; the claim states whether that bound assumes GRH (PARI class groups do unless certified).

## Partial wins

- **p1:** Rank-at-least record: as in (A), but the rank is certified only as >= r (r independent points, no matching upper bound), for some 7 <= r <= 16 with a listed OEIS bound for k's sign, with |k| strictly smaller than that bound and than any rank-r example of that sign found in the same-day literature check of (A).
- **p2:** Rank-17 example: an explicit k with 17 independent points (nonzero regulator as in the main criterion). If an explicit rank->=17 Mordell k is published (Elkies, ANTS-XVI, 2024, or later, as cited in OEIS A031507/A373795 or found by the verifier), |k| must be strictly smaller than the smallest such published |k|. If none is published explicitly, any such k counts.

## How a win is checked

PARI/GP: ellinit([0,0,0,0,k]), check that each point lies on the curve, compute ellheightmatrix and its determinant at high precision, and run ellrank (or Magma descent) for the upper bound. Compare |k| with the bound listed in OEIS on the day as exact digit strings. Minutes per claim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A031507>

## Sources

- <https://oeis.org/A031507>
- <https://oeis.org/A031508>
- <https://oeis.org/A373795>
- <https://doi.org/10.2140/obs.2020.4.233>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Quer's method: a high 3-rank of the class group of Q(sqrt(-3k)) forces a large 3-Selmer group. Search k with large 3-class rank (via class-group computations in PARI) and then hunt points with ellrank. This is how ranks 12+ were reached.
- Elkies-style lattice search: choose k as a value of a polynomial for which y^2 = x^3 + k(t) has many sections, then specialise t.
- Use the k <-> -27k isogeny. A good k divisible by 27 gives a candidate -k/27 on the other sign with smaller |k|.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rank lower bounds from points need the regulator to be clearly nonzero. Dependent points, for example torsion multiples, are common mistakes.
- 2-descent upper bounds can exceed the true rank because of Sha[2]. For full win (A) the upper bound must actually equal r, otherwise it only counts as p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/mordell-curve-rank-records.md
```

Already set up? Say `run V3R1T4S on mordell-curve-rank-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mordell-curve-rank-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
