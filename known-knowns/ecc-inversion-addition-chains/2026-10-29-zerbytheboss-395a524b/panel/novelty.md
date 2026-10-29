# Novelty Skeptic Report — ecc-inversion-addition-chains & gf2-polymult-8term-25-products

context: subagent (fresh invocation)
target_id: ecc-inversion-addition-chains
review_utc: 2026-10-29T17:16:00Z

## Novelty Audit

### 1. Addition Chains Novelty Evaluation (Lens 1)
- **Baseline Sources**:
  - `mmcloughlin/addchain` live results table (`doc/results.md`).
  - Brian Smith's ECC inversion addition chains live table (`briansmith.org/ecc-inversion-addition-chains-01`).
- **Secondary Curve Inversion Baselines vs Discovered Records**:
  - **M-383** ($N = 2^{383} - 187$, $d = 2$, $E = 2^{383} - 189$):
    * `addchain` baseline: 396 total steps (382 squarings, 14 additions).
    * Discovered chain: **395 total steps** (382 squarings, 13 additions).
    * Improvement: Strictly shorter by 1 addition ($395 < 396$).
    * Source of novelty: Discovered optimal 11-addition sequence for run-length block $R(375)$ ($[1, 2, 4, 8, 16, 24, 25, 50, 100, 125, 250, 375]$) versus addchain's 12 additions ($[1, 2, 4, 8, 16, 20, 22, 44, 88, 176, 352, 374, 375]$).
  - **M-511** ($N = 2^{511} - 187$, $d = 2$, $E = 2^{511} - 189$):
    * `addchain` baseline: 525 total steps (510 squarings, 15 additions).
    * Discovered chain: **524 total steps** (510 squarings, 14 additions).
    * Improvement: Strictly shorter by 1 addition ($524 < 525$).
    * Source of novelty: Discovered optimal 12-addition sequence for run-length block $R(503)$ ($[1, 2, 4, 8, 16, 32, 64, 96, 100, 101, 201, 402, 503]$) versus addchain's 13 additions ($[1, 2, 4, 6, 8, 16, 22, 30, 60, 120, 240, 480, 502, 503]$).
- **Literature and Library Audit**:
  - Neither Brian Smith's page nor standard open-source cryptographic libraries (BoringSSL, Go crypto, fiat-crypto, RustCrypto) document chains for M-383 or M-511 shorter than `addchain`'s 396 and 525 baselines.
  - The discovered chains for M-383 (395) and M-511 (524) constitute genuine, novel record additions.

### 2. NIST Multipliers and Polynomial Tensor Audit (Lens 2)
- Evaluated 4 NIST standard-basis SLP field multipliers: $\text{GF}(2^6)$ (57 gates), $\text{GF}(2^7)$ mod $x^7+x^4+1$ (84 gates), $\text{GF}(2^7)$ mod $x^7+x^3+1$ (85 gates), and $\text{GF}(2^8)$ AES (117 gates). All match known optimal or near-optimal SLP literature baselines.
- For $T_{8 \times 8 \times 15}$, rank 26 remains the best known upper bound in the literature; no false claim of 25 products is made.

pass: true
