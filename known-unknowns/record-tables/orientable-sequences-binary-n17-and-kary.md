# Orientable sequences: a binary orientable cycle of order 18-20 longer than the best claimed period, or a k-ary period beating the Mitchell-Wild tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (an ILP on the order-n de Bruijn graph with HiGHS or SCIP as in Mitchell 2026, or cycle joining plus local search; a check takes linear time) · open as of 2026-10-30

## The problem

An orientable sequence OS_k(n) is a periodic sequence over k symbols in which each length-n window occurs at most once per period in either direction. No window equals the reversal of another window, and no window is a palindrome. Dai, Martin, Robshaw and Wild introduced them in 1993 for position sensing. Chris J. Mitchell, 'Searching for binary orientable sequences' (arXiv:2610.33601 v1, 24 Oct 2026, ILP searches with HiGHS and SCIP), settled the maximum binary period for every n <= 16 (31776 at n = 16; aperiodic length 31810). He reports no maximum for n >= 17. A write-up on Drew Stone's site (drewstone.github.io/research/orientable-sequences, assessed 2026-10-07, merged 2026-10-12; an LLM-run ILP search with no outside review, whose sequence and certificate repository was not public on 2026-10-30) gives the same maxima as Mitchell for n = 9..16. It claims the exact maximum 63578 for n = 17, an OS_2(18) of period 128794 with an uncertified bound of 128796, and an OS_2(19) of period 257650 with an uncertified bound of 257652. The L*_n column of Joe Sawada's debruijnsequence.org orientable page still lists the Gabrić-Sawada periods 63135, 128639, 257272 and 519160 for n = 17..20. The DMRW upper bounds there are U_n = 64662, 129911, 260386 and 521964. The best acyclic lengths on the same page ('Extended from OS') are 63219, 128680, 257340 and 519212, against bounds 65296, 130833, 261650 and 523795. The claimed periods give longer acyclic sequences of length p + n - 1: 63594 (n = 17), 128811 (n = 18) and 257668 (n = 19). For k = 3..8, Mitchell and Wild's Table 7 ('New orientable sequences', arXiv:2507.02526, Acta Inform. 63 (2026) 14) gives the largest known periods with upper bounds for n = 2..8; the bound is met for n <= 3 and for n = 4 with k odd. Mitchell and Wild, arXiv:2603.18646 v2 (14 Aug 2026), Table 3 raised many cells. Examples: k = 3 gives 303 (n = 6), 948 (n = 7) and 3006 (n = 8); k = 4 gives 396, 1744, 7480 and 31000 for n = 5..8.

## What counts as a win

Success means a binary periodic orientable sequence of order n, 18 <= n <= 20, given as one period of length p, verified exhaustively. The p cyclic windows must be pairwise distinct, and no window may equal the reversal of any window, itself included. The period p must be STRICTLY GREATER (direction: max) than the best period claimed for that n at verification time on the debruijnsequence.org orientable page (L*_n column), in the latest version of arXiv:2610.33601, on drewstone.github.io/research/orientable-sequences, and in any newer paper or write-up by Mitchell, Wild, Gabrić, Sawada, Stone or others found by a fresh search. On 2026-10-30 these values were 128794 (n = 18), 257650 (n = 19) and 519160 (n = 20). The period must also be at most the DMRW bound U_n (129911, 260386, 521964); a larger value means a checker bug. n = 17 does not count, because its claimed maximum 63578 meets its claimed upper bound. At n = 18 and 19 the claimed but uncertified upper bounds (128796, 257652) leave at most 2 of headroom; n = 20 has the most room.

## Partial wins

- **p1:** A binary aperiodic (acyclic) orientable sequence of order n, 17 <= n <= 20, verified exhaustively (all length-n windows distinct, no window equal to the reversal of any window). It must be strictly longer than the best acyclic length on the debruijnsequence.org orientable page, the length p + n - 1 implied by the best claimed period (including drewstone.github.io/research/orientable-sequences), and any newer source (context 2026-10-30: 63594, 128811, 257668, 519212 for n = 17..20). It must also be at most the bound Û_n (65296, 130833, 261650, 523795).
- **p2:** A k-ary orientable sequence for a cell with 3 <= k <= 8 and 4 <= n <= 8 whose largest known period is still below the Table 7 upper bound of arXiv:2507.02526 (this excludes n = 4 with k odd, where the bound is met). Its period must be strictly greater than the maximum for that cell over Table 7 of arXiv:2507.02526, Table 3 of arXiv:2603.18646 (latest version) and any newer source, and at most the Table 7 upper bound.
- **p3:** The exact maximum binary period for n = 18 or n = 19: an explicit OS_2(n) of period at least the best claimed one (128794 or 257650), together with an ILP upper bound equal to its period, obtained by two different solvers (for example HiGHS and SCIP) on a model the claimant publishes, which a skeptic re-runs. This is labelled computational.

## How a win is checked

Read the period as a string s of length p. Form the p cyclic windows w_i = s[i..i+n-1] (indices mod p), put them in a set W and check |W| = p. Then check that reverse(w) is not in W for every w in W; this also excludes palindromes. Compare p with the live values and with U_n. Calibrate the checker by accepting one of Mitchell's published maximum-period examples (n <= 16) and rejecting a de Bruijn sequence. For k-ary cells, use the same check over k symbols.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://debruijnsequence.org/db/orientable>

## Sources

- <https://arxiv.org/abs/2610.33601>
- <http://debruijnsequence.org/db/orientable>
- <https://drewstone.github.io/research/orientable-sequences>
- <https://arxiv.org/abs/2507.02526>
- <https://arxiv.org/abs/2603.18646>
- <https://arxiv.org/abs/2108.03069>
- <https://arxiv.org/abs/2407.07029>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Scale Mitchell's ILP: maximise the number of de Bruijn-graph edges in a balanced, connected edge set with at most one edge from each reversal pair. He reports that the optimum was always connected up to n = 16. At n = 18 the model has 2^18 edge variables; symmetry breaking, the parity cuts described on the drewstone.github.io write-up and warm starts from the Gabrić-Sawada cycle may help.
- Local improvement: start from the Gabrić-Sawada cycle-joining sequence and use cycle-swap moves (remove a cycle of windows, insert a longer one) while keeping the orientable constraint.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Periodic and aperiodic records are separate tables. For n >= 17, Mitchell's derived aperiodic values p + n - 1 (63151 and so on) are below the debruijnsequence.org 'Extended from OS' values, but the drewstone.github.io periods give longer ones (63594, 128811, 257668).
- The bracketed values in Table 3 of arXiv:2603.18646 compare with an older table, not with Table 7 of arXiv:2507.02526. Take the maximum over both tables.
- Negative orientable sequences (NOS) are a different object; values such as 318 for NOS_3(6) are not OS records.
- The drewstone.github.io claims (63578, 128794, 257650) have no outside review, and their sequences were not public on 2026-10-30. They still set the bar: a sequence that beats only the debruijnsequence.org values is not a win.
- The area moved five times in 2026 (Mitchell, Wild, Stone). Re-check arXiv listings for Mitchell and Sawada, and the drewstone.github.io research page, before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/orientable-sequences-binary-n17-and-kary.md
```

Already set up? Say `run V3R1T4S on orientable-sequences-binary-n17-and-kary`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `orientable-sequences-binary-n17-and-kary`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
