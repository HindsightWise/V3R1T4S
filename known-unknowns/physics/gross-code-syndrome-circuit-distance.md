# Gross code syndrome extraction: settle the Strikis-Browne-Beverland conjecture that their depth-8 circuit has circuit distance 11, or reach 12 with an interleaved circuit

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (a refutation search takes hours; a proof needs an exact MaxSAT/ILP or UNSAT certificate on a detector error model with ~10^5 mechanisms, or on the much smaller extended code of the residual errors) · open as of 2026-10-30

## The problem

The [[144,12,12]] gross code (Bravyi et al., Nature 627, 778 (2024), arXiv:2308.07915; l = 12, m = 6, A = x^3+y+y^2, B = y^3+x+x^2) loses distance to hook errors in its syndrome-extraction circuit (SEC). By BP-OSD search, all 936 variants of the original syndrome cycle have circuit-level distance d_circ <= 10, and Bravyi et al. conjecture d_circ = 10 for their Eq. (9) cycle. Armands Strikis, Dan E. Browne and Michael E. Beverland (arXiv:2603.05481, v2 14 Sep 2026) proved several restrictions using residual-error and extended-code-distance bounds. No non-interleaved single-ancilla CNOT circuit reaches d_circ = 12 (Proposition 4), no uniformly tiled one reaches 11 (Proposition 5), and only three three-colour tilings survive (Proposition 6). They gave an explicit depth-8 three-colour-tiled left-right schedule (their Figure 12). They conjecture that it has d_circ = 11, since ten thousand outer loops of their minimum-weight search found no undetectable logical error below 11. They also prove that interleaving X and Z checks cannot lower circuit distance, and leave open whether any interleaved circuit reaches 12. They cite morphing circuits (Mackenzie H. Shaw and Barbara M. Terhal, PRL 134, 090602 (2025), arXiv:2407.16336) as reaching circuit distance twelve with the gross code's qubit counts. Shaw and Terhal report only a BP-OSD upper bound, d_circ <= 12, for end-cycle [[144,12,12]] codes with weight-9 checks derived from the [[288,12,18]] BB code. That is a different code and circuit family and does not settle this question. Circuit distance follows Strikis et al. Sec. II C. It is the fewest error mechanisms of standard circuit noise (each failing operation counted once) that flip no detector but flip a logical observable, in an m-round X- or Z-basis memory experiment followed by one perfect round. d_circ is the smaller of the two basis values.

## What counts as a win

Success means EITHER (a) or (b). (a) Take the Figure 12 schedule of arXiv:2603.05481v2 on the gross code's H_X and H_Z (Bravyi et al.). Compile it to a Stim circuit with standard circuit noise (Strikis et al. Sec. II C), for X- and Z-basis memory experiments with m noisy rounds and one perfect final round. Then exhibit, for some m <= 12, an explicit set of at most 10 error mechanisms that flips no detector and flips at least one logical observable (refuting the conjecture). Alternatively, give a machine-checkable proof that for m = 12 every such set, in either basis, has at least 11 mechanisms (confirming d_circ = 11). (b) Any CNOT-based SEC for the gross code with a single ancilla per check (interleaving of X and Z checks allowed, depth stated) with d_circ = 12 at m = 12, certified by such a proof. A proof is either an exact optimum of the minimum undetectable logical error problem, from a MaxSAT/ILP solver with optimality re-established independently, or an UNSAT certificate (DRAT/LRAT) for 'at most d-1 mechanisms', checked by drat-trim or cake_lpr. The proof may be on the detector error model. For non-interleaved circuits it may instead be on the extended code of the residual-error set, which Strikis et al. Theorem 1 shows equals d_circ, provided the residual set is re-derived from the circuit by code. Re-fetch arXiv:2603.05481 and search arXiv before claiming.

## Partial wins

- **p1:** A certified exact circuit distance of 10 (witness plus lower-bound proof as in (a)) for the original Bravyi et al. syndrome cycle at m = 12; only the upper bound d_circ <= 10 is published.
- **p2:** A certified d_circ = 11 (as in (a)) at m = 12 for any non-interleaved single-ancilla gross-code circuit other than Figure 12, showing that the bound of Proposition 4 is attained.

## How a win is checked

Rebuild the circuit from Figure 12's time-step labels and the check matrices of Bravyi et al.; BB144 matrices are also in github.com/PurePhys/LR-circuits/parity_check_matrices. Generate X- and Z-basis memory circuits in Stim and export the detector error model without decomposition. For a refutation, XOR the claimed columns: no detector bit may remain, some observable bit must flip, and there must be at most 10 columns. For a proof, rebuild the CNF or ILP from the DEM, or from the residual-error extended code, with the claimant's published script. Validate the encoding against brute force on small instances (m = 1 or 2, and the [[72,12,6]] code). Then check the UNSAT proof with drat-trim or re-solve to optimality with a second solver (for example Gurobi and SCIP, as benchmarked in arXiv:2603.22532). Stim's search_for_undetectable_logical_errors gives only upper bounds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2603.05481>

## Sources

- <https://arxiv.org/abs/2603.05481>
- <https://arxiv.org/abs/2308.07915>
- <https://arxiv.org/abs/2407.16336>
- <https://github.com/PurePhys/LR-circuits>
- <https://doi.org/10.5281/zenodo.18853600>
- <https://arxiv.org/abs/2603.22532>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For non-interleaved circuits, Strikis et al. Theorem 1 gives d_circ = d_ext(E), the extended-code distance of the residual-error set. That is a code-capacity distance problem on 144 qubits plus residual columns, far smaller than the full DEM. Certifying d_ext = 11 for the Figure 12 residual pattern by anchored cluster search (Rowshan-Devitt, arXiv:2609.39395) or exact MIP may be the shortest route to a proof.
- For a refutation, run BP-OSD searches with many random priors (Bravyi et al. Eq. (12)) and Stim's undetectable-error search on the DEM, focused on supports near the Figure 11 residual errors.
- For (b), interleaving can only help (their theorem). Search interleaved CNOT orders with a SAT/ILP model of hook propagation over the 72 checks of each type, scored by extended-code distance.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Circuit distance depends on the number of rounds m and on the noise model; use Strikis et al.'s standard circuit noise and state m.
- BP-OSD and Stim's undetectable-error search give upper bounds only.
- Morphing circuits (Shaw-Terhal) and flag-qubit circuits are different circuit families and do not count for (a) or (b).
- Figure 12 is a picture, and the paper's released Stim circuits (Zenodo 10.5281/zenodo.18853600) cover other codes only, so the gross-code circuit must be rebuilt by hand. Transcription errors in CNOT time steps silently change the circuit. Publish the transcribed schedule and check its residual pattern against Figure 11.
- Code distance 12 caps d_circ; a claimed value above 12 signals a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/gross-code-syndrome-circuit-distance.md
```

Already set up? Say `run V3R1T4S on gross-code-syndrome-circuit-distance`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gross-code-syndrome-circuit-distance`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
