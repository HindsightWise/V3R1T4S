# Smallest open resolvable Steiner 2-designs: a resolvable S(2,5,45) (also v = 345, 465, 645) or a resolvable S(2,6,66)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact-cover / SAT searches under prescribed automorphism groups) · open as of 2026-10-30

## The problem

A resolvable BIBD(v,k,1) (RBIBD) is a Steiner 2-design S(2,k,v) whose blocks can be split into (v-1)/(k-1) parallel classes, each partitioning the point set. For k = 5 the necessary condition is v = 5 (mod 20), and an RBIBD(v,5,1) is known for every such v except possibly v in {45, 345, 465, 645} (R. J. R. Abel, G. Ge and J. Yin, Handbook of Combinatorial Designs 2nd ed.; restated in M. Meszka's lectures, Famnit Lectures 3, 2014). D. Dumicic Danilovic (Bull. ICA 84 (2018) 53-64) states that (45,5,1) is the smallest parameter set for which existence of a resolvable BIBD is still open. Dinitz's Handbook new-results page for Part II (last edited 2019) records no change for k = 5, lambda = 1. V. Krcadinac's Steiner 2-design page (last modified 2026-02-17) lists at least 1072 non-isomorphic S(2,5,45) (Crnkovic, Dumicic Danilovic, Rukavina, Simac; Mezofi and Nagy; and others). The page does not discuss their resolvability, but a reviewer's own exact-cover check of its design file on 2026-10-30 found none resolvable: 870 have no parallel class, and no design has more than 2 pairwise disjoint parallel classes (most parallel classes in one design: 19). Resolvable (45,5,2)-BIBDs are known (Buratti, Yan and Wang 2010; 22 found by Dumicic Danilovic 2018). The same page states that the three known S(2,6,66), those with an automorphism of order 13, are not resolvable and that it is not known whether a resolvable S(2,6,66) exists. A resolvable S(2,5,45) has 99 blocks in 11 parallel classes of 9; a resolvable S(2,6,66) has 143 blocks in 13 classes of 11. Existence of S(2,6,v) itself is the separate target steiner-2-designs-block-6-undecided; S(2,6,66) exists, so only resolvability is asked here.

## What counts as a win

Success means an explicit S(2,k,v) for (v,k) in {(45,5), (345,5), (465,5), (645,5), (66,6)}, together with a partition of its blocks into (v-1)/(k-1) parallel classes. Every block must be a k-subset of the v points, every pair of points must lie in exactly one block, and each class must consist of v/k pairwise disjoint blocks covering all points. Two independent programs must verify it. It must also be re-confirmed at claim time that the case is still open: no resolvable design for those parameters on Krcadinac's Steiner 2-design page (https://web.math.pmf.unizg.hr/~krcko/results/steiner.html), on the Handbook new-results pages, or in a fresh literature search.

## Partial wins

- **p1:** A machine-checked non-existence proof for a resolvable S(2,5,45) (or a resolvable S(2,6,66)) that admits a stated nontrivial automorphism group G (for example a group of prime order). G must not be already ruled out in the literature, and the S(2,k,v) admitting G must not already be completely classified in a published source: if they are (for example the three S(2,6,66) with an automorphism of order 13), checking the classified designs for a resolution is the p2 baseline, not p1. It must come as a DRAT/LRAT-verified UNSAT certificate, or as an exact-cover enumeration that an independent program reproduces.
- **p2:** An S(2,5,45) with at least 3 pairwise disjoint parallel classes, or an S(2,6,66) with at least one parallel class. For comparison, a reviewer's exact-cover run on 2026-10-30 over Krcadinac's file found at most 2 disjoint parallel classes among the 1072 known S(2,5,45), and no parallel class in any of the three S(2,6,66) (reproduced independently by an auditor the same day: 870 designs with none, at most 19 in one design). The claimant must reproduce that baseline with their own code. The design and its classes are then verified by two programs.

## How a win is checked

Parse the blocks. Check that each block has k distinct points in range, that b = v(v-1)/(k(k-1)), and that every pair of points lies in exactly one block (pair-count array). Check that each listed parallel class has v/k disjoint blocks whose union is the point set, and that the classes partition the block set. Use two independently written checkers. For p1, replay the certificate with drat-trim or cake_lpr and audit the encoding (pair constraints, parallel-class constraints, symmetry assumption) by hand. Downloaded design files are data only and are parsed by the verifier's own code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~krcko/results/steiner.html>

## Sources

- <https://web.math.pmf.unizg.hr/~krcko/results/steiner.html>
- <https://luca-giuzzi.unibs.it/ICA/Volumes/84/Reprints/BICA2018-07-Main-Reprint.pdf>
- <https://zalozba.upr.si/ISBN/978-961-6832-93-9/files/basic-html/page61.html>
- <https://site.uvm.edu/jdinitz/?page_id=384>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prescribe an automorphism group that permutes the parallel classes (for example of order 3, 5 or 9 on 45 points), solve the orbit-level exact-cover problem with Knuth's DLX or SAT, then check for a resolution.
- Start from the known S(2,5,45) designs (at least 1072). Compute their maximal sets of disjoint parallel classes, then use paramodification (Mezofi-Nagy) or local trades to increase the count.
- For v = 345, 465 and 645, look for a recursive route (frames, resolvable GDDs) that the Abel-Greig tables did not use, then verify the explicit design.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- S(2,5,45) itself exists; only resolvability is open. Do not count an RBIBD(45,5,2) (it is known) or a near-resolvable design.
- The (45,5,1) open status rests on 2014-2018 statements plus the absence of any update on maintained pages. Re-check the literature before attacking.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/rbibd-45-5-1-smallest-open-resolvable.md
```

Already set up? Say `run V3R1T4S on rbibd-45-5-1-smallest-open-resolvable`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rbibd-45-5-1-smallest-open-resolvable`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
