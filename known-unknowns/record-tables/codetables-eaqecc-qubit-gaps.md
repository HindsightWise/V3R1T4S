# Entanglement-assisted qubit codes [[n,k,d;c]]: raise a lower bound in Grassl's EAQECC table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

codetables.de (Markus Grassl) hosts a table of bounds on the minimum distance of entanglement-assisted qubit codes [[n,k,d_lower-d_upper;c]] (non-catalytic setting) for n <= 64, last changed 10.07.2025. On 2026-10-28 the table has 7,752 parameter cells, of which 6,715 show a gap d_lower < d_upper; 5,354 of those gap cells have c >= 1, 616 of them with n <= 25 (e.g. [[5,2,3-4;3]], [[6,1,4-5;1]], [[7,0,5-6;4]]). Small-n gaps are within reach of exhaustive or SAT search; any explicit code with larger d is mechanically checkable. Only cells with c >= 1 count here: c = 0 cells are ordinary qubit stabilizer codes, covered by the codetables qubit entries already in the bank, and the companion qutrit table is its own bank target (eaqecc-qutrit-codetables-gaps).

## What counts as a win

Success means, for a cell with c >= 1, an explicit stabilizer matrix S over GF(2) in symplectic form, with n-k+c rows and 2n columns (the standard EA representation), such that an independent script verifies (1) GF(2)-rank of S is n-k+c, (2) the symplectic Gram matrix S Omega S^T has GF(2)-rank exactly 2c (so exactly c ebits are needed), and (3) the EA minimum distance d, defined as in the table (minimum symplectic weight of a vector in the symplectic dual of rowspace(S) that is not in rowspace(S) ∩ its symplectic dual), is computed EXACTLY by full enumeration; and d is STRICTLY GREATER (direction: max) than d_lower for (n,k,c) in http://www.codetables.de/EAQECC/qubit.php re-fetched live immediately before claiming, with d <= d_upper.

## Partial wins

- **p1:** Close a gap from above for a small cell (n <= 12): exhaustive, re-runnable non-existence search proving no [[n,k,d_upper;c]] code exists, lowering d_upper.

## How a win is checked

Symplectic linear algebra over GF(2) in Python (galois or hand-rolled bit ops); enumerate the symplectic dual of rowspace(S) (2^(n+k-c) vectors; feasible for n <= ~25) for minimum symplectic weight outside the isotropic part; parse the cell from the live table HTML (format [[n,k,dl-du;c]]2). Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.codetables.de/EAQECC/qubit.php>

## Sources

- <http://www.codetables.de/EAQECC/qubit.php>
- <https://arxiv.org/abs/2207.05647>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exhaustive search for small n via the classical-code correspondence: an EA qubit code with c ebits comes from any additive (n, 2^(n-k+c)) code over GF(4) whose symplectic Gram rank is 2c; search quasi-cyclic additive codes and compute both quantities.
- Start from best classical GF(4)-linear codes in codetables.de and choose c to trade ebits for distance (Brun-Devetak-Hsieh construction), then puncture/shorten using the table's propagation rules.
- SAT/ILP for small cells: encode existence of S with rank and weight constraints, solve with kissat with symmetry breaking (column permutations, local Cliffords).
- Cross-domain import (quantum chemistry graph states): EA codes with k=0 relate to graph states plus Bell pairs; use graph-state local-complementation orbit enumeration (as in Danielsen's database) to search.
- Cross-domain import (machine learning for code search, RL decoders): use a learned surrogate of min-distance from symplectic-weight enumerator features to prioritise candidates before exact checks.
- Cross-domain import (lattice basis reduction): search over Construction-A lattices of the codes and use short-vector counts as a quick distance proxy.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The EA distance definition (catalytic vs non-catalytic, degenerate vs not) must match the table's explanation; the table states the non-catalytic setting.
- Propagation rules in the table (subcode, lengthening, puncturing, teleportation) mean a new code in one cell may already be implied; the claim must beat the live d_lower of its own cell.
- A code where the Gram rank is not exactly 2c uses a different number of ebits and belongs to another cell.
- Distance by random sampling of logical operators is not a proof; enumerate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/codetables-eaqecc-qubit-gaps.md
```

Already set up? Say `run V3R1T4S on codetables-eaqecc-qubit-gaps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `codetables-eaqecc-qubit-gaps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
