# Erdős #272: more than C(N,2)+1+floor((N-1)/4) subsets of {1..N} with pairwise AP intersections, or the exact t(13)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (maximum-clique search over the 2^N - 1 nonempty subsets; N = 13 means 8191 vertices) · open as of 2026-10-30

## The problem

Let t(N) be the largest number of distinct sets A_1..A_t in {1..N} such that every pairwise intersection is a nonempty arithmetic progression (Erdős Problem #272, from Simonovits-Sós and Erdős-Graham). Simonovits and Sós proved t(N) = O(N^2) and conjectured C(N,2)+1. Szabó (Europ. J. Combin. 1999) disproved this with a construction of B(N) = C(N,2)+1+floor((N-1)/4) sets and proved t(N) = N^2/2 + O(N^{5/3}(log N)^3). He conjectured t(N) = C(N,2)+O(N) and that every extremal family has a common element (the kernel conjecture). Stijn Cambie (erdosproblems forum, Aug 2025) verified N <= 9, and for 10 <= N <= 14 found B(N) under the assumption that the family contains a singleton (for N = 13: five such extremal families, all through 7). Zhanfu Yang, arXiv:2607.23004 (v1, 25 Jul 2026), determines t(3..12) = 4, 7, 12, 17, 23, 30, 39, 48, 58, 69 by exhaustive maximum-clique computation; all equal B(N). Yang proves that B(N) is the exact maximum over starred families (those with a common element) for every N, and conjectures t(N) = B(N) for all N, which reduces to Szabó's kernel conjecture (Problem 7.1). Starred families were checked exhaustively for N <= 13 and a structured class for N <= 61. A Lean proof of Szabó's first question in the form t(N) = N^2/2 + O(N) ('Erdős problem 272 - szabo strong') was marked solved on the Conjectures.io bounty pool on 11 Sep 2026; it is unrefereed and gives no exact value. The erdosproblems.com page for #272 shows no resolution of the exact value or the kernel question. Open: t(13) (B(13) = 82), and any N with t(N) > B(N).

## What counts as a win

An explicit family F of distinct subsets of {1..N}, for some N >= 13, such that every pairwise intersection of members is a nonempty arithmetic progression (singletons count as APs; all checked exhaustively), with |F| STRICTLY GREATER (direction: max) than B(N) = C(N,2)+1+floor((N-1)/4) and than any larger value published for that N at verification time. Re-check https://www.erdosproblems.com/272, its forum thread and the arXiv page of 2607.23004 first. Such an F refutes Yang's Conjecture 1.3 and, by Yang's Theorem 1.4, must have no common element. A non-starred F larger than B(N) for N <= 12, or a starred F larger than B(N) for any N, contradicts published computation or proof: treat it as a bug and re-verify both sides before any claim.

## Partial wins

- **p1:** A complete enumeration, up to isomorphism, of all maximum families (size B(N) = t(N)) for one N in 10..12. It must come from two independently written exhaustive implementations whose outputs agree, and it must report for each family whether its members share a common element. Yang's Problem 7.1 asserts in passing that every maximum family for N <= 12 is starred, but Section 6 describes no such check. A non-starred maximum family would disprove Szabó's kernel conjecture.
- **p2:** A certified value of t(13). Either a family of size 83 or more (which is also the full win), or a proof that no 83-family exists. The proof is an exhaustive search log plus an agreeing independent implementation, or a checked DRAT/LRAT proof for a SAT encoding.

## How a win is checked

An independent script: check distinctness, that every set lies in [N], and for every pair that the intersection is nonempty with constant consecutive gaps. Compute |F| and B(N) exactly, and the common intersection of all members. Calibrate on Szabó's construction (Section 2 of arXiv:2607.23004), which must give B(N) for N = 5..14. For a p2 exhaustive claim, re-run with a separately written clique solver and require agreement on N = 3..12 with 4, 7, 12, 17, 23, 30, 39, 48, 58, 69.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/272>

## Sources

- <https://arxiv.org/abs/2607.23004>
- <https://www.erdosproblems.com/272>
- <https://www.erdosproblems.com/forum/thread/272>
- <https://doi.org/10.1006/eujc.1999.0302>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Yang's Section 7 localises a counterexample in one regime: by Theorem 7.5 and Proposition 7.6, for N >= 10^4 and a family larger than B(N) whose members of size >= 4 are all progressions, the triples form a star at some c and the members avoiding c are progressions of more than N/12 elements and difference at most 12. This is proved only under those hypotheses; for small N or non-progression members the structure is unconstrained.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Empty intersections are forbidden (with them allowed, the Graham-Simonovits-Sós answer is different).
- The sets must be distinct; the empty set is excluded automatically because every intersection must be nonempty.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-272-ap-intersection-families.md
```

Already set up? Say `run V3R1T4S on erdos-272-ap-intersection-families`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-272-ap-intersection-families`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
