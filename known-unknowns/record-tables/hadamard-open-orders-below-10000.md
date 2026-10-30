# Hadamard conjecture frontier: a Hadamard matrix at one of the 85 orders up to 10000 with no known construction (smallest 2396)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (structured Goethals-Seidel, bordered or recursive searches over groups of order about 600 to 2500; checking a claim takes laptop-minutes) · open as of 2026-10-30

## The problem

A Hadamard matrix of order n is an n x n matrix H with entries +1 or -1 and H H^T = nI; one is conjectured to exist for every n divisible by 4. From Kharaghani and Tayfeh-Rezaie's order 428 (2005) until 2026 the smallest open order was 668. On 12 August 2026 L. Alpöge, P. Voinov and S. Reynolds-Haertle announced matrices at the twelve open orders below 2000 (668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964); Epoch AI's FrontierMath open-problems page now marks order 668 as solved (human + AI; reported by an Anthropic researcher crediting three humans and Claude). Egan, Kotsireas, London and Ó Catháin (arXiv:2610.27175, 19 Oct 2026) verified those matrices; built matrices at sixteen further orders, five of which (5436, 6644 and 7852 from A. Schumer's T-matrices of order 151; 7172 and 8476 from J. D. Jones's T-matrices of order 163) had been posted earlier by those authors and were found independently; checked exactly the twenty-two orders settled by others while the paper was in preparation (T. Cooley: 2092, 2292, 2588 and 3676, where Schumer had earlier given a skew matrix of order 3676; K. Kumar: 2148, 2284, 2636 and 3964, thirteen orders from a Seberry-Yamada product theorem, and 9172 from Cooley's 2292 by Miyamoto's theorem; Kharaghani, Mohammadian, Tayfeh-Rezaie and Zaitsev independently gave a BH(1142,4), which also yields 2284); credited L. Schneider's T-matrices of order 103; and listed in their Table 5 the 95 orders n <= 10000 with no known Hadamard matrix, all of the forms 4p, 4*3p, 4*5p, 4*7p, 4*9p, 4*11p, 4*13p or 8p with p a prime congruent to 3 mod 4. Their Hadamard Matrix Explorer (math74.com/Hadamard, version 57, October 2026), which hosts the paper's matrices, lists 86 unknown orders at this check: 2396, 2676, 2876, 2956, 3004, 3452, 3628, 3788, 3884, 4076, ... up to 9836 (full list on the status page). One of them, 5912 = 8*739, is already constructed in K. Kumar's repository (hadamard/5912, Spence's construction over Z_211 x F_7 with a multiplier group of order 45), so 85 remain open. The nine orders dropped since Table 5 are 2572, 3356, 3436, 3820, 4204, 6712, 6796, 8248 and 8696, and orders keep falling (for example, K. Kumar settled 2572 = 4*643 on 21 Oct 2026 with a quaternary conference matrix). Kumar's FRONTIER.md (github.com/vatskishan03/Hadamard, October 2026) independently lists 83 unresolved orders 4n < 10000 with n odd (85 if Middletownbooks' 2292 and 2588 are not accepted), exactly the explorer's odd-n orders, plus 37 unresolved orders 10000 < 4n <= 11996 from Cati and Pasechnik's Table 4 (n <= 2999); of the orders 8p it keeps only 4792 and 5752 open. The smallest open order is 2396 = 4*599. Tao's optimization-constants page for C_23a still gives 668 and is stale.

## What counts as a win

Success means an explicit n x n matrix H with every entry +1 or -1 and H H^T = nI computed exactly over the whole matrix (integer arithmetic), for an order n that is listed on the live unknown-orders page https://www.math74.com/Hadamard/unknown.html (re-fetched immediately before claiming; 86 orders at this check, of which 5912 is already constructed in Kumar's repository, smallest 2396) and that no public source settles at claim time. That means: n is not constructed in github.com/vatskishan03/Hadamard (hadamard/ and complex-hadamard/ folders, README.md, FRONTIER.md), in github.com/Middletownbooks/Hadamard (all branches), in the JD-Jones-ASES repositories Hadamard-T and Hadamard-M, in github.com/schneiderlo/hadamard-2060, in Schumer's Zenodo deposit doi:10.5281/zenodo.22820997 or in the latest version of arXiv:2610.27175; no quaternary Hadamard matrix BH(n/2,4), which gives H(n), is listed on https://www.cs.uleth.ca/~zaitsevv/quaternary.html; and a same-day arXiv, GitHub and Zenodo search for the order finds nothing (direction: none; existence target). The full matrix, or seeds plus an array that the verifier expands with its own code, must accompany the claim; a recipe without the matrix is not a result.

## Partial wins

- **p1:** A Hadamard matrix of order 4n with n odd and 10000 < 4n <= 11996 whose order is listed as unresolved in the live FRONTIER.md of github.com/vatskishan03/Hadamard (37 such orders at this check, for example 10012, 10052, 10124, 10172) and is not settled by any other public source at claim time, checked exactly as in the main criterion.

## How a win is checked

Load H and assert it is n x n with entries in {+1,-1}. Compute G = H H^T exactly: Python integers, or numpy int64 (every entry of G is bounded by n, so int64 and even float64 BLAS products are exact for n <= 10^4), and assert G == nI. Re-check with an independently written program (for example row-pair dot products in another language, plus Freivalds tests with random +-1 vectors). If the claim comes as seed sequences and an array (Goethals-Seidel, bordered, Williamson-type, Cooper-Wallis), expand it with the verifier's own code, never by running downloaded code. Then re-fetch the unknown-orders page, Kumar's FRONTIER.md and the other repositories the criterion names, and search arXiv, GitHub and Zenodo for the order.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math74.com/Hadamard/unknown.html>

## Sources

- <https://arxiv.org/abs/2610.27175>
- <https://www.math74.com/Hadamard/unknown.html>
- <https://www.math74.com/Hadamard/>
- <https://github.com/vatskishan03/Hadamard/blob/main/FRONTIER.md>
- <https://www.cs.uleth.ca/~zaitsevv/quaternary.html>
- <https://epoch.ai/frontiermath/open-problems/hadamard>
- <https://arxiv.org/abs/2411.18897>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Goethals-Seidel array over Z_p (or Z_3 x GF(p), or another group of order n/4) with the four first rows invariant under a multiplier subgroup of (Z/pZ)*: the unknowns become orbit signs; the 2026 matrices at 3732, 4492, 5932 and 5020 used multiplier groups of orders 31, 33, 39 and 50 respectively (arXiv:2610.27175).
- Bordered variants (Theorems 3, 5 and 7 of arXiv:2610.27175): the twelve 2026 matrices below 2000 are Goethals-Seidel arrays over abelian groups, nine over cyclic groups (four of them with a border of width 4) and three over non-cyclic groups with a wider border constant on the cosets of a subgroup; Spence's bordered construction for order 4m uses a group of order m - 1.
- Recursive closures: a new T-matrix order t or Williamson-type order w closes every order 4tw at once (Cooper-Wallis); Paley's and Miyamoto's matrices cut into sixteen circulant blocks can be multiplied by T-matrices (Kumar's PALEY_BLOCKS.md and MIYAMOTO_BLOCKS.md; read them as data, do not run downloaded code).
- Quaternary routes: any BH(n/2,4) gives H(n). For order 4m with m odd, a quaternary conference matrix of order (m+1)/2 with the complex Yamada-Kiyasu template gives one; this route settled 2572, 3436, 4204 and 6796 in October 2026 (Kumar). The quaternary table of Zaitsev, Kharaghani, Mohammadian and Tayfeh-Rezaie still lists 1198 (order 2396) as unknown.
- Triage first: Kumar's FRONTIER.md gives, for each open order, the cheapest multiplier or Spence structure with its expected solution count and predicted matching work log10 W. At this check no explorer-listed order has a structure with log10 W <= 13 (about one machine); the best are 4748 (log10 W 15.2, Spence over Z2 x Z593) and 4412 (15.5, Goethals-Seidel with |H| = 19), and 2676 and 2876 have no structure expected to hold ten solutions, so the remaining orders need new ideas or new ingredients.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The list moves every week. Table 5 of the 19 October survey had 95 orders and the explorer (version 57) 86 later in October, one of which, 5912, Kumar's repository has since constructed. Kumar's FRONTIER.md now matches the explorer on odd n (83 orders 4n < 10000) but, covering only odd n in its main table, lists the 8p orders separately (4792 and 5752 open). Check every source the criterion names.
- Every order below 2000 is settled (Alpöge, Voinov and Reynolds-Haertle, August 2026). Tao's C_23a page still says 668; it is stale.
- Seberry-Yamada's Corollary 8.8(i) and Miyamoto's (1991) Corollary 2 omit a symmetry hypothesis their construction needs; orders claimed only through them (2076 and 6108 historically, and Miyamoto's 515/2060 route per the JD-Jones-ASES Hadamard-M erratum) were not valid constructions. A claim through a printed theorem must check every hypothesis on the explicit inputs.
- Seeds are not a matrix: expand them and verify H H^T over the whole matrix; one wrong sign in a border fails it.
- Several independent groups, some AI-assisted, are searching the same orders; same-day duplicates are likely, so re-check right before claiming and record the time.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hadamard-open-orders-below-10000.md
```

Already set up? Say `run V3R1T4S on hadamard-open-orders-below-10000`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hadamard-open-orders-below-10000`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
