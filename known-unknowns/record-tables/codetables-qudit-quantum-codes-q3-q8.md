# Qudit stabilizer codes [[n,k,d]]_q for q = 3, 4, 5, 7, 8: raise a lower bound in Grassl's extended tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Since May 2024 codetables.de has extended tables of bounds for qudit stabilizer codes [[n,k,d]]_q for q = 3,4,5,7,8 up to n = 100 (mainly based on Ezerman-Grassl-Ling-Ozbudak-Ozkaya, arXiv:2405.15057, and Bierbrauer-Edel twisted codes). These tables are young and far less mined than the qubit table: the qutrit table alone has 503 gap cells (d_lower < d_upper) for n <= 40 on 2026-10-28 (page last change 23.05.2024). The existing bank entry codetables-binary-linear counts a record in any codetables.de quantum-code table only as its partial win p1; this entry makes the non-binary qudit tables (q = 3,4,5,7,8) a full target. Claim a qudit record once, here.

## What counts as a win

Success means an explicit stabilizer generator matrix over GF(q) in symplectic form (n-k) x 2n such that an independent script verifies symplectic self-orthogonality exactly, rank n-k, and the exact minimum distance d (minimum symplectic weight over C^perp_s \ C, computed by full enumeration or two independent exact algorithms), with d STRICTLY GREATER (direction: max) than the lower bound for [[n,k]]_q in the live table obtained from http://www.codetables.de/QECC/Tables_color.php?q=<q^2>&n0=1&n1=100&k0=0&k1=100 re-fetched immediately before claiming, and no newer arXiv result giving d.

## Partial wins

- **p1:** Lower an upper bound d_upper for some [[n,k]]_q cell (q in {3,4,5,7,8}) via an exact, independently re-runnable certificate (an LP/shadow-type dual certificate verified in rational arithmetic, or an exhaustive non-existence search a skeptic re-runs), compared with the live table.

## How a win is checked

GF(q) arithmetic (q prime or GF(4), GF(8) via galois); symplectic inner product check; distance by enumeration of the symplectic dual modulo stabilizer (q^(n+k) vectors; feasible when n+k small) or by Brouwer-Zimmermann on the associated additive code; parse table HTML cell. Minutes to an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.codetables.de/QECC/index.html>

## Sources

- <http://www.codetables.de/QECC/index.html>
- <http://www.codetables.de/QECC/Tables_color.php?q=9&n0=1&n1=40&k0=0&k1=40>
- <https://arxiv.org/abs/2405.15057>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Hermitian/symplectic self-orthogonal quasi-twisted codes of index 2-4 over GF(q^2) (the construction that populated the tables); vary twist constants and generator polynomials systematically.
- Nearly self-orthogonal codes plus extension (the 2405.15057 method) applied to cells the paper did not reach.
- Propagation: apply lengthening/puncturing/shortening rules to any new code to improve neighbouring cells.
- Cross-domain import (number theory, algebraic curves): AG-code constructions from curves with many points (Hermitian, Suzuki) give self-orthogonal codes for q=4,8; compute small cases explicitly.
- Cross-domain import (evolutionary algorithms / LinCodeEvolve-style program search): evolve generator programs for QT codes with exact distance as fitness.
- Cross-domain import (combinatorial designs): codes from orbit matrices of designs / strongly regular graphs with self-orthogonality.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Table parameter q in URLs is q^2 (q=9 for qutrits); compare against the right local dimension.
- Degenerate vs pure distance: the table uses the stabilizer (degenerate) distance; compute that.
- Over GF(4) vs GF(2)^2 representation errors in symplectic form are a common false positive.
- Never sample codewords for distance.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/codetables-qudit-quantum-codes-q3-q8.md
```

Already set up? Say `run V3R1T4S on codetables-qudit-quantum-codes-q3-q8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `codetables-qudit-quantum-codes-q3-q8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
