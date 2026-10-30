# MOONSHOT - Congruent ellipsoids: a periodic packing denser than the Donev-Stillinger-Chaikin-Torquato SM2 crystal (0.770732, aspect ratios >= sqrt3)

⚪ **Packings and physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (event-driven or Monte Carlo compression of small periodic cells; certification in minutes) · open as of 2026-10-30

## The problem

Densest packing of congruent ellipsoids (semi-axes a, b, c) in R^3. An affine image of FCC, the densest lattice packing, gives only 0.7405. Bezdek and Kuperberg (1991) built non-lattice packings of elongated ellipsoids of density 0.7533, and Wills (1991) raised this to 0.7585. Donev, Stillinger, Chaikin and Torquato (Phys. Rev. Lett. 92, 255506 (2004), arXiv:cond-mat/0403286) found crystals with two ellipsoids per cell in different orientations, a family later named SM2 by Pfleiderer and Schilling (2007). SM2 beats the best lattice packing for a wide range of aspect ratios near the sphere and reaches 0.770732 for prolate and oblate spheroids with aspect ratio at least sqrt3 (or at most 1/sqrt3). The axis perpendicular to the layers can be rescaled without changing the density, so SM2 crystals of triaxial ellipsoids whose in-layer axes have ratio sqrt3 reach the same 0.770732. Jin, Jiao, Liu, Yuan and Li (Phys. Rev. E 95, 033003 (2017), arXiv:1608.07697) found a 24-particle square-triangle (SQ-TR) crystal. It beats SM2 for self-dual ellipsoids a:b:c = alpha:sqrt(alpha):1 with alpha in (1.365, 1.5625), with a maximum of about 0.75806 at alpha = 93/64, still below 0.770732. So 0.770732 is the densest known value for congruent ellipsoids of any shape. No upper bound close to it is known. Web and arXiv searches on 2026-10-30 found no denser packing published from 2017 to 2026.

## What counts as a win

Success means a periodic packing of congruent ellipsoids with exactly stated semi-axes (rational a >= b >= c) given by a rational lattice basis L and k ellipsoids, each with a rational centre and an orientation given by a rational quaternion. (1) Every pair within the cutoff 2a, including lattice images, has disjoint interiors, certified by a Perram-Wertheim witness: a rational lambda in (0,1) with contact function F(lambda) >= 1 + 1e-12, evaluated in exact rational arithmetic (F >= 1 for any lambda implies non-overlap). (2) The density k*(4/3)*pi*abc/|det L|, with pi enclosed by an interval, is STRICTLY GREATER (direction: max) than 0.770732 + 1e-6 and than any denser value published by verification time.

## Partial wins

- **p1:** A periodic congruent-ellipsoid packing with at least 3 ellipsoids per primitive cell in at least 3 distinct orientations and density >= 0.770732 - 1e-4, certified as in the main criterion. Two-orientation crystals do not count: SM2 crystals of spheroids, and their stretches along the layer normal (which include triaxial ellipsoids), already reach 0.770732.

## How a win is checked

Pure rational arithmetic. Build each ellipsoid matrix A_i = R_i diag(1/a^2,1/b^2,1/c^2) R_i^T from a rational quaternion, normalizing by |q|^2 exactly. Use F(lambda) = lambda(1-lambda) r^T [ (1-lambda) A_i^{-1} + lambda A_j^{-1} ]^{-1} r with r the centre difference. Check the supplied witness lambda exactly; any value F >= 1 certifies non-overlap. Enumerate lattice images with |r| < 2a. Compute |det L| exactly and compare the density lower bound with the bar. Calibrate by rebuilding SM2 at aspect ratio sqrt3 (rational approximation, slightly shrunk) and recovering about 0.7707.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Ellipsoid_packing>

## Sources

- <https://arxiv.org/abs/cond-mat/0403286>
- <https://arxiv.org/abs/1608.07697>
- <https://en.wikipedia.org/wiki/Ellipsoid_packing>
- <https://arxiv.org/abs/0909.0940>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Perram-Wertheim contact tests in floating point can pass for overlapping pairs at near contact; only an exact rational witness counts.
- Affine images of sphere packings never exceed 0.7405; any 'win' that is affine to FCC is a checker bug.
- Stretching an SM2 crystal along its layer normal gives triaxial ellipsoids at exactly the SM2 density; this is a known construction, not a new packing.
- The SQ-TR crystal (Jin et al. 2017) beats SM2 only for self-dual ellipsoids with alpha in (1.365, 1.5625), and stays below 0.770732; it is a shape-specific record, not the overall one.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/congruent-ellipsoids-densest-packing.md
```

Already set up? Say `run V3R1T4S on congruent-ellipsoids-densest-packing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `congruent-ellipsoids-densest-packing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
