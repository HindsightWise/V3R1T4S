# Generalized Collatz maps: a cycle missing from the known lists (Lagarias 3x+k for k < 20000, 3x-k, and the three known 5x+1 cycles)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (parity-vector / cycle-equation search); verification is instant · open as of 2026-10-30

## The problem

For odd k with gcd(k, 6) = 1, Lagarias' 3x+k map is T_k(x) = x/2 if x is even and (3x + k)/2 if x is odd. A cycle is primitive if its elements are coprime to k. Lagarias (1990) conjectured that every such k has at least one primitive cycle and only finitely many. E. G. Belaga and M. Mignotte tabulated the cycles (2000, 2006). Geoffrey H. Morley's OEIS A226607 (b-file rows 1..6667) lists the smallest elements of 42757 primitive cycles for k < 20000, found by following every trajectory that starts below 10^8; A226613 gives the counts. He adds that for k < 158195 no start below 10^8 reaches a primitive cycle whose minimal element exceeds 28306063. So a cycle whose elements all exceed 10^8 cannot have been seen by these searches. For the 3x-k map, Morley's A226630 and A226629 list the k with primitive cycles and the conjectured counts. For the 5x+1 map (x -> 5x+1 if x is odd, x/2 if even) only three cycles are known: the cycles through 1, 13 and 17 (A393125, M. F. Hasler, February 2026). Kontorovich and Lagarias predict that most 5x+1 orbits diverge.

## What counts as a win

CONFIRMED (full win) for an explicit cycle: distinct positive integers x_1..x_L with T(x_i) = x_{i+1} and T(x_L) = x_1, checked with exact integers. T is T_k for some 1 < k < 20000 with gcd(k, 6) = 1, and every element is coprime to k (primitive). The cycle's minimal element must NOT be among the entries of row n = floor(k/3) + 1 of https://oeis.org/A226607. The b-file b226607.txt stores rows 1..6667 flattened; row n begins after the first A226613(1) + ... + A226613(n-1) entries and has A226613(n) entries, taken from b226613.txt. Re-fetch both before the claim. Direction: max on the number of known cycles. k = 1 (the Collatz problem itself) is out of scope.

## Partial wins

- **p1:** A primitive T_k cycle for some 20000 <= k < 158195 (gcd(k, 6) = 1) whose minimal element exceeds 10^8, beyond the reach of every search described in A226607.
- **p2:** A primitive cycle of the 3x-k map T(x) = x/2 or (3x - k)/2, with k at most the largest entry of the A226630 b-file. Either k is absent from A226630, or the cycle is beyond the count A226629 gives for that k (cycles listed by smallest element; the claimant reproduces Morley's cycles for that k first).
- **p3:** A fourth cycle of the 5x+1 map x -> 5x+1 (x odd), x/2 (x even) on positive integers, different from the three cycles listed in A393125. Merely resolving a '?' entry of A393125 does not count here, since that entry carries keyword 'more' and belongs to the OEIS-more target.

## How a win is checked

Iterate the map over the claimed cycle with Python integers. Check closure, that the elements are distinct and coprime to k (for primitivity), and the minimal element. Compare with the A226607 row for k (or the A226630/A226629 data, or the A393125 list) fetched live. Reproduce a few listed cycles for the same k to confirm the map convention.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A226607>

## Sources

- <https://oeis.org/A226607>
- <https://oeis.org/A226613>
- <https://oeis.org/A226630>
- <https://oeis.org/A226629>
- <https://oeis.org/A393125>
- <http://hal.archives-ouvertes.fr/hal-00129656>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Cycle equation (Bohm-Sontacchi): a parity vector with O odd steps and L total steps gives x_1 = k*N/(2^L - 3^O), where N is a fixed sum of 3^i 2^j terms. Enumerate the (L, O) with D = 2^L - 3^O dividing k*N, so that cycles with huge elements (> 10^8) appear directly, with no trajectory search.
- Divisors of the 'Collatz numbers' 2^L - 3^O (Belaga-Mignotte Table 2 gives their factorizations) say which k can carry cycles of a given shape.
- For 5x+1 use the same equation with 2^L - 5^O < 0 handled by sign; a positive cycle needs 2^L > 5^O, which forces L/O > log2(5), long and sparse in odd steps.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Non-primitive cycles (all elements multiples of a divisor of k) are scaled copies of cycles of a smaller k and do not count.
- Use exactly T_k(x) = (3x + k)/2 on odd x (the shortcut form). Row lengths differ under the unshortened map, but cycle sets do not.
- Rows of A226607 are indexed by floor(k/3) + 1 over all odd k coprime to 6; misreading the row index is the easiest false 'new' cycle.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/collatz-type-maps-new-cycles.md
```

Already set up? Say `run V3R1T4S on collatz-type-maps-new-cycles`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `collatz-type-maps-new-cycles`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
