# Permutations sortable by two stacks in series: the exact count for n = 20 (first term beyond Elvey Price-Guttmann)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days (a(19) ~ 4.35 * 10^15, so the count must come from a structural/transfer method, not from testing permutations one by one) · open as of 2026-10-30

## The problem

Knuth asked how many permutations of length n can be sorted by two stacks in series; unlike one stack (Catalan), two stacks in parallel (solved by Albert and Bousquet-Melou) or a deque (counted to n = 100 in A182216), no formula or functional equation is known, and recognition is polynomial (Pierrot-Rossin 2013). Andrew Elvey Price and Anthony J. Guttmann ('Permutations sortable by two stacks in series', Adv. Appl. Math. 2017, arXiv:1510.08663) counted them exactly for all n < 20, giving OEIS A263929 (a(19) = 4,351,269,802,153,188), approximated 19 further coefficients numerically, and estimated the growth rate mu ~ 12.45 +- 0.15. On 2026-10-30 A263929 still ends at n = 19 and carries keyword 'more', and an arXiv search for 'two stacks in series' found no later exact enumeration.

## What counts as a win

Success means the exact number of permutations of length n that are sortable by two stacks in series (Knuth's model: input -> stack 1 -> stack 2 -> output, output increasing), for some n >= 20 strictly beyond the live A263929 entry and b-file, computed by two independently written programs (different algorithms) that agree and that both reproduce a(1..19) exactly.

## Partial wins

- **p1:** A documented independent algorithm (not a per-permutation sortability test) that reproduces all of a(1..19) and reports its running-time growth, making n = 20 a clear projection; reproduction only.

## How a win is checked

Skeptic: brute force over all permutations for n <= 11 with a direct two-stack sortability test (an exhaustive search over stack operations, or the Pierrot-Rossin algorithm) must match both programs; then compare both programs with A263929 for n <= 19 and with each other at the new n. Sanity: a(20)/a(19) should be close to the trend of the paper's approximate coefficients (a(19)/a(18) ~ 10.9).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A263929>

## Sources

- <https://oeis.org/A263929>
- <https://arxiv.org/abs/1510.08663>
- <https://arxiv.org/abs/1304.2860>
- <https://oeis.org/A182216>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Elvey Price and Guttmann count via a decomposition of operation sequences; a transfer matrix over the joint stack contents, with canonical forms to merge equivalent operation words, is the classical route.
- Each sortable permutation has many sorting words; count canonical sorting words (for example by a fixed greedy rule) to avoid overcounting.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Different 'two stacks in series' models exist (West's 2-stack-sortable, which applies the stack-sorting map twice, is A000139 and solved); this target is the general Knuth model.
- Counting operation sequences instead of permutations overcounts; each permutation must be counted once.
- The 19 approximate coefficients in the paper are not exact and do not set a record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/two-stack-series-sortable-count-n20.md
```

Already set up? Say `run V3R1T4S on two-stack-series-sortable-count-n20`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `two-stack-series-sortable-count-n20`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
