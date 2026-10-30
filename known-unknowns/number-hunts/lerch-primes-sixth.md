# Lerch primes: a sixth one beyond 2*10^8 (OEIS A197632)

🔢 **Number hunts** · standard · tractability ★☆☆☆☆ · compute: laptop-days (extending the 2026 search by a factor of 2 is several times its cost; claims check in minutes) · open as of 2026-10-30

## The problem

An odd prime p is a Lerch prime if p divides the Lerch quotient l_p = (sum_{a=1}^{p-1} q_p(a) - w_p)/p, where q_p(a) is the Fermat quotient and w_p the Wilson quotient. Equivalently, sum_{a=1}^{p-1} a^(p-1) - (p-1)! == p (mod p^3). Lerch (1905) showed this congruence holds mod p^2 for every odd prime. Jonathan Sondow named these primes (2011). OEIS A197632 (revision 93, 2026-08-30; keywords hard, more) lists 3, 103, 839, 2237 and 42447347. Veljko Vranic added the fifth term on 2026-08-21 and the comment 'a(6) > 2*10^8 if it exists' on 2026-08-30. His repository github.com/veljkovranic/lerch reports an exhaustive test of every prime up to 200,000,000 with a primitive-root recurrence for Fermat quotients, three independent rechecks of hits (Rust mod p^2/p^3, CPython, FLINT Bernoulli), and invites outside reproduction. The lane checker confirmed the four small terms below 3000. Rene Gy showed a prime is both Lerch and Wilson iff (p-1)! == -1 (mod p^3).

## What counts as a win

CONFIRMED (full win) for a proven prime p > 2*10^8 (direction: the first new term above the bound stated in the live entry) such that (sum_{a=1}^{p-1} pow(a, p-1, p^3) - (p-1)! - p) mod p^3 == 0, computed exactly and checked by two independently written programs. p must be absent from the DATA, comments and b-file of https://oeis.org/A197632 and from the veljkovranic/lerch repository (both re-fetched immediately before the claim), and p must be greater than any searched bound they state at that time. Being a(6) also requires a logged complete search from the stated bound to p; without that it is still a new Lerch prime and counts as the full win.

## Partial wins

- **p1:** Search extension certificate: every prime from 2e8 to at least 4e8 tested, with per-block hashes of l_p mod p published, reproducing all five known terms, and surviving a random 0.5% recomputation by the verifier with a different algorithm.
- **p2:** Independent reproduction of Vranic's 2e8 search with code sharing nothing with his repository, with block hashes that agree (or a demonstrated discrepancy: a prime below 2e8 where the two disagree, settled by a direct mod p^3 computation).

## How a win is checked

Prove p prime. Compute S = sum a^(p-1) mod p^3 directly (O(p) modular powers, or via a primitive root g so that a^(p-1) runs over g^(k(p-1))), and (p-1)! mod p^3 with a fast factorial (FLINT or PARI). Check S - (p-1)! - p == 0 mod p^3. Cross-check with Lerch's formula in the form sum q_p(a) == w_p mod p^2.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A197632>

## Sources

- <https://oeis.org/A197632>
- <https://github.com/veljkovranic/lerch>
- <https://arxiv.org/abs/1110.3113>
- <https://arxiv.org/abs/1311.2242>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Faulhaber's formula gives sum_{a < p} a^(p-1) == p*B_{p-1} (mod p^3) for p > 3, which reduces the test to p*B_{p-1} - (p-1)! == p (mod p^3). Derive this rigorously before relying on it, then look for multi-prime remainder-tree methods for both pieces.
- Amortised remainder trees for (p-1)! mod p^3 (an extension of Costa-Gerbicz-Harvey) remove the O(p) factorial cost per prime.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Vranic may have extended the search since 2026-08-30: re-read the repository's VERIFIED_INTERVALS.md before claiming.
- The congruence holds mod p^2 for every odd prime, so a mod p^2 test accepts every prime and proves nothing; the test must be done mod p^3.
- Overflow: p^3 exceeds 2^64 for p > 2.6e6.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/lerch-primes-sixth.md
```

Already set up? Say `run V3R1T4S on lerch-primes-sixth`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lerch-primes-sixth`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
