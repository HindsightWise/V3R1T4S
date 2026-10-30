# Percolation thresholds still at 3-4 digits: stacked 2D lattices, van der Marck duals, d-dimensional bcc/diamond (d = 4-6) and extended neighbourhoods in Wikipedia's 3D and higher-d tables

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours per lattice (Newman-Ziff on 3D-6D tori) · open as of 2026-10-30

## The problem

Robert Ziff's Wikipedia 'Percolation threshold' page (checked 2026-10-30, last edited 2026-10-23) still lists many periodic lattices with only 3-4 significant digits. Most come from Steven C. van der Marck's 1997-98 studies (Phys. Rev. E 55 (1997) 1514 and 6593; Int. J. Mod. Phys. C 9 (1998) 529; J. Phys. A 31 (1998) 3449) and from Krzysztof Malarz's extended-neighbourhood work (with Kurzawski 2012; Phys. Rev. E 91 (2015) 043301). 3D table examples: kagome stack site 0.3346(4) and bond 0.2563(2), honeycomb stack 0.3701(2)/0.3093(2), dice stack 0.2998(4)/0.2378(4), bow-tie stack 0.2822(6)/0.2092(4), octagonal (union-jack) stack 0.2524(6)/0.1752(2), pentagonal stack 0.3394(4)/0.2793(4), bow-tie stack dual 0.3480(4)/0.2853(4), octagonal stack dual 0.3840(4)/0.3168(4), fcc dual 0.3341(5)/0.2703(3), hcp dual 0.3101(5)/0.2573(3), bcc dual 0.4560(6)/0.4031(6), diamond dual 0.3904(5)/0.2350(5) and 3D kagome bond 0.2709(6). Also site columns for sc neighbourhoods such as NN+3NN 0.1420(1), 2NN+3NN 0.1036(1), NN+2NN+4NN 0.11440(12), NN+3NN+4NN 0.11920(12) and 2NN+3NN+4NN 0.11330(12). Higher-d table: 4D diamond 0.2978(2)/0.2715(3), 4D kagome bond 0.177(1), 4D bcc site 0.1037(3), 4D hypercubic 3NN, NN+3NN and 2NN+3NN site 0.04540(23), 0.04000(23), 0.03310(23), 5D diamond 0.2252(3)/0.2084(4), 5D bcc 0.0446(4)/0.033(1), 5D kagome bond 0.130(2), 6D diamond 0.1799(5)/0.1677(7) and 6D bcc site 0.0199(5). Zhipeng Xun, Robert Ziff and co-authors (2020-22) redid the bond columns of the neighbourhood rows and some site cells to 7 digits. Where they overlap, Malarz's 2015 4NN site values disagree strongly with equivalent lattices (sc-2NN+4NN = fcc NN+2NN, 0.1361408(8) vs 0.15950(12); sc-3NN+4NN = bcc NN+2NN, 0.1759432(8) vs 0.20490(12); sc-1..4, 0.0801171(9) vs 0.10000(12)), so his remaining 4NN cells are suspect.

## What counts as a win

Success means, for at least one cell of the live Wikipedia 3D or 'other higher-dimensional lattices' table whose best listed value has uncertainty >= 1e-4 (re-fetched immediately before claiming), a threshold with stated one-sigma uncertainty at most 1e-6. Five conditions apply. (a) Two estimators agree within 3 combined sigma, for example two wrapping probabilities with finite-size fits, or wrapping plus a cluster-size ratio. (b) The value is within 3 sigma of the listed one, or the discrepancy is explained. (c) The same code reproduces the simple cubic site 0.31160768(15) and bond 0.24881185(10) (Xu et al. 2014) to at least 6 digits. (d) The lattice is defined explicitly (basis, neighbour vectors) and matches the table's z and the cited paper's construction. (e) A literature search finds no published value below 1e-6 for that lattice or any lattice equivalent to it. Three kinds of cell are excluded: cells fixed by an exact identity (3D and d-dimensional kagome site = diamond bond), cells equivalent to a lattice already known to 1e-6 (sc-2NN+4NN = fcc NN+2NN; sc-3NN+4NN = bcc NN+2NN; sc-3NN = bcc), and the ice Ih row, which is covered by the separate hcp-fcc / ice-diamond twins entry. Direction: smaller uncertainty.

## Partial wins

- **p1:** Five or more such cells, each to uncertainty <= 1e-6 under the same rules, published as one table with code.
- **p2:** A cell improved to uncertainty <= 1e-5 (10 times or more better than listed) under rules (a)-(e), for a lattice whose construction is fully specified.

## How a win is checked

Skeptic (< 1 hour): rebuild the lattice from the stated basis and neighbour list and check z and site counts against the table; rerun the claimant's simulation at two sizes with fresh seeds; refit the released data; check the sc reproduction.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://doi.org/10.1103/PhysRevE.55.1514>
- <https://doi.org/10.1103/PhysRevE.55.6593>
- <https://arxiv.org/abs/cond-mat/9802187>
- <https://arxiv.org/abs/1501.01586>
- <https://arxiv.org/abs/2111.10975>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Stacked lattices are a 2D Archimedean or Laves lattice times Z with vertical bonds; build them from the 2D tilings already used for the 2-uniform entry.
- For the high-d bcc and diamond rows, Mertens-Moore's hypercubic code (wrapping on hypertori, L up to 64 in 4D) is the template.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'Dual' here means van der Marck's construction in PRE 55, 6593; a different dual gives a different, wrong lattice. Check z-bar.
- Some cells (e.g. sc NN+4NN site) already have a 7-digit value in the same row; only the best value in a cell counts, and a lattice equivalent to another row (sublattice decompositions of extended sc neighbourhoods) inherits that row's value.
- Malarz 2015's sc 4NN site values (0.11440, 0.11920, 0.11330, 0.15950, 0.20490, 0.10000, all (12)) disagree by 15-25% with equivalent-lattice values where checkable; expect discrepancies on the remaining 4NN cells, check your neighbour shells against the equivalences first, and explain any discrepancy under rule (b).
- This is the 3D/high-d analogue of the 2-uniform entry; one cell is one partial harvest, not a separate target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/percolation-3d-higher-d-low-precision-rows.md
```

Already set up? Say `run V3R1T4S on percolation-3d-higher-d-low-precision-rows`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `percolation-3d-higher-d-low-precision-rows`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
