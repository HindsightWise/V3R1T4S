# KnotInfo crosscap numbers: a nonorientable spanning surface beating the best upper bound for an 11- or 12-crossing knot (573 intervals)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The crosscap number C(K) is the smallest first Betti number of a nonorientable surface in S^3 bounded by K. KnotInfo (Charles Livingston and Allison Moore, knotinfo.org) records it from several sources. Upper bounds include Seifert-algorithm bounds (C(K) <= 2g(K)+1) and state surfaces. Results and bounds come from Murakami-Yasuhara, Teragaito, Hirasawa-Teragaito (2-bridge knots, arXiv:math/0504446), Burton-Ozlen (normal surfaces and integer programming, arXiv:1107.2382), Adams-Kindred (arXiv:1205.5520), Kindred (all alternating knots through 13 crossings, arXiv:1905.11367), Kalfagianni-Lee (Jones-polynomial bounds, arXiv:1408.4493), Ito-Takimura, and Jaco, Rubinstein, Spreer and Tillmann, 'Slope norm and an algorithm to compute the crosscap number' (arXiv:2108.07599, Algebr. Geom. Topol. 24 (2024) 4307-4351). JRST determined 196 previously unknown crosscap numbers (all five open 10-crossing knots, 45 of 96 open 11-crossing knots and 146 of 668 open 12-crossing knots), and all 196 values are installed in the database, although the description page still calls this preliminary work on 195 knots. In database_knotinfo 2026.10.5 every knot through 10 crossings is determined, and the 573 entries still left as intervals after JRST are 51 at 11 crossings and 522 at 12, mostly [2,5] (298) and [2,4] (263). For these, can an explicit nonorientable spanning surface close the interval or lower the upper bound?

## What counts as a win

For a knot K whose crosscap_number is an interval [a,b] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming, and whose crosscap number is not determined in any source the skeptic finds after arXiv:2108.07599 (AGT 24 (2024), already installed): a certified nonorientable spanning surface of K with first Betti number k = a, which closes the interval. Accepted certificates: (i) a PD code D, verified as K by SnapPy/Regina, and a Kauffman state s of D whose state surface is nonorientable, with k = c(D) - |s| + 1, where |s| is the number of state circles; or (ii) a Regina triangulation of the exterior of K with real torus boundary and a boundary edge representing the meridian (meridian filling certified as S^3 by Regina and the exterior identified as K), with a connected nonorientable normal surface whose single boundary curve meets the meridian once, and k = 1 - Euler characteristic.

## Partial wins

- **p1:** For a knot eligible as in the main criterion, a certificate (i) or (ii) with a < k < b, i.e. k STRICTLY LESS (direction: min) than the listed upper bound b and than every published upper bound for K, lowering the bound without closing the interval.
- **p2:** A demonstrated KnotInfo inconsistency: a verified certificate with k below a listed lower bound, or a listed exact value contradicted by such a certificate, with inputs saved.

## How a win is checked

(i) Skeptic identifies D with SnapPy/Regina, rebuilds the state surface from s and counts the state circles. Skeptic checks one-sidedness directly. A band joining a state circle to itself already gives a Mobius band. Otherwise propagate a normal orientation over the disks and half-twisted bands, taking nesting of the state circles into account, or rebuild the surface in Regina. (ii) Skeptic loads the triangulation in Regina, checks the meridian edge by filling along it and recognising S^3, identifies the exterior as K, and verifies the normal surface: connectedness, nonorientability, Euler characteristic, and that its boundary meets the meridian once. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/crosscap_number.html>

## Sources

- <https://knotinfo.org/descriptions/crosscap_number.html>
- <https://arxiv.org/abs/1107.2382>
- <https://arxiv.org/abs/1408.4493>
- <https://arxiv.org/abs/2108.07599>
- <https://arxiv.org/abs/1905.11367>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: enumerate all 2^c states on many non-minimal diagrams of K (state surfaces of non-minimal diagrams can beat minimal ones).
- Conventional: Regina normal-surface enumeration in small ideal triangulations of the exterior, in the spirit of Burton-Ozlen and JRST.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A state surface can be orientable. Check one-sidedness explicitly, since an orientable surface bounds the genus, not the crosscap number.
- Jaco-Rubinstein-Spreer-Tillmann's 196 values (AGT 2024) are already in the database even though the description page calls them preliminary. The remaining intervals are knots where their normal-surface algorithm was inconclusive or too large (around 30 tetrahedra), so plain Q-fundamental enumeration in the Burton-Ozlen triangulations is unlikely to settle them.
- The relation C(K) <= 2g(K)+1 already gives an upper bound. Make sure yours is strictly below every listed or published bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-crosscap-number-bounds.md
```

Already set up? Say `run V3R1T4S on knotinfo-crosscap-number-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-crosscap-number-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
