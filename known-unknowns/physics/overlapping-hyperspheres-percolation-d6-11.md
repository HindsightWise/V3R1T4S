# Continuum percolation of overlapping hyperspheres in d = 6-11: beat the Torquato-Jiao (2012) thresholds, still the most precise published values

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (union-find on cell lists in d-dimensional tori; memory, not CPU, limits d >= 9) · open as of 2026-10-30

## The problem

For the Poisson Boolean model of equal overlapping hyperspheres, the critical reduced density eta_c (expected number of sphere centres per sphere volume) has no closed form. In d = 3 the best values are Christian Lorenz and Robert Ziff's 0.341889(3) (J. Chem. Phys. 2001) and Piotr Brzeski and Grzegorz Kondrat's critical volume fraction 0.2895693(26), i.e. eta about 0.341884 (J. Stat. Mech. 2022, 053202), with an outlier 0.341935(8) (Gori-Trombettoni 2015). Brzeski and Kondrat also improved d = 4 and 5 by factors of about 230 and 10. For d = 6..11 the Wikipedia 'Percolation threshold' page (higher-dimension continuum table, checked 2026-10-30) lists only Salvatore Torquato and Yang Jiao (J. Chem. Phys. 137 (2012) 074106, arXiv 1208.3720, rescaled-particle method): eta_c = 0.02339(5) (d = 6), 0.01051(3) (7), 0.004904(6) (8), 0.002353(4) (9), 0.001138(3) (10), 0.0005530(3) (11), plus older Dall-Christensen values for d <= 8. These are 3-4 digit numbers from a single method, while hypercubic lattice thresholds in the same dimensions are known to 8-11 digits (Mertens-Moore 2018).

## What counts as a win

Success means, for at least one d in 6..11, a value of eta_c for overlapping equal hyperspheres with stated one-sigma uncertainty at most one tenth of Torquato-Jiao's (d = 6: 5e-6; 7: 3e-6; 8: 6e-7; 9: 4e-7; 10: 3e-7; 11: 3e-8), such that (a) two estimators or methods agree within 3 combined sigma (for example wrapping-probability crossings on hypertori, and spanning or largest-cluster scaling, or a discrete-to-continuum extrapolation in the Brzeski-Kondrat manner), (b) the same code reproduces eta_c(3) = 0.34189 to within 1e-5, (c) data and code are released, and (d) a literature search immediately before claiming finds no published value for that d with smaller uncertainty. Agreement with Torquato-Jiao is not required, but a discrepancy above 3 sigma must be reported. Direction: smaller uncertainty.

## Partial wins

- **p1:** d = 3: eta_c with uncertainty <= 1e-6 under rules (a), (c) and (d), better than both Lorenz-Ziff and Brzeski-Kondrat, and resolving the 0.341889 vs 0.341935 disagreement.
- **p2:** Any d in 6..11 with uncertainty at most one third of Torquato-Jiao's, same rules.

## How a win is checked

Skeptic (< 1 hour): rerun the claimant's code at two system sizes in the claimed d with fresh seeds; check the overlap test (distance < diameter) and periodic wrapping in a toy configuration; refit the released crossing data; confirm the d = 3 reproduction.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/1208.3720>
- <https://doi.org/10.1088/1742-5468/ac6519>
- <https://doi.org/10.1063/1.1338506>
- <https://arxiv.org/abs/cond-mat/0203026>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- In high d, nearly all overlaps are between pairs; tree-like expansions (Torquato-Jiao's lower bound) give a control variate for the Monte Carlo.
- Cell lists in d >= 8 waste memory; use a k-d tree or random-shift hashing on coordinates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Wikipedia 4D/5D Brzeski-Kondrat numbers sit in the eta column but look like volume fractions; read the paper before comparing.
- eta_c, phi_c = 1 - exp(-eta_c) and the mean number of overlaps 2^d eta_c are different quantities; state which one is measured.
- Finite-size corrections in high d are large because the torus side is only a few diameters at feasible N; report the side length in diameters.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/overlapping-hyperspheres-percolation-d6-11.md
```

Already set up? Say `run V3R1T4S on overlapping-hyperspheres-percolation-d6-11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `overlapping-hyperspheres-percolation-d6-11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
