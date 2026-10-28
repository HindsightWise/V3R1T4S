# Equiangular lines: more equiangular lines in R^18, R^19, R^20 or R^42 than the best known

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The maximum number of equiangular lines in R^d is known exactly for d <= 17 and d = 21..41, 43 (OEIS A002853). Open cases include d = 18, 19, 20 and 42. On 2026-10-28 the best bounds are 57 <= a(18) <= 59 (lower bound Greaves-Syatriadi-Yatsyna 2021, arXiv:2104.04330; upper bound Greaves-Syatriadi, JCTA 2023, arXiv:2206.04267), 72 <= a(19) <= 74, 90 <= a(20) <= 94 (upper bounds Greaves-Syatriadi-Yatsyna 2020, arXiv:2002.08085) and 276 <= a(42) <= 288. The OEIS comment still gives a(18) <= 60, so it lags on the upper bound; its lower bounds are current. Lin, Munemasa, Taniguchi and Yoshino (arXiv:2503.06377, 2025) found at least 246,896 sets of 57 equiangular lines in R^18, and Munemasa, Szöllősi and Yoshino (arXiv:2606.10421, v2 Oct 2026) constructed further 57-line sets from Latin squares of order 6, but no larger set is known. A configuration is a Seidel matrix with smallest eigenvalue of multiplicity N - d, checkable exactly.

## What counts as a win

Success means a symmetric N x N Seidel matrix S (zero diagonal, +-1 off-diagonal) whose smallest eigenvalue lambda_min has multiplicity >= N - d, established in exact arithmetic (exact characteristic polynomial and exact rank of S - lambda_min*I over the field of lambda_min, via sympy or PARI), so that the N lines live in R^d; and N is STRICTLY GREATER (direction: max) than the larger of the lower bound stated in OEIS A002853 (https://oeis.org/A002853, re-fetched live immediately before claiming) and the best lower bound found in an arXiv search on the day.

## Partial wins

- **p1:** A configuration achieving the best known count in d = 19 (72 lines) or d = 20 (90 lines) that is not switching-equivalent to any configuration in the literature, certified by exact rank and a switching-class invariant (e.g. Seidel spectrum or canonical form of the associated two-graph).
- **p2:** A lowered upper bound: an exact, independently re-runnable certificate (exhaustive enumeration in exact arithmetic, or an SDP/LP dual certificate verified in rational arithmetic) proving a(18) <= 58, a(19) <= 73 or a(20) <= 93.

## How a win is checked

Load S; check symmetry/entries; compute exact characteristic polynomial (integer matrix, sympy or PARI) and the multiplicity of its smallest root via exact rank over the minimal polynomial's field; N - mult <= d. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A002853>

## Sources

- <https://oeis.org/A002853>
- <https://arxiv.org/abs/2206.04267>
- <https://arxiv.org/abs/2104.04330>
- <https://arxiv.org/abs/2002.08085>
- <https://arxiv.org/abs/2503.06377>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Greaves-style approach: enumerate Seidel matrices with prescribed characteristic polynomial modulo small primes (mod-4 / mod-p constraints) and extend cliques of compatible blocks.
- Start from known 57/72/90-line systems, apply switching and try to add lines via exact feasibility (each added line must keep the rank condition), using lattice/Gram completion.
- Cross-domain import (frame theory / signal processing): use alternating projection algorithms for Grassmannian frames to find near-equiangular numerical configurations, then round to +-alpha Gram entries and certify exactly.
- Cross-domain import (quantum information, SIC-POVM search): reuse numerical Gram-matrix optimisation pipelines and exact-recognition (PSLQ/LLL) from SIC research.
- Cross-domain import (spectral graph theory / two-graphs from strongly regular graph catalogues): search regular two-graphs and their descendants from Brouwer's SRG tables for large switching classes with the right spectrum.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Stale scoreboard: the OEIS comment lags the literature on upper bounds (it still says a(18) <= 60; Greaves-Syatriadi proved a(18) <= 59). Check the Greaves et al. papers and a fresh arXiv search before claiming.
- Numerical eigenvalue multiplicity is not proof; use exact arithmetic.
- Lines vs vectors: N lines means N unit vectors up to sign; antipodal duplicates do not count.
- Configurations in d dimensions that actually span fewer dimensions are still valid, but a rank miscount in floating point creates fake records.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/equiangular-lines-dims-18-20-42.md
```

Already set up? Say `run V3R1T4S on equiangular-lines-dims-18-20-42`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `equiangular-lines-dims-18-20-42`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
