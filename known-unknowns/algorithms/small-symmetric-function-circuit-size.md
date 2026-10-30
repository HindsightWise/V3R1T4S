# Small symmetric Boolean functions over the full binary basis: smaller circuits for SUM_n (sideways sum), MAJ_n, SORT_n, or exact values such as Knuth's MOD3 n = 6 cases

⚡ **Algorithms** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (SAT-based exact synthesis and local subcircuit improvement); verification laptop-minutes · open as of 2026-10-30

## The problem

Circuit size over B2 (two-input gates computing any of the 16 binary functions; equivalently XAIG with free negations) is the classical measure of TAOCP 7.1.2. SUM_n outputs the binary representation of x1+...+xn and underlies every symmetric function. Best known B2 sizes (Kulikov-Pechenev-Slezkin, MFCS 2022, Table 3; circuit files in alexanderskulikov/circuit_improvement/circuits/sum; Cirbo, AAAI 2025, Table 3; Goncharov-Kulikov-Levtsov, arXiv:2509.13966): SUM_2..SUM_5 = 2, 5, 9, 11 (optimal); SUM_6 <= 16, SUM_7 <= 19, SUM_8 <= 25, SUM_9 <= 27, SUM_10 <= 31 (sum10_size31.ckt, verified exhaustively by this review), SUM_11 <= 34, SUM_15 <= 51, SUM_16 <= 59, SUM_31 <= 119. AIG basis (AND only, free inverters; Cirbo): SUM_5, 7, 9, 11, 15 <= 17, 28, 41, 52, 77. Asymptotically 2.5n - O(1) <= size(SUM_n) <= 4.5n + o(n) (Stockmeyer; Demenkov-Kojevnikov-Kulikov-Yaroslavtsev), and size(SUM_n) <= size(SUM_k) n/(k - ceil(log2(k+1))) + o(n), so a SUM_15 with 49 gates, a SUM_7 with 17 or a SUM_31 with 116 would beat 4.5n. Cirbo lists XAIG MAJ_7, 9, 11, 13, 15 <= 17, 24, 31, 45, 48 and SORT_12..16 <= 58, 62, 68, 73, 82. Knuth (TAOCP 7.2.2.2, answer to ex. 480) found size(MOD3^r_n) for 3 <= n <= 5, proved size(MOD3^0_6) = 12 and conjectured size(MOD3^r_n) = 3n - 5 - [(n+r) = 0 mod 3]; Kulikov et al. proved the matching upper bound, so MOD3^1_6 and MOD3^2_6 have 13-gate circuits and are conjectured optimal, a case Knuth called 'tantalizingly close' to solver limits. OPEN as of 2026-10-30 (repository last changed 2026-03; Cirbo 1.1.0 of 2026-10-13).

## What counts as a win

Success means an explicit circuit, as a straight-line program over two-input gates with each gate's 4-bit truth table, that computes the stated multi-output function exactly on all 2^n inputs and has STRICTLY FEWER gates (direction: min) than the value listed in the statement for that function and basis: SUM_n in B2 for n in {6, 7, 8, 9, 10, 11, 15, 16, 31}, or in the AIG basis for n in {5, 7, 9, 11, 15}. For SUM_n the outputs are the ceil(log2(n+1)) bits of x1+...+xn. Gate count is the number of two-input gates; inputs and constants are free; in the AIG basis only AND gates count and negations are free. A candidate must also beat every smaller circuit for the same function and basis published at claim time: re-check the three primary papers, the circuit_improvement circuits folder, what the current Cirbo generators produce, and any IWLS 2023-2026 contest circuit whose truth table equals the function.

## Partial wins

- **p1:** A B2 circuit with strictly fewer gates than listed for XAIG MAJ_n (n in {7, 9, 11, 13, 15}; output [x1+...+xn > n/2]) or SORT_n (n in 12..16; outputs the sorted input bits), verified exhaustively, and also smaller than any circuit for the same function in the circuit_improvement maj/sort folders and the IWLS 2023-2026 contest results.
- **p2:** An exact value for MOD3^1_6 or MOD3^2_6 (output [x1+...+x6 = r mod 3]): either a SAT proof (CNF from an independently re-implemented circuit-existence encoding that allows unused gates, plus a DRAT/LRAT certificate checked by drat-trim or cake_lpr) that no B2 circuit with at most 12 gates computes it (settling it at 13), or a circuit with at most 12 gates (disproving Knuth's conjecture at n = 6), provided no later source has settled that case.
- **p3:** A certified lower bound: a checked UNSAT proof (same certificate standard as p2) that no B2 circuit with at most 15 gates computes SUM_6, making the listed 16 optimal, provided no published proof exists.

## How a win is checked

Evaluate the straight-line program on all 2^n inputs (n <= 31: bit-sliced over 2^31 inputs is minutes in C; for n <= 16 trivial) and compare with the defined function; count gates and confirm each gate's basis membership. For lower bounds, rebuild the CNF encoding independently (Kojevnikov-Kulikov-Yaroslavtsev style), check the certificate with drat-trim or cake_lpr, and review the symmetry-breaking constraints for soundness.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2509.13966>

## Sources

- <https://arxiv.org/abs/2102.12579>
- <https://arxiv.org/abs/2412.14933>
- <https://arxiv.org/abs/2509.13966>
- <https://github.com/SPbSAT/cirbo>
- <https://github.com/alexanderskulikov/circuit_improvement>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Local SAT improvement of 7-gate windows (Kulikov's circuit_improvement) seeded with MDFA-based SUM circuits from the STACS 2026 generator.
- Search for new constant-size blocks on the (p, p xor q) encoding beyond MDFA; any SUM_k block beating the 4.5(k - ceil(log2(k+1))) threshold improves the asymptotic bound.
- For MOD3_6 use strong symmetry breaking (topological gate order, normal gates) and incremental SAT with proof logging.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- B2 sizes and AIG sizes are different tables; do not compare across bases.
- Count only two-input gates; a circuit that relies on free fan-in-3 gates or unary gates that the basis does not include is invalid.
- An UNSAT result is only as good as its encoding: symmetry breaking that is not sound for multi-output functions has produced wrong 'optimality' claims; have the encoding re-derived independently.
- Knuth's TAOCP Volume 4B (2022) answer to 7.2.2.2-480 and its errata may contain newer MOD3 values; check before claiming p2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/small-symmetric-function-circuit-size.md
```

Already set up? Say `run V3R1T4S on small-symmetric-function-circuit-size`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `small-symmetric-function-circuit-size`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
