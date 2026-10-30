# Three-colour Rado numbers R_3(ax + by = cz): refute an Ahmed–Zaman–Bright conjecture or settle a cell beyond the SAT tables

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The k-colour Rado number R_k(E) is the least n such that every k-colouring of [1,n] has a monochromatic solution of E in positive integers (infinite if no such n exists). Yuan Chang, Jesús De Loera and William Wesley (ISSAC 2022, arXiv:2210.03262) used SAT to compute R_3(ax+by=cz) for all small coefficients (1 <= a,b,c <= 5 per their abstract, <= 6 as cited later), R_3(ax-ay=bz) for a,b <= 15 and R_3(ax+ay=bz) for a,b <= 10. They also proved Myers' conjecture R_3(x-y=(m-2)z) = m^3-m^2-m-1. Tanbir Ahmed, Lamina Zaman and Curtis Bright (arXiv:2505.12085 v3, Oct 2025; SC-square 2025) tabulated R_3(ax+by=bz) for 1 <= b <= 15, 1 <= a <= 30 and R_3(ax+ay=bz) for 1 <= a <= 15, 1 <= b <= 25, and proved lower bounds with symbolic sets. They conjecture: (1.1) R_3(ax+by=bz) = a^3+a^2+(2b+1)a+1 for coprime a > b >= 3 with a^2+a+b > b^2+ba, where the lower bound is their Theorem 1.3; and (1.2) R_3(ax+ay=bz) = a^3 b for odd a coprime to b with 3 <= a < b <= 2a-1. For odd a >= 7 they prove only R_3(ax+ay=(a+1)z) >= a^3(a+1). Values outside these tables are open, as are both conjectures.

## What counts as a win

Success means refuting Conjecture 1.1 or 1.2 of the latest arXiv:2505.12085 for an admissible (a,b), with one of two certificates. (i) A 3-colouring of [1, V], where V is the conjectured value, with no monochromatic solution in positive integers (variables need not be distinct), verified by two independent programs. This proves R_3 > V (direction: max). (ii) For Conjecture 1.2 only, at an (a,b) where the lower bound R_3 >= a^3 b is not proven (it is proven for b = a+1 with odd a >= 7, Theorem 1.4): a DRAT or LRAT certificate, checked by drat-trim or cake_lpr, that every 3-colouring of [1, V-1] has a monochromatic solution. This proves R_3 < V (direction: min). Re-fetch arXiv:2505.12085 and search for newer Rado-number papers immediately before claiming.

## Partial wins

- **p1:** A new exact value R_3(ax+by=cz) for positive a,b,c <= 30 with gcd(a,b,c) = 1, a+b != c and R_3 finite, for a triple that appears, up to swapping a and b, in none of the tables of arXiv:2210.03262, arXiv:2505.12085 or later papers found by a fresh search. (With repetition allowed, a+b = c gives the monochromatic solution x = y = z, so R = 1 trivially; such cells do not count.) It needs a valid colouring of [1, R-1] and a checked DRAT or LRAT UNSAT certificate for [1, R].
- **p2:** A new exact four-colour Rado number R_4(ax+by=cz) with a,b,c <= 6 and gcd(a,b,c) = 1, for an equation with a = c or b = c (so R_4 is finite by Rado's theorem; the other columns-condition case a+b = c is trivial, R = 1 via x = y = z), excluding x+y=z (Schur, R_4 = 45) and counting (a,b,c) and (b,a,c) as one equation, with no published value found by a fresh search. It needs a valid colouring of [1, R-1] and a checked UNSAT certificate for [1, R].

## How a win is checked

Colouring check: for every pair (x, y) in [1,N]^2 with a x + b y divisible by c and z = (a x + b y)/c in [1, N], assert that x, y and z do not all share a colour. This is O(N^2), about 10^10 for N = 10^5, so use C. For the second implementation, loop over (x, z) and solve for y. UNSAT side: regenerate the CNF from the definition with an independently written generator, check the solver's proof with drat-trim or cake_lpr, and confirm that the CNF has exactly one at-least-one-colour clause per integer.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2505.12085>

## Sources

- <https://arxiv.org/abs/2505.12085>
- <https://arxiv.org/abs/2210.03262>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ahmed-Zaman-Bright's symbolic-set colourings are unions of intervals scaled by powers of a. Search the parametric family one level richer (more intervals per colour) with a solver, for (a,b) near the boundary a^2+a+b = b^2+ba of Conjecture 1.1.
- For Conjecture 1.2, test even a and the edge b = 2a-1 first, where Observation 2.3 says patterns break down.
- Incremental SAT: fix the best colouring of [1, V-1] except a sliding window and try to extend to V.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention: R_k is the least n at which every colouring fails, so a valid colouring of [1, N] proves R > N.
- Equations with degree of regularity < 3 have R_3 = infinity. Check Rado's conditions and the dor results in arXiv:2210.03262 before computing.
- Do not require x, y, z to be distinct; the standard Rado number allows x = y.
- With repetition allowed, every equation with a+b = c has the solution x = y = z, so its Rado number is 1; such cells are not new values. Scaled triples (common factor) and a <-> b swaps are the same equation.
- Theorem 1.4 of arXiv:2505.12085 proves R_3(ax+ay=(a+1)z) >= a^3(a+1) for odd a >= 7, so an UNSAT refutation of Conjecture 1.2 cannot exist at b = a+1 there.
- The abstract of arXiv:2210.03262 says exact values for 1 <= a,b,c <= 5, while later citations say <= 6. Check the actual tables before calling a cell new.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/three-colour-rado-numbers-ax-by-cz.md
```

Already set up? Say `run V3R1T4S on three-colour-rado-numbers-ax-by-cz`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-colour-rado-numbers-ax-by-cz`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
