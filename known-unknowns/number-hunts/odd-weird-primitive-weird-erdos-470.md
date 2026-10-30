# MOONSHOT - Erdős #470: an odd weird number, or primitive weird numbers with more than 16 prime factors or a cubed odd prime factor

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (structured abundant-number search with exact subset-sum checks); the odd case has long odds · open as of 2026-10-30

## The problem

n is weird if sigma(n) >= 2n but n is not pseudoperfect (not a sum of distinct proper divisors), and primitive weird if no proper divisor is weird (OEIS A006037, A002975). Erdős Problem #470 on erdosproblems.com asks whether any odd weird number exists and whether there are infinitely many primitive weird numbers (last edited 18 Jan 2026; Guy reports $10 from Erdős for the odd question). Known: no odd weird number below 10^21, and none below 10^28 with abundance below 10^14 (Wenjie Fang, arXiv:2207.12906, 2022, with the yoyo@home volunteer project). An odd weird number has at least 6 prime divisors (Liddy and Riedl, 2018). Melfi (2015) proved there are infinitely many primitive weird numbers if prime gaps satisfy p_(n+1) - p_n < p_n^(1/2)/10 for large n. Gianluca Amato, Maximilian Hasler, Giuseppe Melfi and Maurizio Parton (J. Number Theory 2019, arXiv:1802.07178) found primitive weird numbers with up to 16 DISTINCT prime factors; the largest, with 16 distinct primes, has 14712 digits. They also found the first examples with two or three squared odd prime factors and proved none has a cubed or higher odd prime factor when Omega <= 7; they found none for larger Omega. Counted with multiplicity there is no record to beat: 2^k*p*q examples with Omega up to at least 20 are listed in OEIS A258375 (Robert G. Wilson v, M. F. Hasler). OEIS A002975 (b-file of 1161 terms, Robert G. Wilson v) was last edited 5 Oct 2026 with no larger record.

## What counts as a win

CONFIRMED (full win): an odd n with complete proven factorisation and sigma(n) > 2n, together with an exact, verifier-reimplemented proof that n is not a sum of distinct proper divisors of n. Equivalently, the abundance a = sigma(n) - 2n is not a sum of distinct proper divisors of n. n must be absent from OEIS A006037 and from the erdosproblems.com #470 page, both re-fetched immediately before the claim.

## Partial wins

- **p1:** A primitive weird number with at least 17 DISTINCT prime factors (omega(n) >= 17). It must be certified weird by the same exact check, certified primitive by sigma(n/p) < 2n/p for every prime p | n, and be absent from the Amato-Hasler-Melfi-Parton tables and OEIS A002975 at verification time.
- **p2:** A primitive weird number divisible by p^3 for some odd prime p, with the same certificates (none is known).

## How a win is checked

Prove the factors and compute sigma(n) exactly. Decide whether a = sigma(n) - 2n is a sum of distinct proper divisors of n by an exact subset-sum over the proper divisors not exceeding a: bitset dynamic programming when a is small, otherwise the verifier's own exact branch-and-bound. For primitivity, check that n/p is deficient for every prime p | n: any abundant proper divisor of a weird number would itself be weird, since a pseudoperfect divisor would make n pseudoperfect. Count distinct prime factors for p1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/470>

## Sources

- <https://www.erdosproblems.com/470>
- <https://oeis.org/A006037>
- <https://oeis.org/A002975>
- <https://arxiv.org/abs/2207.12906>
- <https://arxiv.org/abs/1802.07178>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Abundance-boundary search (Fang): odd weird candidates must be barely abundant; enumerate odd primitive abundant numbers with tiny abundance by reverse search and test the subset-sum condition only on those.
- AHMP construction for primitive weird numbers: n = m*p*q with m a deficient 2-power-times-odd core and p, q chosen so that the abundance is small and avoids the subset sums of the divisors of m; push Omega past 16 or include p^3 in m.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Pseudoperfect allows any subset of proper divisors, not only the largest ones; a greedy failure is not a proof of weirdness.
- Weird does not mean primitive weird: a weird number times a prime larger than its sigma is again weird.
- Fang's bounds already exclude odd weird numbers below 10^21.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/odd-weird-primitive-weird-erdos-470.md
```

Already set up? Say `run V3R1T4S on odd-weird-primitive-weird-erdos-470`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `odd-weird-primitive-weird-erdos-470`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
