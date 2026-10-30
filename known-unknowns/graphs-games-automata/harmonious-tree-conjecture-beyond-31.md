# MOONSHOT - Graham-Sloane harmonious tree conjecture: a tree that is not harmonious, a formal proof, or the first verification past Fang's 31 vertices

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster (about 4.7e13 trees on 38 vertices) · open as of 2026-10-30

## The problem

Graham and Sloane (SIAM J. Alg. Discrete Methods 1, 1980) conjectured that every tree is harmonious: for a tree with q edges (q+1 vertices) there is a labeling f: V -> Z_q, injective except that exactly one label is used twice, such that the edge sums f(u)+f(v) mod q are pairwise distinct. Aldred and McKay verified it for trees with at most 26 vertices; Wenjie Fang (arXiv 1106.3490, v2 2012) published a verification for all trees with at most 31 vertices (40,330,829,030 trees at n = 31). Fang's code then ran on the volunteer project yoyo@home, whose Harmonious Trees status page (fetched 2026-10-30) shows the series for 32 to 37 nodes as completed, with no published write-up or certificates. Montgomery, Pokrovskiy and Sudakov proved every tree is almost-harmonious (any abelian group of order n + o(n)); Muyesser and Pokrovskiy (arXiv 2509.05280, v2 6 Oct 2025) confirm the Graham-Sloane conjecture for bounded-degree trees on sufficiently many vertices (their Theorem 1.5: for each maximum degree Delta, all n at least an inexplicit n0(Delta)). Gallian's Dynamic Survey DS6 (28th ed., 30 Oct 2025) still lists the conjecture as open; Gnang and Williams posted a claimed proof (arXiv 2201.02240, v1 only, no journal reference). Credit: Graham, Sloane; Aldred, McKay; Fang and the yoyo@home volunteers; Montgomery, Pokrovskiy, Sudakov; Muyesser, Pokrovskiy; Gallian.

## What counts as a win

Success means EITHER (a) a tree with no harmonious labeling, certified by two independent exhaustive methods (for example SAT with a DRAT/LRAT UNSAT proof checked by drat-trim or cake_lpr plus an independent search); by Fang's published result it has at least 32 vertices (very likely at least 38, given the completed yoyo@home series), and by Muyesser-Pokrovskiy a tree of maximum degree Delta can be a counterexample only below their inexplicit threshold n0(Delta), so their theorem rules out no specific small tree; OR (b) a complete machine-checked proof (Lean 4/Mathlib, Isabelle or Coq) that every finite tree with at least 2 vertices is harmonious, with the formal statement reviewed and no sorry or extra axioms.

## Partial wins

- **p1:** Verification that every tree on 38 vertices (47,436,313,524,262 trees, OEIS A000055) is harmonious: released generator and labeler, independent checker on every emitted labeling, total checked against A000055, and a skeptic rerun of at least 1% of shards. Orders 32 to 37 do not count (yoyo@home series completed).

## How a win is checked

(a) Check the certificate and re-derive the encoding; (b) compile and audit the formal statement and axioms. Partial win: rerun random shards, compare counts with A000055(38), and check sampled labelings (one repeated label, all q sums distinct mod q) with an independent program.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://arxiv.org/abs/1106.3490>
- <http://www.rechenkraft.net/yoyo/y_status_hat.php>
- <https://arxiv.org/abs/2509.05280>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://arxiv.org/abs/2201.02240>
- <https://oeis.org/A000055>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fang's hybrid of probabilistic backtracking, tabu search and constraint programming; reuse labelings across trees that differ by moving one leaf.
- Caterpillars are harmonious (Graham-Sloane); filter only with proven theorems.
- A counterexample search should focus on trees whose harmonious labelings are rare in exhaustive counts for small n.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The tree definition allows exactly one repeated vertex label; injective labelings are impossible for trees since there are q+1 vertices and q residues.
- The Gnang-Williams arXiv proof is an unrefereed claim.
- Do not confuse harmonious with graceful labelings or with the 'almost-harmonious' theorem.
- Every tree with an alpha-labeling is harmonious, so a counterexample must have no alpha-labeling.
- The yoyo@home page shows completed workunits for 32-37 nodes but no stated outcome; treat those orders as done, not as open.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/harmonious-tree-conjecture-beyond-31.md
```

Already set up? Say `run V3R1T4S on harmonious-tree-conjecture-beyond-31`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `harmonious-tree-conjecture-beyond-31`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
