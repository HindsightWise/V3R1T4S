# Steiner tree bidirected cut relaxation: an explicit instance with integrality gap above Vicari's 6/5 (hypergraphic 8/7 and BCR+ 36/31 as partial wins)

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (instance search; each candidate needs one exact LP and one exact Steiner tree computation, minutes for graphs with up to about 60 vertices and 15 terminals) · open as of 2026-10-30

## The problem

For the Steiner tree problem in graphs, the bidirected cut relaxation (BCR) directs edges both ways from a root terminal. It asks for capacity at least 1 into every vertex set that contains a terminal but not the root. Its integrality gap is famously open. Byrka, Grandoni and Traub (arXiv:2407.19905, FOCS 2024) proved the first upper bound below 2: 1.9988. The same paper cites 6/5 as the best lower bound, proved by Vicari (arXiv:2002.07912) with simplex-based instances whose gaps tend to at least 6/5. That improved the 36/31 ~ 1.161 of Byrka, Grandoni, Rothvoss and Sanita, which came from Skutella-type set-cover instances. Vicari's Table 1 also records two more lower bounds: the hypergraphic relaxation HYP has gap at least 8/7 (Skutella's instance; Konemann, Pritchard and Tan) and at most ln 4 ~ 1.386 (Goemans, Olver, Rothvoss and Zenklusen). BCR with Steiner-vertex flow-balance constraints (BCR+) has gap against the integral optimum at least 36/31. Vicari's 6/5 is a limit over a family, so a single finite instance above 6/5 would be new.

## What counts as a win

An explicit finite instance: an undirected graph, a terminal set R and nonnegative rational edge costs, with OPT_STP / OPT_BCR strictly greater than 6/5 (higher is better). It must also be strictly greater than any lower bound published at claim time; re-check arXiv. The certificate has two parts. (i) A feasible BCR solution, rational directed capacities for a stated root terminal, of cost L, so that OPT_BCR <= L. Feasibility is checked by exact max-flow from the root to every terminal. (ii) A certified lower bound U on the minimum Steiner tree cost: exact enumeration (Dreyfus-Wagner DP, or MST over every Steiner-vertex subset), or an ILP solve with a VIPR-style certificate. The verifier checks U/L > 6/5. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** An explicit instance with OPT_STP / OPT_HYP strictly greater than 8/7, the best known lower bound for the hypergraphic relaxation (upper bound ln 4). The upper bound on OPT_HYP is a rational feasible solution of the full-component LP, with every partition or subtour constraint checked exhaustively (feasible for small terminal counts).
- **p2:** An explicit instance with OPT_STP / OPT_BCR+ strictly greater than 36/31, where BCR+ adds the Steiner-vertex flow-balance (in-degree <= out-degree) constraints, certified as in the main criterion with the extra constraints checked.

## How a win is checked

About 200 lines of Python with exact rationals (fractions) plus networkx max-flow on rational capacities. Check that the stated directed solution satisfies x_uv >= 0, and that root-to-terminal max-flow is at least 1 for every terminal; this is equivalent to all BCR cut constraints. Compute L. Compute the Steiner optimum by Dreyfus-Wagner over terminals (O(3^|R| n)) or brute force over Steiner subsets, with an independent second implementation. Calibrate on Skutella's 8/7 instance and on a small Vicari simplex instance, and confirm that BCR is exact on series-parallel graphs and on spanning-tree instances. For p1, enumerate full components exactly for |R| <= 10 and check the HYP subtour form.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2407.19905>

## Sources

- <https://arxiv.org/abs/2002.07912>
- <https://arxiv.org/abs/2407.19905>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Vicari's instances embed Steiner instances into simplices through the dual formulations of Chakrabarty, Devanur and Vazirani. Larger simplex dimensions and non-uniform cost profiles are the obvious knobs. Search their parameters with exact LP scoring.
- Cast the search as a bilevel problem: fix a graph template and optimise edge costs to maximise OPT_STP subject to the LP value being at most 1, using cutting planes on the Steiner trees that achieve the optimum.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Vicari's 6/5 is a limit. A finite instance just below 6/5 is not a win.
- Do not confuse BCR (directed) with the undirected cut relaxation (gap exactly 2) or with HYP; each has its own bar.
- Floating-point LP values are not certificates; give the rational primal solution.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/steiner-tree-bcr-integrality-gap-lower-bound.md
```

Already set up? Say `run V3R1T4S on steiner-tree-bcr-integrality-gap-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `steiner-tree-bcr-integrality-gap-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
