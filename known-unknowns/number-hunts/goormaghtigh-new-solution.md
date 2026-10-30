# Goormaghtigh conjecture: a third number that is a repunit ( > = 3 digits) in two bases

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster · open as of 2026-10-30

## The problem

Goormaghtigh (1917) asked about (x^m - 1)/(x - 1) = (y^n - 1)/(y - 1) with x > y > 1 and n > m > 2, that is, numbers that are repunits with at least three digits in two different bases. The only known solutions are 31 = 111_5 = 11111_2 and 8191 = 111_90 = 1111111111111_2. The conjecture that there are no others is open (Wikipedia, edited 2026-10-26; Grantham 2026). Known partial results: Makowski-Schinzel (no others with both bases <= 10, or with the larger exponent n <= 5); Davenport-Lewis-Schinzel (finitely many for fixed exponents); Nesterenko-Shorey and Bugeaud-Shorey (effective bounds in restricted cases with gcd(m-1, n-1) > 1; Bugeaud-Shorey needs gcd(m-1, n-1) large relative to (n-1)/(m-1)); Yuan (2005, m = 3 with odd n); He-Togbe (2008, at most one solution for fixed bases). Bennett-Garbuz-Marten (Publ. Math. Debrecen 96 (2020); Theorems 3, 4 and 6) proved there are no others with both bases <= 10^5, none with gcd(m-1, n-1) > 1 and n <= 50, none with n = m+1 for 3 <= m <= 17, and none with (n-1)/(m-1) = 3. Jon Grantham (arXiv 2410.03677, Integers 24 (2024) A98; v3 2026-10-17 corrects the computation and supplies code, data and a Lean 4 development) proved there is no other prime value (a 'Goormaghtigh prime') below 10^700. Bennett-Gherga-Kreso (Trans. AMS 373 (2020)) settle further small-exponent cases used by Grantham. Credit: Goormaghtigh, Makowski, Schinzel, Yuan, He, Togbe, Shorey, Bugeaud, Bennett, Garbuz, Marten, Gherga, Kreso, Grantham.

## What counts as a win

CONFIRMED for integers x > y > 1 and n > m > 2 with (x^m - 1)/(x - 1) = (y^n - 1)/(y - 1) exactly (Python big integers), where the common value is neither 31 nor 8191, and no third solution is listed on https://en.wikipedia.org/wiki/Goormaghtigh_conjecture at verification time. Solutions with an exponent 2 (repunits 11_x) are outside the problem and do not count.

## Partial wins

- **p1:** Goormaghtigh-prime frontier: a computation proving that there is no Goormaghtigh prime other than 31 and 8191 below 10^E, for E strictly greater than 700 (Grantham, arXiv 2410.03677 v3) or than any larger bound published at verification time. The only non-computational steps allowed are citations of published theorems by exact statement number. Code, data and survivor logs must be published, and the verifier reruns the computation independently (fully, or on sampled intervals plus a coverage check).
- **p2:** Base-range extension: a computation proving that the two known solutions are the only ones with both bases <= Y, for Y strictly greater than 10^5 (Bennett-Garbuz-Marten 2020, Theorem 3) and than any larger published range. It must use a published explicit exponent bound (for example He-Togbe's Lemma 2.3, as used in BGM Section 2) plus exhaustive sieving and Baker-Davenport reduction. Every step is rerunnable by the verifier in PARI/GP or Sage, and nothing is left unproved apart from citations of published theorems.

## How a win is checked

Exact big-integer evaluation of both repunits and the inequalities, under 1 second. For the partial wins, the verifier reruns the claimant's code and an independent reimplementation on sampled ranges, checks that the ranges are covered, and checks that every cited theorem is applied within its stated hypotheses.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Goormaghtigh_conjecture>

## Sources

- <https://en.wikipedia.org/wiki/Goormaghtigh_conjecture>
- <https://arxiv.org/abs/2410.03677>
- <https://personal.math.ubc.ca/~bennett/BeGaMa-PMD-2020.pdf>
- <https://github.com/31and8191/goor1/>

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/goormaghtigh-new-solution.md
```

Already set up? Say `run V3R1T4S on goormaghtigh-new-solution`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `goormaghtigh-new-solution`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
