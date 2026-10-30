# Least Carmichael number with exactly 62 prime factors: the next term a(62) of OEIS A006931

🔢 **Number hunts** · standard · tractability ★★★☆☆ · compute: laptop-days (subset-product search over primes below a few thousand) · open as of 2026-10-30

## The problem

A Carmichael number is a squarefree composite n with p - 1 | n - 1 for every prime p | n (Korselt's criterion). OEIS A006931 (N. J. A. Sloane and Richard Pinch) gives the least Carmichael number with exactly n prime factors. Its b-file (Jonathan Webster) runs to n = 61: terms 3..35 come from Pinch's tables, and terms 36..39 were found by Aidan Johnson and Sylvia Webster (Butler University undergraduates) with a prime-by-prime search with composite completions. Those four are reported in Andrew Shallue and Jonathan Webster's 'Algorithms for Carmichael numbers' (arXiv:2506.09903, v3 13 Jan 2026), which also tabulates all 308,279,939 Carmichael numbers below 10^24. Terms 40..61 were computed by Jonathan Webster and Sylvia Webster (b-file installed in OEIS edit #70, 17 Aug 2026). a(61) has 140 digits. Our own check on 2026-10-30 confirmed that every term from a(36) to a(61) is a Carmichael number with the stated number of prime factors, all of them below 2700. a(62) is not listed. Alford, Grantham, Hayman and Shallue (Math. Comp. 2014) gave constructive upper bounds for a(3) to a(19565220), so a Carmichael number with 62 prime factors exists.

## What counts as a win

CONFIRMED (full win): a squarefree n with exactly 62 distinct prime factors, given with its complete proven factorisation, satisfying (n - 1) % (p - 1) == 0 for every p | n, TOGETHER WITH an exhaustive-search program and log showing that no Carmichael number with exactly 62 prime factors is smaller, which the verifier reimplements independently and reproduces; a(62) must still be absent from the data and b-file of https://oeis.org/A006931, re-fetched immediately before the claim.

## Partial wins

- **p1:** Upper bound: an explicit Carmichael number with exactly 62 distinct prime factors and at most 145 decimal digits (a(61) has 140), checked by Korselt's criterion, while a(62) is still absent from A006931 at verification time.

## How a win is checked

Trial-divide n (all factors are expected to be small) and check squarefreeness, the count of 62 factors and Korselt's criterion with Python big integers. Compare the digit length with 145 and confirm a(62) is still absent from the b-file. For the full win, independently reimplement the minimality search and confirm nothing smaller exists, for example a prime-by-prime search with composite completions up to the claimed value, or an enumeration of candidate lambda values L and subsets of primes p with p - 1 | L whose product is 1 mod L.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006931>

## Sources

- <https://oeis.org/A006931>
- <https://oeis.org/A006931/b006931.txt>
- <https://arxiv.org/abs/2506.09903>
- <https://arxiv.org/abs/1203.6664>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Subset-product formulation (Erdős construction; Alford-Grantham-Hayman-Shallue): fix a smooth L, list the primes p with p - 1 | L and p not dividing L, and look for 62 of them whose product is 1 mod L, minimising the product; meet-in-the-middle over residues mod L.
- Seed from a(61): inspect its prime set and lambda, and try swapping or adding a few primes so that the product stays 1 mod the new lambda.
- Integer programming on logarithms (imported from operations research): minimise sum log p subject to a modular product constraint, with branch-and-bound pruning by the smallest possible remaining product.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The count is of distinct prime factors; Carmichael numbers are squarefree by definition.
- A small 62-factor example is only an upper bound; claiming a(62) needs a complete minimality search.
- Korselt's criterion needs p - 1 | n - 1 for EVERY prime factor, not just lambda(n) computed from a subset.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/carmichael-least-62-prime-factors.md
```

Already set up? Say `run V3R1T4S on carmichael-least-62-prime-factors`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `carmichael-least-62-prime-factors`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
