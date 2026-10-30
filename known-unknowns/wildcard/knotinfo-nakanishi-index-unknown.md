# KnotInfo Nakanishi index: prove the Alexander module cyclic (index 1) for one of the 229 11- and 12-crossing knots listed [1;2]

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The Nakanishi index m(K) is the minimum size of a square presentation matrix of the Alexander module H_1 of the infinite cyclic cover, a module over Lambda = Z[t,t^-1]; m(K) = 1 exactly when the module is cyclic. KnotInfo (Charles Livingston and Allison Moore, knotinfo.org) records values from several sources: Nakanishi's computations via Kawauchi's book, Kearton-Wilson, Borodzik and Friedl's program Knotorious, 82 values by Castellano-Macias and Owad (arXiv:1908.01693), 77 [1,2] entries set to 1 by Ana Wright via algebraic unknotting number, and three 12-crossing knots (12a_504, 12a_642, 12n_278) settled by Tetsuya Ito (Arch. Math. 2025, arXiv:2501.15821). In database_knotinfo 2026.10.5, 229 entries are still '[1; 2]': 42 at 11 crossings and 187 at 12. For all of them the second Alexander polynomial is 1. In every case checked, the first elementary ideal of V - tV^T is the whole ring, so the module is cyclic after localising at every maximal ideal, and no residue-field rank count can show m = 2. Proving m = 1 needs an explicit global generator, which has a finite certificate: unimodular row and column operations over Lambda, allowing an identity block, that bring a presentation matrix to diag(1, ..., 1, Delta). Can such a certificate be found for one of the 229?

## What counts as a win

For a knot K whose nakanishi_index is '[1; 2]' in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming, and not settled in any paper the skeptic finds: let V be KnotInfo's seifert_matrix of K (n x n) and A = V - tV^T. A certificate that the Alexander module is cyclic: an integer k >= 0 and square matrices P and Q of size n + k over Z[t,t^-1], with det P and det Q units (+-t^j) checked by exact polynomial arithmetic, such that P * (A block-diagonal I_k) * Q = diag(1, ..., 1, f), where f is +-t^j times the Alexander polynomial of K. This sets m(K) = 1.

## Partial wins

- **p1:** Settle 10 or more of the 229 entries at m = 1, each with the certificate above, in one reproducible run.
- **p2:** A certificate as above for a knot that KnotInfo lists with Nakanishi index exactly 2, with inputs saved, demonstrating a table error.

## How a win is checked

Skeptic rebuilds A from the KnotInfo Seifert matrix and checks that det A reproduces the listed Alexander polynomial up to units. Skeptic then multiplies P (A + I_k block) Q exactly in Z[t,t^-1] and checks the diagonal form, and that det P and det Q are units. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/nakanishi_index.html>

## Sources

- <https://knotinfo.org/descriptions/nakanishi_index.html>
- <https://github.com/soehms/database_knotinfo>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: randomised unimodular row and column operations over Lambda (Euclid on entries with a unit leading or trailing coefficient), stabilising with an identity block when stuck.
- Conventional: search for a generator vector x with H_1 = Lambda x using Grobner bases over Z[t,t^-1], then extend it to the unimodular certificate.
- Conventional: an algebraic unknotting number of 1 (Fogel, Murakami) implies a cyclic module, so search for single 'algebraic crossing changes' of the Seifert form, as Ana Wright did with Knotorious.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- E_1 = Lambda (local cyclicity) does not prove cyclicity over Lambda, which is not a PID. That is exactly why these entries are open, so the certificate must be an explicit global diagonalisation.
- Rank counts of A over residue fields F_p[t]/(g) cannot certify m = 2 for these knots, because their first elementary ideal is the unit ideal. Do not claim 2 that way.
- Use the KnotInfo Seifert matrix and check that it reproduces the listed Alexander polynomial before building A.
- Check Ito (Arch. Math. 2025, arXiv:2501.15821) and any later preprint for knots already settled but not installed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-nakanishi-index-unknown.md
```

Already set up? Say `run V3R1T4S on knotinfo-nakanishi-index-unknown`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-nakanishi-index-unknown`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
