# Claesson-Jelinek-Steingrimsson conjecture: 1324-avoiders with k inversions never decrease from length n to n+1 (counterexample, or the first full table at n = 18)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days (Meng enumerated all 4.6 * 10^11 members of Av_17(1324) in about 18 hours on four cores; Av_18(1324) is about 7.5 times larger, and inversion-pruned enumeration covers low-k regions quickly) · open as of 2026-10-30

## The problem

Let a(n, k) be the number of 1324-avoiding permutations of length n with exactly k inversions. Anders Claesson, Vit Jelinek and Einar Steingrimsson (2012) conjectured a(n, k) <= a(n+1, k) for all n, k; the conjecture implies gr(Av(1324)) <= e^(pi sqrt(2/3)) ~ 13.002. Svante Linusson and Emil Verkama (arXiv:2408.15075) proved it for k <= 2n - 7; Lingsen Meng (arXiv:2609.06717 v2, 9 Sep 2026) extended the proof, computer-assisted, to all n and k <= 2n + 6, with regions growing like sqrt(n) for huge n, and states that the unrestricted conjecture is open. Claesson, Linusson, Ulfarsson and Verkama (arXiv:2604.01143, 2026) proved inversion monotonicity for some subclasses. Direct tables: Claesson et al. 2012 for n <= 15; Ruth Hoffmann, Ozgur Akgun and Christopher Jefferson (arXiv:2311.17581) the full table for n = 16; Meng (Section 8 and archival supplement of 2609.06717) a full enumeration of all 458,374,397,312 members of Av_17(1324), about 18 hours on four cores, reproducing the whole table for n <= 17, plus an inversion-pruned table of a(n, k) for n <= 26, k <= 55 and residual runs to n = 30, k <= 63; he checked a(n+1, k) >= a(n, k) directly for n <= 25, k <= 2n + 3. So the inequality is verified for every k only through the step 16 -> 17; from n = 17 on it is unchecked for k > max(55, 2n + 6) up to C(n, 2), which is where a counterexample would have to live.

## What counts as a win

Success means explicit n, k with a(n, k) > a(n+1, k), both values exact and computed by two independently written programs that agree and that reproduce the published tables exactly: the full rows for n <= 17 (Hoffmann-Akgun-Jefferson to n = 16, Meng's n = 17) and Meng's n <= 26, k <= 55 table. Alternatively, a kernel-checked formal proof (Lean, Rocq or Isabelle, no sorry or extra axioms) of the full conjecture. Re-check arXiv for later versions of 2609.06717 and new results before claiming.

## Partial wins

- **p1:** The complete row a(18, k) for every k = 0..153, computed by two independent programs that agree, that reproduce the full n = 17 row of Meng's supplement, and whose row sum equals A061552(18) in the OEIS b-file; this certifies the conjecture at the step n = 17 -> 18 for every k (or refutes it, which is the full win).
- **p2:** Exact a(n, k) for every n <= 30 and every k <= 70, extending Meng's archived table (n <= 26, k <= 55) and his k <= 63 runs, with every inequality a(n, k) <= a(n+1, k) for n <= 29 and k <= 70 checked; two independent programs as above.

## How a win is checked

Skeptic reruns both programs on n <= 13 (minutes) against brute force over all permutations, checks agreement with the Hoffmann-Akgun-Jefferson n <= 16 tables and Meng's n = 17 row and n <= 26, k <= 55 table, checks each full row sums to A061552(n), then compares the claimed (n, k) entries. A full rerun at n = 18 may take days; agreement of two independent implementations is then the main evidence.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.06717>

## Sources

- <https://arxiv.org/abs/2609.06717>
- <https://arxiv.org/abs/2408.15075>
- <https://arxiv.org/abs/2311.17581>
- <https://arxiv.org/abs/2604.01143>
- <https://arxiv.org/abs/1111.5736>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Add an inversion-count dimension to a known 1324 counting algorithm (Conway-Guttmann transfer matrix, or Johansson-Nakamura functional equations): states multiply by at most C(n,2)+1 but no permutation is generated.
- Use the symmetries inverse and reverse-complement (both preserve 1324-avoidance and inversion count) to cut generation work by up to 4x.
- Complement (pi_i -> n+1-pi_i) maps 1324-avoiders with k inversions to 4231-avoiders with C(n,2)-k inversions, so the open high-k part of the 1324 table equals the low-k part of the 4231 table, where generation from few inversions is cheap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Complement maps 1324-avoiders to 4231-avoiders and k inversions to C(n,2) - k inversions; it is a bijection between different tables, not a symmetry of a(n, k). Inverse and reverse-complement are true symmetries of a(n, k).
- The stabilisation a(n, k) = a(k+2, k) for n > k + 2 (Hoffmann et al. Conjecture 2) means low-k columns carry no new information; the open region is large k.
- The full n = 17 row is already in Meng's supplement (2609.06717, Section 8), so the first new full row is n = 18, with about 3.4 * 10^12 avoiders for generate-and-filter enumeration; budget accordingly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/av1324-inversion-monotonicity-conjecture.md
```

Already set up? Say `run V3R1T4S on av1324-inversion-monotonicity-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `av1324-inversion-monotonicity-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
