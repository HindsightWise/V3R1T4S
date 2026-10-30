# ⚗️ Chemistry and materials

Quantum-chemistry benchmark sets, crystal and molecular structure records and materials benchmarks with mechanical scorers; no toxicity or weapon-relevant endpoints.

**8 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [JARVIS-Leaderboard single-entry materials tasks: halide perovskites (5 properties), MXene…](jarvis-single-entry-perovskite-mxene-phonon-dos.md) | harvest | laptop-hours |
| ★★★☆☆ | [JARVIS-Leaderboard QM9 (qm9_std_jctc, 130,829 molecules): beat ALIGNN's test MAE on one o…](jarvis-qm9-std-jctc-property-mae.md) | harvest | laptop-days (CPU training of a graph network on about 100k small molecules; a GPU shortens this to hours) |
| ★★★☆☆ | [JARVIS-Leaderboard catalysis adsorption energies (AGRA O, OH, CO, CHO, COOH and TinNet O,…](jarvis-agra-tinnet-adsorption-energy-mae.md) | harvest | laptop-hours |
| ★★★☆☆ | [Quantum-corrected Lennard-Jones clusters (Xe, Ar, Ne with harmonic zero-point energy): lo…](ccd-quantum-lj-zpe-rare-gas-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [CHIPS-FF on JARVIS-Leaderboard: a universal force field with lower MAE than all 16 listed…](jarvis-chipsff-umlip-defect-surface-elastic-mae.md) | harvest | laptop-hours to evaluate an existing open model; needs cluster to train a new one |
| ★★☆☆☆ | [Fullerene isomer counts: the number of fullerenes (OEIS A007894) or IPR fullerenes (A0468…](fullerene-isomer-counts-beyond-c400.md) | standard | laptop-days via the published oriented-count formula plus a symmetry-restricted count of the (under a million) achiral C402 fullerenes; needs cluster for brute-force generation (about 1.3e11 fullerenes, 2.6e11 oriented, at C400 alone) |
| ★★☆☆☆ | [SSUB experimental formation enthalpies on JARVIS-Leaderboard (1,726 compounds, compositio…](jarvis-ssub-experimental-formation-enthalpy-mae.md) | standard | laptop-hours |
| ★☆☆☆☆ | [Matbench v0.1 large tasks (mp_e_form, mp_gap, mp_is_metal): beat the best published Matbe…](matbench-large-mp-tasks.md) | standard | needs cluster (fine-tuning a pretrained model like JMP-L over 5 nested folds of 106k-133k structures takes GPU-days); the partial wins fit laptop-days on one GPU |

← [All categories](../README.md)
