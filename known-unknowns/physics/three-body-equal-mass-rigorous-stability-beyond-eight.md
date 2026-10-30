# Three-body problem: a computer-assisted proof of KAM (or linear) stability for an equal-mass periodic orbit other than the figure-eight, from the Hristov-Hristova-Tanikawa list of 971

⚛️ **Physics** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days per orbit (CAPD-style validated integration of the variational equations) · open as of 2026-10-30

## The problem

In the planar equal-mass zero-angular-momentum three-body problem, the figure-eight (Moore 1993, Chenciner-Montgomery 2000) is linearly stable and has been proven KAM-stable by computer (Tomasz Kapela and Carles Simo, Nonlinearity 20 (2007) 1241-1255). Kapela and Simo later gave a general computer-assisted method for KAM stability around arbitrary periodic orbits ('Rigorous KAM results around arbitrary periodic orbits for Hamiltonian systems', arXiv 1105.3235). They applied it to the figure-eight and to two orbits of the rotating-Eight family, which have non-zero angular momentum and are not in the list below. Milovan Suvakov and Veljko Dmitrasinovic (2013) found the linearly stable Bumblebee, Moth I, Moth II and Butterfly III; Dmitrasinovic, Hudomal, Shibayama and Sugita (2018) extended the list to 20, Li and Liao (2017) found hundreds of new periodic orbits, and Danya Rose (thesis) 25 linearly stable collisionless ones. Ivan Hristov, Radoslava Hristova and Kiyotaka Tanikawa (arXiv 2510.22802; New Astronomy 125, July 2026) found 971 initial conditions (685 distinct solutions) of linearly stable collisionless periodic orbits in the Martynova-Orlov-Rubinov domain. They publish 100-digit initial conditions and 40-digit monodromy eigenvalues and stability angles at db2.fmi.uni-sofia.bg/3bodystab971, grouped into four stability regions (Schubart/S 377, Intermediate-Moth 147, Figure-8 346, Broucke 101). All satisfy the order-4 non-resonance condition. They call them candidates for KAM-stable orbits, leave the twist condition to future work and write that it would be excellent to prove KAM stability rigorously as done for the figure-eight. Their stability checks are high-precision floating point, not interval proofs.

## What counts as a win

A computer-assisted proof (outward-rounded interval arithmetic) of KAM stability for at least one solution in the 971-row list that is not the figure-eight itself. Required: existence of the periodic orbit near the listed initial condition (interval Newton or Krawczyk on a Poincaré-section return map); ellipticity of the reduced monodromy (the nontrivial multipliers certified on the unit circle and distinct); non-resonance of the stability angles to the order the cited KAM theorem needs; and the cited theorem's twist (non-degeneracy) condition certified. For the two stability angles this is a certified non-zero determinant of the 2x2 matrix of first Birkhoff coefficients, or the exact twist quantity the cited theorem uses, as in Kapela-Simó 2007 and arXiv 1105.3235. The solution must not have a published rigorous KAM proof (literature search re-run before claiming).

## Partial wins

- **p1:** A computer-assisted proof of existence and linear stability (certified ellipticity of the reduced monodromy) for one listed solution other than the figure-eight, with no prior rigorous linear-stability proof found by a literature search.
- **p2:** The p1 certificate for at least one solution in each of the four stability regions of the list (in the Figure-8 region, a solution other than the figure-eight).

## How a win is checked

Skeptic: check that the certified initial condition lies within 1e-30 of the posted row of the 100-digit (vx, vy, T, T*) data file at db2.fmi.uni-sofia.bg/3bodystab971. Re-run the posted proof script with CAPD or another open-source validated ODE solver. Confirm the Krawczyk inclusion, the interval enclosure of the reduced monodromy eigenvalues on the unit circle, the non-resonance inequalities, and that the twist determinant (or the cited theorem's twist quantity) is certified non-zero. Hours per orbit.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2510.22802>

## Sources

- <https://arxiv.org/abs/2510.22802>
- <https://db2.fmi.uni-sofia.bg/3bodystab971/>
- <https://arxiv.org/abs/1105.3235>
- <https://arxiv.org/abs/1303.0181>
- <https://arxiv.org/abs/1705.00527>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The full monodromy has trivial multipliers equal to 1 from the energy, angular momentum and symmetries; ellipticity must be certified on the reduced (symplectically reduced or section) matrix, or the trivial block must be handled explicitly.
- Symmetry type II solutions appear as two rows with the same T*; they are one solution, not two.
- Scale-invariant period T* differs from T; use the normalisation of the data file.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/three-body-equal-mass-rigorous-stability-beyond-eight.md
```

Already set up? Say `run V3R1T4S on three-body-equal-mass-rigorous-stability-beyond-eight`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-body-equal-mass-rigorous-stability-beyond-eight`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
