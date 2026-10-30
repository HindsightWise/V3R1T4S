# Odd perfect number proof tree: factor a 'most wanted roadblock' composite on Ochem's lists

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (ECM over the list; NFS for the smaller C193-C230 entries needs cluster) · open as of 2026-10-30

## The problem

Pascal Ochem and Michael Rao proved bounds on any odd perfect number N with a factor-chain proof tree like the one of Brent, Cohen and te Riele: N > 10^1500 (since pushed to N > 10^2200), Omega(N) >= 101 (since pushed to >= 115) and Omega(N) >= 2 omega(N) + 51. The tree stalls at 'roadblocks', composite factors c of sigma(p^e) that nobody has factored; each roadblock forces an expensive detour. Ochem's page publishes mwrb2200.txt, 'the most difficult composites for the proof of N > 10^2200' (format 'p q-1 composite weight', so c divides sigma(p^(q-1)); 1,629 composites from 193 to 1,099 digits; Last-Modified 2026-09-01; weights up to 63,862,958, 16 of them at least 1,000,000). The top line, '11 330' C344 (weight 63,862,958), is the Cunningham number 11,331- = (11^331-1)/10, which 'Lu' split as p136 * p209 by SNFS in 2026 (Cunningham update page149.txt, #6886); it was still listed on 2026-10-30, so the largest open weight is 25,238,981 (127 192 C404) and 15 open composites have weight at least 1,000,000. It also publishes complete composite files t570 ... t2300 (2/2025) and the known-factor file checkfacts.txt (12/2022). The page says every composite that gets factored, even partially, is removed from the list within a few days. The page source (partly commented out) acknowledges earlier factorizations by Tom Womack and Ryan Propper and NFS reservations by Warut Roonguthai and Frank Schickel; the page points helpers to the mersenneforum OPN threads. This continues the old oddperfect.org roadblock lists, now offline (archived).

## What counts as a win

CONFIRMED (full win) for a line 'p q-1 c w' of https://www.lirmm.fr/~ochem/opn/mwrb2200.txt (re-fetched immediately before the claim) and a prime f, proven prime, with 1 < f < c and c mod f = 0, where c divides sigma(p^(q-1)) = (p^q - 1)/(p - 1), provided f is not in checkfacts.txt and, when p <= 12, c has not already been split in the Cunningham main tables or on any Cunningham update page (page149.txt or later, linked from https://homes.cerias.purdue.edu/~ssw/cun/index.html) at verification time; the line '11 330' C344 (Cunningham 11,331-, split on page149.txt #6886) does not count (direction: max on the count of roadblock composites split).

## Partial wins

- **p1:** A proven prime factor of any composite in one of the tXXXX.txt files (t570 ... t2300) linked from https://www.lirmm.fr/~ochem/opn/ that is not in checkfacts.txt at verification time and, when p <= 12, is not already in the Cunningham main tables or on a Cunningham update page (page149.txt or later).
- **p2:** A proven prime factor of one of the composites in mwrb2200.txt whose weight (fourth column) is at least 1,000,000 (16 listed, C305-C572, on 2026-10-30; 15 open, since '11 330' C344 was already split as Cunningham 11,331- on page149.txt), dividing the listed composite, which must still be listed and must not be already split in the Cunningham tables or update pages at verification time.

## How a win is checked

Recompute sigma(p^(q-1)) = (p^q-1)/(p-1) exactly, confirm c divides it and equals the listed composite, check c mod f = 0, prove f prime (PARI isprime / ECPP). For p1 also grep f in checkfacts.txt.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.lirmm.fr/~ochem/opn/mwrb2200.txt>

## Sources

- <https://www.lirmm.fr/~ochem/opn/>
- <https://www.lirmm.fr/~ochem/opn/mwrb2200.txt>
- <https://www.lirmm.fr/~ochem/opn/opn.pdf>
- <https://www.lirmm.fr/~ochem/opn/opnf.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sort by weight per digit: high-weight composites under 230 digits give the most proof-tree pruning per unit of NFS effort.
- Note that the second column is q-1, the exponent in sigma(p^(q-1)), so q is the exponent of p^q - 1: run SNFS on (p^q-1)/(p-1) with the cyclotomic polynomial for q when p is small.
- Cross-check with Cunningham tables: when p is 2..12 the number is a Cunningham cofactor and may already be factored there.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The file's second column is q-1, not q; a wrong exponent gives a different number.
- checkfacts.txt (12/2022) is older than the t-files; also check the mersenneforum OPN threads before claiming novelty for p1 (the forum shows a Cloudflare bot check to scripts; record BLOCKED and leave the forum check to a human).
- A factor of sigma(p^(q-1)) outside c (already known and divided out) does not count.
- mwrb2200.txt can lag: on 2026-10-30 its top line '11 330' C344 was still listed although it is Cunningham 11,331-, split on page149.txt. For p = 3, 5, 7, 11 always rebuild the Cunningham number and check its main table and update pages first.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/opn-roadblock-composites.md
```

Already set up? Say `run V3R1T4S on opn-roadblock-composites`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `opn-roadblock-composites`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
