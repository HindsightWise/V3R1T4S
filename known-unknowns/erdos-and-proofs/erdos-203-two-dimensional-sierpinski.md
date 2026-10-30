# Erdős #203: an m coprime to 6 with every 2^k 3^l m + 1 composite (a two-dimensional Sierpiński number)

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (covering search over prime pools from cyclotomic gcds) · open as of 2026-10-30

## The problem

Is there an integer m >= 1 with gcd(m,6) = 1 such that 2^k 3^l m + 1 is composite for all k, l >= 0 (Erdős-Graham [ErGr80, p.27])? Ordinary Sierpiński numbers (one exponent) exist via covering systems; here the covering must work on the two-dimensional torus. For a prime p, the pairs (k,l) with p | 2^k 3^l m + 1 form one coset of a lattice of index |H_p| = | < 2,3> mod p| = lcm(ord_p 2, ord_p 3); a covering set P needs sum 1/|H_p| >= 1. Forum: AnimishSharma (2026-06-21) proves the subgroup formula and the density condition and, computationally, excludes coverings with lcm |H_p| < 5040 among primes p <= 5e7, with best coverage 71-72% at moduli 5040 and 10080; veljjanoski (2026-09-15, code: github.com/veljjanoski/erdos203) builds complete prime pools from gcd(Phi_a(2), Phi_b(3)) (442 primes with |H_p| <= 2000, sum 1/|H_p| = 1.97; 1006 primes with |H_p| <= 5000, sum 2.15) and reaches at best 76.0% exact coverage of the torus at N = 55440 (55 primes); his README also reports sampled (not exact) strip coverages up to 81.3% with the 1006-prime pool. Off the forum, the-omega-institute/trureturing issue #9414 (2026-09-22, an AI-agent project, reviewed only by agents) claims that no prime-only covering exists using primes with |H_p| <= 5000 (all sizes), plus finite-family obstructions at N = 404779703328000. Any solution must itself be an ordinary Sierpiński number (take l = 0); 78557 fails (2*3^2*78557+1 = 1414027 is prime). Status: open on erdosproblems.com and in the teorth database.

## What counts as a win

CONFIRMED: an integer m >= 1 with gcd(m,6)=1, together with a finite set P of primes, such that for EVERY (k,l) in Z_{ > =0}^2 some p in P divides 2^k 3^l m + 1 and 2^k 3^l m + 1 > p. Checked by: for each p, computing a = ord_p(2), b = ord_p(3) and the set of residue pairs (k mod a, l mod b) killed by p; verifying the union covers all of Z_A x Z_B with A = lcm of the a's and B = lcm of the b's; and confirming 2^k 3^l m + 1 != p for the finitely many small (k,l) where equality could occur. A proof that no such m exists is also a full win (pure thought, checkable line by line or in Lean).

## Partial wins

- **p1:** An exact, reproducible proof (density computation plus exhaustive search where needed) that no covering set exists with lcm(|H_p| : p in P) < 10080, valid for primes of every size (using that p | gcd(Phi_a(2), Phi_b(3)) bounds the pool). This improves the forum exclusion (lcm < 5040, primes p <= 5e7) and is not implied by the trureturing #9414 claim (all |H_p| <= 5000), because it must also handle primes with 5000 < |H_p| < 10080 that divide the lcm.

## How a win is checked

Independent re-implementation: compute multiplicative orders with exact integer arithmetic, build the killed cosets, and count uncovered cells of the torus (or verify the covering by iterating over a coarser CRT decomposition). For m itself, spot-check thousands of random (k,l) by direct trial division by P. For p2, re-derive the complete prime pool from cyclotomic gcds and recompute the density sums exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/203>

## Sources

- <https://www.erdosproblems.com/203>
- <https://www.erdosproblems.com/forum/thread/203>
- <https://github.com/veljjanoski/erdos203>
- <https://github.com/the-omega-institute/trureturing/issues/9414>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Look for nested lattice chains: primes whose (ord_p 2, ord_p 3) pairs divide each other, mimicking the 2|4|8|...|64 chains of 1D Sierpiński coverings; the forum found these are rare at small order, so consider primes of order in the 10^4-10^6 range from factor tables of 2^a - 1 and 3^b - 1.
- Partial algebraic factorisations (m a perfect power) can cover a sublattice without primes; the forum tried cubes and 12th powers with no gain, but other shapes are untested.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The density condition sum 1/|H_p| >= 1 is necessary but far from sufficient; plateaus near 1 - exp(-sum) are expected for random choices.
- m must be coprime to 6, and the case 2^k 3^l m + 1 = p itself must be excluded.
- Erdős-Graham's variant with primes q = 1 mod 4 has the trivial answer m = 1 (Dogmachine); do not confuse the variants.
- Torus coverage percentages are not a partial win: sampled strips already reach about 81%, and a trureturing construction attempt (#9414) is reported to fail only at (k,l) = (1,2). Only a complete covering counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-203-two-dimensional-sierpinski.md
```

Already set up? Say `run V3R1T4S on erdos-203-two-dimensional-sierpinski`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-203-two-dimensional-sierpinski`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
