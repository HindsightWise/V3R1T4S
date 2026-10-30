# Quantum Latin squares: realise an 'uncertain' cardinality for order 7, 9, 11 or 23 (Zhang-Lv-Cao Table 6)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (exact-arithmetic constructions; numerical search for seeds) · open as of 2026-10-30

## The problem

A quantum Latin square QLS(v) is a v x v array of unit vectors in C^v whose every row and every column is an orthonormal basis. Its cardinality c is the number of distinct vectors up to a global phase (Paczos et al.), so v <= c <= v^2, and c = v+1 never occurs. Yuyuan Zhang, Mingzhen Lv and Haitao Cao (arXiv:2607.19969 v2, 23 Jul 2026) prove that every c in [v, v^2] except v+1 is attained for all v >= 8 except v = 9, 11, 23. With known results for v <= 5 and order 6 now closed (Zhipeng Xu, arXiv:2607.11800, and Das-Kumar, arXiv:2608.12607, cardinality 29), the open orders are 7, 9, 11 and 23. Their Table 6 lists the uncertain cardinalities: v=7: 24-27, 29-42 and 45; v=9: 34, 60-62, 65-71, 73, 74; v=11: 13-19, 21, 48, 50, 54-115 (except 105, 111, 112) and 119; v=23: 528. Table 6 lists 105, 111 and 112 for v = 11 as both attainable and uncertain, so treat those three as attainable.

## What counts as a win

Success means an explicit QLS(v) for v in {7, 9, 11, 23} whose cardinality c lies in the uncertain set of Table 6 of arXiv:2607.19969 (latest version, re-fetched immediately before claiming), with c not settled by any later paper (search arXiv for 'quantum Latin square' cardinality at that order). Entries must be given exactly: algebraic numbers in a stated number field, for example cyclotomic or quadratic surds. Two independent exact-arithmetic programs must confirm that every row and every column is an orthonormal basis and that exactly c distinct rays occur.

## Partial wins

- **p1:** A numerical QLS(v) for an uncertain (v, c) with entries to at least 30 significant digits, every row and column orthonormal to residual below 1e-25, and the c rays pairwise separated (1 - | < u,w > | > 1e-6 for distinct rays, below 1e-25 for identified ones), without an exact certificate. This is a PROMISING result, not CONFIRMED.

## How a win is checked

Parse the exact entries. For each row and each column, check <u_i, u_j> = delta_ij exactly. Two unit vectors are the same ray iff | < u,w > | = 1; group the v^2 entries into rays exactly and count them. Use two independent CAS or exact-arithmetic implementations (for example SymPy and PARI/GP or Sage).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.19969>

## Sources

- <https://arxiv.org/abs/2607.19969>
- <https://arxiv.org/abs/2607.11800>
- <https://arxiv.org/abs/2608.12607>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Schur-product and direct-sum constructions from dephased Butson Hadamard matrices (Xu's method for order 6) carry over to 9 = 3x3 and to the prime orders with BH(p,p).
- Order 23 asks only for c = 528 = v^2 - 1; the order-6 value 35 = 6^2 - 1 was realised by a mixed Butson construction, a template to adapt.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point orthogonality is not a certificate; exact entries are required for a full win.
- Vectors equal up to a global phase are the same ray; count rays, not vectors.
- Order 6 is closed; do not target it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/quantum-latin-square-cardinalities-7-9-11-23.md
```

Already set up? Say `run V3R1T4S on quantum-latin-square-cardinalities-7-9-11-23`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quantum-latin-square-cardinalities-7-9-11-23`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
