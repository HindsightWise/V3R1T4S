# Super edge-magic tree conjecture (Enomoto-Llado-Nakamigawa-Ringel): extend the verification past 17 vertices, or a tree that is not super edge-magic

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (18-22 vertices); laptop-days to 25 vertices · open as of 2026-10-30

## The problem

An edge-magic total labeling of a graph with p vertices and q edges is a bijection from V and E to {1..p+q} with f(u)+f(uv)+f(v) constant over all edges; it is super edge-magic if the vertices get {1..p}. Equivalently (Figueroa-Centeno, Ichishima and Muntaner-Batle) a graph is super edge-magic iff there is a bijection f: V -> {1..p} whose edge sums f(u)+f(v) form q consecutive integers. Enomoto, Llado, Nakamigawa and Ringel (SUT J. Math. 34, 1998) conjectured that every tree is super edge-magic (which implies the Kotzig-Rosa conjecture that every tree is edge-magic total). S. M. Lee and Q. X. Shan verified it by computer for all trees with at most 17 vertices (MCCCC 2002); Fukuchi and Oshima proved it for trees of order n with diameter at least n-5. Gallian's Dynamic Survey DS6 (28th ed., 30 Oct 2025, Section 5.2) still gives 17 vertices as the verification bound. Tree counts (OEIS A000055): 123,867 on 18 vertices, 823,065 on 20, 5,623,756 on 22, 104,636,890 on 25. Credit: Enomoto, Llado, Nakamigawa, Ringel; Lee and Shan; Fukuchi and Oshima; Gallian.

## What counts as a win

Success means EITHER (a) a certificate that every tree on at most 25 vertices is super edge-magic: for each n in 18..25, a file giving every unlabeled tree on n vertices (as from nauty gentreeg) with a bijection to {1..n} whose n-1 edge sums are consecutive integers, where an independent checker regenerates the trees, confirms the counts equal A000055(n), matches every tree by canonical form and checks each labeling; OR (b) a tree with no super edge-magic labeling, certified by two independent exhaustive methods (for example SAT with a DRAT/LRAT UNSAT proof plus an independent search). Before claiming, re-check the latest DS6 edition and the literature for a higher verification bound; orders already covered do not count.

## Partial wins

- **p1:** Certificate (as in (a)) that every tree on at most 20 vertices is super edge-magic.
- **p2:** Certificate that every tree on at most 22 vertices is super edge-magic.

## How a win is checked

Regenerate trees with gentreeg n, compare counts with A000055, canonically label and match certificate entries, and for each labeling check it is a bijection onto {1..n} and that the sorted edge sums are consecutive. Minutes per order up to 22; about an hour at 25.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://oeis.org/A000055>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the consecutive-edge-sum reformulation: a much smaller search than total labelings.
- Every tree with an alpha-labeling is super edge-magic (DS6 Section 5.2; with threshold k, map lower labels l to k+1-l and upper labels u to u+1). Brinkmann, Crevals, Melot, Rylands and Steffen (DMTCS 14, 2012, https://dmtcs.episciences.org/569/pdf) tabulate the alpha-deficit of all trees up to 26 vertices, so label every tree via a fast alpha-labeling search and spend exact search only on the deficitary residue.
- Caterpillars are super edge-magic by construction; label everything else with CP-SAT or randomized backtracking seeded from a caterpillar spine.
- Record the hardest trees per order; they are the natural place to look for a counterexample.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Super edge-magic requires vertex labels exactly {1..p}; an edge-magic total labeling with other vertex labels does not count.
- The 17-vertex bound comes from a 2002 conference talk cited in DS6; a later unpublished extension may exist, so search before claiming.
- Certificates must cover every isomorphism class; check the count against A000055.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/super-edge-magic-trees-beyond-17.md
```

Already set up? Say `run V3R1T4S on super-edge-magic-trees-beyond-17`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `super-edge-magic-trees-beyond-17`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
