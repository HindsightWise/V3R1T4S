# Randomized metric distortion: certify a lower bound above Charikar-Ramakrishnan's 2.11264 (current window [2.11264, 2.13713])

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-hours (LP over candidate distributions, with metrics found by column generation over consistent metrics); exact rational checking of a certificate takes seconds to minutes · open as of 2026-10-30

## The problem

In metric voting, voters and candidates lie in an unknown (pseudo)metric, and each voter ranks candidates by distance. A randomized rule sees only the rankings. Its distortion is the worst ratio of expected social cost (sum of voter-to-winner distances) to the optimal social cost, over all elections and all consistent metrics. Deterministic rules have optimal distortion 3 (Gkatzelis, Halpern and Shah 2020). For randomized rules, Charikar and Ramakrishnan ('Metric Distortion Bounds for Randomized Social Choice', SODA 2022, arXiv:2111.03694) and, independently, Pulyassary and Swamy (arXiv:2111.08698, 2021) disproved the conjectured value 2; Charikar and Ramakrishnan's (0,1,2,3)-metrics give the current bounds. Their Table 1 gives 2.02613 for m = 3 (tight), 2.04957 for m = 4, 2.06323 for m = 5, 2.07206 for 6, 2.07822 for 7, 2.08276 for 8, 2.08625 for 9, 2.08900 for 10, and 2.11264 as m tends to infinity. Their Conjecture 1 says these lower bounds are optimal. The upper bounds fell quickly in 2026: 2.753 (Charikar, Ramakrishnan, Wang and Wu, J. ACM 2024), then 5/2 (Frank arXiv:2608.17863, Ye arXiv:2608.21202), 2.1441 (Shah arXiv:2608.29308 v2), and 2.13713 (Cai, Charikar, Hastings, Ramakrishnan, Wang and Ye arXiv:2609.08259, 8 Sep 2026), which quotes 2.11264 as the lower bound. MathWorld's Metric Voting Distortion page reports no lower-bound improvement since 2022.

## What counts as a win

A finite certificate: (i) an election with m candidates and voter types with positive rational weights and strict rankings; (ii) K explicit rational pseudometrics d_1..d_K on voters plus candidates. Each must satisfy symmetry, d(x,x) = 0, nonnegativity and every triangle inequality, and be consistent with the rankings (d(v,a) <= d(v,b) whenever v ranks a above b). (iii) Rational weights lambda_k >= 0 summing to 1 such that D = min over candidates c of sum_k lambda_k SC_k(c)/OPT_k, with OPT_k = min_c SC_k(c) > 0. Every randomized rule then has distortion >= D on this election. Full win: D >= 2.1127, strictly above Charikar-Ramakrishnan's limit 2.11264 (direction: higher). Any certificate with D > 2.13713 contradicts the published upper bound of arXiv:2609.08259 and must be treated as a checker bug until three independently written exact checkers agree. Re-check arXiv for newer lower bounds before claiming.

## Partial wins

- **p1:** For a fixed m in 4..10, a certificate with exactly m candidates and D >= (Table 1 value for that m) + 0.00001, refuting Charikar-Ramakrishnan's Conjecture 1 at that m. m = 3 is excluded because 2.02613 is proven tight.

## How a win is checked

Python with fractions.Fraction. Check that the weights are positive and the rankings are permutations. Check each metric: symmetric, zero diagonal, nonnegative, all O(N^3) triangle inequalities, and ranking consistency for every voter and candidate pair. Compute SC_k(c) and OPT_k exactly, check lambda, and compute D exactly. Compare with the bar using exact rationals. Negative control: rebuild CR's m = 3 construction from arXiv:2111.03694 (Appendix A or Section 4 with Table 1 parameters) and get a certificate close to 2.02613 from below, never above. By the weak-duality argument, no valid certificate for m = 3 may exceed 2.02613.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.08259>

## Sources

- <https://arxiv.org/abs/2111.03694>
- <https://arxiv.org/abs/2609.08259>
- <https://arxiv.org/abs/2608.29308>
- <https://arxiv.org/abs/2608.17863>
- <https://mathworld.wolfram.com/MetricVotingDistortion.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CR restricted to (0,1,2,3)-metrics and a particular matrix structure; they note numerically that freeing more rows of M did not help within that family. Column generation over general biased metrics (their Proposition 4) is the natural next step.
- Mine the worst-case elections of the new upper-bound analyses (stable lotteries, Integrated Veto mixtures): where their proofs are tight, a lower-bound election may hide.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using different elections for different metrics is invalid: the certificate must fix one election, because the rule's output is fixed per election.
- Floating-point LP optima are not certificates; rationalise lambda and recheck exactly.
- Consistency uses each voter's own ranking; ties in distance are allowed but must not reverse a strict preference.
- Family-specific lower bounds do not move the bar: Shah's v2 proves 2.136 only for rules in his random-size stable-lottery family, and Cai et al. give matching lower bounds only for stable k-lotteries. A win must bind every randomized rule, which the single-election certificate above does.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/randomized-metric-distortion-lower-bound.md
```

Already set up? Say `run V3R1T4S on randomized-metric-distortion-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `randomized-metric-distortion-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
