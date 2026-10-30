# Fewest squares tiling a rectangle: a counterexample to h(dn,dm) = h(n,m) beyond the 388 x 388 table, or new exact rows of OEIS A219158

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-days (exact minimum-square tiling search per rectangle) · open as of 2026-10-30

## The problem

h(n,m) is the minimum number of integer-sided squares that tile an n x m rectangle (Kenyon, 'Tiling a rectangle with the fewest squares', JCTA 1996; Walters 2009). Bertram Felgenhauer's page computes h exactly for all rectangles up to 388 x 388. Results are by Felgenhauer to 300 (2013), Ed Pegg Jr to 160, and Massimo Ortolano to 388, with rows 323 and 352 corrected on 2017-08-26. A 2025-06-08 change was cosmetic. Ortolano's OEIS b-file A219158 (rows 1..388, corrected by Qizheng He) records the same table. The page lists the conjecture h(dn,dm) = h(n,m) (scaling never helps) and says it is 'likely to be false', citing MathOverflow question 116382. Inside the 388 table no scaled pair violates it (re-checked 2026-10-30 on all 48,490 pairs), so a counterexample with exact h(n,m) needs a scaled rectangle with a side above 388. On MathOverflow, Pegg (2017) reported that his search of rectangles with maximum side <= 760 left a single possible counterexample (2 x 697x611 in 16 squares vs a 17-square 697x611). He collected 4944 more 'possible counterexamples' (scaled tilings beating the best known unscaled tiling, where the unscaled minimum is unproven) in a Wolfram demonstration. On 2026-09-29 a MathOverflow answer by jvvk tiled 697x611 with 14 squares, which rules that case out. A related conjecture, h(n+m,m) = h(n,m)+1 for n >= m, is already refuted on the page (h(112,53) = h(59,53) = 11). For squares, Sascha Kurz observed that A018835(n) = min over prime divisors p of A018835(p) up to n = 104.

## What counts as a win

Success means integers d >= 2 and n, m <= 388 with max(dn, dm) > 388, plus an explicit tiling of the dn x dm rectangle by integer squares (list of (x, y, s)) that uses STRICTLY fewer squares than h(n,m) as given in the live Felgenhauer table / A219158 b-file. h(n,m) must also be independently re-derived by the claimant's own exact search, because the counterexample depends on it being a true minimum. The table, MathOverflow question 116382 and Pegg's 'Possible Counterexamples to the Minimal Squaring Conjecture' demonstration must be re-fetched before claiming, and the pair must not already be reported or refuted there. Expect the d = 2, max side <= 760 range to have been swept heuristically already.

## Partial wins

- **p1:** A complete new row of exact values h(389, m) for all m = 1..389 (or the next row missing from the live table), computed by two independently written exact programs that agree and that reproduce a random sample of at least 1,000 entries of the existing table, including rows 323 and 352.
- **p2:** A computer-checked proof that h(dn,dm) = h(n,m) for all d >= 2 with dn, dm <= D and n, m <= 388, for some D >= 600, labelled as a bounded result. It needs two agreeing programs.

## How a win is checked

Check the tiling's exact coverage of dn x dm and count its squares (milliseconds). Look up h(n,m) in the live table and recompute it with an independent exact search (Felgenhauer-style valley search or a SAT model with a cardinality bound proving that h(n,m)-1 squares fail), with the DRAT proof checked if SAT is used.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://int-e.eu/~bf3/squares/>

## Sources

- <http://int-e.eu/~bf3/squares/>
- <https://oeis.org/A219158>
- <https://doi.org/10.1006/jcta.1996.0104>
- <https://oeis.org/A018835>
- <https://mathoverflow.net/questions/116382/tiling-a-rectangle-with-the-smallest-number-of-squares/>
- <http://demonstrations.wolfram.com/PossibleCounterexamplesToTheMinimalSquaringConjecture/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search for n x m where the optimal tiling is 'basic' (no guillotine cut) and highly irregular, like 13 x 11. Scaling by d lets squares of non-multiple sizes appear, so search dn x dm tilings in which some squares are not multiples of d.
- Upper-bound heuristics first: build dn x dm tilings from imperfect squared rectangles of low order with the right aspect ratio (from squaring.net catalogues) and compare their counts with h(n,m).
- A cheap filter: the table gives h(n,m) for all n, m <= 388, so scan candidate (n, m, d) with dn just above 388 by the number of squares in the best known tiling.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Felgenhauer warns that his list had wrong rows between 2016-06-14 and 2017-08-26. Use the current list, and spot-check against your own exact computation.
- Within the 388 table, scaled pairs are already present and show no counterexample, so a win must leave the table range.
- Do not run the downloadable young.cc/Young.hs. Write your own search (bank rule: no downloaded code).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/fewest-squares-rectangle-scaling-counterexample.md
```

Already set up? Say `run V3R1T4S on fewest-squares-rectangle-scaling-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fewest-squares-rectangle-scaling-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
