# Criterion Skeptic Report — `penney-permutations-rotation-conjecture`

context: subagent (fresh invocation)
target_id: penney-permutations-rotation-conjecture
review_utc: 2026-10-28T18:50:00Z

## Criterion Compliance Audit

1. **Target Specification & Win Criterion**:
   - Criterion (from `repo/bank/targets.json` and `repo/known-unknowns/graphs-games-automata/penney-permutations-rotation-conjecture.md`):
     - Partial win `p1`: "Pr(sigma precedes tau) < 1/2 for all sigma in S_4"
     - Partial win `p2`: "Pr(sigma precedes tau) < 1/2 for all sigma in S_5"
     - Full win: "A specific k >= 4 and sigma in S_k whose right rotation tau satisfies Pr(sigma precedes tau) >= 1/2"

2. **Evaluation of Submitted Results for Claim `p1`**:
   - For all 24 permutations $\sigma \in S_4$, taking $\tau = (\sigma_2, \sigma_3, \sigma_4, \sigma_1)$:
     - An exact finite horizon $H \le 36$ is exhibited.
     - Exact non-negative integer counts $A(H), B(H), R(H)$ are computed where $A(H) + B(H) + R(H) = H!$.
     - In every case, $2 \cdot (A(H) + R(H)) < H!$, which implies $(A(H) + R(H))/H! < 1/2$ and $B(H)/H! > 1/2$.
     - Because $\Pr(\sigma \prec \tau) \le (A(H) + R(H))/H!$, this rigorously proves $\Pr(\sigma \prec \tau) < 1/2$.
   - Independent verification scripts recompute the counts and verify all inequalities in seconds.
   - All conditions for Partial Win `p1` are completely satisfied.

3. **Status Declaration**:
   - Because $S_5$ (`p2`) and the full conjecture for general $k$ remain open, this claim is properly and strictly classified as `CONFIRMED_PARTIAL` (`p1`).

pass: true
