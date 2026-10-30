# Small Steiner 3-designs: construct S(3,5,41), S(3,6,46) or S(3,5,50), the open cases with v <= 50

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (Kramer-Mesner with prescribed automorphism groups; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Steiner system S(3,k,v) is a family of k-subsets of a v-set covering every 3-subset exactly once. Kiermaier, Krčadinac and Wassermann (arXiv:2509.23483, 27 Sep 2025) tabulate the 25 admissible parameter sets with v <= 50: 20 were known, S(3,7,37) does not exist (there is no inversive plane of order 6), and 4 were open. They constructed S(3,6,42) by extending Steiner 2-designs with prescribed extension groups, and tried the other three, S(3,6,46), S(3,5,41) and S(3,5,50), without success, finding many new derived designs S(2,5,45), S(2,4,40) and S(2,4,49) instead. Krčadinac's live table (web.math.pmf.unizg.hr/~krcko/results/steiner3.html, data set on Zenodo) still marks these three '?'. The same paper constructed rotational Steiner quadruple systems RoSQS(46) and RoSQS(92), leaving v = 56, 70, 82, 86 and 98 open below 100 in Ji and Zhu's table, and notes that v = 94 is the only open order below 100 for cyclic SQS. Liu and Feng (arXiv:2610.25951, 19 Oct 2026) settled the symmetric cyclic case, which does not reach 94 = 2*47 because 47 = 11 mod 12.

## What counts as a win

Success means an explicit S(3,5,41) (1066 blocks of size 5 on 41 points), S(3,6,46) (759 blocks of size 6 on 46 points) or S(3,5,50) (1960 blocks of size 5 on 50 points) with every 3-subset of the point set in exactly one block, checked exhaustively by two independent programs, where Krčadinac's table (re-fetched) still marks the case '?' and a fresh arXiv search finds no construction (direction: none; existence target). A rigorous nonexistence proof (DRAT/LRAT on a regenerated CNF, or an exhaustive search the skeptic re-runs) also counts.

## Partial wins

- **p1:** A cyclic Steiner quadruple system CSQS(94): blocks of size 4 on Z_94 with every 3-subset in exactly one block and the block set invariant under x -> x + 1.
- **p2:** A rotational Steiner quadruple system RoSQS(v) for v in {56, 70, 82, 86, 98}: an SQS(v) on Z_(v-1) plus one fixed point whose block set is invariant under x -> x + 1 (fixing the extra point).

## How a win is checked

Read the blocks, check sizes and the block count C(v,3)/C(k,3), index every 3-subset by its combinatorial rank and require each to be covered exactly once. For p1 and p2 also apply the claimed automorphism to every block and check that the block set is unchanged. Use two independent checkers; then re-fetch the table and search arXiv.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~krcko/results/steiner3.html>

## Sources

- <https://web.math.pmf.unizg.hr/~krcko/results/steiner3.html>
- <https://arxiv.org/abs/2509.23483>
- <https://arxiv.org/abs/2610.25951>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend the derived design: the blocks through one point of an S(3,k,v) form an S(2,k-1,v-1). The authors publish 10791 S(2,4,40), 1072 S(2,5,45) and 22080 S(2,4,49) used in their extension attempts; try extension groups they did not.
- Kramer-Mesner with a prescribed group G: the design is a union of G-orbits of k-sets covering each G-orbit of 3-sets once; solve the 0/1 system with an exact-cover, SAT or ILP solver (the authors' GAP package Prescribed Automorphism Groups implements the method).
- For CSQS(94) and RoSQS(v), the cyclic structure reduces the problem to choosing base blocks that cover each orbit of triples once, a moderate exact cover for modern SAT solvers.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- S(3,6,42), RoSQS(46) and RoSQS(92) are already constructed; S(3,7,37) does not exist.
- A CSQS(94) cannot be symmetric: Liu and Feng (arXiv:2610.25951) prove the Grannell-Griggs criterion as an iff, and 94 = 2*47 with 47 = 11 mod 12 fails it, so searches that assume the multiplier -1 fixes every block orbit are provably empty.
- Admissibility of S(3,k,v) needs C(v-i,3-i)/C(k-i,3-i) integral for i = 0, 1, 2; recheck before moving to other parameters.
- Check all C(v,3) triples, not only those through a fixed point.
- Design files from the web page and Zenodo are data in GAP format; parse them, never run them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/small-steiner-3-designs-open.md
```

Already set up? Say `run V3R1T4S on small-steiner-3-designs-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `small-steiner-3-designs-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
