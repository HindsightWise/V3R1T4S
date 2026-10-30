# Five-colour bipartite Ramsey number b5(2) (26-28): a rectangle-free 5-colouring of the 26 x 26 grid, or a proof that none exists

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (SAT on 676 cells x 5 colours with symmetry assumptions) · open as of 2026-10-30

## The problem

The bipartite Ramsey number b_k(2) is the least b such that every k-colouring of the edges of K_{b,b} has a monochromatic C4; equivalently every k-colouring of the b x b grid has a monochromatic rectangle (four cells at the corners of an axis-parallel rectangle). Known: b2(2) = 5 (Beineke-Schwenk), b3(2) = 11 (Exoo 1991), b4(2) = 19 (Dybizbanski-Dzido-Radziszowski, Ars Combin. 2015; the 4-colouring of the 18 x 18 grid was also found by Steinbach and Posthoff in 2012, and the two colourings are isomorphic). For five colours 26 <= b5(2) <= 28 (Dybizbanski-Dzido-Radziszowski, arXiv:1303.5475, Theorem 10). The lower bound is the affine construction over GF(5): rows and columns are indexed by GF(5) x GF(5), and cell ((a,b),(a',b')) gets colour a*a' - b - b'. The upper bound is the Zarankiewicz bound z(28;2) <= 156, since 5 * 156 < 784. They conjectured b5(2) = 28 (Conjecture 11); Collins-Riasanovsky-Wallace-Radziszowski (2016) call it the smallest open case for five colours. Fenner-Gasarch-Glover-Purewal (arXiv:1005.3750) show the 25 x 30 grid is 5-colourable. Liu, Chew and Heule (arXiv:2012.12582, AAAI 2021) tried SAT with internal 'shift pattern' symmetries on the 26 x 26 grid without success; their closest attempts left 2 or 3 unsatisfied clauses. An arXiv check (to 30 Oct 2026) found no later settlement. DS1 does not cover bipartite Ramsey numbers, so no maintained table tracks this value.

## What counts as a win

Either (a) an explicit 5-colouring of the 26 x 26 grid (a 26 x 26 matrix over {0..4}) with no monochromatic rectangle, verified by two independent programs, proving b5(2) >= 27 STRICTLY GREATER (direction: max) than the current 26; or (b) a proof that every 5-colouring of the 27 x 27 grid has a monochromatic rectangle, proving b5(2) <= 27 STRICTLY BELOW (direction: min) the current 28, certified by a DRAT/LRAT UNSAT proof of a stated CNF with only provably sound symmetry breaking, re-checkable by a referee. A rectangle-free 5-colouring of the 27 x 27 grid would settle b5(2) = 28.

## Partial wins

- **p1:** A certified UNSAT proof (drat-trim/LRAT) that no rectangle-free 5-colouring of the 26 x 26 grid exists within a precisely stated symmetry class not already excluded in arXiv:2012.12582 (for example colourings invariant under a stated cyclic shift of rows and columns).
- **p2:** An explicit 5-colouring of the 26 x 26 grid with exactly one monochromatic rectangle, or of the grid minus one cell with none, verified exhaustively (a near-miss object no published source reports).

## How a win is checked

For each colour c and each pair of rows (r1, r2), count the columns where both rows have colour c; a count of 2 or more is a rectangle. That is 5 x C(26,2) x 26 operations; implement with numpy bit operations and with plain loops. Check the matrix shape and colour range. For (b), regenerate the CNF and check the proof with drat-trim or cake_lpr.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1303.5475>

## Sources

- <https://arxiv.org/abs/1303.5475>
- <https://arxiv.org/abs/1604.01257>
- <https://arxiv.org/abs/2012.12582>
- <https://arxiv.org/abs/1005.3750>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Status checked only by arXiv searches and the papers above (no maintained table exists); re-check Gasarch-style grid-colouring literature before claiming.
- Each colour class must be a C4-free bipartite graph, so 5 z(n;2) >= n^2 is necessary. z(n;2) is known exactly for all n <= 31 (Collins et al. 2016, Table 3, from DDR and Afzaly-McKay): z(26;2) = 138, z(27;2) = 147, z(28;2) = 156. The counting slack is 690 - 676 = 14 cells for 26 x 26 and 735 - 729 = 6 for 27 x 27, so in a 27 x 27 colouring every colour class has at least 141 edges, close to extremal; 5 * 156 = 780 < 784 is the upper bound 28.
- Liu-Chew-Heule already exclude 26 x 26 colourings in which the whole grid splits into shift-pattern subgrids (sizes 2, 13 or 26) and several 25 x 25-plus-border patterns; a p1 class must be one they did not exclude.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/bipartite-ramsey-b5-quadrilateral.md
```

Already set up? Say `run V3R1T4S on bipartite-ramsey-b5-quadrilateral`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bipartite-ramsey-b5-quadrilateral`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
