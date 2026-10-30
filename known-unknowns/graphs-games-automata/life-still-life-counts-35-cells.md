# Game of Life still-life enumeration: the number of strict and pseudo still lifes with 35 cells (A019473, A056613), or quasi still lifes with 23 cells (A330283)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (counting, not listing: a(34) is 3.5e10 strict still lifes, and a(35) is expected to be about 2.5 times larger; the quasi count at n = 23 is laptop-hours) · open as of 2026-10-30

## The problem

Count finite still lifes in Conway's Life (B3/S23) with exactly n live cells, up to rotation and reflection. A strict still life cannot be split into two or more smaller still lifes (A019473). A pseudo still life can be split that way (A056613, using the 'two or more' definition). A quasi still life is made of two or more strict still lifes that share dead neighbour cells which stay dead for the same reason as when the parts are separated (A330283). Current state: A019473 and A056613 are known through n = 34 (strict a(34) = 35,422,864,104; pseudo a(34) = 41,058,173,683). The terms beyond 30 were computed by Nathaniel Johnston with Simon Ekström's still-life enumeration program, with a(34) added in January 2020. Earlier terms came from Robert Munafo, Mark Niemiec, Ekström and others. A330283 (Johnston, Dec 2019) is known through n = 22 (26,943,317). Wikipedia's still-life table is documented only up to 34 cells. Strictness can be decided in polynomial time (Cook 2003).

## What counts as a win

An exact value of A019473(35) or A056613(35), computed by two independent programs that agree. At least one program must not be derived from Ekström's code. Both programs must reproduce every listed term for n <= 30 exactly, and at least one must reproduce n = 31..34. At claim time the value must be in neither the live OEIS entry nor the enumeration table of Wikipedia's 'Still life (cellular automaton)' article. Report the run logs, the per-n counts and the symmetry-class breakdown (counts by symmetry group), so a skeptic can re-run any slice.

## Partial wins

- **p1:** The exact value of A330283(23) (quasi still lifes with 23 cells), from two independent programs that also reproduce A330283(8..22) exactly, and not already in the live OEIS entry.
- **p2:** An independent confirmation of A019473(34) and A056613(34): a program not derived from Ekström's code reproduces both 34-cell counts exactly, with logs and per-symmetry-class counts. A discrepancy counts instead only if two independent programs agree on the new value and it is backed by explicit lists of the disputed objects.

## How a win is checked

Run both programs. Spot-check samples of enumerated objects with lifelib (apgcode, still-life test, strict/pseudo classification) and with an independent numpy stepper. Compare the small-n counts with OEIS, and check that the strict and pseudo totals at each n agree with a single combined enumeration of all still lifes. Fetch the OEIS entries live.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A019473>

## Sources

- <https://oeis.org/A019473>
- <https://oeis.org/A056613>
- <https://oeis.org/A330283>
- <https://en.wikipedia.org/wiki/Still_life_(cellular_automaton)>
- <https://www.mrob.com/pub/seq/a019473.html>
- <https://conwaylife.com/forums/viewtopic.php?p=38931#p38931>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Strict, pseudo and quasi have different definitions. A056605 is a known incorrect version of the strict count, so do not reproduce it.
- Counting is up to the 8 symmetries of the square, so orbit counting must handle the symmetric objects correctly.
- Strict still lifes need not be 8-connected (several islands can stabilise each other), so a pure polyplet enumeration misses objects.
- Use 64-bit (or wider) counters.
- The OEIS 2026-10-27 edit (A019473 rev. 73) added a MathWorld link, not a new term. Wikipedia (edited 2026-09-19) and search snippets of LifeWiki's Still life page stop at 34 cells (strict, pseudo) and 22 cells (quasi). LifeWiki and the conwaylife.com forums were Cloudflare-blocked here (BLOCKED), so check them by any route that is not blocked before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/life-still-life-counts-35-cells.md
```

Already set up? Say `run V3R1T4S on life-still-life-counts-35-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `life-still-life-counts-35-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
