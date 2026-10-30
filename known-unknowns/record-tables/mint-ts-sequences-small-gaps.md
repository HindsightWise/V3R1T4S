# (t,s)-sequences in base 2 or 3: close a MinT gap between the best known t and the lower bound (smallest: is there a (4,8)-sequence in base 2?)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: pure thought plus laptop-hours (exact LP certificates or exhaustive digital searches) · open as of 2026-10-30

## The problem

A (t,s)-sequence in base b is an infinite sequence in [0,1)^s whose aligned blocks of b^m points form (t,m,s)-nets for every m. Smaller t is better. MinT (Schurer and Schmid, University of Salzburg; database last updated 2024-09-05) lists, on 2026-10-30, these gaps in base 2: s = 8, best digital t = 5 (Niederreiter-Xing, genus 5), lower bound t >= 4; s = 9, 6 vs 5; s = 10, 8 vs 6; s = 11, 9 vs 7; s = 12, constructive 11, a digital 10 known to exist (Niederreiter-Xing on a manYPoints curve of genus 10 with 13 rational places), bound 7. Base 3: s = 8, 3 vs 2; s = 10, 4 vs 3; s = 12, 5 vs 4; s = 13, 6 vs 4. A (t,s)-sequence gives a (t,m,s+1)-net for every m, so MinT's bounds come from finite cases. For example, no (3,m,8)-net exists for large m because m-reduction gives a (3,16,8)-net, whose embedded OOA(2^16, 8, S_2, 4, 13) violates the linear-programming bound for OOAs (Martin-Stinson). Explicit sequence records come from Niederreiter and Xing's function-field constructions, implemented by Pirsic.

## What counts as a win

Either of two outcomes is a win. (A) Lower bound: an exact certificate that no (t,m,s+1)-net in base b exists for some m, with b in {2,3}, t equal to MinT's live lower bound for (t,s)-sequences (http://mint.sbg.ac.at/query.php?b= < b > &m=seq&s= < s > &p=mst, 'Lower bound on t'), where that bound is STRICTLY BELOW the best known t (direction: raise the bound). The certificate is an exact rational dual solution of the LP bound for an OOA(b^m, s+1, S_b, T, m-t) of any depth T, verified in exact arithmetic. MinT's lower bound for that s then rises. (B) Construction: a digital (t,s)-sequence over F_b, b in {2,3}, with t STRICTLY BELOW (direction: min) the smallest t listed on that MinT page (constructive or existence-only), defined by a finite algebraic recipe for its generator matrices and accompanied either by a machine-checked proof (Lean, Coq or Isabelle) of its t-value or by an instance of a published theorem whose hypotheses (genus, number and degrees of places of an explicit function field) are verified by two independent computer algebra systems. Neither outcome may already appear in any paper or preprint of any date (MinT lists no new methods after 2008, so the literature since then counts).

## Partial wins

- **p1:** A digital-only bound: a re-runnable exhaustive proof (DRAT checked with drat-trim, or two independent programs that agree) that no digital (4,m,9)-net over F_2 exists for some m (MinT's digital net bound for s = 9 is 4, e.g. at m = 13, 14, 20 and 25). This proves that no digital (4,8)-sequence over F_2 exists. It counts only if no paper or preprint already proves that the least t of a digital 8-dimensional sequence over F_2 is 5.
- **p2:** A constructive digital (10,12)-sequence over F_2, matching MinT's existence value (constructive value 11): an explicit genus-10 function field over F_2 with at least 13 rational places (genus and place count confirmed by two computer algebra systems), plus generator matrices built from it by the Niederreiter-Xing construction, with the exact t-value of the induced digital (t,m,13)-nets confirmed to be at most 10 for every m <= 30. It counts only if no explicit such function field and no generator matrices of a digital (10,12)-sequence over F_2 are already published (check the references of the manYPoints entry for q = 2, g = 10 and Pirsic's Niederreiter-Xing matrix files).

## How a win is checked

For (A), rebuild the OOA LP (Martin-Stinson ordered Hamming scheme, or MinT's cited LP for OOAs) for the stated parameters and check the dual certificate in exact rationals. For (B), re-run the proof checker or both CAS computations, then sample-check the t-value of the generated nets for m <= 30 with an independent rank checker. Read the live MinT 'Seq' cell over http before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://mint.sbg.ac.at/table.php?b=2&p=mst&mode=cd&opt=bd&minx=0&miny=1&dx=30&dy=21>

## Sources

- <http://mint.sbg.ac.at/table.php?b=2&p=mst&mode=cd&opt=bd&minx=0&miny=1&dx=30&dy=21>
- <http://mint.sbg.ac.at/query.php?b=2&m=seq&s=8&p=mst>
- <http://mint.sbg.ac.at/query.php?b=2&m=seq&s=12&p=mst>
- <http://mint.sbg.ac.at/table.php?b=3&p=mst&mode=cd&opt=bd&minx=0&miny=1&dx=30&dy=21>
- <http://mint.sbg.ac.at/history.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- MinT's sequence bounds use the OOA LP only up to depth 4; LP bounds at depth 5-8, or for larger m, may be sharper.
- For p1, the digital (4,13,9)-net search only involves the first 9 rows of nine 13 x 13 matrices over F_2; exploit the column-operation symmetry.
- Constructions using places of higher degree (Niederreiter-Xing construction III) can beat the rational-place bound N_2(g).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Sequences have their own MinT query pages (m=seq). The page with m=inf and a given s is the (t,infinity,s)-net, which corresponds to the (t,s-1)-sequence; do not mix up the offsets.
- Finite checks of nets from a sequence prove nothing about all m; a construction needs a proof.
- Curves from manYPoints: lowering N_q(g) is the separate target manypoints-curves-finite-fields-lower-bounds.
- MinT lists no new methods after 2008; check the literature since then (e.g. duality theory for digital sequences) before claiming. Table URLs need their range parameters or MinT returns 'Argument dx is missing'.
- Pirsic's legacy Niederreiter-Xing page (sites.google.com/site/isabelpirsic/nxlegacy) redirected to a Google login on 2026-10-30. Nuyens' QMC generators page (people.cs.kuleuven.be/~dirk.nuyens/qmc-generators/) says it mirrors those matrices (nxmats.tgz). Check both before claiming p2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mint-ts-sequences-small-gaps.md
```

Already set up? Say `run V3R1T4S on mint-ts-sequences-small-gaps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mint-ts-sequences-small-gaps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
