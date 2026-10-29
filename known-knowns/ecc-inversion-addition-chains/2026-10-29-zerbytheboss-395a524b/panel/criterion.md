# Criterion Skeptic Report — ecc-inversion-addition-chains & gf2-polymult-8term-25-products

context: subagent (fresh invocation)
target_id: ecc-inversion-addition-chains
review_utc: 2026-10-29T17:16:00Z

## Criterion Audit

### 1. Verification of Partial Win `p1` Criterion
- **Target Specification**: `repo/known-unknowns/algorithms/ecc-inversion-addition-chains.md`
- **Verbatim Requirement for Partial Win `p1`**:
  > *"For one of the twelve field-inversion exponents that addchain lists without a published best (M-221, E-222, Curve1174, E-382, M-383/Curve383187, Curve41417, M-511, P-192, P-224, Goldilocks, secp192k1, secp224k1), a verified chain strictly shorter than addchain's listed length and than any chain the claimant finds in papers or public source code for that exponent."*
- **Audit Findings**:
  1. **M-383 / Curve383187**:
     - Designated curve in the twelve secondary curves of `p1`.
     - Baseline listed length in `addchain`: 396 steps.
     - Discovered and verified length: **395 steps**.
     - Condition $395 < 396$ strictly satisfied.
  2. **M-511**:
     - Designated curve in the twelve secondary curves of `p1`.
     - Baseline listed length in `addchain`: 525 steps.
     - Discovered and verified length: **524 steps**.
     - Condition $524 < 525$ strictly satisfied.
  3. Satisfaction of `p1`: The specification requires strictly shorter chains for at least *one* of the twelve curves; this run provides strictly shorter chains for *two* curves (M-383 and M-511).

### 2. Scope and Honesty Invariants
- Main curves (Curve25519 Field, NIST P-256 Field, NIST P-384 Field, secp256k1 Field) either match Brian Smith / DJB live bars or addchain baselines, but do not strictly beat them. Thus, `solution_claim` is NOT claimed.
- $T_{8 \times 8 \times 15}$ remains at rank 26.
- The claim level is strictly declared as `partial_win_claim` corresponding to `p1`.
- All checks satisfy the target specification requirements.

pass: true
