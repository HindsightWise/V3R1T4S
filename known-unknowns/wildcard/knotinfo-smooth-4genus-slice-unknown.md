# KnotInfo: close one of the last interval-valued smooth 4-genus entries (13 crossings) by an explicit ribbon disk or genus-1 cobordism

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

KnotInfo (Charles Livingston and Allison Moore, knotinfo.org) lists the smooth 4-genus of prime knots up to 13 crossings. All entries through 12 crossings are now determined, the last ones by Brittenham and Hermiller, Stoimenow's ribbon searches, Lamm and Herald-Kirk-Livingston. In database_knotinfo 2026.10.5 (the monthly mirror, released 2026-10-05) exactly 19 entries are still intervals, all 13-crossing knots. Six are [0,1]: 13n_65, 13n_3871, 13n_3872, 13n_3897, 13n_3936, 13n_4582. Thirteen are [1,2], e.g. 13a_2554, 13a_2844, 13a_4184, 13n_459, 13n_863, 13n_2496. Dunfield and Gong (arXiv:2512.21825) ran large ribbon and slice-obstruction searches over all 352.2 million prime knots up to 19 crossings and left smooth sliceness undetermined for about 11,400 of them, so the [0,1] cases have survived serious search. Upper bounds are constructive and mechanically checkable. Band moves that produce an unlink certify a ribbon disk. A genus-g cobordism to a slice knot certifies g4 <= g. Can an explicit construction realise the lower bound for one of these 19 knots?

## What counts as a win

For a knot K whose smooth_four_genus is an interval [a,b] in the live KnotInfo database (https://knotinfo.org/, or its database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming, and not resolved in any paper the skeptic finds: a saved sequence of band moves on a verified diagram of K that realises the lower bound a. (i) If a = 0: n bands producing an (n+1)-component link that Regina certifies is the unlink (each component unknotted and the link split), which is a ribbon disk. (ii) If a = 1: a genus-1 cobordism, given as band moves, from K to a knot that KnotInfo lists with smooth_four_genus 0. Every intermediate identification must be checked by SnapPy and Regina.

## Partial wins

- **p1:** A ribbon certificate in the sense of (i) for a 14- or 15-crossing knot that Dunfield-Gong (arXiv:2512.21825) list as of unknown smooth sliceness, checked the same way.
- **p2:** A concordance, given as band moves checked by SnapPy and Regina, between two of the six [0,1] knots, or between one of them and a knot of 14 or 15 crossings, so that a future ribbon disk for one settles both.

## How a win is checked

Skeptic replays the band moves in SnapPy (link diagrams via PD codes), identifies each result with Regina (unknot/unlink recognition, knot identification), and checks genus bookkeeping. Under 30 minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/>

## Sources

- <https://knotinfo.org/>
- <https://knotinfo.org/descriptions/smooth_4_genus.html>
- <https://github.com/soehms/database_knotinfo>
- <https://pypi.org/project/database-knotinfo/>
- <https://arxiv.org/abs/2512.21825>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: exhaustive search of short bands between diagram arcs (Herald-Kirk-Livingston style computer search for ribbon disks).
- Conventional: symmetric-union and 2-bridge ribbon templates (Lisca's classification) applied to near-template knots.
- Cross-domain import (reinforcement learning, as in the 'RL for ribbon knots' work): agents choosing band moves with rewards from simplification of hyperbolic volume.
- Cross-domain import (graph rewriting / chemistry reaction search): treat band moves as reactions and run beam search over the reaction network with canonical PD hashing.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Topologically slice vs smoothly slice: constructions here are smooth; lower bounds from Freedman-type results do not apply.
- Unlink recognition must certify split + trivial components; a link with unknotted components can still be non-trivial.
- Several entries were resolved by personal communications or new papers not yet installed; search arXiv before claiming.
- The six [0,1] knots have survived Dunfield-Gong's ribbon search; expect long odds and record negative results honestly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-smooth-4genus-slice-unknown.md
```

Already set up? Say `run V3R1T4S on knotinfo-smooth-4genus-slice-unknown`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-smooth-4genus-slice-unknown`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
