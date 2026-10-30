# Small hypergraph Ramsey numbers: beat R(4,5;3) >= 35, R(4,6;3) >= 63, R(5,5;3) >= 88, R(4,4,4;3) >= 79 or R(5,5;4) >= 35, or settle R(K4-t,K5;3) in 14-16

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (cyclic or SAT colourings of triples on 35-90 points; checking needs at most C(89,5) ~ 4.2e7 subsets) · open as of 2026-10-30

## The problem

R(s,t;3) is the least N such that every red/blue colouring of the triples of an N-set contains s points with all triples red or t points with all triples blue (similarly for 4-uniform and three colours). The only known nontrivial value is R(4,4;3) = 13 (McKay-Radziszowski 1991). DS1 revision #18 (Apr 2026) Section 7.1 lists the lower bounds R(4,5;3) >= 35 (Dybizbanski 2018), R(4,6;3) >= 63, R(5,5;3) >= 88, R(4,4,4;3) >= 79 (Dybizbanski's addendum, cyclic colourings), R(5,5;4) >= 35 (Exoo 2021), and 14 <= R(K4-t,K5;3) <= 16 (Exoo; Lidicky-Pfender), where K4-t is K4^(3) minus one triple. Dybizbanski's page notes that only cyclic colourings were searched and no negative results exist. No 2026 arXiv paper found improves these small cells (recent work is asymptotic: Conlon-He-Nie-Post, Gishboliner-Hajebi-Li). Credit: Dybizbanski, Exoo, McKay-Radziszowski, Lidicky-Pfender, Budden-Hiller-Rosenberg.

## What counts as a win

An explicit colouring of all r-subsets (r = 3 or 4) of {0..N-1} (a file listing each subset and colour, or a rule plus the expanded file) such that no s-set is monochromatic in colour 1 and no t-set in colour 2 (no u-set in colour 3 for R(4,4,4;3)), verified by exhaustive enumeration of all s-, t- and u-subsets with two independent programs, with N+1 STRICTLY GREATER (direction: max) than the lower bound in the live DS1, Dybizbanski's page and any newer paper. Off-by-one: a colouring on N points proves R >= N+1.

## Partial wins

- **p1:** R(K4-t,K5;3) improved: a verified colouring of the triples of a 14-point set with no red K4-t and no blue K5^(3) (giving >= 15), or a certified (DRAT/LRAT or exact flag-algebra) proof that R(K4-t,K5;3) <= 15.
- **p2:** A new lower bound for R(4,7;3) or R(5,6;3), witnessed by an explicit verified colouring. It must be strictly above every value stated for that number in DS1 or any newer paper, and above the trivial bounds R(4,7;3) >= 64 and R(5,6;3) >= 89 (from adding one point whose triples all get colour 2). The claim must state the comparison value and its source. Multicolour numbers with a 5 in the last colour, such as R(4,4,5;3), do not count: the lexicographic product behind DS1 7.1.a (Bruce-Budden-Hiller) already gives R(4,4,5;3) >= (13-1)^2+1 = 145.

## How a win is checked

Load the colouring into a dictionary keyed by sorted r-tuples and check it covers all C(N,r) subsets exactly once. For each s-subset test whether all its r-subsets are colour 1 (and likewise for t, u); use itertools in one implementation and a bitmask/numba sweep in another. For cyclic colourings also verify the expanded file, not only the orbit representatives.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://inf.ug.edu.pl/ramsey>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://inf.ug.edu.pl/ramsey>
- <https://arxiv.org/abs/1704.03592>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Go beyond cyclic symmetry: colourings invariant under x -> x+d and x -> -x, or under an affine group AGL(1,p), then SAT over orbit colours.
- Seed from Dybizbanski's published 34-point colouring (colouring.txt on his page) and run SAT on a one-point extension.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not run downloaded verifier code (verif.cpp); write your own checker.
- Bounds derived by recurrences in DS1 7.1.f (e.g. R(5,6;4) >= 67) are not explicit colourings; p2 needs an explicit object.
- Lexicographic products (Bruce-Budden-Hiller, DS1 7.1.a) give R(s,t,5;3) >= (R(s,t;3)-1)^2+1 for free. Compare any multicolour claim against these implied bounds, not only against printed values.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hypergraph-ramsey-small-lower-bounds.md
```

Already set up? Say `run V3R1T4S on hypergraph-ramsey-small-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypergraph-ramsey-small-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
