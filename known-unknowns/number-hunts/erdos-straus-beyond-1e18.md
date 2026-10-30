# MOONSHOT - Erdős–Straus conjecture (Erdős #242): 4/n with no 3-term Egyptian fraction, or verification beyond 10^18

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days for a range-extension partial win; needs cluster for a large extension · open as of 2026-10-30

## The problem

The Erdős–Straus conjecture (Erdős problem #242) says that for every n > 2 there are positive integers x < y < z with 4/n = 1/x + 1/y + 1/z. It suffices to treat primes n, and Mordell's identities cover every prime except those in six classes mod 840 (1, 121, 169, 289, 361, 529). Verification history: Oblath to 1e5; Yamamoto to 1e7; Swett to 1e14; Salez to 1e17 (arXiv 1406.6307, 2014); Spiridon Mihnea and Bogdan C. Dumitru to 1e18 (arXiv 2509.00128, 2025-08-29), extending Salez's modular-filter sieve with S_29 to a set R_8 of 2,101,514 residue classes. Problem page #242 (last edited 2026-05-07) cites the 1e18 bound and still lists the problem as open. Its forum thread rejects several 2025-2026 'proofs': a ResearchGate paper, arXiv 2508.07367, the Bradford preprint arXiv 2602.11774, and a Lean 'full CRT coverage' claim. A counterexample is believed not to exist; the realistic win is a certified extension.

## What counts as a win

CONFIRMED (full win) for an integer n > 10^18 with a complete proof that no positive integers x, y, z solve 4/n = 1/x + 1/y + 1/z (finite exhaustive case analysis, machine-checked or independently re-run in full). This is a moonshot. A full proof of the conjecture counts only as a Lean proof with no sorry and a clean axiom audit. Range extensions are partial wins only and must start from the bound stated on https://www.erdosproblems.com/242 and in arXiv 2509.00128 at verification time (1e18 on 2026-10-30; direction: larger verified bound).

## Partial wins

- **p1:** Certified extension: every prime p in (1e18, 1e18 + 1e16] that lies in a residue class not covered by the published identities and filters is given an explicit (x, y, z), and the code that proves the remaining classes are covered is released. The verifier checks 4xyz == n(xy + yz + zx) exactly for a random 10^6 of the listed primes and re-runs the class-coverage proof.
- **p2:** Independent reproduction of the 1e17 to 1e18 range (Mihnea-Dumitru) with code sharing nothing with theirs, publishing per-block hashes of the hard primes and their solutions, or a demonstrated error in their filter (a prime in a class they excluded as covered for which their identity fails).

## How a win is checked

For listed solutions, check 4*x*y*z == n*(x*y + y*z + z*x) with exact integers. For coverage, re-derive each modular identity symbolically (SymPy) and check that the union of covered classes plus the explicitly solved primes is the whole range. Spot-check random primes with an independent solver.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/242>

## Sources

- <https://www.erdosproblems.com/242>
- <https://www.erdosproblems.com/forum/thread/242>
- <https://arxiv.org/abs/2509.00128>
- <https://arxiv.org/abs/1406.6307>
- <https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Add one more prime filter (S_31) to the Salez/Mihnea-Dumitru sieve so the surviving class density drops, then sieve primes only in surviving classes.
- For survivors, use the divisor criterion: a solution with x = ceil(n/4) + t exists iff some divisor condition on (4x - n) holds; search small t first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many 'proofs' circulate; the problem page and its forum thread reject all of them so far.
- Periodicity arguments do not prove a residue class is covered (Bloom on the #242 forum).
- The generalized Erdős–Straus–Schinzel versions (5/n, k/n) are different problems.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/erdos-straus-beyond-1e18.md
```

Already set up? Say `run V3R1T4S on erdos-straus-beyond-1e18`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-straus-beyond-1e18`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
