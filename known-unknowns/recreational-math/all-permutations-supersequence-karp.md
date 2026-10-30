# Shortest word containing every permutation of 1..n as a subsequence (Karp's problem, OEIS A062714): settle n = 10, or circular n = 7

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-minutes to check a candidate word (10! subsequence tests); laptop-days or more for exhaustive optimality proofs · open as of 2026-10-30

## The problem

Karp's problem (Chvatal-Klarner-Knuth 1972, problem 36) asks for the minimum length a(n) of a word over {1..n} containing every permutation of 1..n as a (not necessarily contiguous) subsequence. Known values (A062714): 1, 3, 7, 12, 19, 28, 39 (Malcolm Newey 1973 for n <= 7), a(8) = 52 (proved by Oliver Tan, 'Conjecture on Supersequence Lower Bound related to Connell Sequence', arXiv:2501.11386, Jan 2025, refuting Newey's conjectured 51 from A337300; it also follows from Vitaliy Garnashevich's 2020 lexicographically least optimal word in A136094, and Pontus von Bromssen entered it in A062714 in Aug 2025) and a(9) = 66 (Vitaliy Garnashevich, Oct 2025; A136094 lists lexicographically least optimal words to n = 9). Upper bounds: n^2 - 2n + 4 (Newey; Koutas-Hu), ceil(n^2 - 7n/3 + 19/3) for n >= 7 (Sasa Radomirovic 2012), and families approaching n^2 - (5/2 - eps)n for infinitely many n (Oliver Tan 2022); the lower bound is n^2 - C n^(7/4 + eps) (Kleitman-Kwiatkowski 1976), and deciding whether a word contains all permutations is coNP-complete (Uznanski 2015). For n = 10, Radomirovic's bound is 83 and Newey's conjectured formula A337300 gives 81. A062714 carries keyword 'more' with no a(10) on 2026-10-30. The circular variant (word on a circle, A373728, Lecouturier-Zmiaikou 2012) is known to n = 6 (2, 4, 8, 12, 17 for n = 2..6; entry by Michel Marcus, June 2024, keyword 'more') and open at n = 7.

## What counts as a win

Success means determining a(10) of A062714 exactly: an explicit word over {1..10} of length L containing all 3,628,800 permutations as subsequences, plus a re-runnable exhaustive computer proof that no word of length L - 1 does, whose method reproduces a(8) = 52 and a(9) = 66. Alternatively, determining the circular value A373728 at n = 7 in the same way (explicit circular word and a proof that nothing shorter works, reproducing the known value 17 at n = 6). Re-check A062714, A136094, A373728 and arXiv before claiming.

## Partial wins

- **p1:** An explicit word over {1..10} of length at most 82 containing every permutation of 1..10 as a subsequence (strictly below Radomirovic's 83, the best published construction at n = 10), after checking A062714, A136094 and the papers cited there for a shorter published word.
- **p2:** An explicit word over {1..11} of length at most 101 containing every permutation of 1..11 as a subsequence (strictly below Radomirovic's ceil(121 - 77/3 + 19/3) = 102), after the same check.
- **p3:** An explicit circular word for n = 7 of length at most 24 containing every permutation of 1..7 as a subsequence read around the circle from some starting point (strictly below the Lecouturier-Zmiaikou bound a(n) < n^2/2 + n/4 - 1, which gives at most 25 at n = 7), after checking A373728 and its links for a shorter published word.

## How a win is checked

For an explicit word: for every permutation of 1..n, run greedy left-to-right subsequence matching (for circular words, try every starting position) and assert all succeed; 10! x 82 steps is under a minute in C. For a lower-bound proof: rerun the claimant's exhaustive search, confirm it reproduces a(8) = 52 and a(9) = 66 (or circular a(6) = 17), and audit every pruning rule on small n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A062714>

## Sources

- <https://oeis.org/A062714>
- <https://oeis.org/A136094>
- <https://oeis.org/A373728>
- <https://oeis.org/A337300>
- <https://doi.org/10.37236/2859>
- <https://arxiv.org/abs/2201.06306>
- <https://arxiv.org/abs/1506.05079>
- <https://arxiv.org/abs/2501.11386>
- <https://arxiv.org/abs/1009.5106>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lift the optimal n = 9 words of A136094: Radomirovic's and Tan's constructions insert a new letter into a good shorter word; try all insertion schedules of the letter 10 into length-66 optimal words.
- Local search with an incremental checker: track, for each permutation prefix, the earliest matching position, so a one-letter edit only re-checks affected permutations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Subsequence, not substring: the substring version is the superpermutation problem, a different bank entry.
- Newey's conjectured values A337300 are wrong from n = 8 on (51 vs 52); do not use them as known lengths.
- The words in A136094 are lexicographically least optimal words; other optimal words exist and may lift better.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/all-permutations-supersequence-karp.md
```

Already set up? Say `run V3R1T4S on all-permutations-supersequence-karp`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `all-permutations-supersequence-karp`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
