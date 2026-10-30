# Are the pure quartic fields Q(13^(1/4)), Q(61^(1/4)) and Q(116^(1/4)) norm-Euclidean? (last open cases of Lemmermeyer's classification)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (Cerri-Lezowski Euclidean-minimum algorithm for a mixed-signature quartic field, unit rank 2) · open as of 2026-10-30

## The problem

Egami (Tokyo J. Math. 2 (1979)) proved, for m not of the form 2p^2, that only finitely many pure quartic fields Q(m^(1/4)) are norm-Euclidean. Lemmermeyer gave an elementary proof with the Behrbohm-Redei technique and showed that m must lie in {2, 3, 5, 7, 12, 13, 20, 28, 52, 61, 116, 436}. His survey 'The Euclidean algorithm in algebraic number fields' (update of Expo. Math. 13 (1995)) records m = 2, 5, 12, 20 as norm-Euclidean and m = 7, 28, 52, 436 as not, which 'leaves the open cases m = 3, 13, 61 and 116'. Since then, Pierre Lezowski's table of Euclidean minima (Bordeaux; algorithm in Math. Comp. 83 (2014) 1397-1426) gives Q(3^(1/4)) (discriminant -6912) as norm-Euclidean with M = 11/12. On 2026-10-30 the table's search page serves unexecuted PHP, but its SQLite file tables/table_euc.db downloads. The other three fields all have class number 1 in the LMFDB: Q(13^(1/4)) = 4.2.35152.1, Q(61^(1/4)) = 4.2.3631696.1, Q(116^(1/4)) = 4.2.1560896.1. None of them appears in Lezowski's table: its signature-(2,1) quartic part stops at |d| = 42591 and has no entry of discriminant -35152. Nothing deciding them was found on 2026-10-30. OEIS A187774 lists all twelve candidates as 'norm-Euclidean', which conflicts with Lemmermeyer's survey for m = 7, 28, 52 and 436.

## What counts as a win

CONFIRMED (full win) when norm-Euclideanity of Q(m^(1/4)) is decided for every m in {13, 61, 116}, each by one of two certificates. (i) Norm-Euclidean: a finite cover of a fundamental domain of K tensor R modulo O_K (coordinates in a stated Z-basis of the maximal order) by rational boxes, each paired with gamma in O_K, such that an interval-arithmetic upper bound of |N(x - gamma)| over the box is < 1; or an output of Lezowski's 2014 algorithm (critical points plus a covering) proving M(K) < 1. (ii) Not norm-Euclidean: an explicit xi in K with a finite certificate, in the Cerri-Lezowski framework (critical orbit under units plus a covering of its complement), proving |N(xi - gamma)| >= 1 for all gamma in O_K. For unit rank > 1, M(K) is attained at a point of K and is rational (Lezowski, Theorem 1.6), so one of the two certificates always exists. The verifier rechecks each certificate with independent interval-arithmetic code. Each field must still be undecided in the literature at verification time.

## Partial wins

- **p1:** A certificate as in (i) or (ii) for one of the three fields.
- **p2:** Certificates as in (i) or (ii) for two of the three fields, or a certified exact Euclidean minimum M(K), with its critical points, for one of them, independently recomputed.

## How a win is checked

Rebuild the maximal order (PARI nfinit(x^4-m)) and confirm the discriminants -35152, -3631696 and -1560896. Parse the boxes or critical points and verify the covering of the fundamental parallelotope exactly over Q. Bound |N(x - gamma)| on each box with arb/mpmath interval arithmetic, and recheck unit-orbit claims with exact arithmetic.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.maths.dur.ac.uk/users/alexander.stasinski/Student%20projects/2024-2025/Lemmermeyer.pdf>

## Sources

- <https://www.maths.dur.ac.uk/users/alexander.stasinski/Student%20projects/2024-2025/Lemmermeyer.pdf>
- <https://www.math.u-bordeaux.fr/~plezowsk/pdf/articles/algo.pdf>
- <https://www.math.u-bordeaux.fr/~plezowsk/tables/index.php?langue=en>
- <https://www.math.u-bordeaux.fr/~plezowsk/tables/table_euc.db>
- <https://www.lmfdb.org/NumberField/4.2.35152.1>
- <https://www.lmfdb.org/NumberField/4.2.3631696.1>
- <https://www.lmfdb.org/NumberField/4.2.1560896.1>
- <https://projecteuclid.org/download/pdf_1/euclid.tjm/1270216331>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Implement Cerri's algorithm for unit rank >= 2: unit actions shrink the search to a compact set, and local covering by boxes then terminates.
- Look first for small-denominator candidate points xi (denominators dividing small prime ideals) with |N(xi - gamma)| >= 1; Egami's and Lemmermeyer's non-Euclidean proofs for m = 7, 28, 52, 436 work this way.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Z[m^(1/4)] is not always the maximal order; use O_K.
- Lemmermeyer's survey predates Lezowski's table: m = 3 is settled there (M = 11/12). m = 13 is NOT settled: its class number is 1, not 2.
- Lezowski's HTML table served raw PHP on 2026-10-30; query table_euc.db (table euc, column euclidean < 0 means norm-Euclidean) with sqlite3 instead, by discriminant (disc is stored as text, e.g. '-35152').
- Floating-point norm bounds near 1 are not certificates; use interval arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/pure-quartic-norm-euclidean-61-116.md
```

Already set up? Say `run V3R1T4S on pure-quartic-norm-euclidean-61-116`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pure-quartic-norm-euclidean-61-116`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
