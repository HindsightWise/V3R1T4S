# Gset Max-k-Cut (k = 3, 4): a better k-partition than the best published for a Gset graph

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (local search on graphs of 800 to 20,000 vertices; checking a partition takes milliseconds) · open as of 2026-10-30

## The problem

Max-k-Cut asks for a partition of the vertices into k parts that maximises the total weight of edges joining different parts; on Gset it is benchmarked mainly for k = 3 and 4. Ma and Hao's multiple search operator heuristic (MOH, Ann. Oper. Res. 248, 2017) tabulated k = 2, 3, 4 and 8 on Gset. In 2026 three works raised several bars: Garvardt, Gruettemeier, Komusiewicz and Morawietz (Parameterized local search for Max c-Cut, Ann. Oper. Res., 2026); Shao and Yang's PEAF (J. Intell. Algorithms Sci. Comput., 2026; arXiv:2607.17158); and Khan, Redding and Shukla's population-dynamics method (PAMC, arXiv:2606.25203). Shao and Wu (East Asian J. Appl. Math. 15, 2025) report a Gurobi value of 16670 for G81 with k = 4. Yaocheng Chen's certificate release (github.com/yaochengchen/gset-maxkcut_by_PdSB, v2.0.0, 15 Oct 2026) publishes explicit partitions with verifiers. It improves G81 k=3 to 16510, G22 k=4 to 18787 and G55 k=3 to 12437 (re-checked for this entry from the Stanford G55 file). It matches G1-G5 at k=3 (15165, 15172, 15173, 15184, 15193) and at k=4 (16804, 16810, 16806, 16814, 16816), G22 k=3 (17169) and G43 (8573, 9377). G55 at k=4, G70 at k = 3, 4 and G48-G50 at k = 3, 4 (6000, PAMC table) have every edge cut, so they are optimal and closed.

## What counts as a win

A labelling of the vertices of a Gset graph with labels 0..k-1, k in {3, 4}, whose k-cut value sum_{ij in E, label_i != label_j} w_ij, recomputed from the Stanford Gset file, is STRICTLY GREATER (direction: max) than the highest published value for that (graph, k) at claim time. Confirmed bars on 2026-10-30 include G81: 16510 (k=3) and 16670 (k=4); G22: 17169 and 18787; G55 k=3: 12437; G43: 8573 and 9377; and G1-G5 as in the statement. For other pairs the bar is the maximum over MOH 2017, Shao and Wu 2025 (EAJAM 15), Garvardt et al. 2026, PEAF (arXiv:2607.17158), PAMC (arXiv:2606.25203), the Chen release and any later publication. Pairs whose bar equals the total positive edge weight (all such edges cut, such as G55 k=4, G70 k=3,4 and G48-G50 k=3,4) cannot be won.

## Partial wins

- **p1:** For k = 5 on one of G1-G5, a partition strictly better than the values in Chen's release (17706, 17710, 17705, 17710, 17711), which themselves beat PEAF 2026 Table 21 on G1-G4.

## How a win is checked

Download G < i> from https://web.stanford.edu/~yyye/yyye/Gset/, read one label per vertex (n lines), check that labels lie in 0..k-1, and recompute the k-cut in integers (signed for +-1 graphs such as G81). This takes milliseconds. The Chen release's verify.py is a reference, but write your own checker. Re-read the listed papers and search for newer Max-k-Cut results before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/yaochengchen/gset-maxkcut_by_PdSB/main/results.csv>

## Sources

- <https://github.com/yaochengchen/gset-maxkcut_by_PdSB>
- <https://raw.githubusercontent.com/yaochengchen/gset-maxkcut_by_PdSB/main/results.csv>
- <https://leria-info.univ-angers.fr/~jinkao.hao/papers/MaHaoAOR2016.pdf>
- <https://arxiv.org/abs/2607.17158>
- <https://arxiv.org/abs/2606.25203>
- <https://doi.org/10.1007/s10479-026-07426-0>
- <https://web.stanford.edu/~yyye/yyye/Gset/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the best Max-Cut solutions and split each side (k = 4) or use 3-colouring-like tabu search; then run label-move and swap tabu search with long-term memory (MOH-style).
- Low-degree sparse graphs (G55, G60, G70, G81) are near the all-edges-cut ceiling: the gap is the number of monochromatic edges. Attack them as a graph-colouring-defect minimisation (minimise monochromatic edges) with colouring heuristics such as TabuCol and partialcol.
- Potts-machine and population annealing dynamics (PAMC) carry over directly from Max-Cut.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many papers report Max-k-Cut on Gset with different k or with balanced-partition constraints (graph k-partitioning). Only unconstrained Max-k-Cut with k = 3 or 4 counts here.
- Some instances are trivially optimal when every edge can be cut (bar = total edge weight); check the total before attacking.
- Chen's release is recent and partly self-reported against a literature check of 15 Oct 2026; its G81 k=4 value (16666) is below the Gurobi value 16670 in Shao and Wu 2025.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/gset-max-k-cut-records.md
```

Already set up? Say `run V3R1T4S on gset-max-k-cut-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gset-max-k-cut-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
