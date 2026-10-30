# Fibonacci and Lucas numbers F_n, L_n (n < 10,000): a new factor of a listed composite cofactor

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (GMP-ECM or P-1 on the large cofactors; NFS on the C200-C280 holes needs cluster) · open as of 2026-10-30

## The problem

The Fibonacci and Lucas factorization tables at mersennus.net/fibonacci carry on the Brillhart-Montgomery-Silverman tables (Math. Comp. 1988). They list known factors of F_n and L_n for n < 10,000, mark composite cofactors with (C), and publish every remaining composite in composite2000.gz ... composite10000.gz, along with 'holes' files. On 2026-10-30 every F_n and L_n with n <= 1000 is fully factored. The first holes are F1423 (C276) and L1423 (C232); fibholes.txt lists 3,641 incomplete F_n and lucholes.txt 7,604 incomplete Lucas entries (7,224 distinct L_n; the Aurifeuillian parts L_nA and L_nB are listed separately). The history page shows steady progress through 2026: L1673 C203 split by NFS (K. Askine et al., 2026-10-21), B. Kelly's ECM factors of L2507, L2581 and L2728, many P-1/ECM factors by H. Bock of C700-C1350 cofactors (2026-02 to 2026-10), and results from NFS@Home, G. Childers, S. Batalov and yoyo@home. The status page for 1000 < n < 2000 says B. Kelly ran 20158 ECM curves at B1=110M and 8000 at B1=260M on every composite, and A. Kruppa ran P-1 (B1=1G, B2=1T) and P+1 on them. Blair Kelly and Hartmut Bock are the most frequent contributors on the references page.

## What counts as a win

CONFIRMED (full win) for an index n < 10000 and a prime p, proven prime, that divides a composite cofactor of F_n or L_n listed in the matching composite*.gz file linked from https://mersennus.net/fibonacci/composite.html, re-fetched immediately before the claim, with p absent from the big tables (fibonacci.txt / lucas.txt) and from history.html at verification time (direction: max on the count of known factors).

## Partial wins

- **p1:** Hole filled: a complete proven-prime factorisation of every remaining cofactor of some F_n or L_n listed in fibholes.txt or lucholes.txt, so that the number would leave the holes list.
- **p2:** A proper prime factor of the first-hole composites (F1423 C276 or L1423 C232) as listed at verification time.

## How a win is checked

Compute F_n or L_n exactly (Python big integers or PARI fibonacci()), divide out the factors in the big table, confirm the remaining cofactor matches the composite file entry, check divisibility by p, and prove p prime (PARI isprime or ECPP). For p1, prove every remaining part prime.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mersennus.net/fibonacci/history.html>

## Sources

- <https://mersennus.net/fibonacci/>
- <https://mersennus.net/fibonacci/composite.html>
- <https://mersennus.net/fibonacci/history.html>
- <https://mersennus.net/fibonacci/fibholes.txt>
- <https://mersennus.net/fibonacci/lucholes.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- ECM with small B1 (1e6-11e6) across the thousands of C700-C2000 cofactors for n > 4000; these got far less ECM than the n <= 2000 range, and H. Bock's 2026 harvest shows factors of 30-45 digits are still there.
- Use the known shape of primitive factors: a primitive prime p (p != 5) of F_n or L_n satisfies p = +-1 mod n for odd n, so put n into the P-1 stage-1 exponent to catch p = 1 mod n and run P+1 for p = -1 mod n.
- Use the status pages to pick composites with the least ECM effort recorded.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Factors already listed in the big tables or history do not count; known algebraic factors of F_n and L_n (from divisors of n) are not new factors.
- The site's server rejects some non-browser clients; fetch honestly and record BLOCKED if it refuses.
- A probable-prime factor must be proven before the claim counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/fibonacci-lucas-composite-factors.md
```

Already set up? Say `run V3R1T4S on fibonacci-lucas-composite-factors`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fibonacci-lucas-composite-factors`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
