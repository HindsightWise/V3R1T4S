# Generalized repunits (b^p-1)/(b-1): a first (probable) prime for one of the 26 bases b <= 1024 with none known (smallest: b = 185)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days per base for most bases (just above the published limits candidates have roughly 55 000 to 155 000 digits; one gwnum-based PRP test takes minutes to an hour); b = 185 above p = 350 000 means candidates of about 800 000 digits, which is cluster scale · open as of 2026-10-30

## The problem

For a base b that is not a perfect power, the generalized repunit conjecture predicts infinitely many primes (b^p-1)/(b-1) with p prime. Several bases still have no known prime or PRP at all. Richard Fischer's table (GenRepu.txt, 30.09.2026) shows every base <= 200 except 185 has one, and that (185^p-1)/184 is composite for all p < 350000. The public Google Docs table 'Smallest odd prime p such that (b^p-1)/(b-1) and (b^p+1)/(b+1) is prime for bases 2<=b<=1024' (linked from Wikipedia's Repunit article; the OEIS A084740 links credit Eric Chen with these base tables) lists 41 positive bases with no known PRP. Its search limits are 66337 for b=185, 63659 for 269, 63421 for 281, 50000 for 301-400, 30000 for 401-512 and 19001 for 513-1024. That list is stale. Norman Luhn's live table of generalized repunit PRPs with at least 1000 digits (TableRepunitGen, updated 29 Oct 2026) now has PRPs for 15 of those bases, found by Michael Stocker (2020), Jinyuan Wang (2023-24), Serge Batalov and Tom Wu. Examples: b=485 at p=99523 and b=1005 at p=89087. On 2026-10-30 these 26 bases have no known PRP: 185, 269, 281, 380, 384, 385, 396, 452, 465, 511, 574, 598, 601, 631, 632, 636, 711, 759, 771, 795, 866, 881, 938, 951, 956, 1015.

## What counts as a win

CONFIRMED (full win) for a base b from the 26 listed in the statement and a prime p such that N = (b^p-1)/(b-1) is a probable prime. N must pass a strong Fermat test to base 3 and a BPSW test (strong base 2 plus strong Lucas), rerun independently. At claim time b must still have no entry on Luhn's live TableRepunitGen (https://pzktupel.de/Primetables/TableRepunitGen.php, re-fetched), in Fischer's GenRepu.txt or in the OEIS A084740 data or b-file. p must be larger than every published search limit for b: 350000 for b=185 (Fischer), otherwise the Google Doc limit. A primality proof is not required: every source table accepts PRPs. Each base that leaves the no-PRP list counts (direction: min on the number of bases <= 1024 with no known PRP, 26 on 2026-10-30).

## Partial wins

- **p1:** Search-range certificate for one listed base: every prime p from that base's published limit up to at least 1.5 times the limit sieved and PRP-tested with no hit. The sieve file, the factors that remove each candidate and the PRP residues are saved, so a verifier can recheck the factors of a random 2% of removed candidates and retest a random 2% of the survivors.

## How a win is checked

Recompute N exactly and confirm that p is prime and b is on the list. Run PFGW (Fermat base 3) and PARI/GP ispseudoprime (BPSW) on the verifier's own install. Check that b is absent from the live Luhn, Fischer and OEIS sources and that p exceeds the published limit. Spot-check sieve factors: any prime factor q of N satisfies q = 1 (mod 2p).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/Primetables/TableRepunitGen.php>

## Sources

- <https://pzktupel.de/Primetables/TableRepunitGen.php>
- <http://www.fermatquotient.com/PrimSerien/GenRepu.txt>
- <https://docs.google.com/document/d/e/2PACX-1vRha5-vd9Covl4k6I02lOEdWdhsXnBCeFT3FHyhMYTO1i7jtZdTV3wQw2yXgTNja5k_-XINgqL9VNmo/pub>
- <https://oeis.org/A084740>
- <https://en.wikipedia.org/wiki/Repunit>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sieve all 26 bases together over prime exponents. Any factor q of (b^p-1)/(b-1) is 1 mod 2p, so trial factoring by 2kp+1 is cheap and removes most candidates.
- Rank bases by expected primes per CPU-hour. The heuristic count of primes per base between exponents x and y is about e^gamma*ln(y/x)/ln(b), so small b near 300-400 with low published limits pay best.
- Use gwnum-based PRP testing with Gerbicz error checks (PRST or PFGW) so that a hardware fault never yields a false PRP at 100 000+ digits.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Google Doc's no-prime list is out of date: 15 of its positive bases have PRPs in Luhn's table. Always check Luhn's table first.
- Published search limits are lower bounds. Jinyuan Wang, Michael Stocker and others searched well past the Doc's limits without always publishing them, so a 'new' PRP may already be known unreported.
- Perfect-power bases (and composite p) give algebraic factors and can never count.
- Base 598 was on both of the Doc's lists, but the negative-base form is solved ((598^32077+1)/599, Jinyuan Wang, May 2024). Only (598^p-1)/597 is still open, and it is a different number from the base -598 repunit.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/generalized-repunit-first-prime-bases-to-1024.md
```

Already set up? Say `run V3R1T4S on generalized-repunit-first-prime-bases-to-1024`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `generalized-repunit-first-prime-bases-to-1024`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
