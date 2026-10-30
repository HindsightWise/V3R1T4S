# Butson Hadamard catalogue n <= 21, q <= 17: settle an unknown cell (BH(15,12), BH(16,15), BH(17,12), BH(17,15), BH(19,15))

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (orderly generation, SAT over Z_q exponents, structured circulant/core searches; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Butson Hadamard matrix BH(n,q) is an n x n matrix whose entries are q-th roots of unity with H H* = nI. The online catalogue of Lampio, Ostergard and Szollosi (electronic supplement to Orderly generation of Butson Hadamard matrices, Math. Comp. 89 (2020) 313-331), the Aalto wiki page 'Matrices up to monomial equivalence' (created by F. Szollosi, last updated by P. Lampio on 17 November 2025, re-fetched 2026-10-30), gives for 2 <= n <= 21 and 2 <= q <= 17 the exact number of BH(n,q) up to monomial equivalence, 'E' (existence known) or 'U' (existence unknown); cells excluded by the Lam-Leung theorem are white (0). Czifra, Matolcsi and Szollosi (arXiv:2511.11230, J. Algebraic Combin. 64 (2026) Paper 29) filled the cell BH(18,14), which the page now shows as E. Five cells remain U: BH(15,12), BH(16,15), BH(17,12), BH(17,15) and BH(19,15). None of these is reachable from a smaller root of unity: for example BH(15,3) and BH(15,6) do not exist (catalogue zeros). Ong and Schmidt's Gauss-sum family (arXiv:2609.22754) only gives square orders q^2 with root order lcm(6, d), so it does not touch these cells. Settle one U cell by an explicit matrix or a certified non-existence proof.

## What counts as a win

Success means, for one (n,q) marked 'U' on the live page https://wiki.aalto.fi/display/Butson/Matrices+up+to+monomial+equivalence (re-fetched immediately before claiming), either (a) an explicit n x n matrix of exponents in Z_q whose rows are pairwise orthogonal, checked exactly in Q(zeta_q) by two independent programs, or (b) a non-existence proof whose computational part (exhaustive orderly generation with logs, or a DRAT/LRAT-checked UNSAT certificate on a CNF the skeptic regenerates) the skeptic re-runs; and a same-day arXiv search finds no earlier settlement of that cell (direction: none; existence target).

## Partial wins

- **p1:** An exact count up to monomial equivalence for a catalogue cell currently marked 'E' (existence known, count unknown), such as BH(13,12) or BH(14,8), produced by an orderly-generation or canonical-form enumeration that an independent implementation reproduces to the same count.
- **p2:** An explicit BH(26,22) or BH(30,26), instances p = 11, 13 of Conjecture 1 of arXiv:2511.11230 (BH(2p+4,2p) exists for every prime p), after the claimant shows that no such matrix is published, checked exactly as in the main criterion.

## How a win is checked

Store exponents e_rj in Z_q. For each pair of rows r != s form P(x) = sum_m c_m x^m where c_m = #{j : e_rj - e_sj = m mod q}; orthogonality holds exactly when P(x) is divisible by the cyclotomic polynomial Phi_q(x) over Q (integer polynomial remainder zero). Check all pairs with two independent programs; no floating point. For non-existence, regenerate the CNF or rerun the enumeration from the claimant's code and verify the certificate with drat-trim or cake_lpr.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.aalto.fi/display/Butson/Matrices+up+to+monomial+equivalence>

## Sources

- <https://wiki.aalto.fi/display/Butson/Matrices+up+to+monomial+equivalence>
- <https://arxiv.org/abs/2511.11230>
- <https://arxiv.org/abs/2609.22754>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lam-Leung vanishing-sum structure: for q = 12 or 15 each row inner product is a vanishing sum of q-th roots of unity, which decomposes into rotated regular 2-, 3- or 5-gons; enumerate admissible row types first.
- Positive-definite-function criterion of arXiv:2511.11230 as a pruning test or a route to non-existence.
- Core or 2-circulant ansatz for n = 16, 17, 19 (prime orders admit circulant cores with a border).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Cells are counted up to monomial equivalence; a non-existence claim must cover all matrices, not one normal form family, unless the reduction is proved.
- Numerical orthogonality is not a proof; use exact cyclotomic arithmetic.
- The page uses 'U' for unknown and 'E' for known existence; BH(18,14) changed from open to E in late 2025.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/butson-hadamard-small-catalogue-unknown-cells.md
```

Already set up? Say `run V3R1T4S on butson-hadamard-small-catalogue-unknown-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `butson-hadamard-small-catalogue-unknown-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
