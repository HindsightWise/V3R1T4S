# Directed percolation on the square lattice: more digits of p_c than Jensen's series values 0.644700185(5) (bond) and 0.70548522(4) (site)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (Jensen-type transfer-matrix series; memory-bound, each doubling of RAM adds terms) · open as of 2026-10-30

## The problem

Directed percolation in 1+1 dimensions has no exact threshold (it is not conformally invariant). The record values are still Iwan Jensen's low-density series results (J. Phys. A 32 (1999) 5233, doi 10.1088/0305-4470/32/28/304, arXiv cond-mat/9906036). With a new transfer-matrix algorithm he extended the bond series to order 171 and the site series to order 158 using about 5.5 GB, and estimated p_c(bond) = 0.644700185(5) and p_c(site) = 0.70548522(4); an earlier analysis in the same paper gave 0.70548515(20). Monte Carlo values are less precise: Wikipedia lists 0.6447001(2) and 0.7054852(3) from Junfeng Wang, Zongzheng Zhou, Qingquan Liu, Timothy Garoni and Youjin Deng (Phys. Rev. E 88 (2013) 042102, arXiv 1201.3006). The Wikipedia 'Percolation threshold' directed-percolation table (checked 2026-10-30) lists nothing more precise for the (1+1)-d square lattice. Jensen's algorithm has a growth factor below 2^(1/8), so each doubling of memory adds about 8 terms; a machine with 100 times his memory should add about 50 terms. The same applies to the triangular, honeycomb and kagome cases of his 2004 paper.

## What counts as a win

Success means an estimate of the directed square-lattice threshold with stated uncertainty at most 1e-9 for bond (5 times smaller than 5e-9) or at most 1e-8 for site (4 times smaller than 4e-8), such that (a) it comes from exact series longer than Jensen's (bond > 171 or site > 158 terms) or from an independent method, (b) the series coefficients are released as exact integers and the first 100 agree exactly with an independent recomputation (and with Jensen's where available), (c) at least two series (for example mean cluster size and moments of the cluster length) analysed with differential approximants give consistent p_c, (d) the value agrees with Jensen's within 3 combined sigma or the discrepancy is analysed, and (e) a literature search before claiming finds no better published value. Direction: smaller uncertainty.

## Partial wins

- **p1:** Exact low-density series for bond directed percolation on the square lattice to at least 190 terms (or site to at least 175), released as exact integers, with the first 100 terms independently recomputed by a second program.
- **p2:** An independent Monte Carlo or transfer-matrix estimate of p_c(bond) with uncertainty <= 2e-8, ten times better than Wang et al. 2013 and consistent with Jensen within 3 sigma.

## How a win is checked

Skeptic (< 1 hour): recompute the first 40-60 series terms with a simple brute-force or row-transfer program and compare exactly; rerun the claimant's differential-approximant analysis on the released series and vary the approximant orders; check the stated uncertainty against the spread.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/cond-mat/9906036>
- <https://arxiv.org/abs/cond-mat/0405504>
- <https://arxiv.org/abs/1201.3006>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Jensen computed modulo primes and reconstructed by CRT; the same trick plus 64-bit hashing of boundary states and disk-backed sorting now fits much longer series.
- Biased differential approximants with the DP exponents fixed from the best Monte Carlo (beta, nu_par, nu_perp) sharpen p_c from the same series.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Jensen's university series page returns 403 today; do not use mirrors of uncertain provenance, recompute instead.
- Series analysis error bars are judgement calls; require the spread over many approximant orders, not the best few.
- Site vs bond and diagonal vs nearest-neighbour conventions differ between papers; the table row is the (1+1)-d square lattice, diagonal.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/directed-percolation-square-lattice-threshold-digits.md
```

Already set up? Say `run V3R1T4S on directed-percolation-square-lattice-threshold-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `directed-percolation-square-lattice-threshold-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
