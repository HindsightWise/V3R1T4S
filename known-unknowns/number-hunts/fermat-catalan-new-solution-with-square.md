# Fermat-Catalan: an eleventh solution of a^m + b^n = c^k with 1/m + 1/n + 1/k < 1 (one exponent equal to 2)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster · open as of 2026-10-30

## The problem

The Fermat-Catalan conjecture says that a^m + b^n = c^k with a, b, c coprime positive integers and 1/m + 1/n + 1/k < 1 has only finitely many solutions, counted as distinct triples (a^m, b^n, c^k). Wikipedia (edited 2026-06-04, 'as of 2024') lists ten known solutions: 1^m+2^3=3^2, 2^5+7^2=3^4, 7^3+13^2=2^9, 2^7+17^3=71^2, 3^5+11^4=122^2, 33^8+1549034^2=15613^3, 1414^3+2213459^2=65^7, 9262^3+15312283^2=113^7, 17^7+76271^3=21063928^2, 43^8+96222^3=30042907^2. We rechecked all ten, and each one has an exponent 2. The larger ones come from the 1993 Fermat-day computer search at Utrecht (cited in Beukers, Duke Math. J. 91 (1998)). Adam Sikora (arXiv 2410.21552, 2024) verified that these are the only coprime solutions with min exponent d <= 113 and all three powers below M_d, where M_2 = 2^71, M_3 = 2^80, M_4 = 2^100 and M_d = 2^113 for d >= 5. Darmon-Granville proved finiteness for each fixed signature. Many signatures are fully solved (Poonen-Schaefer-Stoll for (2,3,7); Bruin; Chen; Ellenberg; and others). Target: a new solution. This target covers only solutions with an exponent equal to 2. A solution with all exponents >= 3 would be a Beal counterexample, which is a live-prize matter (see held). Credit: Beukers, Zagier, Darmon, Granville, Sikora, Poonen, Schaefer, Stoll, Bruin.

## What counts as a win

CONFIRMED for positive integers a, b, c with gcd(a,b,c) = 1 and positive integers m, n, k with 1/m + 1/n + 1/k < 1 (exact rational comparison) and min(m,n,k) = 2, such that a^m + b^n = c^k exactly in Python big integers. The triple (a^m, b^n, c^k), up to swapping the two summands, must not be among the solutions listed on https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture at verification time (ten on 2026-10-30). By Mihailescu's theorem, no new solution has a, b or c equal to 1. A solution with m, n, k all >= 3 is outside this target: report it to the human (Beal Prize) and make no claim here.

## Partial wins

- **p1:** Search certificate: an exhaustive search, independently reimplemented by the verifier, proving that the ten known solutions are the only coprime ones with max(a^m, b^n, c^k) <= B over all admissible signatures with an exponent 2. B must be strictly greater than 2^71 = 2361183241434822606848 (Sikora 2024, the largest such bound found on 2026-10-30) and than any larger bound published at verification time. The run ships hashed logs, and the verifier reruns sampled ranges (enumerating x^p - y^q = +-z^2 style differences against a squares test).

## How a win is checked

Exact big-integer evaluation, a gcd check, exact rational comparison of 1/m+1/n+1/k with 1, and a set comparison with the ten listed triples. Under 1 second. For p1, independent reimplementation and sampled reruns.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture>

## Sources

- <https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture>
- <https://arxiv.org/abs/2410.21552>
- <https://arxiv.org/abs/math/0508174>
- <https://en.wikipedia.org/wiki/Beal_conjecture>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fix a signature (2, 3, k) or (2, 4, k) not yet solved in the literature and search via the associated Frey-curve twists or Thue equations, which turn the search into finitely many low-degree equations that can be searched much further than brute force.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Signatures already solved completely (for example (2,3,7), (2,3,8), (2,3,9), (2,4,5)) cannot give new solutions. A claimed solution there is a bug.
- Non-coprime triples, such as scalings like 2^3 + 2^3 = 2^4, never count.
- Brute force with all powers below 2^71 repeats Sikora's 2024 search and cannot find anything new.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/fermat-catalan-new-solution-with-square.md
```

Already set up? Say `run V3R1T4S on fermat-catalan-new-solution-with-square`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fermat-catalan-new-solution-with-square`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
