# Muonic molecular ions dd-mu and dt-mu: a lower variational energy for the weakly bound (J,v) = (1,1) states than Frolov's 2025 values (the (2,0) states of dd-mu, dt-mu and tt-mu are partial wins)

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (three-body exponential bases with L = 1 or 2 angular parts, quad or multiprecision arithmetic) · open as of 2026-10-30

## The problem

Muon-catalysed fusion is driven by the resonant formation of the weakly bound (J, v) = (1,1) states of the muonic molecular ions dd-mu+ and dt-mu+. These states have binding energies of about 1.975 eV and 0.660 eV, and their energies set the formation rates. Alexei M. Frolov (arXiv:2503.17389v1, 17 March 2025) computed the (1,1) states of dd-mu and dt-mu and the rotationally excited (2,0) states of dd-mu, dt-mu and tt-mu. He used three-body exponential expansions with up to 5,500 functions and the masses of his eq. (14): m_mu = 206.7682830 m_e, M_d = 3670.48296788 m_e, M_t = 5496.92153573 m_e. Energies are in muon-atomic units (hbar = m_mu = e = 1). His Table I, best rows: dd-mu (1,1), N = 3842: -0.47368672970969890623. dt-mu (1,1), N = 3842: -0.4819915265298649455. dt-mu (2,0), N = 5500: -0.500118077325475. dd-mu (2,0), N = 3700: -0.4887083249914. tt-mu (2,0), N = 3800: -0.5125686450010. He reports that his (1,1) results are about 1,000 times more accurate than his 2019 values (Phys. Lett. A 389, 1288). The binding energies he quotes (1.97498052811 eV and 0.66032991051 eV for the (1,1) states) can be reproduced from these totals and the muonic-atom energies -1/(2(1 + m_mu/M)). The (2,0) rows are still converging: tt-mu moves by 4e-10 between N = 3700 and 3800, and dd-mu by 3e-11. Earlier work at other mass values includes Korobov's three-body calculations, Kamimura (PRA 38, 621, 1988) and Vinitsky, Ponomarev and coworkers. Energies at different mass ratios are not comparable at these digit levels, so the record is defined for the eq. (14) masses.

## What counts as a win

Success means an explicit variational wavefunction for the (1,1) state of dd-mu or of dt-mu. It is a three-body Coulomb system with charges (+1, +1, -1) and exactly the masses of arXiv:2503.17389 eq. (14), in muon-atomic units with the centre of mass removed. The state has total angular momentum L = 1, natural parity (-1)^L, and, for dd-mu, the exchange symmetry (-1)^L under d <-> d. The energy must be the SECOND-lowest root of the generalized eigenproblem in that symmetry block (Hylleraas-Undheim-MacDonald: the second root bounds the (1,1) level from above). The checker's certified root must be STRICTLY LOWER (direction: min) than Frolov's Table I value for that state (-0.47368672970969890623 for dd-mu, -0.4819915265298649455 for dt-mu) by at least 1e-19. It must also be lower than any other published variational value for the identical masses found by a literature search immediately before claiming.

## Partial wins

- **p1:** A (2,0) cell: for dd-mu, dt-mu or tt-mu, with the same masses, L = 2, natural parity (exchange-symmetric spatial part for dd-mu and tt-mu), the lowest root of that block certified STRICTLY LOWER than Frolov's Table I value (-0.4887083249914, -0.500118077325475 or -0.5125686450010) by at least 1e-13.
- **p2:** An open, checkable certificate for either (1,1) state whose certified second root lies within 1e-15 of Frolov's Table I value, above or below. It is the first public reproduction, since Frolov releases no wavefunctions.

## How a win is checked

Checker (under an hour for a few thousand functions): build the basis with the declared angular coupling (e.g. Korobov's r1^l1 r2^l2 {Y_l1 x Y_l2}_LM exp(-a r1 - b r2 - c r12) with l1 + l2 = L). Compute the overlap and Hamiltonian matrices with the published closed-form three-body integrals in arb ball arithmetic at >= 40 digits, using the exact eq. (14) mass ratios. Solve the symmetric generalized eigenproblem, certify the required root (second for the (1,1) states, lowest for (2,0)) with an error ball, and compare it with the bar. Then recompute the binding energy with Frolov's factor 5626.451612133 eV per m.a.u. as a consistency check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2503.17389>

## Sources

- <https://arxiv.org/abs/2503.17389>
- <https://arxiv.org/pdf/2503.17389v1>
- <https://doi.org/10.1103/PhysRevA.38.621>
- <https://arxiv.org/abs/1806.05388>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Korobov's variational expansion with exponents drawn pseudo-randomly from several intervals (including very small ones for the long-range tail of the weakly bound state) is the standard tool for these states and needs no exotic integrals.
- The (1,1) state is very diffuse (a d or t nucleus far from a compact t-mu or d-mu atom): add a sub-basis with small exponents in the nucleus-atom distance, and optimise that sub-basis separately.
- The tt-mu and dd-mu (2,0) rows still move at 1e-10 to 1e-11 per 100 functions, so p1 should be within reach with a few thousand well-tempered functions in quad precision.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Masses: use exactly the eq. (14) values (m_mu = 206.7682830, M_d = 3670.48296788, M_t = 5496.92153573 m_e). The paper calls them CODATA 2022 values, but all three are the CODATA 2018 values (CODATA 2022 gives 206.7682827, 3670.482967655 and 5496.92153551). Never substitute a CODATA table lookup: any change in the last digits shifts the energies by far more than the margins, and results for other masses are not comparable.
- State identity: the (1,1) energy is the SECOND root in the L = 1 natural-parity block (the (1,0) state lies about 230 eV below it), and a lowest-root bound does not bound it.
- Frolov's Table I prints two columns headed dt-mu (2,0). They are one state continued to larger N (4,500-5,500). His text lists the (2,0) binding energies in the order 'dd-mu, dt-mu, tt-mu' as 102.65, 86.49 and 172.70 eV, but recomputation from the totals shows that 102.65 eV belongs to dt-mu and 86.49 eV to dd-mu.
- Binding energies in eV depend on the conversion factor; the success test is on the total energy in m.a.u.
- Earlier, more mature codes (Korobov's, Kamimura's) were run at other mass sets. Their published numbers are not the bar, but the literature search before claiming must also look for any recalculation at the eq. (14) masses.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/muonic-molecular-ions-weakly-bound-states-energies.md
```

Already set up? Say `run V3R1T4S on muonic-molecular-ions-weakly-bound-states-energies`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `muonic-molecular-ions-weakly-bound-states-energies`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
