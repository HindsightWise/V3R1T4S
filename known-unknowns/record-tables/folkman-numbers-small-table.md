# Small vertex and edge Folkman numbers: improve a bound in the Hassan-Radziszowski-Van Overberghe 2026 tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (witness graphs on 15-65 vertices; arrowing checked by small SAT instances) · open as of 2026-10-30

## The problem

G -> (a1,...,ak)^v means every k-colouring of the vertices of G has a colour-i K_{a_i}; ^e is the edge version. The Folkman number F(a1,...,ak; H) is the least order of an H-free graph with that property. Hassan, Radziszowski and Van Overberghe (arXiv:2605.16542, May 2026; code at github.com/Steven-VO/vertexFolkman, witnesses on House of Graphs) tabulate a_i in {2,3}, k <= 4, H in {K_n, J_n = K_n - e, n = 4,5,6} plus C4 and W5. Open entries: Fv(2,2,3;J4) 20-36, Fv(3,3;J4) 24-45 (Table 1 prints 23, but Section 4.5 proves >= 24), Fv(2,3,3;K4) 20-24 (Bikov-Nenov), Fv(2,3,3;J5) 15-18, Fv(3,3,3;K4) <= 51, Fv(3,3,3;J5) <= 32, Fv(3,3,3;K5) <= 21, Fe(3,3;J5) <= 43, Fv(3,3;C4) 30-63, Fe(3,3;W5) <= 64, Fv(2,3,3,3;K5) <= 32, Fv(3,3,3,3;K6) <= 30. Fv(3,3;K5) = 8, which Tong Niu re-proved (arXiv:2605.05526), already follows from Luczak-Urbanski's Lemma 1 and is not open. Excluded: the edge Folkman number Fe(3,3;4) (21-786), which carries a Graham prize (erdosproblems.com/582), and the existence of Fe(3,3; complement of P2 u P3), which bounds it. Credit: Hassan, Radziszowski, Van Overberghe, Bikov, Nenov, Coles-Radziszowski, Deng-Liang-Shao-Xu.

## What counts as a win

Either (a) an explicit graph G (graph6 or edge list) on N vertices that is H-free and arrows the stated tuple, with N STRICTLY BELOW (direction: min) the upper bound in arXiv:2605.16542 (latest version), Bikov's papers and any newer source; H-freeness checked exhaustively, arrowing certified by a DRAT/LRAT UNSAT proof that no vertex (resp. edge) colouring avoids every colour-i K_{a_i}; or (b) for an entry with a printed lower bound (Fv(2,2,3;J4), Fv(3,3;J4), Fv(2,3,3;K4), Fv(2,3,3;J5), Fv(3,3;C4)), a lower bound STRICTLY ABOVE (direction: max) the published one (for Fv(3,3;J4) that is the 24 of Section 4.5, not the 23 printed in Table 1), i.e. a proof that no H-free graph on N vertices arrows the tuple, by a re-runnable exhaustive generation (e.g. nauty geng with stated filters) plus per-graph SAT certificates, or a single checkable certificate. Lower bounds for upper-bound-only entries count only under p1. The witnesses for Fe(3,3;4) and Fe(3,3; complement of P2 u P3) are out of scope.

## Partial wins

- **p1:** A certified lower bound (as in (b)) for an upper-bound-only entry, strictly above both the monotonicity bound and the deletion-inequality bound in pitfalls, and above any bound found by a fresh search: Fv(3,3,3;K5) >= 16 (monotonicity from Fv(3,3,3;J6) = 15 and the deletion inequality both give 15), Fv(3,3,3;J5) >= 19 (the deletion inequality gives 18), Fv(3,3,3;K4) >= 25 (the deletion inequality gives 24), or Fe(3,3;J5) >= 16 (it is >= Fe(3,3;K5) = 15).
- **p2:** An exact value: an entry of Tables 1-2 of arXiv:2605.16542 settled by a new certified witness meeting a known or new certified lower bound.

## How a win is checked

H-freeness: exhaustive subgraph search for K_n / J_n (clique enumeration with one missing edge allowed), C4 (A^2 off-diagonal at most 1) or W5 (C4 in a neighbourhood), cross-checked by SAT. Arrowing: encode one Boolean (or one-hot) variable per vertex (edge) colour and one clause per K_{a_i} forbidding colour i on all of it; solve with CaDiCaL/kissat, require UNSAT and check the DRAT proof with drat-trim. Lower bounds: re-run the stated generation and check each certificate.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2605.16542>

## Sources

- <https://arxiv.org/abs/2605.16542>
- <https://github.com/Steven-VO/vertexFolkman>
- <https://arxiv.org/abs/1611.06418>
- <https://arxiv.org/abs/1609.03468>
- <https://arxiv.org/abs/2605.05526>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Semi-polycirculant generation gave most 2026 bounds; vary block structures, or search Cayley graphs of non-abelian groups.
- Locally linear graphs gave Fv(3,3;J4) >= 24 (all maximal locally linear graphs on 23 vertices checked); extending that enumeration to 24 vertices would give 25.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Fe(3,3;4) has a $100 Graham prize attached (erdosproblems.com/582) and is held separately; any graph found here that is K4-free and edge-arrows (3,3) must be reported to the human, not posted.
- Vertex versus edge arrowing are different: Fv(3,3;C4) and Fe(3,3;W5) are linked by Fe(3,3;W5) <= Fv(3,3;C4)+1.
- Table 1 prints Fv(3,3;J4) >= 23, but Section 4.5 of the same paper proves >= 24; a lower-bound claim must reach 25.
- Deletion inequality: if G -> (3,3,3)^v and S is an independent set, then G - S -> (2,3,3)^v (give S the colour of the independent class; two independent sets together contain no triangle), so |G| >= Fv(2,3,3;H) + alpha(G). With R(4,4) = 18, R(4,5) = 25 and R(3,5) = 14 this already gives Fv(3,3,3;K4) >= 24, Fv(3,3,3;J5) >= 18 and Fv(3,3,3;K5) >= 15; a lower bound at or below these is not new.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/folkman-numbers-small-table.md
```

Already set up? Say `run V3R1T4S on folkman-numbers-small-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `folkman-numbers-small-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
