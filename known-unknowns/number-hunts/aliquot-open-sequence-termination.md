# Open aliquot sequences below 5,000,000: terminate one (reach a prime) or close it into a cycle

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (YAFU/CADO-NFS on C100-C140 cofactors along a downdriver run) · open as of 2026-10-30

## The problem

An aliquot sequence iterates s(n) = sigma(n) - n. The Catalan-Dickson conjecture says every sequence terminates (reaches a prime and then 1) or becomes periodic; Guy and Selfridge conjectured that many grow without bound. The MersenneForum aliquot table (rechenkraft.net/aliquot/AllSeq.html, made by Dubslow with ChristianB, hosted by Rechenkraft.net and fed from FactorDB) lists every open sequence with starting value below 5,000,000: 46,322 sequences on 2026-10-30 (reservations current as of 02:10 UTC), from 276 to 4,999,980, with 2,947 reserved. For each it gives the current index, the size, the known factors and the size of the composite blocking the next step, the driver or guide (Clifford Stern's classes), the reservation and the last progress. All 64 sequences in the 'Downdriver!' state (where terms tend to shrink) are reserved (59 by yafu@home, 5 by Batalov). The smallest blocking composites (C61-C64) sit on unreserved sequences, most of them carrying the 2^2*7 driver (two of the C64s carry the 2^4*31 guide). Earlier work includes Wolfgang Creyaufmueller's tables (aliquot.de) and the extensions by Paul Zimmermann, Christophe Clavier and many mersenneforum contributors.

## What counts as a win

CONFIRMED (full win) for a sequence listed as open in https://www.rechenkraft.net/aliquot/AllSeq.txt (re-fetched immediately before the claim), other than the Lehmer five (276, 552, 564, 660, 966). The claim is a chain of terms starting from the sequence's term at the index the live table lists. The table shows only that term's known factors and the size of its blocking composite; the full term is the FactorDB entry whose id AllSeq.json gives. Each term in the chain has a complete proven-prime factorisation, and each next term equals sigma minus the term. The chain must end at a prime (the sequence terminates) or at a term already in a known aliquot cycle, including perfect numbers and amicable pairs (direction: max on the count of resolved sequences).

## Partial wins

- **p1:** An unreserved sequence advanced by at least 20 indices beyond the live table's index, with every term fully factored into proven primes.
- **p2:** A merge: a chain from a listed sequence's last term reaching a term that a different listed open sequence also reaches, shown by complete factorised chains for both.

## How a win is checked

Recompute sigma from each factorisation with Python big integers, check each step s(t_i) = t_{i+1}, prove every prime factor (BPSW below 2^64, PARI isprime / ECPP above), confirm the start matches the table's last term at its index, and confirm the final prime (or the cycle member against Moews' list).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.rechenkraft.net/aliquot/AllSeq.txt>

## Sources

- <https://www.rechenkraft.net/aliquot/AllSeq.html>
- <https://www.rechenkraft.net/aliquot/AllSeq.txt>
- <https://www.rechenkraft.net/aliquot/AllSeq.json>
- <https://github.com/MersenneForum/MersenneForumAliquot>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Advance the unreserved sequences with the smallest blocking composites (C61-C100 in the 2026-10-30 snapshot) with YAFU or aliqueit; each step takes minutes to hours on a laptop, and a driver change can start a downward run toward termination.
- Rank by Stern's class and the absence of a 3 in the factorisation; the table has checkboxes for exactly this.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- rechenkraft.net (the status source) and FactorDB have intermittently refused automated clients (on 2026-10-30 some fetches were refused and others succeeded); fetch honestly and record BLOCKED instead of working around it.
- The table lists the known factors and the size of the blocking composite (for example C61), not the term itself; take the full term from FactorDB by the id in AllSeq.json and check its index and factors against the table.
- Reserved sequences (including every 'Downdriver!' one on 2026-10-30) are being run by someone else; coordinate through a human on the reservation thread.
- A term lower in the table than the live index (stale cache) leads to duplicated work; always start from the live last term.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/aliquot-open-sequence-termination.md
```

Already set up? Say `run V3R1T4S on aliquot-open-sequence-termination`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `aliquot-open-sequence-termination`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
