# Scholz-Brauer conjecture: an addition chain for 2^n - 1 of length n - 1 + l(n) at one of the six unrepaired non-Hansen numbers (33167549, 33247629, 33573479, 33580601, 33626279, 44177985)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-hours (constraint search over the optimal chains of n); verification takes minutes · open as of 2026-10-30

## The problem

The Scholz-Brauer conjecture (Scholz 1937, Brauer 1939; Knuth, TAOCP vol. 2, section 4.6.3) says l(2^n - 1) <= n - 1 + l(n), where l is the length of a shortest addition chain. It holds whenever n has an optimal star chain (Brauer) or an optimal l^0 chain (Hansen). Neill Clift found the smallest non-Hansen number, 5784689 (August 2005), so the conjecture holds for n < 5784689. Clift's Star and l^0 page lists the first 40 non-Hansen numbers. It colours those for which a chain of length n - 1 + l(n) for 2^n - 1 is known: built by hand (red), by Gecode edge labelling (green), by the 'spawn' construction (purple; Repair page, September 2026 update, credited there to Claude Fable 5.1), or as a continuation 2m of a repaired m (blue). Six entries are uncoloured: 33167549, 33247629, 33573479, 33580601, 33626279 and 44177985. The Repair page says a CP-SAT model of the spawn template, run over all their optimal chains, proves that these six cannot be repaired that way. The template uses elements 2^s(2^v - 1) plus at most two spawned powers of two. Related: Flammenkamp's page reports that on 1 July 2024 Clift showed equality can fail, first with n = 30978119. Clift's smallest example so far (ExactScholz2 page) gives l(2^1541527 - 1) <= 1541551 < l(1541527) + 1541526 = 1541552. Clift's Scholz-Brauer page also gives a 'monster', 32428466573: he proves that the derivative graph of its chain cannot be labelled, and all its chains appear to share that structure.

## What counts as a win

CONFIRMED (full win) for an explicit addition chain for 2^n - 1, with n one of the non-Hansen numbers still uncoloured on http://www.additionchains.com/StarL0.html (re-fetched before the claim; on 2026-10-30 these are 33167549, 33247629, 33573479, 33580601, 33626279 and 44177985). The chain must be written in Clift's run format: comma-separated items, where 'a,...,b' is a doubling run a, 2a, ..., b = 2^d*a contributing d + 1 elements. Every element after the initial 1 must equal the sum of two earlier elements, checked with exact integers. The chain must end at 2^n - 1, and its length (elements after the initial 1) must be AT MOST n - 1 + l(n). Here l(n) is the true shortest-chain length from Clift's complete table (all n <= 2^39, Flammenkamp's page), confirmed by the verifier's own optimal-chain run on n. Direction: min on the number of uncoloured entries. A chain for 2m when m is already repaired does not count.

## Partial wins

- **p1:** A smaller strict-inequality example: an n < 1541527 together with an explicit chain for 2^n - 1 of length at most n + l(n) - 2 (strictly below n - 1 + l(n)), verified as in the full win, with l(n) taken from Clift's table and rechecked by the verifier.
- **p2:** The monster: an explicit chain for 2^32428466573 - 1 of length at most 32428466572 + l(32428466573), with l(32428466573) from Clift's table (the number is below 2^39). Verified with an exact run-length (bit-interval) representation of the elements.

## How a win is checked

Parse the run format and keep each element exactly. Store runs by odd part and exponent range so that membership of any 2^j*s is O(1). For each non-run element, and for each run start, find an earlier pair summing to it. Count the elements and compare with n - 1 + l(n) (or n + l(n) - 2 for p1). Python big integers are fine up to about 10^8 bits. Use Clift's published 5784689 chain (length 5784715, Repair page) and his 1541527 chain (length 1541551, ExactScholz2 page) as regression tests: the checker must accept both with exactly those lengths. Read l(n) from Clift's add39 data (linked from Flammenkamp's page) and recheck it with an independent optimal-chain program the verifier writes. Re-fetch StarL0.html and Repair.html to confirm that n is still unrepaired.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.additionchains.com/StarL0.html>

## Sources

- <http://www.additionchains.com/StarL0.html>
- <http://www.additionchains.com/Repair.html>
- <http://www.additionchains.com/ScholzBrauer.html>
- <http://www.additionchains.com/ExactScholz2.html>
- <https://wwwhomes.uni-bielefeld.de/achim/addition_chain.html>
- <https://doi.org/10.1007/s00607-010-0118-8>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Widen the Repair-page CP-SAT model: elements 2^s(2^v - 1) with free offsets, plus three or more spawned powers of two (2^m - 1) + 1 = 2^m. The page shows two spawns cannot fix the six.
- Mix templates: let some elements be general sums such as 2^a(2^b - 1) + 2^c(2^e - 1), not only Mersenne-shaped blocks, and solve the edge labelling of the derivative graph as a SAT problem.
- Use the exact-equality machinery in reverse: Clift's 1541527 construction saves a step through an 'impossible' building-block set from a 2^47 - 1 chain. Saved steps elsewhere could pay for a non-Hansen gap.
- Search all optimal chains of n (Clift's nmc program counts them) for one whose derivative graph needs only a small, local repair.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting: a run 'a,...,b' adds d + 1 elements, and the initial 1 is not counted. Off-by-one errors here fake a win.
- l(n) must be the true optimum. Using a longer chain for n makes the target bound easier and the claim wrong.
- Continuations (2m of a repaired m, coloured blue) are trivial and do not count.
- Disproving the conjecture would need a proven lower bound on l(2^n - 1); no chain can do that, and nothing here asks for it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/scholz-brauer-unrepaired-non-hansen.md
```

Already set up? Say `run V3R1T4S on scholz-brauer-unrepaired-non-hansen`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `scholz-brauer-unrepaired-non-hansen`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
