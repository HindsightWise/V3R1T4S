# Lander-Parkin-Selfridge at k = 5: a solution of a^5 + b^5 = c^5 + d^5 (5.2.2) or a^5 + b^5 + c^5 = d^5 (5.1.3)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (the search-extension partial wins are laptop-days to cluster scale) · open as of 2026-10-30

## The problem

The Lander-Parkin-Selfridge (LPS) conjecture (Math. Comp. 21 (1967)) says that a nontrivial equal sum of k-th powers x1^k+...+xm^k = y1^k+...+yn^k in positive integers needs m+n >= k. It holds for k <= 4 (Fermat's Last Theorem for exponents 3 and 4), so the first open exponent is k = 5. There the only possible counterexample types are 5.2.2 (a^5+b^5 = c^5+d^5, also called Taxicab(5,2,2), OEIS A046881(5)) and 5.1.3 (a^5+b^5+c^5 = d^5). Neither has a known solution (Wikipedia 'Lander, Parkin, and Selfridge conjecture', edited 2026-09-14; MathWorld 'Diophantine Equation--5th Powers', updated 2026-10-29; Wikipedia 'Generalized taxicab number', edited 2026-09-06; OEIS A046881). Search frontiers for 5.2.2: MathWorld, citing Guy (UPINT, 1994, p. 140), still quotes 1.02e26, but larger bounds are published. Randy Ekl (Math. Comp. 67 (1998) 1309-1315, Table 9) gives 4.01e30. Stuart Gascoigne's exhaustive search (September 2002, reported on Christian Boyer's multimagie.com 'Squares of cubes' page) found no sum below 3.26e32. Julien Courties (OEIS A046881 comment, Nov 2020) gives a(5) > 1e33, the largest bound found on 2026-10-30. Jaroslaw Wroblewski (2006) searched only special forms, up to 2.43e37. Bill Butler's unreviewed long-double search to 3.6e28 (durangobill.com) is superseded. For 5.1.3, MathWorld cites Lander et al. (1967) for 'no solutions known' and states no search bound. Ekl 1998 extends search limits for many k.m.n types; its table could not be read on 2026-10-30 because the AMS site showed a bot check. Credit: Lander, Parkin, Selfridge, Guy, Ekl, Gascoigne, Courties, Wroblewski, Butler, and Meyrignac's EulerNet. The 5.1.4 case is a separate bank entry.

## What counts as a win

CONFIRMED for positive integers a, b, c, d with a^5 + b^5 = c^5 + d^5 and {a,b} != {c,d} as multisets, or positive integers a, b, c, d with a^5 + b^5 + c^5 = d^5. Both sides are checked exactly with Python big integers. The win also needs that neither the Wikipedia LPS article nor MathWorld's 5th-powers page lists a solution of that type at verification time. Either one disproves the LPS conjecture. Solutions using zero or negative terms, and solutions of the 5.1.4 or 5.2.3 types (Lander-Parkin, Scher-Seidl, Frye, Braun), do not count.

## Partial wins

- **p1:** 5.2.2 frontier: an exhaustive sorted-sums (Bernstein-style) enumeration in exact integer arithmetic, proving that there is no nontrivial a^5+b^5 = c^5+d^5 with a^5+b^5 <= B. The verifier reimplements it independently on randomly chosen windows, with matching per-window counts and hashed full logs. B must be strictly greater than 1e33 (Julien Courties, OEIS A046881, Nov 2020, the largest bound found on 2026-10-30; earlier exhaustive bounds: Gascoigne 2002, 3.26e32; Ekl 1998, 4.01e30). B must also exceed any larger bound published at verification time (re-check OEIS A046881, Boyer's multimagie.com Squares of Cubes page and EulerNet).
- **p2:** 5.1.3 frontier: an exhaustive search, reimplemented and spot-rerun as in p1, proving that a^5+b^5+c^5 = d^5 has no positive solution with d <= B. B must be strictly greater than the largest 5.1.3 bound in the literature, which the claimant cites and the verifier confirms. That includes Ekl 1998 (Math. Comp. 67, search-limit tables) and EulerNet; MathWorld states no numeric 5.1.3 bound on 2026-10-30.

## How a win is checked

Exact big-integer evaluation and a multiset comparison, under 1 second. For the partial wins, the verifier reimplements the merge of sorted a^5+b^5 streams (or the 5.1.3 kernel) with exact integer arithmetic, not long doubles, reruns sampled windows, compares counts and log hashes, and audits that the windows cover the claimed range.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture>

## Sources

- <https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture>
- <https://mathworld.wolfram.com/DiophantineEquation5thPowers.html>
- <https://oeis.org/A046881>
- <http://www.multimagie.com/English/SquaresOfCubes.htm>
- <https://doi.org/10.1090/S0025-5718-98-00979-X>
- <https://www.durangobill.com/Ramanujan.html>
- <https://en.wikipedia.org/wiki/Generalized_taxicab_number>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use modular sieving: fifth powers mod 11 are 0 or +-1, and mod 25, 31, 41 they are similarly sparse. Combine this with Bernstein's heap-based sorted-sums method in exact 128-bit or multiprecision arithmetic to pass Butler's range without floating-point error.
- 5.2.2 as a curve problem: for a fixed ratio s = a+b and t = c+d, the equation becomes a plane quartic condition. Search for rational points on the genus-1 or genus-2 quotients that Browning's paucity arguments use, rather than scanning by brute force.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- MathWorld's 1.02e26 and Butler's long-double 3.6e28 are far below the published exhaustive 5.2.2 bounds (Ekl 4.01e30, Gascoigne 3.26e32, Courties 1e33, all cited in OEIS A046881). A search that passes only Butler's or MathWorld's figure is not a partial win.
- Moving a negative term across turns signed 5.1.4 or 5.2.3 solutions (for example Braun's 2026 one) into look-alike equations. Those are not 5.2.2 or 5.1.3 solutions in positive integers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/fifth-powers-lps-5-2-2-or-5-1-3.md
```

Already set up? Say `run V3R1T4S on fifth-powers-lps-5-2-2-or-5-1-3`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fifth-powers-lps-5-2-2-or-5-1-3`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
