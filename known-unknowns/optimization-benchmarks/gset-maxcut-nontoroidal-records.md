# Gset Max-Cut: a larger cut than the best published for a non-toroidal Gset graph (G60 14190, G61 5799, G63 27047, G64 8753, G70 9595, ...)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (GPU or many-core local search on graphs of 800 to 10,000 vertices; checking a cut takes milliseconds) · open as of 2026-10-30

## The problem

Gset (C. Helmberg and F. Rendl, generated with G. Rinaldi's rudy; hosted by Yinyu Ye at Stanford) has 71 Max-Cut graphs with 800 to 20,000 vertices: random graphs, 'planar' graphs (unions of two planar graphs, not themselves planar) and toroidal grids, with +1 or +-1 weights. It is still the main heuristic Max-Cut benchmark. Its records come from breakout local search (Benlic and Hao 2013), global equilibrium search teams (Shylo, Glover and Sergienko 2015), MOH (Ma and Hao 2017), the large-population island algorithm (Goudet, Goeffon and Hao, Comput. Oper. Res. 168, 2024), population annealing (Khan and Shukla, arXiv:2510.21105, Oct 2025: G63 27047, the first gain over 27045 in about ten years) and Cosm (Zick, Shukla and Marakov, arXiv:2605.30355v4, 11 Oct 2026). Cosm set a new G64 record of 8753 (previous 8752) and reached the best-known 14190 (G60), 5799 (G61) and 9595 (G70). The toroidal graphs are closed. Ikuta, Imai and Yano (RIMS Kokyuroku 1941, 2015, in Japanese) solved every toroidal instance with up to 10,000 vertices to optimality with CPLEX 12.6, all except G77 and G81. Cosm reports Gurobi certificates for G72, G77 and G81 (G81 = 14060). Glass and Feder (arXiv:2606.28478, Jun 2026) obtain planar-relaxation upper bounds matching the known cuts of G11, G48, G49, G57, G65, G72, G77 and G81, and a new matching 4872 for G62; their bounds leave small gaps elsewhere (e.g. G66 6364 vs 6366, G67 6950 vs 6952), but those instances were already solved in 2015. The random and two-planar instances have no published upper bounds near their records.

## What counts as a win

A +-1 (or 0/1) assignment to the vertices of a Gset graph that is not toroidal (not G11-G13, G32-G34, G48-G50, G57, G62, G65-G67, G72, G77 or G81), whose cut value sum_{ij in E, x_i != x_j} w_ij, recomputed from the Stanford Gset file, is STRICTLY GREATER (direction: max) than the highest cut published for that graph at claim time. Bars confirmed on 2026-10-30: G60 14190, G61 5799, G63 27047, G64 8753, G70 9595. For every other instance the bar is the maximum over the BLS, GES, MOH and Goudet et al. 2024 tables, Cosm (arXiv:2605.30355v4), Khan and Shukla (arXiv:2510.21105) and any later publication found by a literature search.

## How a win is checked

Download the graph from https://web.stanford.edu/~yyye/yyye/Gset/ (first line n m; then lines i j w, 1-based). Read the partition (one label per vertex), check it has exactly n entries, and recompute the cut in integers. This takes milliseconds. Reproduce the bar by re-reading the cited tables (Cosm Supplementary Table S5 gives G60/G61/G64/G70/G72/G77/G81), and search for anything newer before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2605.30355>

## Sources

- <https://web.stanford.edu/~yyye/yyye/Gset/>
- <https://arxiv.org/abs/2605.30355>
- <https://arxiv.org/abs/2510.21105>
- <https://arxiv.org/abs/2606.28478>
- <https://arxiv.org/abs/2505.18508>
- <https://leria-info.univ-angers.fr/~jinkao.hao/BLS_max_cut.html>
- <https://doi.org/10.1016/j.cor.2024.106684>
- <https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1941-09.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Physics heuristics dominate the recent records: population annealing with non-local moves (G63), switched collective dynamics (Cosm), parallel tempering. Run them long and wide on a GPU.
- Memetic search with large populations and backbone-preserving crossover (Goudet et al. 2024) produced six records; combine it with the strongest one-flip/two-flip tabu as the local improver.
- G64 has a very heterogeneous degree distribution (maximum degree 589). Treat hub vertices as a small exact subproblem (enumerate or branch on hubs, optimise the rest by local search).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- There is no single maintained Gset leaderboard; best-known values are scattered across papers and some tables lag (e.g. GES tables list G70 at 9591 and MOH at 9544, against 9595). Always compare with the maximum over all sources.
- Toroidal instances are solved: CPLEX optimality for all up to 10,000 vertices (Ikuta et al. 2015), Gurobi certificates for G72, G77 and G81 (Cosm), and matching planar bounds (Glass and Feder 2026). A 'record' there is a bug.
- G81 and other +-1-weight graphs: the cut is a signed sum, not a count of crossing edges; Ising energy and cut differ by an affine map. Recompute the cut from the edge list.
- QPLIB contains some Max-Cut instances under other names; this entry is only for the Gset files.
- Ikuta et al. 2015 (RIMS Kokyuroku 1941, pp. 49-56) is in Japanese and tabulates CPLEX lower and upper bounds for all Gset graphs; include it when compiling bars and when checking whether a two-planar instance is already proved optimal.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/gset-maxcut-nontoroidal-records.md
```

Already set up? Say `run V3R1T4S on gset-maxcut-nontoroidal-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gset-maxcut-nontoroidal-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
