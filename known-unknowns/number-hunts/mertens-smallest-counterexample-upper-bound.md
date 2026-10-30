# Smallest Mertens counterexample: a certified bound below exp(3.485 x 10^18) (2026 claim under review), or below Kim-Nguyen's published exp(1.96 x 10^19)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days (BKZ-80..90 plus pruned enumeration in dimension about 140; 74,000 zeta zeros at 300 digits take under a core-day) · open as of 2026-10-30

## The problem

No explicit x with |M(x)| > sqrt(x) is known. Pintz (1987) made the 1985 disproof effective: with h_P(y) = 2 sum_{gamma < 14000} alpha exp(-1.5e-6 gamma^2) cos(gamma y - psi), any y in [e^7, e^50000] with |h_P(y)| > 1 + e^-40 gives x < exp(y + sqrt(y)) for the smallest counterexample x. Saouter and te Riele (2014) refined this to h_StR(y) = 2 sum_{gamma < 74000} alpha exp(-3e-9 gamma^2) cos(gamma y - psi), where |h_StR(y)| > 1 + 6e-8 suffices for practical y. Bounds: exp(3.21e64) (Odlyzko-te Riele data), exp(1.59e40) (Kotnik-te Riele 2006), exp(1.004e33) (Saouter-te Riele 2014), exp(1.017e29) (Rozmarynowycz-Kim, arXiv:2305.00345). The peer-reviewed record is from Seungki Kim and Phong Q. Nguyen (ANTS XVI, 2024; arXiv:2502.21021): BKZ-88 reduction plus pruned enumeration found y = 19571878850562201959.215107 with h_StR(y) = -1.007, so x < exp(1.96e19). That is far below Kotnik-van de Lune's conjectured location exp(5.15e23), and took 'barely half a day on a single core'. The paper says that 'an even lower bound ... may be attainable' with better parameters, and lists small refinements (perturbing y; the sharper x < exp(y + 2 sqrt(k y)) of Saouter-te Riele Lemma E). Wikipedia (edited 2026-03-15) still cites exp(1.96e19). A public repository, github.com/bzyzz/mertens_bound (last commit 2026-10-22, marked 'not peer-reviewed'), claims x < exp(3484971332733178124), about exp(3.485e18). Its lattice-found point v = 3484971332733132396.538... gives K_2 = 0.9957 at Saouter-te Riele's parameters, below 1. With Gaussian width k = 1.5e-10, summed over all 2,325,572 zeros below T0 = 1.3e6, it gives K_2 = 1.0003052504 +- 2.3e-11, using error terms J1..J6 re-derived for those parameters (E <= 2.4e-11) that no specialist has checked yet. Target: a certified upper bound smaller than that claim, or, by the published criterion alone, smaller than Kim-Nguyen's.

## What counts as a win

Success means a real y (or v), given exactly, evaluated in rigorous ball arithmetic over the complete zero list below the stated cutoff, that meets one of three criteria. The first is |h_StR(y)| > 1 + 6e-8 (Saouter-te Riele's published parameters). The second is |h_P(y)| > 1 + e^-40 with y in [e^7, e^50000] (Pintz). The third is the bzyzz/mertens_bound criterion at its stated (k, T0, T1) with its error bound E. The claim also gives the resulting bound B on the smallest counterexample, computed by the formula that goes with the criterion used. B must be STRICTLY SMALLER (direction: min) than exp(3484971332733178124), the smallest public claim on 2026-10-30. A claim that uses the bzyzz criterion inherits its unreviewed status and must say so. A claim that uses a new kernel or new error terms gives the full derivation, and the skeptic checks every inequality numerically. A refinement (Saouter-te Riele Lemma E, the |M(x +- n)| argument) counts only when compared with the same refinement applied to the record point. The skeptic re-evaluates h at y with independently computed zeros and re-checks the theorem's hypotheses (range of y, error margin). Before claiming, re-check arXiv, the Wikipedia page and the bzyzz/mertens_bound README for a newer record, and beat it.

## Partial wins

- **p1:** An independent certified re-evaluation of Kim-Nguyen's best y values (Tables 1-2) for h_P and h_StR, confirming or correcting their reported values to 3 decimals.
- **p2:** A certified y with |h_StR(y)| > 1 + 6e-8 and y < 1.0e20 that is not in Kim-Nguyen's tables (an independent hit of the same quality).
- **p3:** A bound below the published record by the published criterion alone: a certified y < 19571878850562201959.215107 with |h_StR(y)| > 1 + 6e-8 at Saouter-te Riele's own parameters (k = 3e-9, zeros below 74,000), so that exp(y + sqrt(y)) < exp(y_KN + sqrt(y_KN)) without relying on unreviewed error terms.
- **p4:** An independent check of the bzyzz/mertens_bound certificate, done with separately written code: either the ball-arithmetic K_2 sum at its point over all zeros below 1.3e6, or a numerical re-derivation of its error terms J1..J6 and the 1/zeta bound. The result either confirms it or documents a concrete error.

## How a win is checked

Compute zeros below 74,000 with Arb at 300 digits, complete by N(T). Evaluate h_StR(y) with an independent ball-arithmetic script and check the enclosure against 1 + 6e-8. Recompute B from the formula. This takes hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Mertens_conjecture>

## Sources

- <https://antsmath.org/ANTSXVI/papers/KimNguyen.pdf>
- <https://arxiv.org/abs/2502.21021>
- <https://zenodo.org/records/10775723>
- <https://arxiv.org/abs/2305.00345>
- <https://github.com/bzyzz/mertens_bound>
- <https://en.wikipedia.org/wiki/Mertens_conjecture>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the Kim-Nguyen Zenodo code: it builds the lattice (3.2) with parameters (N, nu, nu_y, nu_t) and runs enumeration around a target. A wider parameter sweep (they tried only a few N) is the cheapest lever.
- Their Figure 3: the best y are not the closest lattice points, so enumerate a ball and rank by the exact h rather than by distance.
- Bias the lattice toward small y: weight the y-coordinate more heavily so short vectors correspond to smaller y, since the bound is about exp(y).
- Hathi (2023) refined Saouter-te Riele's estimates (cited by Kim-Nguyen as not fully exploited); a sharper explicit lemma with a proof lowers the threshold below 1 + 6e-8 or allows a larger kernel.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The threshold is |h| > 1 plus a small margin, not |h| > 1; check the enclosure, not the midpoint.
- Pintz's theorem needs y in [e^7, e^50000]; Saouter-te Riele's h_StR needs its own range conditions (Lemma E). Check them.
- Comparing a refined bound for your y with the unrefined headline bound for Kim-Nguyen's y is a fake improvement.
- This bound says nothing about limsup |q|; it is the location of the first counterexample.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/mertens-smallest-counterexample-upper-bound.md
```

Already set up? Say `run V3R1T4S on mertens-smallest-counterexample-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mertens-smallest-counterexample-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
