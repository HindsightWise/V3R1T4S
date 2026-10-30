# Elliptic curves over Q of rank r = 5..11 with smaller conductor than the Elkies-Watkins records

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (searches for curves with many small integral points, then 2-descent and conductor computation) · open as of 2026-10-30

## The problem

The smallest conductors of elliptic curves over Q of rank 0..4 are 11, 37, 389, 5077 and 234446 (OEIS A052432; minimality comes from Cremona's complete tables). For higher ranks only upper bounds are known. Noam Elkies and Mark Watkins (ANTS VI, 2004, arXiv math/0403374, Table 2) list the smallest conductors they found: rank 5: 19047851 ([0,0,1,-79,342], previously known); rank 6: 5187563742; rank 7: 382623908456; rank 8: 249649566346838; rank 9: 32107342006814614; rank 10: 10189285026863130793; rank 11: 18031737725935636520843. They credit Tom Womack's earlier compilations (2000). Cremona's 'Best known conductors' table (originally Womack's, updated April 2012, https://johncremona.github.io/conductors.htm) still lists exactly these records on 2026-10-30. OEIS A052432, whose data stops at rank 4, quotes the rank 5, 6, 7 and 11 values in a comment as 'just upper bounds'. The authors were fairly certain about ranks 5-8 but expected that gains remain at ranks 9-11: their rank-11 record has prime conductor, and their searches were not exhaustive. Their Table 4 gives the matching records for smallest minimal |discriminant|, for ranks 5-10.

## What counts as a win

CONFIRMED (full win) for an elliptic curve E/Q, given by its global minimal model, with r in {5, ..., 11} independent rational points (Neron-Tate height matrix determinant > 0 at 100 and at 200 digits, agreeing), whose conductor N (PARI ellglobalred, with complete factorisation of the discriminant) is STRICTLY BELOW (direction: min) the Elkies-Watkins Table 2 value for that r. N must also be below any smaller value for that r on OEIS A052432, on Cremona's 'Best known conductors' table (https://johncremona.github.io/conductors.htm, originally Womack's), or in later literature, checked at verification time. Rank must be shown by explicit points; analytic rank does not count. The curve may have rank greater than r; it is then compared in every row it qualifies for.

## Partial wins

- **p1:** For r in {9, 10, 11}, a curve with r independent points, not isomorphic to any curve in Elkies-Watkins Table 2, whose conductor is below the fifth (largest) Table 2 value for that r: 77211251506212554 for r=9, 39432942782223365758 for r=10, 252948166615918192888894 for r=11.
- **p2:** For r in {7, 8, 9, 10}, a curve with r independent points whose minimal discriminant has |Delta| STRICTLY BELOW the first entry of Elkies-Watkins Table 4 for that r: 1829517077483, 409086620841461, 95276302704064331 and 50881111474471687972.

## How a win is checked

PARI/GP: E = ellinit(a); ellminimalmodel; ellglobalred gives the conductor (factor the discriminant completely); check ellisoncurve for each point; ellheightmatrix at \p100 and \p200 with determinant agreement. Compare against the Elkies-Watkins tables and a fresh check of OEIS A052432, Cremona's best-known-conductors table and the literature.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A052432>

## Sources

- <https://arxiv.org/abs/math/0403374>
- <https://oeis.org/A052432>
- <https://johncremona.github.io/conductors.htm>
- <https://people.math.harvard.edu/~elkies/compnt.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Elkies-Watkins search lattices of curves with many integral points with |x| <= h^2. Extending to larger h and smaller U-parameters, which they suggest for rank 9, is the most direct route.
- Bias the search toward curves whose discriminant has large |Delta|/N, i.e. squarefull factors; the authors note their rank-11 record has prime conductor, so there is room.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- OEIS links Cremona's 'Best known conductors' page at an old Warwick URL that no longer resolves; the live copy is https://johncremona.github.io/conductors.htm (still the Elkies-Watkins records for ranks 6-11 on 2026-10-30). Check it, OEIS and the literature before claiming.
- Do not compare a non-minimal model's discriminant; use the minimal model and the true conductor, including wild primes 2 and 3.
- Ranks 5-8 are believed optimal by the authors; expect wins at r = 9-11.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/elliptic-curve-rank-small-conductor-records.md
```

Already set up? Say `run V3R1T4S on elliptic-curve-rank-small-conductor-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `elliptic-curve-rank-small-conductor-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
