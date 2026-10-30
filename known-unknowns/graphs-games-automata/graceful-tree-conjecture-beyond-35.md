# MOONSHOT - Graceful tree (Ringel-Kotzig) conjecture: a tree with no graceful labeling, a formal proof, or the first verification past Fang's 35 vertices

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (about 6.2e12 trees on 36 vertices) · open as of 2026-10-30

## The problem

The graceful tree conjecture (Ringel, Kotzig, Rosa 1960s): every tree with q edges has an injective vertex labeling into {0..q} whose edge differences are exactly 1..q. It implies Ringel's conjecture that K_{2n+1} decomposes into copies of any tree with n edges (proved only for large n by Montgomery, Pokrovskiy and Sudakov and by Keevash and Staden) and Kotzig's cyclic-decomposition conjecture. Wenjie Fang (arXiv 1003.3045, 2010) verified it for every tree with at most 35 vertices (2,262,366,343,746 trees at n = 35). Brinkmann, Crevals, Melot, Rylands and Steffen (DMTCS 14, 2012) computed alpha-deficits of all trees with maximum degree 3 up to 36 vertices: none on 36 vertices is deficitary, so all of them have alpha-labelings and are graceful; most, not all, trees on 37 vertices were tested. Gallian's Dynamic Survey DS6 (28th ed., 30 Oct 2025, Section 2.1) says the conjecture 'remains open even for trees with maximum degree 3' and records no verification beyond 35. Claimed proofs by Edinah Gnang (arXiv 1811.07614; arXiv 2202.03178, v3 31 Jan 2025) and J. Keen (Zenodo 2026, abstract redacted) are unrefereed and not accepted; a July 2026 ResearchGate preprint by P. Pajo titled as a verification at n = 36 could not be read (403) and is unconfirmed. Credit: Ringel, Kotzig, Rosa; Fang; Brinkmann et al.; Gallian.

## What counts as a win

Success means EITHER (a) a tree T with no graceful labeling, certified by two independent exhaustive methods (for example a SAT encoding with an UNSAT proof in DRAT/LRAT checked by drat-trim or cake_lpr, plus an independent backtracking search); necessarily T has at least 36 vertices; OR (b) a complete machine-checked proof (Lean 4 with Mathlib, Isabelle or Coq) of 'every finite tree has a graceful labeling', with the formal statement reviewed to match the standard definition and no sorry or extra axioms. Gnang's arguments count only if formalised as in (b).

## Partial wins

- **p1:** Verification that every tree on 36 vertices (6,226,306,037,178 trees, OEIS A000055) is graceful: released deterministic code that generates all trees (count checked against A000055) and passes each emitted labeling through an independent checker, with logs, reproduced by a skeptic on a random sample of at least 1% of the generation shards plus the shard totals, and no earlier complete, checkable verification of n = 36 found at claim time.
- **p2:** The same standard of verification for every tree with maximum degree at most 3 on 37 and on 38 vertices (59,574,334,817 and 138,533,927,938 trees, OEIS A000672); n = 36 and below is already covered by Brinkmann et al. (2012) and Fang (2010).

## How a win is checked

(a) Check the proof certificate and rebuild the CNF independently; confirm T is a tree. (b) Compile the formal proof, print axioms, review the statement. Partial wins: rerun the released generator and checker on random shards, compare shard counts and the total with A000055 (or A000672), and validate each sampled labeling with an independent checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://arxiv.org/abs/1003.3045>
- <https://dmtcs.episciences.org/569/pdf>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://arxiv.org/abs/2202.03178>
- <https://oeis.org/A000055>
- <https://oeis.org/A000672>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fang's probabilistic backtracking plus Horton's ideas; most trees fall instantly, so the cost is generation (WROM / gentreeg) and the rare hard trees.
- Use known theorems (caterpillars, lobsters with perfect matchings, trees with alpha-labelings) only as a filter whose correctness is proven, never as an unchecked skip.
- For a counterexample hunt, search trees with few graceful labelings (Anick's statistics point to particular caterpillar-like families).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Gnang's and Keen's proofs are unrefereed claims; citing them is not a win.
- Proving a tree has no graceful labeling needs a certified exhaustive search, not a timeout.
- Ringel's packing conjecture and Kotzig's rho-labeling conjecture are weaker consequences; a verification of those alone is not a win here.
- Trees with maximum degree 3 on at most 36 vertices are already done (Brinkmann et al. 2012 via alpha-labelings); do not claim them.
- Pajo's 2026 ResearchGate preprint on n = 36 returned 403 when this entry was checked; read it honestly if accessible before claiming p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/graceful-tree-conjecture-beyond-35.md
```

Already set up? Say `run V3R1T4S on graceful-tree-conjecture-beyond-35`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `graceful-tree-conjecture-beyond-35`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
