# Generalized Wagstaff / negative-base repunits (b^p+1)/(b+1): a first (probable) prime for one of the 41 bases b <= 1024 with none known (smallest: b = 97)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days per base (candidates of roughly 40 000 to 300 000 digits; b = 97 needs exponents above 800 000, so that base alone is cluster scale) · open as of 2026-10-30

## The problem

(b^p+1)/(b+1) is the base -b repunit. The conjecture predicts infinitely many primes for every b that is not a perfect odd power (b = m^r with r odd > 1) and not of the form 4k^4; those excluded bases have algebraic factorisations. OEIS A084742 records that a(97) > 800000 (Wang Runsen, May 2023), and Richard Fischer's GenRepuP.txt (05.10.2026) also gives ( > 800000) for b = 97. The Google Docs base table linked from Wikipedia's Repunit article lists 54 bases <= 1024 with no known PRP. Its limits are 59863 for 97, 59509 for 103, 59021 for 113, 50000 for 161-400, 30000 for 401-512 and 17327 for 513-1024. That list is stale: Norman Luhn's live generalized Wagstaff table (TableWagstaffGen, 1385 entries of at least 1000 digits, updated 26 Oct 2026) has PRPs found by Jinyuan Wang in 2024 for 13 of them (445, 498, 557, 592, 598, 624, 717, 730, 873, 923, 944, 996, 1004). On 2026-10-30 these 41 bases have no known PRP: 97, 103, 113, 186, 187, 220, 304, 306, 309, 335, 414, 416, 428, 433, 459, 486, 539, 550, 587, 597, 617, 637, 659, 665, 671, 677, 696, 726, 740, 754, 766, 790, 851, 890, 914, 929, 943, 965, 984, 985, 1005.

## What counts as a win

CONFIRMED (full win) for a base b from the 41 listed in the statement and a prime p such that N = (b^p+1)/(b+1) passes a strong Fermat test to base 3 and a BPSW test, rerun independently. At claim time b must still have no entry on Luhn's live TableWagstaffGen (https://pzktupel.de/Primetables/TableWagstaffGen.php, re-fetched), in Fischer's GenRepuP.txt or in OEIS A084742. p must exceed every published limit for b: 800000 for b=97, otherwise the Google Doc limit. A PRP suffices, as in all the source tables. Each base that leaves the list counts (direction: min on the count of bases <= 1024 with no known PRP, 41 on 2026-10-30).

## Partial wins

- **p1:** Search-range certificate for one listed base other than 97: every prime p from the published limit up to at least 1.5 times the limit sieved and PRP-tested with no hit. The sieve file and PRP residues are saved so a verifier can retest a random 2% of survivors and recheck the removing factors of a random 2% of removed candidates.

## How a win is checked

Recompute N, confirm that p is prime and b is listed. Run PFGW Fermat base 3 and PARI/GP ispseudoprime on the verifier's own install. Confirm b is absent from Luhn's live table, Fischer's file and OEIS A084742, and that p exceeds the stated limit. Any prime factor q of N satisfies q = 1 (mod 2p).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/Primetables/TableWagstaffGen.php>

## Sources

- <https://pzktupel.de/Primetables/TableWagstaffGen.php>
- <http://www.fermatquotient.com/PrimSerien/GenRepuP.txt>
- <https://docs.google.com/document/d/e/2PACX-1vRha5-vd9Covl4k6I02lOEdWdhsXnBCeFT3FHyhMYTO1i7jtZdTV3wQw2yXgTNja5k_-XINgqL9VNmo/pub>
- <https://oeis.org/A084742>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Skip b = 97 (above 800 000, about 1.6 million digits per candidate). The bases 161-512 at limits of 30 000-50 000 are the cheapest per expected prime.
- Sieve many bases at once using q = 1 mod 2p, then PRP-test in increasing p so each base stops at its first hit.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Doc lists 97, 103 and 113 with limits near 60 000, but Fischer and OEIS give 800 000 for 97. Use the maximum over all sources.
- 13 bases on the Doc's list already have PRPs (Jinyuan Wang 2024). Check Luhn's table first.
- Bases of the form 4k^4 (324, 1024) and odd perfect powers have algebraic factorisations and are excluded.
- Do not confuse (b^p+1)/(b+1) with the positive-base repunit target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/generalized-wagstaff-first-prime-bases-to-1024.md
```

Already set up? Say `run V3R1T4S on generalized-wagstaff-first-prime-bases-to-1024`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `generalized-wagstaff-first-prime-bases-to-1024`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
