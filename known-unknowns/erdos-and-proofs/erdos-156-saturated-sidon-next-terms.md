# Erdős #156 small cases: minimum size of a maximal (saturated) Sidon set in {1..n}: settle a(189) in {9, 10}, and the nine-mark threshold

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (exhaustive nine-mark saturated-Sidon search with blocker pruning); a witness search is laptop-hours · open as of 2026-10-30

## The problem

Erdős problem #156 (Erdős-Sárközy-Sós) asks whether some maximal Sidon set in {1..N} has size O(N^(1/3)). Ruzsa constructed one of size O((N log N)^(1/3)). OEIS A382397(n) is the minimum size of an inclusion-maximal (saturated) Sidon subset of {1..n}. Felix Huber (Aug 2026) extended it to n = 183 (b-file 0..183, a(n) = 9 for 145 <= n <= 183). His preprint 'Saturated Sidon Sets in Consecutive Intervals: The Eight-Mark Threshold Is 144' (A399118 a-file) proves that an 8-element saturated Sidon set exists for interval length 144 and never for any larger length. Writing E_k for the lengths admitting a saturated k-set, he records that E_9 contains [45, 183]. A k-set blocks at most (k^3-k)/2 outside points, so sets of size <= 7 cannot be saturated for n >= 176. The table has moved past the b-file outside OEIS. The erdos-frontier-atlas gap map (curation 2026-09-27) gives the 9-set {39,43,72,78,99,100,112,119,143}, which is saturated in {1..n} for 143 <= n <= 188, so A382397(n) = 9 for 184 <= n <= 188 and max E_9 >= 188. The d3lefts project (GitHub issue #46, 29 Oct 2026) gives the 10-set {50,51,57,79,94,105,126,140,150,167}, which is saturated in {1..189}. Both were re-checked on 2026-10-30. So 9 <= a(189) <= 10, and a(189) = 9 exactly when 189 is in E_9. Huber's open questions ask for terminal values max E_k for other k. In the forum (16 Sep 2026), veljjanoski computed the cyclic analogue: the largest n with an inclusion-maximal k-element Sidon set in Z_n is c(3..7) = 14, 30, 50, 84, 126. Target: decide a(189).

## What counts as a win

Success means the exact value of A382397(189). If a live source has settled it, the target is instead a(n) at the first n >= 189 that no live source settles. Re-fetch https://oeis.org/A382397, the forum thread and the erdos-frontier-atlas gap map before claiming. If the value is 9, give an explicit 9-element Sidon subset of {1..189} that is inclusion-maximal (adding any other x in {1..189} creates a repeated difference), checked by two programs. The lower bound 9 then follows from Huber's theorem (no saturated 8-set for n >= 145) and the counting bound (k <= 7 impossible for n >= 176). The verifier must confirm both, including Huber's {0..n-1} versus {1..n} convention. If the value is 10, the 10-element witness is already public, so success needs a certificate that no saturated 9-element Sidon set exists in {1..189}: two agreeing, independently written exhaustive searches, or a DRAT/LRAT-checked UNSAT proof on an independently regenerated CNF.

## Partial wins

- **p1:** An explicit saturated 9-element Sidon set in {1..n} for some n >= 190, checked by two programs, provided no live source already lists such an n. Sidon means all positive differences are distinct; saturated means adding any further x in {1..n} breaks this. This shows max E_9 >= n, beyond the public n = 188 witness and Huber's [45,183]; n = 189 itself is the main target.
- **p2:** The cyclic analogue c(8): the largest n such that Z_n contains an inclusion-maximal 8-element Sidon set (a+b = c+d mod n only trivially, sums with a <= b including a = b). It needs a witness and an exhaustive search over all n up to the trivial bound (k^3+k^2+2k)/2 = 296 stated in the forum, by two independent programs, extending veljjanoski's c(3..7) = 14, 30, 50, 84, 126.

## How a win is checked

Check the Sidon property by computing all C(k,2) differences (or all sums a+b with a <= b). Check saturation by trying every x not in A and confirming that a repeated difference appears. Calibrate first. Exhaustive searches must reproduce a(n) for 140 <= n <= 183 and the 8-mark threshold 144. The checker must accept {39,43,72,78,99,100,112,119,143} as saturated in {1..188} and reject it in {1..189} (189 is addable), and must accept {50,51,57,79,94,105,126,140,150,167} as saturated in {1..189}. Then check the new claim. For p2, calibrate on c(7) = 126 with its witness {0,21,50,103,104,119,121}.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A382397>

## Sources

- <https://oeis.org/A382397>
- <https://oeis.org/A399118>
- <https://oeis.org/A399118/a399118.pdf>
- <https://www.erdosproblems.com/156>
- <https://www.erdosproblems.com/forum/thread/156>
- <https://github.com/veljjanoski/erdos156>
- <https://github.com/techno-optimist/erdos-frontier-atlas/blob/main/atlas/gap_map.json>
- <https://github.com/d3lefts/d3lefts/issues/46>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use Huber's blocker criterion: a set is saturated iff each outside point x is blocked by some (a,b,c) with x = a+b-c, x = 2a-b or x = (a+b)/2. Build sets by choosing minimal witnesses that block the new endpoint, as in his canonical search classes.
- Use the capacity bound: a 9-set blocks at most (9^3-9)/2 = 360 outside points. Huber's first-return lemma (a saturated witness at a new length must contain both endpoints) cuts the search for {1..189} sharply; adapt his endpoint-root enumeration from 8 to 9 marks.
- For p1 or a 9-mark witness at 189, start from the public 9-set saturated in {1..188} and the 10-sets saturated at 184 and 189, then perturb or delete marks with an exact saturation check.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Inclusion-maximal is not maximum: the target is the smallest saturated set, not the largest Sidon set (Golomb ruler problems are separate and held).
- Huber uses [n] = {0..n-1}; OEIS uses {1..n}. Both have n points, but a mismatched convention can shift a threshold by one.
- A set saturated in {1..n} stays saturated in {1..n'} for max(A) <= n' <= n, because blocking depends only on A and x. Saturation can fail as n grows, and a cardinality can reappear after disappearing, so a failed search at one n says nothing about larger n.
- At least two public AI-agent efforts (d3lefts issues #46/#91 and erdos-frontier-atlas) are working this cell. Their annealing near-candidates at n = 184..200 were not saturated, and their timeouts are not UNSAT proofs. Re-check any third-party witness before relying on it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-156-saturated-sidon-next-terms.md
```

Already set up? Say `run V3R1T4S on erdos-156-saturated-sidon-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-156-saturated-sidon-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
