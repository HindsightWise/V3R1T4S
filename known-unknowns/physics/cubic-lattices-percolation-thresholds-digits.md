# Simple cubic, bcc, fcc and diamond percolation thresholds: beat the Xu-Wang-Lv-Deng (2014) precision, e.g. sc site 0.31160768(15), sc bond 0.24881185(10)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: needs cluster (or laptop-days with a GPU union-find code); L up to 1024 and 1e8+ samples per size · open as of 2026-10-30

## The problem

The basic 3D thresholds are known only numerically. Best values (Xiao Xu, Junfeng Wang, Jian-Ping Lv and Youjin Deng, Front. Phys. 9 (2014) 113, arXiv 1310.5399, Table V, from simultaneous fits of wrapping probabilities sharing universal parameters): simple cubic bond 0.24881185(10) and site 0.31160768(15); bcc bond 0.18028762(20) and site 0.2459615(2); fcc bond 0.12016377(15) and site 0.19923517(20); diamond bond 0.3895892(5) and site 0.4299870(4). The simple cubic values rest on Junfeng Wang, Zongzheng Zhou, Wei Zhang, Timothy Garoni and Youjin Deng (Phys. Rev. E 87 (2013) 052107, arXiv 1302.0421; sc bond 0.24881182(10), site 0.3116077(2), L <= 512). The Wikipedia 'Percolation threshold' 3D table (edited 2026-10-23 by Robert Ziff) lists no later improvement for these lattices; for bcc it still shows Lorenz-Ziff 1998 values 0.2459615(10) and 0.1802875(10), and for fcc bond it adds Hu-Charbonneau 2021 0.120169(2), which sits 2.6 sigma from Xu et al. In 4D and above Mertens and Moore (2018) reached 1e-8 to 1e-11, so 3D is now the least precise of the hypercubic family.

## What counts as a win

Success means a threshold for at least one of the eight (lattice, site/bond) pairs above with stated one-sigma uncertainty at most one third of the Xu et al. 2014 Table V uncertainty for that pair (for example <= 5e-8 for sc site, <= 3e-8 for sc bond), such that (a) two estimators (for example two wrapping probabilities, or wrapping probability and a cluster-size ratio) agree within 3 combined sigma, (b) the value is within 3 sigma of Xu et al. or the discrepancy is analysed, (c) the fit includes at least two correction-to-scaling terms and is stable when the smallest sizes are dropped, (d) raw per-size data and code are released, and (e) a literature search immediately before claiming finds no published value for that pair with smaller uncertainty. Direction: smaller uncertainty.

## Partial wins

- **p1:** Independent reproduction, with own code, of all eight Xu et al. Table V thresholds to uncertainty <= 3 times theirs and agreement within 3 sigma, with released data; reproduction only.
- **p2:** One of the eight pairs with uncertainty at most one half of Xu et al.'s, under the same rules (a)-(e).

## How a win is checked

Skeptic (< 1 hour): rerun the claimant's code at two small sizes with fresh seeds and compare wrapping probabilities with the released data; refit the released data with the claimant's and one alternative correction ansatz; check the reproduction of the Wang et al. 2013 sc values at L <= 128.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/1310.5399>
- <https://arxiv.org/abs/1302.0421>
- <https://arxiv.org/abs/2102.09682>
- <https://arxiv.org/abs/cond-mat/9806224>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Simultaneous fits across lattices sharing the universal wrapping limits and y_t = 1/nu (Xu et al.'s trick) gain a factor of 2-3; feeding in nu from the most precise percolation exponent studies gains more.
- GPU union-find with path compression (or Hoshen-Kopelman on slabs) makes L = 1024-2048 sweeps cheap; microcanonical Newman-Ziff gives all p at once.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several Xu et al. Table V values (sc bond 0.24881185(10), bcc site 0.2459615(2) and bond 0.18028762(20), fcc bond 0.12016377(15)) are not in the Wikipedia rows; compare against Table V of arXiv 1310.5399, not only the wiki row.
- Correlated estimators from the same samples are not independent methods; their agreement does not validate the error bar.
- Random-number quality matters at this precision; use a modern generator and report it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/cubic-lattices-percolation-thresholds-digits.md
```

Already set up? Say `run V3R1T4S on cubic-lattices-percolation-thresholds-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cubic-lattices-percolation-thresholds-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
