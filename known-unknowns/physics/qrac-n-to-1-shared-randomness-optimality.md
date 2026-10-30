# n-to-1 qubit random access codes with shared randomness: prove the 4-to-1 code (p = 0.741481) optimal, or beat a numerical optimum for n = 4..9

⚛️ **Physics** · standard · tractability ★★★☆☆ · compute: laptop-hours (rigorous interval branch-and-bound over 2(n-1) measurement angles) · open as of 2026-10-30

## The problem

In an n-to-1 quantum random access code (QRAC) with shared randomness (SR), Alice encodes n bits into one qubit and Bob must output any requested bit; p is the worst-case success probability. Andris Ambainis, Debbie Leung, Laura Mancinska and Maris Ozols (arXiv:0810.2937, 2008-2009) showed that with SR the problem reduces to choosing n unit vectors v_i in R^3 (Bob's measurement axes): the optimal encoding is then fixed and p = 1/2 + S/(n 2^(n+1)) with S = sum over x in {+-1}^n of ||sum_i x_i v_i||. They proved p <= 1/2 + 1/(2 sqrt n), tight only for n = 2, 3 (orthogonal axes), and found numerical codes for n = 4..12 (Table 2): 0.741481 (n = 4, exactly 1/2 + (1+sqrt3)/(8 sqrt2)), 0.713578, 0.694046, 0.678638, 0.666633, 0.656893 (n = 9). Their open problem 'Optimality of numerical codes' asks to prove the optimality of any of these for n >= 4. Laura Mancinska and Sigurd Storgaard (arXiv:2106.00155) proved the m-qubit bound p <= 1/2 + (1/2) sqrt(2^(m-1)/n) for SR codes, which for m = 1 is the old bound. Shuo Tan and Syed Jafar (arXiv:2607.10414, v3 23 Oct 2026) settled the binary (n, n-1) and (n, n-2) families and list (2,1), (3,1), (3,2), (4,2) and (6,2) as the only cases solved before them, so the 4-to-1 optimum is open: it lies in [0.741481, 0.75].

## What counts as a win

Success means EITHER (a) a rigorous, independently re-checkable proof that the optimal n-to-1 QRAC with SR for n = 4 has p <= 0.741481 + 1e-6, i.e. that max over unit vectors v_1..v_4 in R^3 of S/(4*2^5) + 1/2 does not exceed that value (interval-arithmetic branch-and-bound with a posted cover of the parameter domain, an exact SOS certificate, or a machine-checked proof); OR (b) n unit vectors in R^3 for some n in 4..9 whose p, computed in mpmath at 40 digits from the formula above, is STRICTLY GREATER (direction: max) than the arXiv:0810.2937 Table 2 value for that n by at least 1e-6 (re-fetch Tan-Jafar arXiv:2607.10414 and search arXiv before claiming, in case a newer value or proof exists).

## Partial wins

- **p1:** A rigorous certified upper bound p(4) <= 0.745 for the 4-to-1 QRAC with SR (strictly below the proven 0.75), re-checkable as in (a).
- **p2:** A rigorous optimality proof, as in (a), for n = 5 (0.713578) or n = 6 (0.694046) within 1e-6.

## How a win is checked

(b): recompute p from the posted vectors in mpmath; first check the formula reproduces 0.853553 (n = 2, orthogonal axes) and 0.741481 for the paper's n = 4 code. (a), p1, p2: re-run the posted interval branch-and-bound with an independent implementation (mpmath.iv or Arb), checking that the boxes cover the whole domain (v_1 fixed to (0,0,1) by symmetry, remaining 2(n-1) angles) and that each box's rigorous upper bound is below the claimed value; or re-check the SOS identity in exact rationals.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.10414>

## Sources

- <https://arxiv.org/abs/0810.2937>
- <https://arxiv.org/abs/2607.10414>
- <https://arxiv.org/abs/2106.00155>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- S is a sum of norms that is Lipschitz in the angles; the sign symmetries x -> -x and permutations of the v_i cut the domain by a large factor before branch-and-bound.
- For p1, a relaxation (e.g. bounding each ||sum x_i v_i|| by a quadratic SDP-friendly form) may suffice without full branch-and-bound.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Without shared randomness a 4-to-1 qubit QRAC with p > 1/2 does not exist (Hayashi et al.); do not mix the two settings.
- Worst-case p with SR equals the optimal average-case value; compare like with like.
- Table 2 cells for n >= 10 are weak records: a quick multistart BFGS run in this lane (2026-10-30) reached 0.6482412 for n = 10 (table 0.648200) and 0.6410553 for n = 11 (table 0.641051), so they are excluded from (b). The same run reproduced n = 4..9 to all 6 decimals, so those are probably global optima and (a) is the realistic win.
- Floating-point branch-and-bound is not a proof; bounds must be rigorous (outward rounding).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/qrac-n-to-1-shared-randomness-optimality.md
```

Already set up? Say `run V3R1T4S on qrac-n-to-1-shared-randomness-optimality`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qrac-n-to-1-shared-randomness-optimality`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
