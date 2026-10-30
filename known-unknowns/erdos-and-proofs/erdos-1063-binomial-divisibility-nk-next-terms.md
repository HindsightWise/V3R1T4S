# Erdos #1063 (Erdos-Selfridge): n_k for k >= 76 (OEIS A389360 beyond the forum's k = 75)

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (progression sweeps; 89e9 candidates covered k = 60..75) · open as of 2026-10-30

## The problem

n_k is the least n >= 2k such that n-i divides C(n,k) for all but exactly one i in 0 <= i < k (Erdos-Selfridge 1983; Guy B31; OEIS A389360). Values start n_2..n_5 = 4, 6, 9, 12; Monier gave n_k <= k! and Cambie n_k <= k*lcm(2..k-1). rickyc (forum, Jun-Jul 2026) proved n_k >= prod over p^a || k of p^(a + floor(log_p(k-1))), and has two AI-assisted proof claims on the site (Jul-Aug 2026) for asymptotic bounds on log n_k. The OEIS b-file (Chai Wah Wu) ends at k = 59 (a(59) = 4967281530). On the forum, jbell31 (28 Jul 2026, github.com/Jaybell31/dreamwalk/tree/master/erdos1063) extended it to k = 75 (e.g. n_75 = 32639932074432). That work uses rickyc's structural results: the failing index is n mod k, and solutions lie on explicit progressions. Each value was checked by an independent exact-binomial verifier and declared minimal after a sweep of 89,015,468,839 candidates; the repository states that minimality rests on that single sweep implementation. Minimality is also conditional on rickyc's lemmas, which have forum proofs but are not formalised.

## What counts as a win

CONFIRMED: the exact value of n_76: an n with exactly one 0 <= i < 76 such that (n-i) does not divide C(n,76), verified with exact big-integer arithmetic, plus an exhaustive minimality sweep reproduced by two independent implementations. Larger k extend the record.

## Partial wins

- **p1:** A Lean 4 proof (no sorry, standard axioms only) of rickyc's structural lemma used to restrict the search: the unique failing index satisfies e = n mod k, together with the prime-power divisibility conditions. This makes the published minimality claims for k = 60..75 unconditional.
- **p2:** An independent re-derivation of n_60..n_75 by code sharing nothing with jbell31's searcher or verifier, matching all 16 forum values or exhibiting a smaller solution.
- **p3:** Exact n_k for every 76 <= k <= 85 with minimality as in the success criterion.

## How a win is checked

Compute C(n,k) exactly (Python integers) and test each n-i for divisibility, expecting exactly one failure. Re-run the minimality sweep with independent code over the progressions n = r mod D(k,r), and check the predicted candidate count against the number enumerated.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/1063>

## Sources

- <https://www.erdosproblems.com/1063>
- <https://www.erdosproblems.com/forum/thread/1063>
- <https://oeis.org/A389360>
- <https://github.com/Jaybell31/dreamwalk/tree/master/erdos1063>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the progression structure: for each residue r, solutions satisfy n = r mod D(k,r). Sweep candidates in increasing order across all r in parallel.
- Use 128-bit arithmetic: n_k already reaches 3.3e13 at k = 75 and may pass 2^63 soon after.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Take the minimum over all residues r, not the first hit in r-order (a real bug jbell31 reported).
- Respect the n >= 2k floor.
- Values above the OEIS b-file are forum claims; re-derive before relying on them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1063-binomial-divisibility-nk-next-terms.md
```

Already set up? Say `run V3R1T4S on erdos-1063-binomial-divisibility-nk-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1063-binomial-divisibility-nk-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
