# Sequences behind Hadamard constructions: settle a smallest open case in Table 3 of arXiv:2610.27175 (T-sequences, base sequences, Williamson-type matrices, Golay pairs)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (compression, SAT+CAS and exhaustive searches; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

Most recursive constructions of Hadamard matrices rest on sequences whose aperiodic autocorrelations N_a(s) = sum_{i=0}^{m-1-s} a_i a_{i+s} cancel (with the second factor conjugated for entries +-1, +-i). Table 3 of Egan, Kotsireas, London and Ó Catháin (arXiv:2610.27175, 19 Oct 2026) records where each ingredient is known to exist and its smallest open case. Golay pairs exist at lengths 2^a 10^b 26^c and at no other length up to 105 (smallest open 106). Turyn-type sequences TT(n) (four +-1 sequences of lengths n, n, n, n-1 with N_A + N_B + 2N_C + 2N_D = 0) are known for every even n <= 46 (Best, Đoković, Kharaghani and Ramp; London and Kotsireas 2025 and 2026), smallest open 48. Base sequences BS(n+1, n) are known for every n <= 40 (the last of these, BS(40,39), by Đoković 2010), for n = 41, 42 and 43 (Wang and Zhu, arXiv:2506.20296, 2025) and for n = 2^a 10^b 26^c, smallest open 44. T-sequences are known at every length t <= 100 except possibly 97 (Đoković 2010). T-matrices (four circulant {0,+-1} matrices of order t with disjoint supports and sum T_i T_i^T = tI) are also known at 97, 109 and 197 (K. Kumar 2026), 103 (L. Schneider 2026), 151 (A. Schumer 2026, and independently Egan et al.), 163 and 181 (J. D. Jones 2026), smallest open 127. Williamson-type matrices WT(w) are known at every odd w <= 69 and at 73, 79, 91, 93, 95, 97, 103, 109, 127, 133 and 181 (Kharaghani, Mohammadian and Tayfeh-Rezaie, arXiv:2605.08661 v2, through near-Williamson matrices; some of these orders were known classically), at 111 (K. Kumar 2026), in Turyn's family (q+1)/2 and further families, smallest open 71. Complex Golay pairs are known at lengths 1, 3, 5, 11, 13 and every even length up to 26 except 14 (Bright, Kotsireas, Heinle and Ganesh enumerated all lengths up to 28), smallest open 29. Each new ingredient closes Hadamard orders: TT(n) gives H(4(3n-1)), BS(n+1, n) gives T-sequences of length 2n+1, and T-matrices of order t with WT(w) give H(4tw) (Cooper-Wallis).

## What counts as a win

Success means an explicit object settling one of these cells, verified exactly by two independent programs: a Golay pair of length 106; Turyn-type sequences TT(48); base sequences BS(45,44); T-sequences of length 97; T-matrices of order 127; Williamson-type matrices of order 71 (four +-1 matrices A, B, C, D of order 71 with XY^T = YX^T for every pair and AA^T + BB^T + CC^T + DD^T = 284 I); or a complex Golay pair of length 29. A rigorous nonexistence proof for one cell (DRAT/LRAT-checked on a CNF the skeptic regenerates, or an exhaustive search the skeptic re-runs) also counts. The cell must still be open at claim time: Table 3 of the latest version of arXiv:2610.27175 and a same-day search of arXiv, github.com/vatskishan03/Hadamard and the JD-Jones-ASES repositories show no such object (direction: none; existence target).

## Partial wins

- **p1:** A certified exclusion, not previously published, of one of these cells within a precisely stated subclass (for example: no TT(48) with a stated symmetry or compression pattern, no Williamson-type matrices of order 71 of a stated circulant or near-Williamson form, no complex Golay pair of length 29 of a stated structured form), with code and logs the skeptic re-runs to the same empty result or a DRAT/LRAT certificate.

## How a win is checked

For sequences, compute every aperiodic autocorrelation exactly in integers (Gaussian integers for complex Golay pairs, conjugating the second factor) and require the stated combination to vanish at every shift s >= 1; check lengths and alphabets ({+-1}; {0, +-1} with exactly one nonzero sequence at each position for T-sequences; {+-1, +-i} for complex Golay pairs). For T-matrices, check that the supports are disjoint and cover every position and that the periodic autocorrelations sum to zero at every nonzero shift. For Williamson-type matrices, form the four matrices and check XY^T = YX^T and the sum condition exactly. As an end-to-end check, build the Hadamard matrix the cited theorem gives (for example TT(48) gives T-sequences of length 143 and H(572)) and verify H H^T. Use two independent checkers and search the sources named in the criterion.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.27175>

## Sources

- <https://arxiv.org/abs/2610.27175>
- <https://arxiv.org/abs/2605.08661>
- <https://github.com/vatskishan03/Hadamard>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Compression (Đoković-Kotsireas): project candidates onto Z_m for divisors m of the length, enumerate compressed candidates that pass the power-spectral-density test, then lift with SAT; this is how recent TT(n) and T-matrices were found.
- SAT+CAS (Bright et al.): encode the autocorrelation equations in SAT and let a computer-algebra callback prune with PSD bounds; the same pipeline enumerated complex Golay pairs up to length 28 and is the natural route to length 29.
- Near-Williamson matrices (four circulants with B, C, D symmetric) gave every odd w <= 69; extend the Kharaghani-Mohammadian-Tayfeh-Rezaie search to w = 71 with multiplier-orbit restrictions.
- T-matrices of prime order 127: impose invariance under a subgroup of (Z/127Z)* (orders 3, 7, 9, ...), as Egan et al. did with subgroups of orders 5 and 9 for t = 151 and 163.
- A Golay pair of length 106 would refute the Golay-number conjecture; for a nonexistence proof use Borwein-Ferguson-style exhaustive methods with the Eliahou-Kervaire-Saffari restrictions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Aperiodic versus periodic: Golay pairs, base sequences, TT(n) and T-sequences use aperiodic autocorrelation; T-matrices and Williamson-type matrices are periodic objects. Periodic Golay pairs are a separate entry.
- Williamson-type matrices also need amicability XY^T = YX^T; four circulants meeting only the sum condition are Goethals-Seidel input, not WT(71).
- TT(n) has lengths n, n, n, n-1 and weights 1, 1, 2, 2.
- This table changed fast in 2026 (T-matrices at 97, 103, 109, 151, 163, 181 and 197 and WT(111) were all new); re-check Table 3 and the repositories on the day of the claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hadamard-ingredient-sequences-smallest-open.md
```

Already set up? Say `run V3R1T4S on hadamard-ingredient-sequences-smallest-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hadamard-ingredient-sequences-smallest-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
