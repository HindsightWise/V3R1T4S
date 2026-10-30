# KnotInfo concordance genus: a certified concordance to a lower-genus knot for one of the 208 11- and 12-crossing knots listed as intervals (incl. the Conway knot 11n_34 at [1,3])

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

The smooth concordance genus g_c(K) is the minimum Seifert genus of a knot smoothly concordant to K (Livingston). Lower bounds come from Alexander-polynomial factorisation (Casson's argument), signatures and Heegaard Floer invariants. Upper bounds come from exhibiting a concordant knot of lower genus. KnotInfo (Livingston and Moore) compiles results from Livingston (arXiv:math/0107141, arXiv:0807.0765), Kearney ('The concordance genus of 11-crossing knots', arXiv:1208.5059, extending McAtee), and Lamm's slice results. The KnotInfo page lists 20 unknown 11-crossing cases. In database_knotinfo 2026.10.5, 208 entries are intervals: 19 at 11 crossings (e.g. 11a_6 [2,3], 11a_72 [2,4], 11n_34 [1,3], 11n_145 [1,3]) and 189 at 12. The Conway knot 11n_34 is topologically slice but not smoothly slice (Piccirillo), so its smooth g_c is 1, 2 or 3.

## What counts as a win

For a knot K whose smooth_concordance_genus is an interval [a,b] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a knot J with Seifert genus g STRICTLY LESS than b (direction: min), and a concordance between K and J. The genus of J is certified by KnotInfo's three_genus for J or by an explicit Seifert surface (a diagram plus Seifert's algorithm, with g = (c - s + 1)/2). The concordance is certified by a ribbon disk for K # -J (mirror and reverse of J), given as n band moves on a verified diagram of K # -J that produce an (n+1)-component link that Regina certifies as the unlink. g = a closes the interval.

## Partial wins

- **p1:** A certified ribbon concordance in the same form between two different knots that both have interval-valued KnotInfo concordance genus. A future value for one then fixes or bounds the other.
- **p2:** For 11n_34 specifically, a certified concordance to a genus-2 knot, lowering its upper bound from 3 to 2, reported separately because of the Conway knot's prominence.

## How a win is checked

Skeptic builds K # -J, replays the band moves in SnapPy, identifies the result as the unlink with Regina (split and trivial components), and checks the genus of J. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/smooth_concordance_genus.html>

## Sources

- <https://knotinfo.org/descriptions/smooth_concordance_genus.html>
- <https://arxiv.org/abs/1208.5059>
- <https://arxiv.org/abs/0807.0765>
- <https://arxiv.org/abs/math/0107141>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: genus-reducing band moves on K (an oriented band to a 2-component link, then a second band back to a knot) searched for results of lower genus with the same algebraic concordance class.
- Conventional: search for ribbon disks of K # -J for candidates J with matching Alexander-polynomial factorisation, using Herald-Kirk-Livingston style band searches.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Orientation and mirror conventions: concordance from K to J means K # -J is slice, where -J is the reversed mirror. Getting this wrong gives false certificates.
- The KnotInfo text has small inconsistencies (11a_57, 11a_102 and 11n_69 appear as both unknown and resolved). Go by the live data entry.
- Unlink recognition must certify split and trivial components.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-concordance-genus-unknown.md
```

Already set up? Say `run V3R1T4S on knotinfo-concordance-genus-unknown`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-concordance-genus-unknown`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
