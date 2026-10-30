# Magic-state distillation footprint: a distance-4 T-to-T protocol on 8 or 9 qubits (known 8 <= N_T(4) <= 10), or distance 5 on at most 10 qubits

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (XOR-plus-CNF or structured enumeration over the 2^(N-1) - 1 possible check parts; by the n <= 54 classification of arXiv:2609.30860 a winning matrix needs 55 <= n <= 127 distinct columns at N = 8 and 55 <= n <= 255 at N = 9; the z3/CP-SAT run of arXiv:2606.07734 on N = 8 did not finish in two months) · open as of 2026-10-30

## The problem

In the compressed circuit form of triorthogonal-code magic-state distillation, an nT-to-1T protocol on N qubits is a binary N x n matrix G, with one column per pi/8 Pauli-Z-product rotation. Its first row has odd weight, its other rows have even weight, and every pair and every triple of rows overlaps in an even number of positions (Eq. 18 of arXiv:2606.07734). Its distance d is the fewest columns summing to e_1 = (1,0,...,0)^T (Eq. 19), and the output error scales as p^d. Hugo Jacinto, Xavier Valcarce, Victor Barizien, Elie Gouzien and Nicolas Sangouard (arXiv:2606.07734, v2 9 July 2026) define N_T(d) as the fewest qubits that reach distance >= d. Their exhaustive SAT search shows that no such protocol on fewer than 8 qubits exceeds distance 3. Their solver did not finish the N = 8, distance-4 instance after two months of runtime and found no distance-4 solution for N = 8 or 9. Their smallest protocols are distance 4 on N = 10 (lowest T-count 64, output error 495 p^4) and distance 5 on N = 11 (65T-to-1T, 7947 p^5). The 49-to-1 protocol of Sergey Bravyi and Jeongwan Haah (PRA 86, 052329 (2012), arXiv:1209.2426) uses 14 rows. Adam Wills, Shubham P. Jain and Shraddha Singh (arXiv:2609.30860, 25 Sep 2026; code and certificates at github.com/AWillsQuantum/generalised_triorthogonal_classification) then classified every generalised triorthogonal protocol with at most 54 columns and Z-distance >= 3. For one T output their Pareto frontier in (n, N) is (52, 10) and (48, 11) at distance 4 and (53, 11) and (49, 12) at distance 5. So within 54 columns nothing reaches distance 4 on N <= 9 rows or distance 5 on N <= 10. And 52 (distance 4, N = 10) and 53 (distance 5, N = 11) are the fewest T gates at those footprints. Distance >= 3 forces distinct nonzero check parts, so a winning matrix needs 55 <= n <= 2^(N-1) - 1 columns. Hence 8 <= N_T(4) <= 10 and 8 <= N_T(5) <= 11 remain open. For T-to-CCZ protocols (Eqs. 40 and 42), Jacinto et al. prove that distance 3 needs at least 8 qubits. They give a distance-3 47T-to-1CCZ protocol on 9 qubits and a distance-4 48T-to-1CCZ protocol on 10; the most compact distance-4 CCZ factory before them was a 64T-to-2CCZ protocol on 17 qubits. An 8-row CCZ protocol has five check rows and so at most 31 distinct columns. The n <= 54 classification therefore covers all of them and lists none of distance >= 3. So N_CCZ(3) = 9, while 9 <= N_CCZ(4) <= 10 is open.

## What counts as a win

Success means one of the following. (a) An explicit binary matrix G with N <= 9 rows (direction: min N; record N = 10) that satisfies Eqs. (18a)-(18d) of arXiv:2606.07734 exactly over F_2 and has distance d >= 4 by Eq. (19), i.e. no 1, 2 or 3 columns sum to e_1. (b) An explicit G with N <= 10 rows (record N = 11) that satisfies (18a)-(18d) with d >= 5. (c) A machine-checked proof that no G with d >= 4 exists for N = 9, which establishes N_T(4) = 10. Appending a zero row turns any 8-row solution into a 9-row one, so this also covers N = 8. The proof is either a published encoding plus an UNSAT certificate (DRAT, LRAT or FRAT) verified by an independent checker such as drat-trim or cake_lpr, or an exhaustive enumeration with a written completeness argument whose run is reproduced by a second, independent implementation. In every case, re-fetch arXiv:2606.07734 and arXiv:2609.30860 for newer versions and re-run an arXiv search immediately before claiming; none may already show the claimed footprint or proof.

## Partial wins

- **p1:** A T-to-CCZ protocol satisfying Eqs. (40a)-(40d) of arXiv:2606.07734, with distance by Eq. (42) over its seven undetectable patterns, of distance >= 4 on N = 9 qubits (by the classification of arXiv:2609.30860 it needs 55 <= n <= 63 columns). A certificate as in (c) that none exists on N = 9 also counts; it establishes N_CCZ(4) = 10. Distance 3 on N = 8 is already ruled out and does not count.
- **p2:** A certificate as in (c) for N = 8 alone at distance 4, which proves N_T(4) >= 9.

## How a win is checked

Use an independent script of about 30 lines (pure Python or numpy uint8 arithmetic mod 2). (1) Read G (N x n). (2) Check that row 1 has odd weight and rows 2..N have even weight. (3) Check that all C(N,2) pairwise and C(N,3) triple products have even weight. (4) Drop zero columns and pairs of equal columns. (5) Compute d: no column equals e_1; no two columns sum to e_1 (set lookup); no three do (for each pair, look up e_1 + c_i + c_j among the remaining columns). For distance-5 claims, extend to four columns with a table of pair sums. As a control, run the same script on the N = 10 and N = 11 matrices in Appendix D of arXiv:2606.07734 and on the (52, 10) and (53, 11) matrices in pareto_frontier.json of arXiv:2609.30860. For (c), rebuild the encoding from the claimant's generator and check the reduction: deleting a repeated pair of equal columns preserves (18) and cannot lower d, and for d >= 3 the check parts are distinct and nonzero. Check that the clauses or enumeration cover (18) and the forbidden <= d-1 sums. Verify the proof with drat-trim or cake_lpr, or reproduce the enumeration with a second implementation. As a pipeline test, reproduce the paper's UNSAT result for N = 7. Optionally recompute the output-error prefactor with the MacWilliams identity, as the paper does.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2606.07734>

## Sources

- <https://arxiv.org/abs/2606.07734>
- <https://arxiv.org/pdf/2606.07734v2>
- <https://arxiv.org/abs/2609.30860>
- <https://github.com/AWillsQuantum/generalised_triorthogonal_classification>
- <https://github.com/xvalcarce/compact_distillation>
- <https://arxiv.org/abs/1209.2426>
- <https://arxiv.org/abs/2107.09684>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The constraints are linear. (18a)-(18d) say that the sum over selected columns c of f(c) equals [f = c_1] for every monomial f of degree 1 to 3. So the selection vector over the 2^N - 1 nonzero column types lies in an affine subspace (a coset of a punctured Reed-Muller-type code). The search is XOR-SAT plus clauses forbidding small sums equal to e_1. That suits CryptoMiniSat with Gauss-Jordan elimination, or direct coset enumeration; z3 and CP-SAT, used in the paper, are not built around Gauss-Jordan XOR reasoning.
- Symmetry: the map c -> Ac, for any invertible A with A e_1 = e_1, sends solutions to solutions. Substituting linear forms keeps every polynomial at degree <= 3, keeps the coefficient of c_1, and fixes e_1. This group has order 2^(N-1) |GL(N-1,2)|; break it, for example by fixing a basis inside the support.
- Split each column into its logical bit and its check part y in F_2^(N-1). Distance >= 3 makes the check parts distinct and nonzero. The set Y of check parts (plus 0 when n is odd) then has indicator in RM(N-5, N-1), the Nezami-Haah correspondence used by arXiv:2609.30860. The set U of check parts whose logical bit is 1, together with 0, has indicator in RM(N-4, N-1). Distance >= 4 adds only that every line {a, b, a+b} inside Y meets U in 0 or 2 points. For N = 8 this is a search over RM(3,7) codewords of weight 56 to 128.
- The forbidden-sum condition makes the support behave like a cap-type set relative to e_1 in F_2^N. Large sum-free or Sidon-type sets in F_2^8 and F_2^9 are natural seeds.
- Start from the N = 10 matrices in Appendix D of arXiv:2606.07734 and the (52, 10) and (48, 11) matrices of arXiv:2609.30860. Try deleting a row while repairing parities by local search over column sets, keeping at least 55 columns.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Distance here is the protocol distance of Eq. (19): Z errors on injected T states that the N - 1 check qubits miss. It is not the full CSS distance of the associated triorthogonal code, which is a separate record (see the shortest-triorthogonal-code target).
- Eq. (18) treats Clifford corrections as free. T-to-CCZ protocols use Eqs. (40) and (42); keep the two cases separate.
- The paper's unrestricted SAT works in the C convention (Eqs. 15-16, all-ones logical). The G convention (Eqs. 18-19, e_1 logical) is related to it by Eq. (17). Check a claim in one convention only.
- Qubit recycling (Section VI) lowers the number of active qubits, for example 49-to-1 on 5 active qubits. It does not change N, which counts the rows of G.
- A solver timeout, or an UNSAT verdict without a proof certificate, proves nothing; the authors ran two months without convergence.
- Fewer T gates at a footprint already reached is not a win. arXiv:2609.30860 lists (52, 10) at distance 4 and (53, 11) at distance 5, and its classification shows that no protocol with fewer columns exists there.
- A candidate with N <= 9 and at most 54 columns would contradict the classification of arXiv:2609.30860. Re-check it, and the classification's stated scope (full row rank, distinct columns, exact distance), before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/magic-state-distillation-fewest-qubits.md
```

Already set up? Say `run V3R1T4S on magic-state-distillation-fewest-qubits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `magic-state-distillation-fewest-qubits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
