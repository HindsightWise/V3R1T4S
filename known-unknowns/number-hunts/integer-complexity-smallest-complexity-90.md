# Integer complexity: the smallest number of complexity 90, A005520(90), beyond the 10^12 computation of Iraids et al.

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days (expressions with at most 89 ones for every n from 10^12 to about 1.3*10^12, plus exact lower bounds for a few candidates) up to needs cluster (a full exact table to N); verification laptop-hours for spot checks · open as of 2026-10-30

## The problem

A005520(k) is the smallest n with integer complexity ||n|| = k (fewest 1s using + and *). The b-file by Janis Iraids runs to k = 89: a(87) = 424847520719, a(88) = 630371064959, a(89) = 872573642639 (a(68)-a(89) from Iraids, April 2011). It comes from the computation of ||n|| for all n <= 10^12 by Iraids, Balodis, Cernenoks, Opmanis, Opmanis and Podnieks (arXiv:1203.6462; Iraids' online calculator covers n < 10^12). Earlier terms are credited to David W. Wilson, John W. Layman and Piotr Fabian. Since ||n + 1|| <= ||n|| + 1 and no n <= 10^12 has complexity 90, a(90) is the least n with ||n|| >= 90. It is above 10^12 (successive ratios suggest about 1.2-1.3*10^12) and unknown. Ed Pegg Jr. noted that the terms are -1 mod 120. The entry says this holds from a(45) = 590399 through a(89), and that all terms from a(54) to a(89) are prime (Iraids). Faster algorithms exist: Arias de Reyna and van de Lune (2014), Cordwell et al. (2017), and Qizheng He (2023: O(N polylog N) for all n <= N, and O(n^0.6154) for a single n). The entry (last edited 2025-11-26) has no 'more' keyword and lists no a(90).

## What counts as a win

CONFIRMED (full win) for an integer N = a(90) with (a) a certificate that ||N|| = 90: an explicit 90-one expression plus an exact lower-bound proof (for example the Arias de Reyna-van de Lune algorithm or a defect-based certificate) that the verifier reruns, and (b) a proof that ||m|| <= 89 for every m < N: an explicit expression with at most 89 ones for every m, or a published table extension from 10^12 to N reproduced by a second, independently written program. N must be absent from the live https://oeis.org/A005520 data, b-file and history (re-fetched before the claim). Direction: extend the table (first unknown index 90).

## Partial wins

- **p1:** A rigorous lower bound a(90) > X with X >= 1.1*10^12: an exhaustive, independently reproduced computation showing ||n|| <= 89 for all n <= X (explicit expressions with at most 89 ones, or an exact table, for every n in (10^12, X]).
- **p2:** An upper bound a(90) <= M with M < 2*10^12: an explicit integer M with a certificate that ||M|| >= 90, given by an exact single-number lower-bound computation (for example He's 2023 algorithm) that the verifier reruns with an independently written implementation. Because ||n + 1|| <= ||n|| + 1, this proves a(90) <= M.

## How a win is checked

Evaluate the claimed expressions with exact integers and count the 1s. Rerun the lower-bound algorithm for ||N|| >= 90 with an independent implementation. For the 'all smaller m' part, recompute randomly chosen blocks of the claimed table with a second program and diff the hashes. Check that the extension agrees with Iraids' data below 10^12 on sampled n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005520>

## Sources

- <https://oeis.org/A005520>
- <https://oeis.org/A005520/b005520.txt>
- <https://arxiv.org/abs/1203.6462>
- <https://arxiv.org/abs/1404.2183>
- <https://arxiv.org/abs/2308.10301>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Only candidates of the conjectured shape (primes, -1 mod 120) need exact lower bounds first. The rest of the proof is a sieve showing every smaller m has an expression with at most 89 ones, and most m need only a small additive correction to a product form.
- A segmented sieve: a sum term n = a + b with b small covers almost everything, and products need only divisors up to sqrt(n). Stream the table in blocks with a cache of small-complexity values.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Juxtaposing 1s is forbidden.
- Finding the first prime with ||p|| = 90 is not enough; every m < N must be covered.
- Off-by-one in the offset: A005520 has offset 1, with a(1) = 1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/integer-complexity-smallest-complexity-90.md
```

Already set up? Say `run V3R1T4S on integer-complexity-smallest-complexity-90`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `integer-complexity-smallest-complexity-90`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
