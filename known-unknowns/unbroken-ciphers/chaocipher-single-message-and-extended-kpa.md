# Chaocipher: break a single ciphertext-only message, and known-plaintext attack on the Extended variant (open per the Chaocipher Clearing House)

🔐 **Unbroken ciphers** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Chaocipher, invented by John F. Byrne in 1918, uses two dynamically permuted 26-letter alphabets. Its algorithm was revealed in 2010 after his family gave the papers to the National Cryptologic Museum. Moshe Rubin's Chaocipher Clearing House keeps the 'Current State of Chaocipher Research' table, created in Progress Report #25 and last updated 13 January 2023. Solved per the table: key recovery from ciphertext plus plaintext for the Classic system (Scheffler 2010, Rubin 2011, Crypto Forum 2015); in-depth messages with plaintext (Lasry/Rubin 2016, at least 10 messages Classic, 20 Extended); in-depth ciphertext-only messages (Classic needs 60-80 messages, Extended 600-800; a 2015 Crypto Forum hill-climbing attempt failed). George Lasry, Moshe Rubin, Nils Kopal and Arno Wacker (Cryptologia 40(6), 2016) solved Exhibit 6, a real-life challenge by Lou Kruh and Cipher Deavours; whether it can be done with fewer messages is still asked. Still OPEN: (a) recovering the key from a SINGLE ciphertext-only message, for both the Classic and Extended systems; (b) recovering the key from ciphertext plus plaintext for the Extended system ('not yet tackled'). Progress Report #29 (19 April 2026) repeats that 'no method is currently known for solving a single, long Chaocipher ciphertext message'. The task is a reproducible, publishable attack, measured on a frozen benchmark.

## What counts as a win

Freeze a benchmark BEFORE attacking: 100 English plaintexts of a stated length L, drawn from a public corpus not used in development. Encipher each under a fresh, uniformly random Chaocipher key (independent random permutations for both alphabets, plus a uniformly random left/right selection key for Extended). Use an independent reference implementation that has first been checked against Byrne's Exhibit 1 and the solved Exhibit 6 data. (A) Classic single-message ciphertext-only: CONFIRMED if the attack recovers at least 98% of the plaintext letters for at least 50 of 100 messages with L <= 1000, within 2 laptop-hours per message. (B) Extended known-plaintext: CONFIRMED if the attack recovers the starting alphabets and the left/right selection key for at least 90 of 100 pairs with L <= 500. For both, re-fetch the Clearing House table live before claiming and confirm the cell still says 'Open'. Publish the code, the benchmark seeds and the per-message logs.

## Partial wins

- **p1:** Classic single-message attack that succeeds on at least 50 of 100 frozen benchmark messages at some length L <= 3000, each message under an independent uniformly random key.
- **p2:** Extended known-plaintext attack that succeeds on at least 50 of 100 frozen benchmark pairs at L <= 1000.
- **p3:** Fewer messages for Exhibit-6-style depth: recover the key from at most 30 in-depth Classic ciphertext-only messages (the Clearing House table lists 60-80 as required) on a frozen benchmark, with at least 80% success.

## How a win is checked

Use a reference Chaocipher implementation checked against the Clearing House exhibits. Regenerate the benchmark from the published seeds, confirm the keys are uniformly random, run the attack code unchanged, count recoveries with a letter-accuracy script and check wall time per message.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://chaocipher.com/chaocipher-current-state-of-research.htm>

## Sources

- <https://chaocipher.com/chaocipher-current-state-of-research.htm>
- <https://www.mountainvistasoft.com/chaocipher/chaocipher-current-state-of-research.htm>
- <https://chaocipher.com/chaocipher-029.htm>
- <https://chaocipher.com/>
- <https://doi.org/10.1080/01611194.2015.1091797>

## Ideas to start from

Left out on purpose, so this page never spoils the hunt.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/unbroken-ciphers/chaocipher-single-message-and-extended-kpa.md
```

Already set up? Say `run V3R1T4S on chaocipher-single-message-and-extended-kpa`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chaocipher-single-message-and-extended-kpa`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
