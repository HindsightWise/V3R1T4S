# ARCH-COMP AINNCS 2D Spacecraft Docking: verify or falsify the neural controller on the full initial set (unsolved since ARCH-COMP22)

🛡️ **ML robustness** · standard · tractability ★★★☆☆ · compute: laptop-hours (falsification search: millions of exact closed-loop simulations per hour on CPU; sound verification by box splitting with a reachability tool or an interval certificate: hours) · open as of 2026-10-30

## The problem

The 2D Spacecraft Docking benchmark of the ARCH-COMP friendly competition, category AINNCS (neural-network control systems), asks whether a reinforcement-learned controller keeps a deputy spacecraft under a distance-dependent speed limit. Plant (benchmarks/Docking/dynamics.m in https://github.com/Kiguli/ARCH-COMP2026): linear Clohessy-Wiltshire relative motion, d(sx)/dt = vx, d(sy)/dt = vy, d(vx)/dt = 2n*vy + 3n^2*sx + Fx/m, d(vy)/dt = -2n*vx + Fy/m, with m = 12 kg and n = 0.001027 rad/s. Controller: benchmarks/Docking/model.onnx (tf2onnx export, opset 9; input [batch,4] = (sx, sy, vx, vy); a linear pre-processing layer, two hidden layers of 256 tanh units, a linear output layer, a linear post-processing layer and a final tanh; output [batch,2] = (Fx, Fy); 274,562 bytes, sha256 cc46c45e5ee7a0a5df433d31b19089cebe2ae64aeb6a0dc7ec47e51818368bf7 as fetched on 2026-10-29), applied with zero-order hold every 1 s. Initial set X0 = [70,106] x [70,106] x [-0.28,0.28] x [-0.28,0.28] (benchmarks/Docking/specification.txt); property (14): sqrt(vx^2 + vy^2) <= 0.2 + 2n*sqrt(sx^2 + sy^2) for all t in [0, 40] s. History, from the category reports: introduced in ARCH-COMP22 (Manzanas Lopez et al., EPiC vol. 90), where POLAR computed reachable sets for four corner sub-boxes without finding a violation and the report says 'The benchmark has not been fully verified'; ARCH-COMP23 (Manzanas Lopez, Althoff, Forets, Johnson, Ladner and Schilling; EPiC vol. 96, pp. 89-125): CORA 'UNKNOWN' (its reachable set explodes), JuliaReach proves it only for [87,89]^2 x [-0.01,0.01]^2, NNV no result; ARCH-COMP24 (EPiC vol. 103, pp. 64-121): CORA '?', NNV '?', JuliaReach proves it only for [70,106]^2 x [-0.14,0.14]^2, GoTube v2.0 verifies a half-radius set only and only statistically (confidence level 90%); ARCH-COMP25 (EPiC vol. 108, pp. 71-121): CORA '?', JuliaReach '?'; ARCH-COMP26 (Sasaki, Wooding, Johnson, Althoff, Benet, Coogan, Forets, Harapanahalli, Koller, Ladner, Schilling, Zhang, Zhong; EPiC vol. 110, pp. 85-130, published 2026-07-03, doi 10.29007/637n): CORA '?' (its reachable set 'explodes over time'), JuliaReach '?' (again proven only for velocities in [-0.14,0.14]), CROWN-Reach and immrax report no result, and the report says the nonlinear safety specification 'causes the benchmark to remain unsolved one more year'. Simulations reported by POLAR, CORA and JuliaReach show no violation, yet no sound proof and no counterexample exists for the full box. The constraint is tight at the near corner: at (70, 70, +-0.28, +-0.28) the speed is 0.39598 m/s against a limit of 0.40334 m/s (slack 0.0074 m/s), while the tanh-bounded force changes each velocity component by at most about 1/12 m/s per second, so the first control intervals decide. Jafarpour, Harapanahalli and Coogan (arXiv:2307.14938v3) report the property verified 'starting from four different initial sets' with Euler integration of an embedding system (step 0.1 s), not for the full box with validated integration. Either outcome (a counterexample or a sound proof for the full X0) settles the instance.

## What counts as a win

Success means ONE of the following for the unmodified benchmark (model.onnx, dynamics.m and specification.txt from https://github.com/Kiguli/ARCH-COMP2026, sha256 of all three recorded; zero-order hold with a 1 s period: at each instant k = 0,...,39 the force u_k = N(x(k)) is computed from the state at time k and held constant on [k, k+1)). (F) FALSIFICATION: an initial state x0 = (sx, sy, vx, vy) written as exact decimals, with x0 in the closed box X0 checked exactly in rational arithmetic, and a time t* in [0, 40], such that g(x(t*)) = sqrt(vx^2 + vy^2) - 0.2 - 2*0.001027*sqrt(sx^2 + sy^2) >= 1e-6, where the trajectory is computed by the skeptic with the plant integrated exactly between instants (closed-form matrix-exponential solution of the linear ODE in at least 50-digit arithmetic) and N evaluated (i) by onnxruntime CPUExecutionProvider in float32 on the float32-rounded state and (ii) in float64 by a second runtime that is not onnxruntime (onnx.reference.ReferenceEvaluator or a torch re-implementation of the same weights); the violation g >= 1e-6 must hold at some t in [0, 40] in both runs. (V) VERIFICATION of the whole X0: a finite list of axis-aligned boxes whose union contains X0 (checked exactly in rational arithmetic) such that every box is proven safe for all t in [0, 40] (the continuous interval, not only the 41 instants) either (V-a) by a pinned public release of a sound set-based reachability tool (JuliaReach/ClosedLoopReachability.jl, CORA, CROWN-Reach, POLAR-Express, or immrax run in zero-order-hold mode), re-run by the skeptic with the claimant's stated parameters on the unmodified network, returning a verified/satisfied verdict twice in a row; statistical tools (GoTube), sampling and non-validated integration never count; or (V-b) by an explicit interval certificate that the skeptic's own code re-checks: per box and step k, state enclosures B_k (B_0 containing the box) and force enclosures U_k with N(B_k) inside U_k proven by the skeptic's float64 interval or CROWN bound computation, exact-flow images of B_k x U_k at time k+1 inside B_{k+1} (or inside a listed union of boxes that are themselves certified onward), and property (14) proven for all t in [k, k+1] from B_k x U_k by interval arithmetic with outward rounding; the whole re-run of (V-a) or (V-b) must finish within 24 CPU-hours on a laptop. In both cases the live ARCH-COMP AINNCS report and benchmark repository, re-checked immediately before claiming (a newer ARCH-COMP27 AINNCS report supersedes the 2026 one), must not already list the instance as verified or falsified, and a live web search must find no earlier published sound verification or falsification of the full X0 (if one exists, the result is a replication).

## Partial wins

- **p1:** A sound verification (same rules and re-run checks as (V-a) or (V-b), continuous time t in [0, 40]) of the sub-box [70,106] x [70,106] x [-0.21,0.21] x [-0.21,0.21], or of any sub-box of X0 containing it: velocity half-width 0.21 (75% of the original radius) against the largest published sound result, JuliaReach's [-0.14,0.14]^2 (ARCH-COMP24, 25 and 26).
- **p2:** A sound verification of the full X0 for the sampled-time version of property (14) only, i.e. at the 41 instants t = 0, 1, ..., 40, with every sampled state enclosed by a validated method and re-checked as in (V-a) or (V-b); reported as sampled-time and never as settling the benchmark.

## How a win is checked

Skeptic writes their own checker without reading the claimant's code: fetch the three benchmark files from the repository and compare sha256 with the claimant's manifest. For (F): parse the decimal x0 and check membership in X0 with fractions; precompute e^A and G = integral_0^1 e^(As) ds B with mpmath at 50 digits; iterate x_{k+1} = e^A x_k + G u_k with u_k from onnxruntime (float32) and, separately, from onnx.reference in float64; inside each hold interval evaluate g on a fine grid around the claimed t* and refine by local maximisation of the exact flow e^(At) x_k + G(t) u_k; require g >= 1e-6 in both runs. Also run the 16 vertices and 10^5 random initial states and report the largest g seen. For (V): check the cover exactly (recursive splitting of X0 against the box list in rational arithmetic), then either re-run the named tool release on every box with the stated parameters (record versions, wall time, verdicts) or run the skeptic's own interval checker over the certificate (enclosure of N by float64 IBP or auto_LiRPA CROWN with outward slack, containment of the affine images, and an interval bound of g over each hold interval). Finally grep the latest ARCH-COMP AINNCS report on easychair.org and the repository for the Docking row, and web-search for later papers. Minutes for (F), hours for (V).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://easychair.org/publications/paper/GsKW>

## Sources

- <https://easychair.org/publications/paper/GsKW>
- <https://github.com/Kiguli/ARCH-COMP2026>
- <https://raw.githubusercontent.com/Kiguli/ARCH-COMP2026/main/benchmarks/Docking/specification.txt>
- <https://raw.githubusercontent.com/Kiguli/ARCH-COMP2026/main/benchmarks/Docking/dynamics.m>
- <https://easychair.org/publications/paper/Gc39>
- <https://easychair.org/publications/paper/WsgX>
- <https://easychair.org/publications/paper/Vfq4b>
- <https://easychair.org/publications/paper/C1J8>
- <https://juliareach.github.io/ClosedLoopReachability.jl/dev/models/SpacecraftDocking>
- <https://arxiv.org/abs/2307.14938>
- <https://gitlab.com/goranf/ARCH-COMP/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Falsify first, where the slack is smallest: near sx = sy = 70 with |vx| = |vy| = 0.28 the margin is 0.0074 m/s at t = 0. Maximise g over x0 and over t inside the first few hold intervals with exact linear propagation and gradients through the smooth tanh network (multi-start gradient ascent, CMA-ES), remembering that g can peak between two control instants.
- Exploit linearity: between instants the state is an exact affine function of (x_k, u_k), so one closed-loop step is an affine image of the state box plus an enclosure of N; a custom zonotope or box propagation with CROWN linear bounds of the tanh network (auto_LiRPA) and recursive splitting is cheap and yields a (V-b) certificate directly.
- Spend the splitting budget where it matters: JuliaReach already proves |vx|, |vy| <= 0.14 for all positions, so split the outer velocity shell and the near-distance region (sx, sy close to 70) where the speed limit is lowest; use the published JuliaReach and CORA parameters from the ARCH-COMP repeatability archive as a starting point.
- Make the nonlinear property cheap to bound: check vx^2 + vy^2 <= (0.2 + 2n*sqrt(sx^2 + sy^2))^2 on enclosures, using monotonicity of sqrt on an interval bound of sx^2 + sy^2, and bound the in-interval flow with a first-order Taylor model in t.
- If simulations stay safe everywhere, look for an inductive invariant instead of a 40-step tube: a set S containing X0's future after a few steps, with the one-step image of S inside S and property (14) on S, verified once with CROWN bounds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Checking only the 41 control instants: the property is over continuous time and g can be maximal between instants. A sampled-time proof is p2 at most.
- Statistical or sampled verification (GoTube, Monte Carlo, Lipschitz-free sampling) and Euler integration without error bounds are not sound and never count.
- Continuous feedback is not the benchmark: the 2025 and 2026 reports note that immrax interprets benchmarks as continuous feedback; this instance is zero-order hold with a 1 s period.
- The ONNX includes pre- and post-processing layers and a final tanh; dropping them or using the bare 256x256 core changes the controller. Inputs are (sx, sy, vx, vy) in that order and outputs are forces in newtons divided by m = 12 in the plant.
- float32 and float64 controller evaluations can disagree on tiny-margin violations; the 1e-6 margin in two runtimes is required.
- A cover with gaps, or with boxes slightly inside X0 (105.999 instead of 106), fails the exact cover check.
- Do not mistake partial results for the instance: POLAR's 2022 four corner sub-boxes (reachable sets without a violation), JuliaReach's [87,89]^2 x [-0.01,0.01]^2 box (2023) and half-velocity box (2024-2026), GoTube's statistical half-radius result, and the four initial sets of Jafarpour et al. (shown only in their Fig. 6, with non-validated Euler integration) do not settle the full box. Papers that adapt the docking model with a different controller or initial set are different problems: POLAR-Express (Wang et al., arXiv:2304.01218) verifies a variant with a 2x64 tanh controller, extra inputs and x, y in [24, 26] at a fixed velocity, and Wang, Seiler, Dullerud and Hu (arXiv:2609.22576) use an LQR plus NN-residual controller.
- Installing Julia or MATLAB (CORA) is the human's decision; Python-only routes are CROWN-based custom propagation for (V-b) or immrax in zero-order-hold mode.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/arch-comp-ainncs-docking-full-initial-set.md
```

Already set up? Say `run V3R1T4S on arch-comp-ainncs-docking-full-initial-set`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `arch-comp-ainncs-docking-full-initial-set`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
