# Integer complexity Conjecture A: ||2^a 3^b 5^c|| = 2a + 3b + 5c for c < 6 (Selfridge's ||2^a|| = 2a); a counterexample, or a proof beyond Altman's a <= 48

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (defect-based exact algorithms); verification of a counterexample is instant · open as of 2026-10-30

## The problem

The integer complexity ||n|| (Mahler and Popken 1953; Guy 1986) is the fewest 1s needed to write n using +, * and parentheses (OEIS A005245). Selfridge asked whether ||2^a|| < 2a for some a. Iraids, Balodis, Cernenoks, Opmanis, Opmanis and Podnieks (arXiv:1203.6462, 2012, Hypothesis 5) conjectured the general form. Konyagin and Oganesyan call it Conjecture A (arXiv:2603.20876v2, April 2026, where it is still open): for nonnegative a, b, c with a + b + c > 0 and c < 6, ||2^a 3^b 5^c|| = 2a + 3b + 5c. Iraids et al. verified it for all 2^a 3^b 5^c < 10^12 while computing ||n|| for n <= 10^12. Harry Altman (Integers 18 (2018) A45; arXiv:1606.03635) built on the defect delta(n) = ||n|| - 3 log_3 n and the Altman-Zelinsky theory of low-defect numbers. He gave an algorithm that decides when 2^k is stable and proved the case c = 0 for all a <= 48 and every b, by showing that 2^48 is stable with ||2^48|| = 96 (about 20 hours on his laptop). His Haskell implementation is public. Konyagin and Oganesyan (2026) cite a <= 48 as the current state. Other work: Arias de Reyna and van de Lune (algorithms, 2014), Cordwell et al. (2017), Qizheng He (2023), Zelinsky (upper bounds, 2022). A counterexample with b = c = 0 would also answer Selfridge's question.

## What counts as a win

CONFIRMED (full win) for either (a) an explicit expression built only from the literal 1, +, * and parentheses that evaluates exactly to 2^a 3^b 5^c (a + b + c > 0, 0 <= c <= 5) using STRICTLY FEWER than 2a + 3b + 5c ones (direction: min on the ones count), or (b) a Lean 4 (Mathlib) proof of Conjecture A for all such a, b, c, with no sorry and only standard axioms. The expression is checked by parsing it, counting the 1s and evaluating it with exact integers.

## Partial wins

- **p1:** A computer-assisted proof that ||2^a 3^b|| = 2a + 3b for all a <= A and all b, with A >= 49 (strictly beyond Altman's a <= 48). The program must be published, the verifier must rerun it, a second independently written implementation must agree on the case list, and both must reproduce Altman's a <= 48 as a regression.
- **p2:** A computer-assisted proof, independently reimplemented as in p1, that ||2^a 3^b 5^c|| = 2a + 3b + 5c for some fixed c in 1..5, all b and all a <= 10. This lies beyond the box 2^a 3^b 5^c < 10^12 checked by Iraids et al.

## How a win is checked

For an expression: parse it with a restricted grammar (only '1', '+', '*', parentheses), count the 1s, and evaluate it with Python integers. For p1/p2: rerun the published program, diff its output with the second implementation, and confirm the a <= 48 regression. Check the arithmetic of the defect bounds with exact rationals or interval arithmetic, not floats.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2603.20876>

## Sources

- <https://arxiv.org/abs/2603.20876>
- <https://arxiv.org/abs/1606.03635>
- <https://arxiv.org/abs/1203.6462>
- <https://oeis.org/A005245>
- <https://arxiv.org/abs/1207.4841>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Altman's defect algorithm: numbers with defect below a bound s are covered by finitely many 'low-defect polynomials'. Extending a is a matter of pushing s up efficiently (memoisation, better pruning).
- Search for counterexamples near the top of the defect spectrum: an expression for 2^a 3^b using a big sum term, of the shape 2^x 3^y (2^u 3^v + 1), is the only kind that could beat the product form.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Writing 11 or 111 by putting 1s side by side is not allowed; only + and * of 1s.
- Floating-point log_3 in defect comparisons gives wrong cases at the boundary; use exact arithmetic.
- c >= 6 is excluded on purpose: 5^6 has a cheaper representation, so the conjecture is stated only for c < 6.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/integer-complexity-conjecture-a.md
```

Already set up? Say `run V3R1T4S on integer-complexity-conjecture-a`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `integer-complexity-conjecture-a`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
