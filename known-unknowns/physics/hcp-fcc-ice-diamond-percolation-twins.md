# Twin-lattice percolation: are the hcp and fcc bond thresholds equal (both 0.120164 within 1e-6), and how far apart are ice Ih and diamond?

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for the partials (3D Newman-Ziff or wrapping-probability Monte Carlo on L up to 128-256; ice-Ih p1 is laptop-hours); needs cluster (or a GPU union-find code for weeks) for the full Delta win, which needs each threshold to <= 6e-8, beyond Xu et al.'s L <= 128, ~1e8-sample fcc runs · open as of 2026-10-30

## The problem

The hcp and fcc lattices, and ice Ih vs diamond (hexagonal vs cubic diamond), differ only in layer stacking, so their percolation thresholds agree to many digits. Robert Ziff's Wikipedia 'Percolation threshold' page (3D table, last edited 2026-10-23) asks this explicitly. Are the hcp and fcc bond thresholds identical? If not, how far apart are they and which is bigger? The same question is asked for ice and diamond, citing M. F. Sykes, J. J. Rehr and Maureen Glen, 'A note on the percolation probabilities of pairs of closely similar lattices'. Current values: hcp bond 0.1201640(10) and site 0.1992555(10) (Christian Lorenz, Raechelle May and Robert Ziff, J. Stat. Phys. 98 (2000) 961, arXiv cond-mat/9908034). They found the site thresholds different but the bond thresholds equal within errors. fcc bond 0.12016377(15) and site 0.19923517(20) (Xiao Xu, Junfeng Wang, Jian-Ping Lv and Youjin Deng, Front. Phys. 9 (2014) 113, arXiv 1310.5399, Table V). Diamond bond 0.3895892(5) and site 0.4299870(4) (same paper). Ice Ih still carries only the 1961 values 0.433(11) site (Frisch et al.) and 0.388(10) bond (Vyssotsky et al.). So the fcc-hcp bond difference, 2.3e-7 +- 1.0e-6, is consistent with zero at the 1e-6 level and its sign is unknown, and ice Ih has no modern threshold at all.

## What counts as a win

Success means either (A) or (B). (A) A determination of Delta = p_c^bond(hcp) - p_c^bond(fcc) with one-sigma uncertainty at most 3e-8, from simulations of both lattices with the same code, estimator and fit form, with each individual threshold to uncertainty <= 6e-8. The fcc value must be within 3 sigma of Xu et al.'s 0.12016377(15), or the discrepancy must be analysed and shown by both estimators. (B) The same for the ice-Ih / diamond pair, with Delta uncertainty at most 1e-7 for bond or site and the diamond value within 3 sigma of Xu et al. (or the discrepancy analysed). In both cases a second estimator (for example two different wrapping probabilities, or wrapping plus cluster-size ratios) must give a consistent Delta, raw data and code are released, and a literature check immediately before claiming finds no published Delta of that precision. Direction: smaller uncertainty on the difference; a nonzero Delta at >= 5 sigma and a null result at the stated precision both count.

## Partial wins

- **p1:** First modern ice-Ih (hexagonal diamond, z = 4) site and bond thresholds, each with one-sigma uncertainty <= 2e-6, with the same code reproducing Xu et al.'s diamond site 0.4299870(4) and bond 0.3895892(5) within 3 sigma, and a literature search immediately before claiming finding no published ice-Ih value with uncertainty <= 2e-6.
- **p2:** hcp site and bond thresholds each with uncertainty <= 3e-7 (more than 3 times better than Lorenz-May-Ziff), with the same code reproducing the fcc values of Xu et al. within 3 sigma.

## How a win is checked

Skeptic (< 1 hour): build both lattices from their stacking sequences and check coordination 12 (hcp, fcc) or 4 (ice Ih, diamond) and the site counts per periodic cell; rerun short simulations at two sizes with fresh seeds and check consistency with the released data; refit Delta from the released wrapping probabilities with and without the leading correction term; confirm the reproduction tests.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/cond-mat/9908034>
- <https://arxiv.org/abs/1310.5399>
- <https://doi.org/10.1103/PhysRev.123.1566>
- <https://doi.org/10.1103/PhysRev.124.1021>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Correlated sampling: run hcp and fcc with the same random numbers on bonds that map to each other layer by layer, so most noise cancels in Delta; this is the whole trick for a difference far below the individual errors.
- Series view: Sykes-Rehr-Glen and Lorenz-May-Ziff note the low-density series of the twins first differ at high order; an exact enumeration of where they first differ gives the sign expectation to test.
- Periodic cells: hcp needs an even number of layers and ice Ih needs cells compatible with its hexagonal stacking; use tori whose wrapping probabilities have the same universal limit as for the cubic twins, or compare at matched aspect ratio.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Wikipedia lists a third fcc bond value, 0.120169(2) (Hu and Charbonneau 2021, invasion percolation), 2.6 sigma from Xu et al.; use matched-method comparisons, not mixed literature values, for Delta.
- Wrapping probabilities on tori of different shape (hexagonal vs cubic cells) have different universal limits; the threshold is found from size crossings, not from a universal-value equation, unless the cell shapes match.
- The fcc-hcp difference may be far below 1e-8; a null result is a legitimate full win under (A) only at the stated precision.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/hcp-fcc-ice-diamond-percolation-twins.md
```

Already set up? Say `run V3R1T4S on hcp-fcc-ice-diamond-percolation-twins`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hcp-fcc-ice-diamond-percolation-twins`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
