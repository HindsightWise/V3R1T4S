# MOONSHOT - Kurepa's left factorial conjecture: an odd prime p dividing !p = 0!+1!+...+(p-1)!, beyond 2^40

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (the full 2^40 search was a major run; a contiguous range extension is laptop-days) · open as of 2026-10-30

## The problem

Duro Kurepa (1971) conjectured that gcd(!n, n!) = 2 for all n >= 2, where !n = sum_{k=0}^{n-1} k!. This is equivalent to: no odd prime p divides !p. Vladica Andrejic and Milos Tatarevic (Math. Comp. 85, 2016) searched all primes below 2^34 and found none, though heuristics suggest a counterexample probably exists. Their generalised k = 5 variant has the counterexample p = 9632267. Andrejic, Alin Bostan and Tatarevic ('Improved algorithms for left factorial residues', Information Processing Letters 167, 2021; arXiv 1904.09196 v3) computed !p mod p for all primes p < 2^40 and found no odd p dividing !p. Claimed proofs exist and are not accepted: Barsky-Benzaghou (2004, withdrawn in 2011) and V. M. Abramov (arXiv 2209.12677, 2022, withdrawn by the author). No 2024-2026 extension was found on 2026-10-30. Heuristically, the expected count in [2^40, 2^41] is about ln(41/40), roughly 0.025.

## What counts as a win

CONFIRMED (full win) for an explicit odd prime p (proven prime) with sum_{k=0}^{p-1} k! == 0 (mod p), computed exactly by two independent methods. Since the 2021 search covered all p < 2^40 (= 1099511627776), any genuine counterexample should exceed it; a p below 2^40 is reported as a discrepancy with that search and still counts if it checks out. Direction: existence of one counterexample. A proof of the conjecture also counts as the full win, but only as a Lean 4 proof with no sorry and a clean axiom audit.

## Partial wins

- **p1:** Range extension certificate: all primes in [2^40, 2^40 + 10^10] with residues !p mod p published in hashed blocks and every prime with |!p mod p| < 100 (symmetric residue) listed. The certificate must survive a random 0.1% recomputation by the verifier using a different algorithm (a single-prime O(sqrt(p) log p) method).
- **p2:** Independent reproduction: !p mod p computed, with code sharing nothing with the authors', for all 24 primes in Table 1 of arXiv 1904.09196 (primes in (2^34, 2^40) with |!p mod p| < 100) and for p = 6855730873 (residue 2, from arXiv 1409.0800), all matching the published values, or an exactly demonstrated discrepancy.

## How a win is checked

Prove p prime. Compute !p mod p for that single p with an O(sqrt(p) log p) fast algorithm (matrix-product / polynomial multipoint evaluation of the recurrence (s, f) -> (s + f, f*k)), and independently by a straight O(p) loop if p is small enough. Check the residue is 0.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1904.09196>

## Sources

- <https://arxiv.org/abs/1904.09196>
- <https://doi.org/10.1016/j.ipl.2020.106078>
- <https://arxiv.org/abs/1409.0800>
- <https://doi.org/10.1090/mcom/3098>
- <https://oeis.org/A049782>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Port the 2021 amortised remainder-tree idea: !p mod p is a product of 2x2 matrices [[k,0],[1,1]] evaluated mod p, computed for many primes at once.
- GPU batch over consecutive primes with 64-bit Montgomery arithmetic (p < 2^42 fits).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Claimed full proofs (Barsky-Benzaghou 2004, withdrawn 2011; Abramov, arXiv 2209.12677, withdrawn 2022) are not accepted.
- The k-generalised left factorial counterexample (p = 9632267) is not a Kurepa counterexample.
- !p sums k! for k = 0..p-1 (includes 0! = 1).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/kurepa-left-factorial-beyond-2-40.md
```

Already set up? Say `run V3R1T4S on kurepa-left-factorial-beyond-2-40`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kurepa-left-factorial-beyond-2-40`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
