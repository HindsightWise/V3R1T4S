# Shortest addition chains: compute c(48), the smallest n with l(n) = 48, or d(46) (Clift's c(r)/d(r) tables)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (extending the complete l(n) table from 2^39 towards 2^40, terabyte-scale storage); spot verification is laptop-hours · open as of 2026-10-30

## The problem

Let l(n) be the length of a shortest addition chain for n, c(r) the smallest n with l(n) = r (OEIS A003064), and d(r) the number of n with l(n) = r. Knuth, Flammenkamp, Bleichenbacher and Neill Clift built these tables. Clift computed l(n) for every n <= 2^39 (September 2022). He found c(47) = 498691112447 in January 2021, and his c(r)/d(r) page gives d(r) up to d(45) = 243724383149 (September 2022). The OEIS b-file for A003064, taken from Flammenkamp's page in 2021, stops at a(46) = 257661019487. c(47) is known but missing there, so it is not a new term. Flammenkamp's page holds the history and the downloadable l(n) data: add39.4ln.bz2, 51662 MB, covers n <= 2^39. Because the table is complete to 2^39 and lists no n with l(n) = 48, c(48) > 2^39. The ratio c(47)/c(46) is about 1.94, so c(48) is very likely below 2^40. Clift notes that finding chains for c(r) is easy; proving that no shorter chain exists is what takes the time.

## What counts as a win

CONFIRMED (full win) for c(48): an integer N with (a) a certificate that l(N) >= 48, given by an exhaustive shortest-chain search that the verifier reruns with its own independently written program, and an explicit chain of length 48; and (b) for every m < N, an explicit chain of length <= 47. Part (b) may be a published extension of Clift's complete l(n) table from 2^39 up to N, with chains for spot checks. Two independently written programs must agree on N. N must not appear on http://additionchains.com/crdr.html, on Flammenkamp's page or in OEIS A003064 (each re-fetched before the claim). Direction: extend the table (first unknown index).

## Partial wins

- **p1:** d(46): the exact number of n with l(n) = 46, computed by two independently written methods that agree (for example small-step enumeration and a table count), and absent from the live crdr.html and Flammenkamp pages.
- **p2:** A rigorous lower bound c(48) > X with X > 2^39: a published extension of the complete l(n) table beyond 2^39 to X, with no n <= X having l(n) = 48. A second independent program must reproduce randomly chosen blocks exactly.

## How a win is checked

For N: run an independent optimal-chain prover (for example Clift's published ac2fastfg techniques reimplemented) to confirm that no chain of length 47 exists. Check the 48-step chain. Download the claimant's table extension and check chains for random m < N, and for every m in the top 10^7 below N, against the claimed l(m) <= 47. Compare d-counts by recounting the table and the enumeration. Re-fetch crdr.html and A003064.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://additionchains.com/crdr.html>

## Sources

- <http://additionchains.com/crdr.html>
- <https://wwwhomes.uni-bielefeld.de/achim/addition_chain.html>
- <https://oeis.org/A003064>
- <http://www.additionchains.com/Calculating.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Clift's crouton/dual pruning plus the generalized Thurber bounds (Calculating.html) for single-n lower-bound proofs.
- Small-step enumerations (Clift's SmallStepEnumeration pages publish the convex-set enumerations for s <= 5; Flammenkamp's page records Clift's s = 6 work to November 2023) settle most n quickly. Only n not matched by an enumeration need the full search.
- c(r) values follow Flammenkamp's observation that the record holders for the number of small steps are among the c(r).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- c(47) = 498691112447 is already known (Clift, January 2021) even though OEIS's b-file stops at a(46).
- A chain of length 48 for N proves nothing about minimality. Both l(N) >= 48 and l(m) <= 47 for all m < N are needed.
- Flammenkamp's 1997 data had four errors above 2.5*10^6 that Clift found in 2004. Independent recomputation matters.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/addition-chain-c48-d46.md
```

Already set up? Say `run V3R1T4S on addition-chain-c48-d46`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `addition-chain-c48-d46`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
