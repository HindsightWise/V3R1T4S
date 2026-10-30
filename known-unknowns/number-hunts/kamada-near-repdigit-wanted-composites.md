# Near-repdigit factor tables (Kamada): factor a composite on the 'hoped to be factored' lists

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-days (GNFS on a C145-C160 with CADO-NFS on 8+ cores; SNFS difficulty ~210 for the SNFS list) · open as of 2026-10-30

## The problem

Makoto Kamada's STUDIO KAMADA site (stdkmd.net/nrr) keeps factor tables of near-repdigit-related numbers: repunits, near-repdigits such as AA...AB, plateau-and-depression and quasi-repdigit numbers, and near-repdigit palindromes. Its page 'Composite numbers that are hoped to be factored' (wanted.htm, Last-Modified 2026-10-27) has three lists. (1) 100 composites from the top 100 smallest SNFS polynomials, C153-C204, SNFS difficulty 211.00-213.15 (94 'Free to factor' and 6 'Reserved' on 2026-10-30). (2) 1,000 composites suited to GNFS, C145-C192 (992 free); the first is the C145 cofactor of (791*10^264-8)/9 = 8788...88, ECM to t45. (3) 94 composites with no known prime factor, C268-C476, ECM to t55-t65, for example (53*10^267-71)/9 = 5888...881. Each row shows digits, the expression, the ECM level done and whether it is 'Free to factor', 'Reserved' or 'Submitted'. The site credits hundreds of contributors, among them NFS@Home, Greg Childers, Ryan Propper, Serge Batalov and yoyo@home; its July 2026 news credits Propper and Batalov with the near-repdigit prime 6*10^4000494-1.

## What counts as a win

CONFIRMED (full win) for a composite N listed on https://stdkmd.net/nrr/wanted.htm (re-fetched immediately before the claim, with a row status other than 'Submitted') and a prime p, proven prime, with 1 < p < N and N mod p = 0, provided p does not appear for that number in Kamada's factor tables or the 'Contributed factorization results' pages at verification time (direction: max on the count of known factors).

## Partial wins

- **p1:** Complete factorisation of a composite from the 'suitable for GNFS' list into proven primes, with every factor checked by multiplication against the listed composite.
- **p2:** First prime factor of a composite from the 'no prime factor is known' list (C268 and up), proven prime and dividing the listed number.

## How a win is checked

Recompute N from its listed expression and confirm it equals the listed composite, confirm N mod p = 0, prove p (and any cofactor claimed prime) with PARI isprime / ECPP (Primo) for large values, and grep p against Kamada's table page for that expression and the contributed-results pages.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://stdkmd.net/nrr/wanted.htm>

## Sources

- <https://stdkmd.net/nrr/wanted.htm>
- <https://stdkmd.net/nrr/>
- <https://stdkmd.net/nrr/howto.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run GNFS with CADO-NFS on the smallest 'Free to factor' C145-C150 entries; they need about a day or two on a modern 16-thread desktop.
- For SNFS-list entries, build the SNFS polynomial straight from the expression (k*10^n+m) and sieve with CADO-NFS or msieve/ggnfs.
- Extra ECM at t50-t55 on the 'no prime factor known' list before committing to NFS.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rows marked 'Reserved' are being worked on by someone else, and 'Submitted' rows are already done; pick 'Free to factor' rows and re-check the status column before and after the run.
- The listed composite is a cofactor after small factors are removed; recompute it from the expression (note the /9 or /3 denominators shown as fractions on the page) and the table rather than trusting copied digits.
- The tables cover several families with similar names (AA..AB vs ABB..B); match the expression exactly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/kamada-near-repdigit-wanted-composites.md
```

Already set up? Say `run V3R1T4S on kamada-near-repdigit-wanted-composites`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kamada-near-repdigit-wanted-composites`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
