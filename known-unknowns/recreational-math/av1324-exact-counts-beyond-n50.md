# 1324-avoiding permutations: the exact count |Av_51(1324)| (first term beyond Conway-Guttmann-Zinn-Justin's n = 50)

🎲 **Recreational math** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster (the n = 50 run used about 4.2 TB of distributed memory, 168 cores x 20 GB, and memory grows about 4x per +2 in n) unless a new algorithm changes the scaling · open as of 2026-10-30

## The problem

The number of permutations of length n avoiding 1324 (OEIS A061552) has no known formula or useful functional equation. Exact counts: early terms by Darko Marinov (2001) and Vincent Vatter (2005), Michael Albert et al. (to n = 25), Fredrik Johansson and Brian Nakamura (to 31, 2014), Andrew Conway and Anthony Guttmann (to 36, 2015) and Andrew Conway, Anthony Guttmann and Paul Zinn-Justin ('1324-avoiding permutations revisited', Adv. Appl. Math. 2018, arXiv:1709.01248) to n = 50. CGZ's transfer-matrix algorithm has states counted by sums of Catalan numbers up to n/2, ran five times modulo different primes and combined the results by the Chinese remainder theorem; 'the only limit to obtaining additional terms is computer memory'. The OEIS b-file (David Bevan; terms 37-50 credited to Bjarki Agust Gudmundsson) stops at n = 50 on 2026-10-30, and an arXiv search the same day found no exact count beyond n = 50 (2024-2026 work on Av(1324) concerns inversions, involutions, growth bounds and griddings).

## What counts as a win

Success means the exact integer |Av_n(1324)| for some n >= 51 (strictly beyond the largest n in the live A061552 b-file and in every paper found by an arXiv search, re-checked immediately before claiming), computed by two independent runs that agree exactly (two different algorithms, or one algorithm run modulo enough distinct primes with a second, independently written implementation for at least one modulus), where the same code reproduces every published term a(0..50) exactly. The value must also pass the ratio-analysis sanity check in verification_method.

## Partial wins

- **p1:** a(51) modulo a stated prime p >= 2^31, computed by two independently written programs that agree and that both reproduce a(n) mod p for all n <= 50 from the published b-file.
- **p2:** A documented implementation of an algorithm different from CGZ's transfer matrix (for example the insertion-encoding, functional-equation or Combinatorial Exploration route) that reproduces all of a(0..50) exactly; reproduction only, but a prerequisite for the two-run rule.

## How a win is checked

Skeptic: run the claimant's code on small n (<= 30) and compare against the b-file; check the agreement of both independent runs for the new term; if moduli are used, check the CRT reconstruction and that the product of moduli exceeds an upper bound for a(51) (for example 16^51). Sanity: the ratio a(51)/a(50) must sit on the extrapolated ratio curve of CGZ (mu ~ 11.60, with the stretched-exponential correction mu^n mu1^sqrt(n) n^g); a mismatch in the fourth significant figure is a red flag.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A061552/b061552.txt>

## Sources

- <https://oeis.org/A061552>
- <https://oeis.org/A061552/b061552.txt>
- <https://arxiv.org/abs/1709.01248>
- <https://arxiv.org/abs/1405.6802>
- <https://arxiv.org/abs/1309.7117>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Import from statistical-physics series work: CGZ already use modular arithmetic and CRT; a memory-lean variant that streams the transfer matrix from disk (sorted external memory) trades RAM for SSD and may bring n = 51 to one large workstation.
- Exploit symmetry: 1324 is fixed by reverse-complement and inverse, so states can be folded by the symmetry group before storage.
- Start with a(51) mod a single 61-bit prime (p1); that already needs only one run's memory.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Off-by-one in the index: the OEIS offset is 0 (a(0) = 1); the CGZ paper lists terms by length n.
- The data field of the OEIS entry stops at n = 25; the b-file holds n <= 50.
- Integer size: a(50) is about 1.5 * 10^42; use 64-bit or 128-bit residues and arbitrary precision only at the CRT step.
- A computation of 1324-avoiding involutions (A230554) or of 1324-avoiders with few inversions is a different sequence.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/av1324-exact-counts-beyond-n50.md
```

Already set up? Say `run V3R1T4S on av1324-exact-counts-beyond-n50`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `av1324-exact-counts-beyond-n50`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
