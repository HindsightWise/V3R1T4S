# Near-repdigit-related sequences with no known prime (Kamada): 298...89, 25...567, 45...529, 54...427, 454...41

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (candidates of 50 000 to 200 000 digits; PFGW PRP tests of minutes each) · open as of 2026-10-30

## The problem

Makoto Kamada (STUDIO KAMADA) tracks primes in more than 4600 near-repdigit-related decimal sequences. The 'Number of prime numbers in each near-repdigit-related sequence' table was last updated on 2 Aug 2026. Most sequences without a prime are either provably prime-free (covering sets or algebraic factors, marked 'not exist') or are of the form k*10^n+-1, which is Riesel/Sierpinski base-10 territory. Exactly five other sequences are marked '(not found)', with no known (probable) prime. 298w9 = (269*10^(w+1)+1)/9 (2989, 29889, ...) has been searched to n <= 100000. Four have been searched to n <= 50000: 25w67 = (23*10^(w+2)+103)/9, 45w29 = (41*10^(w+2)-239)/9, 54w27 = (49*10^(w+2)-157)/9 and 454w1 = (409*10^(w+1)-31)/9. Here n is Kamada's index (n = w+1 or w+2), so the term has about n digits. None of the five is in Kamada's list of reserved ranges (which on 2026-10-30 holds 31w, 919w and 949w only).

## What counts as a win

CONFIRMED (full win) for one of the five sequences and an integer w such that the term (formula as listed) has index n strictly above the searched range on the live table (https://stdkmd.net/nrr/prime/prime_sequences.htm, re-fetched; the sequence must still show count 0 and '(not found)'), and the term passes a strong Fermat test to base 3 and a BPSW test, rerun independently. A PRP suffices: Kamada's lists record PRPs and proofs separately. Each sequence that gets its first (probable) prime counts (direction: min on the number of such sequences, 5 on 2026-10-30).

## Partial wins

- **p1:** Range certificate: one of the five sequences sieved and PRP-tested with no hit from its listed limit to at least twice that limit (n <= 100000 for the four 50000 sequences, n <= 200000 for 298w9). The sieve file and PRP residues are saved for a verifier's 2% random retest.

## How a win is checked

Recompute the term from the formula for the claimed w and check the n index. Run PFGW Fermat base 3 plus PARI/GP ispseudoprime on the verifier's own install. For p1, retest a random 2% of the sieve survivors and recheck the removing factors of a random 2% of the removed candidates.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://stdkmd.net/nrr/prime/prime_sequences.htm>

## Sources

- <https://stdkmd.net/nrr/prime/prime_sequences.htm>
- <https://stdkmd.net/nrr/prime/prime_sequences.txt>
- <https://stdkmd.net/nrr/prime/>
- <https://stdkmd.net/nrr/coveringset.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Each sequence is (a*10^m + c)/9, so 9*term = a*10^m + c is a k*b^n+c form. Sieve 9*term with srsieve2/mtsieve (k*10^m+c), then PRP-test the survivors divided by 9.
- Before searching, compute small-prime periods to see why these five are so sparse (near-covering sets), and rank the five by expected primes per CPU-hour from their sieve survival rates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Index n is not w: check the n = w+1 or n = w+2 convention for each sequence.
- Kamada's 'pr' status flags are not complete proof records. They do not matter here: a PRP is the win.
- The many k*10^n+-1 sequences with no prime on the same page (for example 4421*10^n-1) mostly duplicate the Conjectures 'R Us base-10 Riesel/Sierpinski work and are not part of this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/kamada-near-repdigit-sequences-without-prime.md
```

Already set up? Say `run V3R1T4S on kamada-near-repdigit-sequences-without-prime`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kamada-near-repdigit-sequences-without-prime`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
