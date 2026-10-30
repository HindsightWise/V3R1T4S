# MOONSHOT - Three mutually orthogonal Latin squares of order 10 (is N(10) >= 3?)

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (SAT with proof certificates); partial wins laptop-days · open as of 2026-10-30

## The problem

N(n) is the largest number of mutually orthogonal Latin squares (MOLS) of order n. E. T. Parker constructed 2 MOLS(10) in 1959, and the nonexistence of a projective plane of order 10 together with Bruck's theorem gives N(10) <= 6. Whether 3 MOLS(10) exist is open: Bright, Keita and Stevens (Electron. J. Combin. 33(1) (2026), #P1.30, published 13 Feb 2026) call it a longstanding open problem. Known constraints: every square in such a triple has trivial symmetry group (McKay, Meynert and Myrvold), the code of any pair has rank exactly 37 (Dukes and Howard; Gill and Wanless), a 10 x 10 Latin square with a 5 x 5 subsquare has no orthogonal mate (Mann), and orthogonal 3 x 3 subsquares cannot extend (Parker). W. Myrvold (1999) split the case where one square has a 4 x 4 Latin subsquare into 28 mate-pattern type pairs and ruled out 20; Bright, Keita and Stevens re-derived those 20 by SAT and found explicit orthogonal pairs in each of the remaining 8, so those cases can only be closed by reasoning about the whole triple. The closest known near-triple (Egan and Wanless) has L1 orthogonal to both L2 and L3, with 91 of the 100 symbol pairs distinct when L2 and L3 are superimposed. This is a different problem from Erdős #723 (order 12), which the bank already lists.

## What counts as a win

CONFIRMED only for three 10 x 10 arrays over {0..9}, each a Latin square, such that each of the three pairs is orthogonal (superimposing the two squares gives all 100 ordered symbol pairs), checked by two independent programs, with no 3 MOLS(10) reported at verification time on https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p30 (re-fetched) or in a fresh arXiv search (direction: none; existence target). A proof that N(10) = 2, as a DRAT/LRAT certificate checked by drat-trim or cake_lpr on a CNF the skeptic regenerates from a documented encoding, also counts.

## Partial wins

- **p1:** A DRAT/LRAT certificate, on a CNF the skeptic regenerates from the encoding of Bright-Keita-Stevens or another documented one, that no orthogonal triple exists in at least one of Myrvold's eight remaining mate-pattern type pairs for a triple in which one square has a 4 x 4 Latin subsquare, provided that case is not already closed in the literature.
- **p2:** Three Latin squares L1, L2, L3 of order 10 with L1 orthogonal to L2 and to L3 such that superimposing L2 and L3 gives at least 92 distinct ordered symbol pairs (direction: max; Egan-Wanless: 91), checked exactly.

## How a win is checked

For each square check that every row and every column is a permutation of 0..9. For each pair (A, B) build the set {(A[i][j], B[i][j])} and require 100 elements. For p2, count the distinct pairs of L2 and L3 and recheck both orthogonalities with L1. For p1, regenerate the CNF from the stated encoding and case definition, run drat-trim (or cake_lpr for LRAT) on the supplied proof, and confirm the case matches Myrvold's classification as described in Section 2 of Bright-Keita-Stevens.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p30>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p30>
- <https://doi.org/10.37236/13960>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Transversal-representation encoding (Bright-Keita-Stevens): an orthogonal mate of L is a decomposition of L into 10 disjoint transversals; a third square needs 10 disjoint transversals common to the first two.
- Start from the orthogonal pairs found in Myrvold's eight open cases: search for 10 disjoint common transversals, and certify failures to earn p1.
- Build the known structure in as constraints: trivial autotopism groups, rank-37 codes for each pair, no 5 x 5 subsquares; break symmetry only over the full isotopy and conjugacy action.
- For p2, run local search over pairs (L2, L3) both orthogonal to a fixed L1, maximising distinct superimposed pairs, starting from the Egan-Wanless near-triple.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Orthogonal pairs of order 10 are plentiful; a pair alone is never a partial win.
- Every square in a 3 MOLS(10) has trivial symmetry group, so searches that assume an automorphism or autotopism are provably empty.
- N(12) and projective planes of order 12 belong to the separate Erdős #723 entry.
- A SAT 'UNSAT' answer without a checked certificate is not a result.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/three-mols-order-10.md
```

Already set up? Say `run V3R1T4S on three-mols-order-10`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-mols-order-10`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
