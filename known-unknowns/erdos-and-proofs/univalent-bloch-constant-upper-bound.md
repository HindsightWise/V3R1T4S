# Univalent Bloch-Landau constant B_u (C_57c): a slit domain with certified inradius/conformal-radius ratio below van Staden's 0.65628589

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 57c. B_u is the infimum, over univalent f on the unit disc with f'(0) = 1, of the inradius of f(D). Equivalently, any simply connected domain Omega and point w0 give the upper bound inradius(Omega) / conformal radius(Omega, w0). Lower bound: 0.5708858 (Brian Skinner 2009). Upper bounds from explicit slit discs: 0.658 (Robinson 1935), 0.65647 (Goodman 1945), 0.6564155 (Beller-Hummel 1985), 0.6563937 (Tom Carroll and Joaquim Ortega-Cerda 2009, theta-function formula), 0.656319277272* (Ortega-Cerda and Bharti Pridhnani 2010, numerical, no rigorous error analysis) and 0.65628589* (Wynand van Staden, preprints.org 202610.1936, 20 Oct 2026, unrefereed, merged into the page via PR #245 on 26 Oct 2026). Van Staden's domain is a disc of radius 5.001117628756668 minus 24 curved slits, invariant under rotation by 2pi/3 and complex conjugation (five base slits and their images). His computer-assisted proof certifies inradius <= 1 + 1e-9 by an exact covering and conformal radius >= 1.523726208329 by an Arb comparison function; code and certificates are at github.com/WynandVStaden/bloch-landau-slit-discs. The README cell reads '0.6563937 (0.65628589*)'. Every explicit domain is a checkable object, and the slit design space (more generations, curved slits, harmonic-symmetry arcs) is barely explored.

## What counts as a win

Success means an explicit simply connected domain Omega (finitely many slits or arcs with exact or rational parameters) and a point w0, with (a) a certificate that inradius(Omega) <= rho (every point of Omega lies within rho of the complement, by exact or interval covering) and (b) a rigorous lower bound R on the conformal radius of Omega at w0 (interval arithmetic or a comparison-domain argument). The ratio rho/R must be STRICTLY LESS (direction: min) than the smallest upper bound on https://teorth.github.io/optimizationproblems/constants/57c.html and in any open pull request touching constants/57c.md (currently 0.65628589*), both re-fetched immediately before claiming.

## Partial wins

- **p1:** A rigorous certificate (in the sense of the main criterion) for the Ortega-Cerda-Pridhnani 2010 domain, turning the numerical 0.656319277272 into a proven upper bound, or showing that its true certified ratio is larger than stated.
- **p2:** An independent re-certification of van Staden's 0.65628589 domain with a conformal-radius lower bound computed by a different method from his comparison function (for example a boundary-integral or Schwarz-Christoffel-type map with a posteriori error bounds), confirming the bound or locating a failure.

## How a win is checked

Skeptic: rebuild Omega from the stated parameters; rerun the inradius covering in exact or interval arithmetic and check that the covering discs reach every point of Omega. Recompute the conformal-radius lower bound with an independent method at two precisions, for example a numerical conformal map checked against van Staden's comparison function, and compare the ratio to the live record. Expected: under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/57c.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/57c.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/57c.md>
- <https://github.com/WynandVStaden/bloch-landau-slit-discs>
- <https://www.preprints.org/manuscript/202610.1936/v1>
- <https://arxiv.org/abs/0806.2282>
- <https://arxiv.org/abs/0809.2483>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Shape-optimisation import: parameterise slit shapes by splines and optimise the ratio with adjoint gradients of the conformal radius (computed by a fast boundary-integral solver), then certify the best design.
- Extend the harmonic-symmetry construction of Carroll and Ortega-Cerda with further generations of arcs, as the Polya-Tchebotarov connection suggests.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The inradius must be bounded for the whole domain, not only near the slits; long thin channels between slits can hide a larger inscribed disc.
- Numerical conformal radii without error bounds are estimates (the 2010 value is starred for exactly this reason).
- The conformal radius is taken at the chosen point w0; changing w0 without recomputing invalidates the certificate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/univalent-bloch-constant-upper-bound.md
```

Already set up? Say `run V3R1T4S on univalent-bloch-constant-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `univalent-bloch-constant-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
