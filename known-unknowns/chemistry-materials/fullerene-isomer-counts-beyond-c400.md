# Fullerene isomer counts: the number of fullerenes (OEIS A007894) or IPR fullerenes (A046880) with 402 carbon atoms or more

⚗️ **Chemistry and materials** · standard · tractability ★★☆☆☆ · compute: laptop-days via the published oriented-count formula plus a symmetry-restricted count of the (under a million) achiral C402 fullerenes; needs cluster for brute-force generation (about 1.3e11 fullerenes, 2.6e11 oriented, at C400 alone) · open as of 2026-10-30

## The problem

A fullerene C_2n is a cubic plane graph whose faces are pentagons and hexagons; IPR fullerenes have no two adjacent pentagons. In A007894 and A046880 enantiomers are counted once. Gunnar Brinkmann, Jan Goedgebeur and Brendan McKay counted all fullerenes up to 400 vertices with buckygen (J. Chem. Inf. Model. 52, 2910, 2012; arXiv:1207.7010). Goedgebeur and McKay counted all IPR fullerenes up to 400 vertices with a recursive IPR generator (J. Math. Chem. 53, 1702, 2015; arXiv:1501.02680). Goedgebeur's OEIS b-files end at n = 200 (C400): A007894(200) = 132,247,999,328 and A046880(200) = 40,286,153,024. The A007894 page notes that a(10)..a(190) were confirmed independently by buckygen and fullgen, while a(191)..a(200) come from buckygen only. The counting picture changed with Philip Engel and Peter Smillie, with an appendix by Goedgebeur (Exact enumeration of fullerenes, Duke Math. J. 174, 575-613, 2025; arXiv:2304.01655). Building on Thurston's Eisenstein-lattice parametrisation, they give an exact formula, a linear combination of Eisenstein series, for the number of ORIENTED fullerenes (mirror images counted separately, OEIS A057210) at every n; for example, there are 1,203,397,779,055,806,181,762,759 oriented fullerenes with 10,000 vertices. The coefficients were fixed by solving a linear system with the first 200 oriented counts from a buckygen run (about 3 CPU years). The authors leave unoriented counts to future work, and the formula does not cover IPR fullerenes. Since A007894(n) = (A057210(n) + achiral(n))/2, where achiral(n) is the number of fullerenes with an orientation-reversing automorphism (839,622 at C400, from the two b-files), A007894(201) now reduces to two steps: evaluate the published formula at n = 201 and count under a million achiral C402 fullerenes. That replaces generating about 1.3e11 fullerenes. No term beyond 400 vertices appears on A007894 (last edited 2026-06-28), A046880 (2025-11-05), A057210 (b-file to n = 200, edited 2026-08-08) or the buckygen page (last updated 2012), checked 2026-10-30.

## What counts as a win

The exact value A007894(201) (fullerenes C402) or A046880(201) (IPR fullerenes C402), or a later term, with released code and per-size counts for every n from the sequence offset up to the claimed index. The released counts must equal the live b-file exactly for every n <= 200, re-fetched immediately before claiming; the generation or counting run must reproduce them, not copy them. The new term must be confirmed by an independent computation: either a second implementation of a different algorithm, or a skeptic re-run of the same code split into residue classes on separate machines, agreeing exactly. A claim that uses the Engel-Goedgebeur-Smillie oriented-count formula has three further requirements. The skeptic must evaluate that formula independently from the published paper at every n used. The formula values must reproduce the A057210 b-file for n <= 200. The achiral count at the new size must be confirmed as above. A value of A057210 alone is not a win, since the published formula already determines it. The term must be absent from the live OEIS entry and from the literature the skeptic finds (direction: first to report).

## Partial wins

- **p1:** Independent confirmation of A007894(191)..A007894(200) (all ten values, exactly matching the b-file) by a program that does not share code with buckygen and does not rely on buckygen-derived counts. The oriented-count formula was fitted to buckygen output, so formula-based values do not count as independent here.
- **p2:** The exact number of achiral fullerenes (those with an orientation-reversing automorphism, equal to 2*A007894(n) - A057210(n)) for every n from 10 to 200. It must be computed by a released method that does not generate all fullerenes, must match the two b-files exactly, and must finish within 24 hours when the skeptic re-runs it on one laptop.

## How a win is checked

Diff the claimed per-size table against https://oeis.org/A007894/b007894.txt and https://oeis.org/A046880/b046880.txt; rerun the released code on a few sizes (n <= 60) and on a random subset of residue classes at the new size; for a generation-based claim, check canonical-form deduplication on a sample with an independent graph-isomorphism tool (e.g. nauty) and check face sizes (12 pentagons) and the IPR condition.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A007894>

## Sources

- <https://oeis.org/A007894>
- <https://oeis.org/A046880>
- <https://oeis.org/A057210>
- <https://oeis.org/A007894/b007894.txt>
- <https://oeis.org/A046880/b046880.txt>
- <https://oeis.org/A057210/b057210.txt>
- <https://arxiv.org/abs/2304.01655>
- <https://caagt.ugent.be/buckygen/>
- <https://arxiv.org/abs/1207.7010>
- <https://arxiv.org/abs/1501.02680>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Index n is half the vertex count (A007894 offset 10 means C20); A046880 starts at n = 30 (C60).
- Enantiomorphic pairs count as one in A007894 and A046880; the Engel-Goedgebeur-Smillie formula counts them twice (A057210), so it must be combined with an achiral count, not used directly.
- fullgen had a programming error for 136 vertices and more (found by the buckygen authors, since fixed); old fullgen output is not an independent check there.
- The oriented-count formula's coefficients were solved from buckygen counts up to C400 (152 unknowns, 200 equations); it is strong evidence but not independent of buckygen for n <= 200.
- An achiral-only generator must catch every orientation-reversing symmetry (mirror planes, inversion and improper rotations S4, S6, ...), not only mirror planes; check it against 2*A007894(n) - A057210(n) for all n <= 200 first.
- A046880(191..200) may already have been checked by the 2015 IPR generator, which is a different algorithm; that is why p1 names A007894 only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/fullerene-isomer-counts-beyond-c400.md
```

Already set up? Say `run V3R1T4S on fullerene-isomer-counts-beyond-c400`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fullerene-isomer-counts-beyond-c400`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
