# Generalized Wilson primes: the first prime of order n for the 24 orders n < 100 with none known (OEIS A128666)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-days (an all-primes Wilson-quotient remainder tree to 1e10 or more; checking a claim takes seconds) · open as of 2026-10-30

## The problem

A prime p >= n is a generalized Wilson prime of order n when p^2 divides (n-1)!(p-n)! - (-1)^n. Order 1 gives the Wilson primes. Equivalently, the Wilson quotient w_p is congruent to the harmonic number H(n-1) mod p. OEIS A128666 (Alexander Adamchuk 2007; terms added by Max Alekseyev 2012; edited by M. F. Hasler 2015; last revision #30, 2025-02-16; keywords hard, more) lists the least such prime for each order. Its comments give values for most n <= 100, including large ones such as a(72) = 14273449 and a(18) = 13151527. They also state that no prime below 1.4*10^7 is known for n in {8, 12, 14, 22, 23, 25, 29, 31, 38, 46, 48, 50, 52, 66, 77, 79, 82, 84, 87, 89, 91, 95, 96, 98, 99}. That list is out of date for n = 31, because the same entry gives a(31) = 20981, which a lane checker confirmed on 2026-10-30. So 24 orders below 100 have no known prime, and no search past 1.4e7 is reported anywhere. The Costa-Gerbicz-Harvey remainder-tree method computes (p-1)! mod p^2 for all p up to 2e13. Every order then follows at no extra cost, because (p-n)! = (p-1)!/((p-1)(p-2)...(p-n+1)) mod p^2. Heuristically, each order expects about ln(ln X / ln 1.4e7) primes up to X: about 0.33 per order at X = 1e10, or roughly 8 hits over the 24 open orders.

## What counts as a win

CONFIRMED (full win) for each pair (n, p) where n is in the open set {8, 12, 14, 22, 23, 25, 29, 38, 46, 48, 50, 52, 66, 77, 79, 82, 84, 87, 89, 91, 95, 96, 98, 99} and p is a proven prime with ((n-1)! * (p-n)! - (-1)^n) mod p^2 == 0. The claim must also show, from a complete logged search, that no prime below p satisfies the condition for that order, which settles a(n). The order must still have no value in the DATA, comments or b-file of https://oeis.org/A128666, re-fetched immediately before the claim. A prime of order n that is not shown to be the least counts as partial win p1. Each order settled counts once. Direction: minimize the number of unsettled orders below 100.

## Partial wins

- **p1:** A proven prime p > 1.4e7 that is a generalized Wilson prime of an open order n (congruence checked exactly), with the minimality search not yet complete. This gives an upper bound on a(n).
- **p2:** Search certificate: all primes up to at least 1e9 tested for all 24 open orders, with the Wilson residues (p-1)! mod p^2 published in hashed blocks. The run must reproduce every known a(n) <= 1e9 from the A128666 comments (for example a(18) = 13151527 and a(72) = 14273449) and survive a random 0.1% recomputation by the verifier.
- **p3:** First prime p > 1.4e7 for an order n in 100 < n <= 200 that has no generalized Wilson prime below 1.4e7 and no value given anywhere in A128666, shown to be the least by a logged search over all primes from n to p. (Most orders in this range have small least primes, for example a(101) = 149 and a(102) = 2903, found in seconds; those do not count.)

## How a win is checked

Prove p prime (BPSW plus PARI isprime). Compute (n-1)! mod p^2 directly, and compute (p-n)! mod p^2 independently, either by a direct product for p up to about 1e8 or as (p-1)! times the inverse of prod_{j=1}^{n-1}(p-j), with (p-1)! from a fast factorial (PARI or FLINT), and check the congruence. For minimality, rerun the claimant's search on random sub-ranges and reproduce all known small a(n). A naive O(p) checker reproduces every listed a(n) < 60000 in minutes; a(31) = 20981 was independently re-confirmed on 2026-10-30.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A128666>

## Sources

- <https://oeis.org/A128666>
- <https://oeis.org/A079853>
- <https://en.wikipedia.org/wiki/Wilson_prime>
- <https://arxiv.org/abs/1209.3436>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Implement the Costa-Gerbicz-Harvey accumulating remainder tree for (p-1)! mod p^2 over all primes in a block, then test all open orders in O(n) per prime from the one Wilson residue.
- Use the equivalent test w_p == H(n-1) (mod p), with H(n-1) mod p precomputed for n <= 200, so each prime needs one Wilson quotient mod p plus a table lookup.
- Run blocks in order of increasing p so the first hit for each order is its least prime, and keep a block log for minimality.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The A128666 comment's 'not known' list wrongly includes n = 31; a(31) = 20981 is already in the same entry.
- p must be at least n; for p < n the expression is undefined.
- An upper bound (some prime of order n) is not a(n) unless every smaller prime was tested.
- Floating point or 64-bit overflow in mod p^2 products: use 128-bit or Montgomery arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/generalized-wilson-primes-open-orders.md
```

Already set up? Say `run V3R1T4S on generalized-wilson-primes-open-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `generalized-wilson-primes-open-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
