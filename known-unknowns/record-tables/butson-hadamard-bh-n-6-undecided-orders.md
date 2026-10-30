# Butson Hadamard matrices BH(n,6): settle one of the undecided even orders below 100 (46, 74, 86, 94)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (2-circulant cyclotomic constructions, SAT/ILP over orbit structures; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Butson Hadamard matrix BH(n,q) is an n x n matrix whose entries are q-th roots of unity with H H* = nI. For q = 6 there is no divisibility obstruction of Lam-Leung type, and F. Szöllősi conjectured that BH(2p,6) exists for every prime p. Czifra, Matolcsi and Szöllősi (arXiv:2511.11230, Nov 2025; J. Algebraic Combin. 64(2), 2026, Paper 29) gave a nonexistence criterion from positive definite functions on finite groups, found BH(18,14), and constructed 2-circulant BH(62,6), BH(82,6) and BH(146,6) from cyclotomic cosets; comparing the published tables, they state that BH(46,6), BH(74,6), BH(86,6) and BH(94,6) seem to be the remaining undecided even orders below 100, and that the smallest outstanding odd order is BH(31,6). Egan, Kotsireas, London and Ó Catháin restate the four even orders as open (arXiv:2610.27175, 19 Oct 2026, Problem 9). Egan and Ó Catháin's complete morphisms BH(n,7) -> BH(6n,6) (arXiv:2610.28394) do not reach these orders.

## What counts as a win

Success means an explicit n x n matrix with entries in the sixth roots of unity (given as exponents 0..5 of w = exp(2 pi i/6)) for n in {46, 74, 86, 94}, whose rows are pairwise orthogonal under the Hermitian inner product, checked exactly in Z[w] by two independent programs, where no BH(n,6) of that order is reported at claim time in a fresh arXiv search or in the latest version of arXiv:2610.27175 (direction: none; existence target). A rigorous nonexistence proof for one of these orders (for example the Czifra-Matolcsi-Szöllősi criterion with a certified computation the skeptic re-runs) also counts.

## Partial wins

- **p1:** An explicit BH(31,6), the smallest outstanding odd order according to arXiv:2511.11230, checked exactly as in the main criterion.

## How a win is checked

Store the matrix as exponents e_ij in Z_6. For each pair of rows r != s count c_m = #{j : e_rj - e_sj = m mod 6} for m = 0..5. Since w^2 = w - 1 and w^3 = -1, the inner product sum_m c_m w^m equals (c0 - c2 - c3 + c5) + w(c1 + c2 - c4 - c5), so orthogonality holds exactly when c0 + c5 = c2 + c3 and c1 + c2 = c4 + c5. Check every pair of rows with two independent programs; no floating point is needed.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2511.11230>

## Sources

- <https://arxiv.org/abs/2511.11230>
- <https://arxiv.org/abs/2610.27175>
- <https://arxiv.org/abs/2610.28394>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- 2-circulant cores over Z_p with entries assigned by cyclotomic cosets of F_p, the method of arXiv:2511.11230 for p = 31, 41 and 73; for p = 23, 37, 43 and 47 enumerate coset assignments exactly.
- Use the positive-definite-function criterion of arXiv:2511.11230 as a pruning test inside an exact search, or to attempt a nonexistence proof at one of the four orders.
- Model each entry as a variable in Z_6 and each row-pair condition as the two linear equations in the verification method; prescribe a group action to make SAT or ILP tractable.
- Any BH(n,3) is a BH(n,6); also look for group-invariant forms suggested by Gauss-sum constructions (Ong and Schmidt, arXiv:2609.22754).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- BH(62,6), BH(82,6) and BH(146,6) are settled. Real Hadamard matrices do not exist at these orders (n = 2 mod 4), and BH(n,4) matrices use a different alphabet.
- The undecided list in arXiv:2511.11230 is stated tentatively ('seem to be'); check the tables it compares before claiming.
- Numerical orthogonality to 1e-12 is not a proof; use exact counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/butson-hadamard-bh-n-6-undecided-orders.md
```

Already set up? Say `run V3R1T4S on butson-hadamard-bh-n-6-undecided-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `butson-hadamard-bh-n-6-undecided-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
