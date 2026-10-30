# Slowly synchronizing binary automata with a sink: beat Ananichev-Vorel's n^2/4 + 2n - 9 reset threshold (n = 16, 28) or the best known value for another n

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (local search over 2-letter automata; the exact reset threshold costs a BFS over 2^n subsets, which is easy at n = 16 and needs a few GB of bitsets at n = 28) · open as of 2026-10-30

## The problem

An automaton with zero (a sink) has a state fixed by every letter. With an unbounded alphabet the maximum reset threshold of n-state synchronizing automata with zero is n(n-1)/2 (Rystsov 1977, tight). For binary automata with zero the maximum is unknown. Volkov's living list (arXiv:2508.15655 v4, 13 Jan 2026, item B1) gives the best known lower bound n^2/4 + 2n - 9, attained for n ≡ 4 (mod 12) from n = 16 on by the Ananichev-Vorel series (J. Autom. Lang. Comb. 24 (2019) 153-164). Other series of order n^2/4 are Martyugin's (Inf. Comput. 206, 2008: two letters, n >= 8, ceil(n^2/4 + 3n/2 - 4)) and Pribavkina's (Math. Notes 90, 2011: any fixed number k of letters, even n >= 2k, n^2/4 + n/2 - 1). The general upper bound n(n-1)/2 applies, so the binary-sink question (is it n^2/4 + O(n)?) is wide open. At n = 16 the record value is 87; at n = 28 it is 243.

## What counts as a win

Success means an explicit binary complete DFA with n states, n in {16, 28}, that has a sink state and is synchronizing, whose exact reset threshold (computed by BFS over subsets) is STRICTLY GREATER (direction: max) than n^2/4 + 2n - 9 (87 for n = 16, 243 for n = 28). It must also exceed every value for that n in any newer source found by a fresh search before claiming (Volkov's list, papers citing Ananichev-Vorel 2019). Two independent programs must confirm the reset threshold.

## Partial wins

- **p1:** For some n with 17 <= n <= 30 and n not ≡ 4 (mod 12), a binary synchronizing automaton with a sink whose exact reset threshold is strictly greater than ceil(n^2/4 + 2n - 9), the Ananichev-Vorel formula evaluated at n. It must also exceed every published value for that n and be confirmed by two independent programs.

## How a win is checked

Check that the input is a 2-letter complete DFA with a state z where both letters map z to z. Run BFS from the full set over subset images under both letters until a singleton is reached; the BFS depth is the reset threshold. Use bitset subsets, and canonicalise to avoid revisiting. Run a second, independent implementation (for example the Szykuła-Zyzik algorithm or a SAT-based shortest-reset-word check). Calibrate on Rystsov's automata R_n (n(n-1)/2) and on Martyugin's series at n = 16 (ceil(64 + 24 - 4) = 84).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2508.15655>

## Sources

- <https://arxiv.org/abs/2508.15655>
- <https://arxiv.org/abs/1701.07954>
- <http://jalc.de/issues/2019/issue_24_2-4/jalc-2019-153-164.php>
- <https://doi.org/10.1016/j.ic.2008.03.020>
- <https://doi.org/10.1134/S0001434611090094>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the Ananichev-Vorel and Martyugin automata and run simulated annealing on single transitions, scoring by exact reset threshold (cheap at n = 16).
- Exploit the sink: synchronizing means reaching z, so the threshold is the maximum over states of a 'reach z from a set' process. Incremental BFS under single-transition changes speeds up the search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Ananichev-Vorel construction is open as arXiv:1701.07954 (v1 lists Ananichev alone; the JALC 2019 version adds Vorel). An almost-permutation automaton A_n with reset threshold 4n - 13, given a tail of length k that is a multiple of the order 6 of a, has reset threshold rt(A_n) + nk (Lemma 2.1). Rebuild A_10 plus a 6-tail (87 at n = 16) and A_16 plus a 12-tail (243 at n = 28) to calibrate.
- For p1, the same tail construction already gives published values for other n just below the bar (for example 211 at n = 26, where the bar is 212; 97 at n = 17, where the bar is 98). A claim must beat both the bar and these values. For small n the exact maxima may already be known from exhaustive searches. The headline cells n = 16 and 28 are beyond exhaustive reach, but check any tables before claiming p1.
- The sink state must be fixed by both letters, and the automaton must be complete.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/binary-sink-automata-reset-threshold-record.md
```

Already set up? Say `run V3R1T4S on binary-sink-automata-reset-threshold-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `binary-sink-automata-reset-threshold-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
