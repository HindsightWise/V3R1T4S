# MOONSHOT - Beckett-Gray codes: does a 9-bit Beckett-Gray code exist? (open for every n >= 9)

⚡ **Algorithms** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster for exhaustive search; laptop-days for heuristic or SAT attempts (a code checks in microseconds) · open as of 2026-10-30

## The problem

A Beckett-Gray code is a cyclic n-bit Gray code (a Hamilton cycle of the n-cube starting at 0^n) in which every 1->0 transition clears the 1-bit that has been set longest. The positions of the 1s behave as a first-in first-out queue; 0->1 transitions are unconstrained. The name comes from Samuel Beckett's play Quad (Knuth, TAOCP 4A, Sec. 7.2.1.1). Cooke, North, Dewar and Stevens (arXiv:1608.06001, 2016; published as J. Combin. Math. Combin. Comput. 126 (2025) 195-200, doi:10.61091/jcmcc126-12) found codes by computer for n = 2, 5, 6, 7 and 8, and showed that none exist for n = 3 and 4. They enumerated all codes for n <= 6: 8 non-isomorphic cyclic codes for n = 5 and 94,841 for n = 6. They estimated the n = 7 search tree at about 2^102 nodes and called an exhaustive n = 7 search infeasible. Their 8-bit code was found by simulated annealing plus backtracking. Sawada and Wong (Electron. Notes Discrete Math. 29, 2007) gave a faster algorithm and almost 10,000 cyclic 7-bit codes. Torsten Mütze's survey 'Combinatorial Gray codes - an updated survey' (arXiv:2202.01280 v4, 30 Jul 2024) lists existence for n >= 9 as open Problem P9. A check on 2026-10-30 of the papers citing Cooke et al. and the survey found no resolution.

## What counts as a win

Success means one of two things. (a) An explicit Beckett-Gray code for some n >= 9: a cyclic sequence of all 2^n distinct n-bit words, starting at 0^n, with consecutive words (including last to first) at Hamming distance 1, in which every 1->0 transition clears the oldest set bit under the FIFO rule simulated from the all-zero start. It must pass two independently written checkers. (b) A rerunnable nonexistence proof for n = 9: an UNSAT certificate (DRAT/LRAT, checked by drat-trim or cake_lpr) of a published SAT encoding whose correctness is argued in a short note.

## Partial wins

- **p1:** An explicit 9-bit Beckett-Gray path: all 512 words visited once from 0^9 with single-bit steps and the FIFO clearing rule at every 1->0 step, without the closing step back to 0^9. It counts only if none is published at claim time, and it is verified by the same checker as the full win.

## How a win is checked

Simulate a queue. Start at 0^9 with an empty queue. At each step exactly one bit changes; if it is set (0->1), push its index; if it is cleared (1->0), require that it equals the queue head and pop it. Check that all 2^9 words are distinct and that the last step returns to 0^9 with an empty queue. Calibrate the checker on the published 8-bit code (Knuth or Cooke et al.) and on codes found for n = 5 and 6.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2202.01280>

## Sources

- <https://arxiv.org/abs/2202.01280>
- <https://arxiv.org/abs/1608.06001>
- <https://doi.org/10.61091/jcmcc126-12>
- <https://en.wikipedia.org/wiki/Gray_code>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The queue structure makes the state the current word plus the queue order; dynamic programming over (word, queue) with transposition tables, plus symmetry breaking on the first transitions, extends Sawada-Wong-style backtracking.
- Try SAT/CP encodings with an explicit queue position per bit, or search for codes invariant under a coordinate rotation of order 3 or 9.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The FIFO rule applies only to 1->0 transitions; 0->1 steps are free. Codes must be cyclic.
- Conventions vary on counting symmetric copies (reversal, renaming); state the convention for counts.
- Search logs and timeouts are not nonexistence proofs.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/beckett-gray-code-n9.md
```

Already set up? Say `run V3R1T4S on beckett-gray-code-n9`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `beckett-gray-code-n9`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
