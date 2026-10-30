# Periodic Golay pairs: settle an undecided length up to 300 (smallest 106)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (multi-level compression and orderly generation; checking is instant) · open as of 2026-10-30

## The problem

A periodic Golay pair of length v is a pair of +-1 sequences A, B with PAF_A(s) + PAF_B(s) = 0 for s = 1..v-1; it gives a Hadamard matrix of order 2v. v must be even with v/2 a sum of two squares, and the Arasu-Xiang condition must hold. Every Golay number 2^a 10^b 26^c is a periodic Golay number. Đoković and Kotsireas (arXiv:1409.5969 v2, 2015) give the lengths then known as products of Golay numbers with S = {1, 34, 50, 58, 72, 74, 82, 122, 202, 226}, and list the sixteen lengths up to 300 that satisfy all necessary conditions but were undecided: 90, 106, 130, 146, 170, 178, 180, 194, 212, 218, 234, 250, 274, 290, 292, 298. Lumsden, Kotsireas and Bright (arXiv:2408.15611 v3, 16 Mar 2025) enumerated all periodic Golay pairs of every length up to 72 with multi-level compression (under 10 CPU-years), found the first pairs of length 90, and state that 106 is now the smallest undecided length. Because a Golay pair of length g and a periodic Golay pair of length v multiply to one of length gv (Đoković-Kotsireas), the length-2 Golay pair and the length-90 pairs also settle 180. Remaining undecided lengths up to 300: 106, 130, 146, 170, 178, 194, 212, 218, 234, 250, 274, 290, 292, 298.

## What counts as a win

Success means explicit +-1 sequences A, B of a length v in {106, 130, 146, 170, 178, 194, 212, 218, 234, 250, 274, 290, 292, 298} with PAF_A(s) + PAF_B(s) = 0 for every s = 1..v-1, computed exactly by two independent programs, where no periodic Golay pair of that length is reported at claim time (fresh arXiv search for 'periodic Golay', and a check that v is not g*v' for a Golay number g > 1 and a newly settled length v') (direction: none; existence target).

## Partial wins

- **p1:** A complete enumeration, up to the equivalences used in arXiv:2408.15611, of the periodic Golay pairs of length 74 (the next admissible length after the published census of lengths up to 72), with code and counts the skeptic reproduces independently.

## How a win is checked

Check lengths and entries; compute PAF exactly and require every sum to be 0 for s = 1..v-1. Sanity check: (sum A)^2 + (sum B)^2 = 2v. Optionally build H = [[A, B], [-B^T, A^T]] from the two circulants and verify H H^T = 2vI. Use two independent checkers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2408.15611>

## Sources

- <https://arxiv.org/abs/2408.15611>
- <https://arxiv.org/abs/1409.5969>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multi-level compression (Lumsden-Kotsireas-Bright): uncompress in several steps along a divisor chain where one exists (130 = 2*5*13, 170 = 2*5*17, 234 = 2*9*13, 250 = 2*125); for v = 2p (106, 146, 178, 194) only compression by 2 or p is available, and arXiv:2408.15611 introduces orderly-generation methods for such cases.
- Supplementary difference sets 2-(v; r, s; lambda) with v = 2(r + s - lambda): search with a prescribed multiplier group, as Đoković and Kotsireas did for length 72.
- Use the structural conjecture of arXiv:2408.15611 (proved for v < 100) to restrict candidate compressions.
- Multiplication: any new length v' gives g*v' for every Golay number g; record all consequences.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Aperiodic Golay pairs are a stronger object (a Golay pair of length 106 is a cell of the Hadamard-ingredients entry); here the autocorrelation is cyclic.
- 90 and 180 are settled; lengths that fail the necessary conditions (v/2 not a sum of two squares, Arasu-Xiang) are impossible, not open.
- PSD tests in floating point are filters only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/periodic-golay-pairs-undecided-lengths.md
```

Already set up? Say `run V3R1T4S on periodic-golay-pairs-undecided-lengths`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `periodic-golay-pairs-undecided-lengths`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
