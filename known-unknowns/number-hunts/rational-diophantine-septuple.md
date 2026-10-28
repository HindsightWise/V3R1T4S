# MOONSHOT - a rational Diophantine septuple

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A rational Diophantine m-tuple is a set of m nonzero rationals such that the product of any two, plus 1, is the square of a rational. Euler knew infinitely many quintuples; Philip Gibbs found the first rational sextuples; Dujella, Kazalicki, Mikic and Szikszai (2017) proved there are infinitely many, and Piezas gave a simpler parametrisation. Andrej Dujella's survey (section 5.2) states it is still not known whether any rational Diophantine septuple exists. The problem is also listed as unsolved on Epoch AI's FrontierMath Open Problems page (no prize); Dujella's page's most recent dated item is Rathbun's 2024 sextuples.

## What counts as a win

CONFIRMED (full win) for seven distinct nonzero rationals a_1..a_7 such that a_i*a_j + 1 is the square of a rational for all 21 pairs i < j, checked with exact rational arithmetic, and no septuple is reported on https://web.math.pmf.unizg.hr/~duje/ratio.html or https://epoch.ai/frontiermath/open-problems/diophantine-septuple (both re-fetched immediately before the claim) or in a same-day literature check. Any pair with a_i*a_j + 1 = 0 must be reported and flagged; a septuple relying on it is a degenerate case and only counts if the literature definition admits it.

## Partial wins

- **p1:** A cube Diophantine quadruple: four distinct positive integers with all six a*b + 1 perfect cubes (Bugeaud and Dujella prove at most 7 elements are possible; the survey's section 7.1 gives only triples such as {2, 171, 25326}), absent from section 7.1 of https://web.math.pmf.unizg.hr/~duje/gener.html and the Bugeaud-Dujella paper at verification time.

## How a win is checked

Python fractions.Fraction: for each pair compute a*b + 1 = u/v in lowest terms and check u and v are perfect squares with math.isqrt. For p1, integers and integer cube roots with exact cubing.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~duje/ratio.html>

## Sources

- <https://web.math.pmf.unizg.hr/~duje/ratio.html>
- <https://web.math.pmf.unizg.hr/~duje/gener.html>
- <https://web.math.pmf.unizg.hr/~duje/dtuples.html>
- <https://web.math.pmf.unizg.hr/~duje/pdf/budu.pdf>
- <https://epoch.ai/frontiermath/open-problems/diophantine-septuple>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend known sextuples: for each sextuple from the Dujella-Kazalicki-Mikic-Szikszai and Piezas families, the seventh element must lie on a curve given by six square conditions; search for rational points on its genus-1 or genus-2 quotients first.
- Elliptic curves induced by Diophantine triples: triples whose induced curve has high rank give more room for extensions; rank by the techniques of the torsion-record tables.
- Hash-join search (imported from databases): enumerate rationals of bounded height, hash a*b+1 squareness by residue fingerprints modulo many primes, and join candidate sets as a clique search in the 'square-product graph'.
- Maximum-clique heuristics (imported from graph algorithms): the problem is a 7-clique in the graph whose vertices are rationals and edges mean ab+1 is a square; use modern clique solvers on large height-bounded vertex sets.
- Groebner-basis and homotopy methods (imported from computer algebra and robotics kinematics) on the variety of sextuples with a free seventh coordinate, to find special subvarieties of low genus.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Repeated elements or zero elements make 'septuples' trivially.
- a*b + 1 = 0 is a degenerate square; flag it rather than count it silently.
- Floating-point squareness checks; use exact rationals only.
- Extending a set that is actually a sextuple with one condition failing (20 of 21 squares) is not a septuple.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/rational-diophantine-septuple.md
```

Already set up? Say `run V3R1T4S on rational-diophantine-septuple`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rational-diophantine-septuple`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
