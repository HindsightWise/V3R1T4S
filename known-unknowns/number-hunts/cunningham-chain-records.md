# Cunningham chains: beat a largest-known record for some length, or find a chain of length 21

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A Cunningham chain of the first kind of length L is p, 2p+1, 4p+3, ... (L primes); of the second kind p, 2p-1, 4p-3, .... The records page at pzktupel.de (continuing the list originally created and maintained by Dirk Augustin; last updated 2026-10-22) lists the largest known chain of each length and kind and the smallest chains. Active 2026 record setters include Serge Batalov (many lengths 3-17), Ryan Propper with Serge Batalov (length 3, first kind, 2026-10-19), John Armitage (lengths 19 and 20) and Nenad Mićić (length 18, first kind). Length 11-14 records (98-149 digits) date from 2013-2018 (Primecoin, Andrey Balyakin), lengths 15-20 records are 25-45 digits, and the longest known chains have length 20 (John Armitage, 2026-03-29 for the second kind and 2026-04-18 for the first kind). No length-21 chain is listed.

## What counts as a win

CONFIRMED (full win) for a chain of length L >= 3 and kind K whose L members are all PROVEN prime and whose initial prime is STRICTLY GREATER (direction: max, compared as integers) than BOTH (a) the initial prime of the largest known chain of length L and kind K on https://pzktupel.de/CC/cc.php, re-fetched immediately before the claim, AND (b) the initial prime of every length-L run of consecutive members of any longer chain of kind K listed anywhere on that page (both tables). Part (b) is needed because the page does not always list sub-chains: on 2026-10-28 the listed length-20 first-kind chain 75949683268775452969189500*2^k-1 contains length-19 sub-chains larger than the listed length-19 first-kind record. A longer new chain counts toward a shorter length L under the same comparison.

## Partial wins

- **p1:** Longest chain ever: a proven Cunningham chain of length 21 or more of either kind (no length-21 chain is listed at verification time). Headline result.
- **p2:** New length-19 or length-20 chain of either kind, any size, whose initial prime is not listed on the page at verification time AND which is not a run of consecutive members of any chain listed on the page (dropping the first member of a listed length-20 chain gives a length-19 chain that is not new).

## How a win is checked

Recompute each member from the initial prime. Prove the first prime (PARI isprime with certificate, or N-1/N+1 proof using the primorial*2^k structure); then each next member q = 2p+1 (resp. 2p-1) has q-1 = 2p (resp. q+1 = 2p) with p already proven, so a Pocklington (resp. Morrison) step proves it. Check the chain cannot be extended backwards in a way that changes its listed length, and compare the initial prime with the live record.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/CC/cc.php>

## Sources

- <https://pzktupel.de/CC/cc.php>
- <https://www.pzktupel.de/JensKruseAndersen/CC.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Primorial-form search: p = k * P# * 2^j - 1 (first kind) with a sieve over k that removes every k for which some member is divisible by a prime up to 10^9 before any primality test.
- Multi-modulus wheel sieving: precompute the admissible residues of k modulo primorials so that every surviving k has no small factor in any of the L members; this is how the length 19-20 chains were found.
- GPU-style bit-sliced sieving (imported from high-performance computing / bitcoin-era Primecoin miners, which set the length 11-14 records): even on a laptop, a vectorised sieve on the CPU cores can test billions of k per hour.
- Extreme-value statistics (imported from risk modelling): fit the distribution of chain lengths found per sieve batch to estimate how many candidates a length-21 hit needs, and choose the primorial size that maximises expected record digits per hour.
- Bi-twin and mixed constellations: a bi-twin chain search also produces long chains of both kinds as a by-product.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Probable-prime members are not proof; but here proofs are cheap through the chain structure, so insist on them.
- A chain that extends further than claimed (or starts earlier) may already be listed under a different length or initial prime.
- Shifting a known chain (starting at its 2nd, 3rd, ... member) gives a shorter chain with a new initial prime that is not a discovery; check every listed chain for containment.
- Mixing up first kind (2p+1) and second kind (2p-1).
- Comparing digit counts instead of exact integers when two chains have the same number of digits.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/cunningham-chain-records.md
```

Already set up? Say `run V3R1T4S on cunningham-chain-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cunningham-chain-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
