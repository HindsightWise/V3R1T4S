# Erdős #773 small cases: largest Sidon subset of the first n squares, a(72) and beyond (OEIS A390813)

✏️ **Erdős problems and proofs** · standard · tractability ★★★★☆ · compute: laptop-hours to laptop-days (maximum independent set / ILP on the sum-collision hypergraph) · open as of 2026-10-30

## The problem

Erdős problem #773 (Alon-Erdős) asks for the size of the largest Sidon subset of {1^2, 2^2, ..., N^2} and whether it is N^(1-o(1)). Known: >> N^(2/3) (Lefmann-Thiele 1995) and <= N exp(-c log N / log log N) (Croot, Mao and Yip, announced on the problem's forum, Apr 2026). OEIS A390813 (submitted by Giorgos Kalogeropoulos, Nov 2025) gives the exact maximum a(n) for n <= 68, with a(43)-a(68) from Christian Sievers (27 Nov 2025); a(68) = 32. Sievers also noted that up to at least n = 68, n = 32 is the only n where no maximum subset contains n^2. Erdős Problem a Day (erdosproblemaday.com, 12 Aug 2026) reports a(69) = 32, a(70) = 33 and a(71) = 33. These come from exhaustive searches conditional on the published OEIS prefix, with a size-33 witness and an independent audit; they are not yet in OEIS and were not re-run for this entry. So a(72) is 33 or 34. The sum-collision structure comes from representations x^2 + y^2 = z^2 + w^2, which are plentiful, so exact values need a genuine combinatorial search. Target: the next exact term a(72).

## What counts as a win

Success means the exact value of A390813(72). If the live b-file or the Erdős Problem a Day #773 page has grown past 71, the target is a(n) at the first index beyond both, re-fetched immediately before claiming. If a(72) = 34, give an explicit 34-element subset of {1..72} whose squares form a Sidon set (all sums x^2+y^2 with x <= y distinct), checked by two programs. This suffices since a(n+1) <= a(n)+1 and a(71) <= 33. If a(72) = 33, give a 33-element witness and a certificate that no 34-element subset exists. The certificate is either two independently written exact searches that agree (e.g., branch and bound and an ILP with all collision constraints), or a DRAT/LRAT-checked UNSAT proof on an independently regenerated CNF. Any prefix values a(k), k <= 71, used as pruning bounds must come from the OEIS b-file or be re-certified in the same run. The value must not appear in the entry, its history, the erdosproblems.com/forum/thread/773 comments or the Erdős Problem a Day #773 page.

## Partial wins

- **p1:** A certified exact value a(N) for some N with 73 <= N <= 100 (not necessarily consecutive with the known values), with witness and exhaustive/UNSAT certificate as in the main criterion.
- **p2:** A second n with 69 <= n <= 100, after Sievers' n = 32, where no maximum Sidon subset of {1^2..n^2} contains n^2. It needs the certified exact value a(n), as in the main criterion, re-certified rather than taken from an unverified source. It also needs a certificate, from the same two-method exact pipeline, that every Sidon subset of {1^2..n^2} containing n^2 has at most a(n) - 1 elements.

## How a win is checked

Enumerate all collisions x^2+y^2 = z^2+w^2 with x <= y, z <= w, {x,y} != {z,w}, in 1..N (including x = y cases) by hashing sums; a set is Sidon in squares iff it contains no collision quadruple. Use two independent implementations. Calibrate the exact searches by reproducing a(60..68) from the b-file and the reported a(69..71) = 32, 33, 33, then run the new N.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A390813>

## Sources

- <https://oeis.org/A390813>
- <https://www.erdosproblems.com/773>
- <https://www.erdosproblems.com/forum/thread/773>
- <https://erdosproblemaday.com/day/773-square-sidon-frontier>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Model it as a maximum independent set in a 4-uniform (and 3-uniform for x = y repeats) hypergraph and solve it with an ILP (HiGHS/CBC) using clique-like cover cuts from parametrised families of collisions (Brahmagupta identities).
- Do incremental search over n: an optimal set at n-1 plus warm starts gives fast lower bounds; only the upper bound needs a full proof.
- Use the many multiplicative symmetries of the collision structure (which are not global symmetries of [1..n]) for cutting planes rather than symmetry breaking.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Sidon here means all sums a+b with a <= b distinct, so 2x^2 = y^2 + z^2 collisions (x = y on one side) count.
- Squares of the indices, not the indices themselves: the set is {x^2 : x in S}.
- A heuristic that fails to find a 34-set proves nothing.
- The Erdős Problem a Day values a(69..71) depend on the OEIS prefix and have not been independently re-run. If an independent exact search disagrees with them, report it, but a disagreement is not a listed win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-773-sidon-squares-next-term.md
```

Already set up? Say `run V3R1T4S on erdos-773-sidon-squares-next-term`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-773-sidon-squares-next-term`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
