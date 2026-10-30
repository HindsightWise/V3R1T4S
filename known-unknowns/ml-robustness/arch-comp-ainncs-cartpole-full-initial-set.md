# ARCH-COMP AINNCS CartPole (Balancing): verify or falsify 1e-3 settling of the neural controller on the full initial set

🛡️ **ML robustness** · standard · tractability ★★☆☆☆ · compute: laptop-hours (falsification: fast simulation of 500 control steps per trajectory; sound verification over 10 s with a 50 Hz controller: hours to days of reachability with splitting) · open as of 2026-10-30

## The problem

The CartPole benchmark ('Balancing' in the CROWN-Reach tables), proposed for ARCH-COMP24 and reused unchanged in 2025 and 2026, asks whether a neural controller balances an inverted pendulum on a cart precisely. Plant (benchmarks/CartPole/dynamics.m in https://github.com/Kiguli/ARCH-COMP2026): dx1/dt = x2, dx2/dt = 2f, dx3/dt = x4, dx4/dt = (0.08*0.41*(9.8*sin(x3) - 2f*cos(x3)) - 0.0021*x4)/0.0105, where x1 is the cart position, x3 the pole angle (0 = upright, not wrapped modulo 2*pi) and f the controller output. Controller: benchmarks/CartPole/model.onnx (PyTorch 2.1.2 export; input [1,4] = (x1, x2, x3, x4); Gemm-tanh-Gemm-tanh-Gemm followed by a final tanh, so f is in (-1, 1); output [1,1]; 19,185 bytes, sha256 ac10c817c994e8ee84dbf44ceffcf7380b7878ea467d2d17ff9fa38eee249529 as fetched on 2026-10-29), applied with zero-order hold every 0.02 s (specifications.txt: 'control period 0.02 s', t = 10 s, i.e. 500 control steps). Initial set X0 = [-0.1,0.1] x [-0.05,0.05] x [-0.1,0.1] x [-0.05,0.05]; property: for t > 8 s (the ARCH-COMP26 report writes t in [8 s, 10 s]) x1, x3 and x4 all lie in [-0.001, 0.001]. Status from the category reports: ARCH-COMP24 (EPiC vol. 103): CORA verifies only a smaller initial set, CROWN-Reach '?', NNV '?', and GoTube v2.0 'fully verifies' it but only statistically (confidence level 90%); ARCH-COMP25 (EPiC vol. 108) and ARCH-COMP26 (Sasaki et al., EPiC vol. 110, pp. 85-130, 2026-07-03): CORA verifies only the box with every radius at 40% of the original ('CartPole*'), CROWN-Reach reports 'Balancing ?' (6.4 s), JuliaReach and immrax report nothing. The 2026 report names CartPole as challenging for most tools because the high control frequency makes over-approximations conservative. No sound verification and no counterexample is published for the full box.

## What counts as a win

Success means ONE of the following for the unmodified benchmark (model.onnx, dynamics.m and specifications.txt from https://github.com/Kiguli/ARCH-COMP2026, sha256 recorded; zero-order hold with period 0.02 s and no extra delay: f_k = N(x(0.02k)) held on [0.02k, 0.02(k+1)) for k = 0,...,499). (F) FALSIFICATION: an initial state x0 written as exact decimals, inside the closed box X0 (checked exactly in rational arithmetic), and a time t* with 8 < t* <= 10 such that max(|x1(t*)|, |x3(t*)|, |x4(t*)|) >= 0.001 + 1e-6, where the trajectory is computed by the skeptic with N evaluated by onnxruntime CPU float32 and, in a second run, in float64 by a runtime that is not onnxruntime, and the ODE integrated between instants by two independent high-accuracy integrators (e.g. scipy DOP853 with rtol = atol = 1e-12, and an mpmath Taylor or Runge-Kutta integrator at 30 digits) that agree to 1e-9; the violation must hold in all four combinations. (V) VERIFICATION of the whole X0: a finite list of axis-aligned boxes whose union contains X0 (checked exactly) such that every box is proven to satisfy the property for all t in [8, 10] (continuous time) by a pinned public release of a sound set-based reachability tool (CORA, JuliaReach/ClosedLoopReachability.jl, CROWN-Reach, POLAR-Express, or immrax in zero-order-hold mode) re-run by the skeptic with the claimant's parameters and returning a verified verdict twice in a row, or by an explicit certificate (per-step state and control enclosures with validated flow enclosures, e.g. interval Picard-Lindelof or Taylor-model steps) that the skeptic's own interval code re-checks with outward rounding; statistical tools (GoTube), sampling and non-validated integration never count; the re-run must finish within 48 CPU-hours on a laptop. In both cases the live ARCH-COMP AINNCS report and repository, re-checked immediately before claiming (a newer ARCH-COMP27 report supersedes 2026), must not already list the full instance as verified or falsified, and a live web search must find no earlier sound verification or falsification of the full X0.

## Partial wins

- **p1:** A sound verification (same rules and re-run checks as (V), continuous time t in [8, 10]) of the centred sub-box with every half-width at least 60% of the original, i.e. [-0.06,0.06] x [-0.03,0.03] x [-0.06,0.06] x [-0.03,0.03] or any sub-box of X0 containing it, against CORA's published 40%-radius box (ARCH-COMP25 and 26).
- **p2:** A sound verification of the full X0 for the sampled-time version of the property only, at the 101 instants t = 8.00, 8.02, ..., 10.00, with each sampled state enclosed by a validated method and re-checked as in (V); reported as sampled-time and never as settling the benchmark.

## How a win is checked

Skeptic writes their own checker without reading the claimant's code: fetch the benchmark files, compare sha256 with the manifest, read the ONNX input shape ([1,4]) and output ([1,1]). For (F): check x0 in X0 with fractions; simulate 500 hold intervals with N from onnxruntime float32 and from onnx.reference float64, integrating each interval with scipy DOP853 (rtol = atol = 1e-12) and with an mpmath Taylor integrator; locate the maximum of max(|x1|, |x3|, |x4|) over (8, 10] by dense output plus local refinement; require >= 0.001 + 1e-6 in all four combinations. Report also the closed-loop equilibrium and the worst case over the 16 vertices and 10^4 random starts. For (V): check the cover exactly, then re-run the named tool on every box (versions, parameters, verdicts, CPU time) or run the skeptic's own interval checker on the certificate. Finally re-read the latest ARCH-COMP AINNCS report and web-search for later results. Minutes for (F), hours to two days for (V).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://easychair.org/publications/paper/GsKW>

## Sources

- <https://easychair.org/publications/paper/GsKW>
- <https://github.com/Kiguli/ARCH-COMP2026>
- <https://raw.githubusercontent.com/Kiguli/ARCH-COMP2026/main/benchmarks/CartPole/specifications.txt>
- <https://raw.githubusercontent.com/Kiguli/ARCH-COMP2026/main/benchmarks/CartPole/dynamics.m>
- <https://raw.githubusercontent.com/Kiguli/ARCH-COMP2026/main/benchmarks/CartPole/README.md>
- <https://easychair.org/publications/paper/Gc39>
- <https://easychair.org/publications/paper/WsgX>
- <https://gitlab.com/goranf/ARCH-COMP/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Linear analysis first: compute the closed-loop equilibrium (f = N(x*) with the sampled dynamics) and the Jacobian of the 0.02 s sampled map there. If x* is not within 1e-3 of the origin in x1, x3, x4, or if the slowest eigenvalue modulus rho gives rho^400 times the initial deviation above 1e-3 along that eigenvector, a counterexample sits near the corresponding corner of X0.
- Falsification by optimisation: differentiable simulation (torch, fixed-step RK4 at 1 ms inside each hold, then confirmation with the strict integrators) and maximisation of max(|x1|, |x3|, |x4|) over t in (8, 10] from the 16 vertices and Sobol starts.
- Verification by contraction rather than by a 500-step tube: find a quadratic Lyapunov function V = x'Px for the linearised sampled map, bound the nonlinear remainder (sin, cos, tanh network) on a small invariant ellipsoid with interval or CROWN bounds, and prove that every state of X0 enters the ellipsoid {V <= c} contained in the 1e-3 box before t = 8 s; only the transient needs reachability.
- Split smartly: CORA proves the 40%-radius box; split the remaining shell, starting with the pole-angle and angular-velocity extremes, and reuse CORA or JuliaReach parameters from the ARCH-COMP repeatability archive.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Control-period versus latency: the 2026 report says 'a latency of 0.02 s' while the repository files say 'control period 0.02 s'; this target uses the repository reading (zero-order hold, period 0.02 s, no extra delay). A claim valid only under another reading must say so and does not count.
- Sampled-time checks: the property must hold for every t in (8, 10], not only at multiples of 0.02 s; a sampled-time proof is p2 at most.
- Integration error and float32 rounding over 500 steps can create or hide a 1e-6-level violation; the two-integrator, two-runtime agreement is required.
- The angle x3 is not wrapped modulo 2*pi; the property is |x3| <= 0.001 literally.
- GoTube's 2024 'full verification' is statistical (90% confidence) and CORA's result covers only the 40%-radius box; neither settles the instance.
- The final tanh is part of the controller; the plant multiplies its output by 2 (x_acc = 2 m/s^2). Do not clip or rescale it again.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/arch-comp-ainncs-cartpole-full-initial-set.md
```

Already set up? Say `run V3R1T4S on arch-comp-ainncs-cartpole-full-initial-set`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `arch-comp-ainncs-cartpole-full-initial-set`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
