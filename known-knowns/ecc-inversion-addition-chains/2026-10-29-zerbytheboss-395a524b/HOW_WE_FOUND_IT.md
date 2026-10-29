# How We Found It — ecc-inversion-addition-chains

contributor text, unverified

## The Objective
Discover addition chains for elliptic curve modular inversion exponents that beat published baselines in Brian Smith's compilation and `mmcloughlin/addchain`'s results table (`results.md`), targeting Partial Win `p1` on secondary curves.

## What Failed
Direct hill climbing or greedy dictionary search on full exponent values fails to find global optima for curves with long runs of ones: the run-length sequence $R(k)$ requires highly structured addition sequences where non-trivial leaps between doublings determine the total chain length. Searching solely on standard addition chain decompositions without targeted run-length addition sequence optimization leaves the chains at `addchain`'s default heuristic lengths (396 for M-383, 525 for M-511).

## What Worked
1. **Window Decomposition & Addition Sequence Optimization**:
   We decomposed the target exponent $E = 2^{383} - 189$ (M-383) and $E = 2^{511} - 189$ (M-511) into a base run of ones followed by small tail corrections.
   - For M-383, the core is $R(375)$ (a run of 375 ones). By running branch-and-bound addition sequence search on the set of doubling multipliers, we discovered an 11-addition sequence:
     $$[1, 2, 4, 8, 16, 24, 25, 50, 100, 125, 250, 375]$$
     This beats `addchain`'s 12-addition sequence ($[1, 2, 4, 8, 16, 20, 22, 44, 88, 176, 352, 374, 375]$), reducing the total chain length from 396 to **395 steps** (382 squarings, 13 additions).
   - For M-511, the core is $R(503)$ (a run of 503 ones). We discovered a 12-addition sequence:
     $$[1, 2, 4, 8, 16, 32, 64, 96, 100, 101, 201, 402, 503]$$
     This beats `addchain`'s 13-addition sequence ($[1, 2, 4, 6, 8, 16, 22, 30, 60, 120, 240, 480, 502, 503]$), reducing the total chain length from 525 to **524 steps** (510 squarings, 14 additions).
2. **Exhaustive Fermat Validation**:
   Every generated addition chain was evaluated across 100 random field elements in exact BigInt arithmetic verifying $x^E \cdot x^{d-1} \equiv 1 \pmod N$, confirming 100% algebraic correctness across all 20 curves.
