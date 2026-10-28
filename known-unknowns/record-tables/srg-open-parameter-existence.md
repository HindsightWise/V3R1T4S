# MOONSHOT - Strongly regular graphs: construct an srg for an open parameter set in Brouwer's table

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Andries Brouwer's online tables list feasible parameter sets (v,k,lambda,mu) of strongly regular graphs up to 1300 vertices, marking each as known to exist, known not to exist, or unknown ('?'). On 2026-10-28 the pages for 51-1300 vertices contain 1,361 rows marked '?'; the smallest are srg(88,27,6,9), srg(99,14,1,2) (Conway's 99-graph, already a separate target), srg(100,33,8,12), srg(111,30,5,9), srg(115,18,1,3), srg(121,36,7,12) and srg(121,48,17,20). The table is actively maintained: recent entries credit Gritsenko for an srg(65,32,15,16), Jose Yip Zheng Ho for an srg(117,58,28,29) (open on the 2026-10-13 draft, now '+'), and 'Kovaľ + AI' and 'Akiyama + AI' for many non-existence and uniqueness results. Construct an srg for any parameter set currently marked '?', excluding (99,14,1,2), which is covered by its own target.

## What counts as a win

Success means an explicit adjacency matrix (or edge list) on v vertices that is k-regular, where every adjacent pair has exactly lambda common neighbours and every non-adjacent pair exactly mu, verified by two independent programs, for a parameter set that is marked '?' (existence unknown) in Brouwer's table at https://aeb.win.tue.nl/graphs/srg/srgtab.html (the relevant sub-page re-fetched live immediately before claiming), excluding srg(99,14,1,2), and with no construction or non-existence proof found by a fresh arXiv/Google Scholar search for those parameters. A graph for the complementary parameters counts for the same table row.

## Partial wins

- **p1:** A machine-checked non-existence proof for a parameter set currently marked '?' (for example via an exhaustive search with a DRAT/LRAT-checkable UNSAT certificate or an exact ILP certificate) that an independent checker re-verifies on a laptop.
- **p2:** A new graph for a row marked '+' (exists) whose number of known non-isomorphic graphs is listed as a single construction, with a canonical-form (nauty/Traces) certificate that it is not isomorphic to any graph the table or its cited sources already give.

## How a win is checked

Compute A^2 and check A^2 = k*I + lambda*A + mu*(J - I - A) with A symmetric 0/1, zero diagonal; this is O(v^3) and instant for v <= 1300. Recompute the eigenvalues and multiplicities and compare with the table row. Confirm the row still shows '?' on the live page and search arXiv for the parameters.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://aeb.win.tue.nl/graphs/srg/srgtab.html>

## Sources

- <https://aeb.win.tue.nl/graphs/srg/srgtab.html>
- <https://aeb.win.tue.nl/graphs/srg/srgtab51-100.html>
- <https://aeb.win.tue.nl/graphs/srg/srgtab101-150.html>
- <https://aeb.win.tue.nl/graphs/srg/srgtab151-200.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prescribed automorphism groups: assume a group G of order dividing v (or acting with few orbits) and solve for a union of orbitals with the right intersection numbers. This is the Kramer-Mesner trick from design theory and turns the search into a small exact cover / ILP.
- From coding theory: projective two-weight codes give srgs. Search for new two-weight codes over GF(q) with the right length and dimension (the table's comments name many such codes) using Kohnert-style prescribed-group ILP.
- From finite geometry: partial geometries, generalized quadrangles and hemisystems give srgs; for rows with geometric-looking parameters, search for the underlying point-line structure instead of the graph.
- Switching: Godsil-McKay or Wallis-Fon-Der-Flaass switching of known graphs with nearby parameters can produce graphs with new parameters; enumerate switching sets with a SAT solver.
- Cyclotomy and Cayley graphs on abelian groups of order v (partial difference sets): exhaust small unions of cyclotomic classes for prime-power v.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Building a graph for a parameter set already marked '+' or '-' and calling it new. Re-read the live row, including the complement row.
- Floating-point eigenvalue checks are not proof; use the exact matrix identity A^2 = kI + lambda A + mu(J-I-A).
- Conway's 99-graph srg(99,14,1,2) is a separate target; do not double-claim it here.
- A table-row non-existence claim produced by an unverified solver run is not a result; it needs a checkable certificate (partial win p1).
- The table is updated often (for example 'Kovaľ + AI' entries in 2026). Check the live page and recent arXiv for the exact parameters before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/srg-open-parameter-existence.md
```

Already set up? Say `run V3R1T4S on srg-open-parameter-existence`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `srg-open-parameter-existence`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
