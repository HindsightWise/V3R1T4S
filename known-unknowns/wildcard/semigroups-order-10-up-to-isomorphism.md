# Semigroups of order 10 up to isomorphism (OEIS A027851(10)), equivalently the self-converse semigroups of order 10, or the labeled count A023814(10)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for the full win (likely a large constraint-solver run on the non-nilpotent order-10 semigroups); the monoid, band and inverse-semigroup partial wins look laptop-days · open as of 2026-10-30

## The problem

Andreas Distler, Chris Jefferson, Tom Kelsey and Lars Kotthoff (CP 2012) counted the semigroups of order 10 up to isomorphism or anti-isomorphism: A001423(10) = 12,418,001,077,381,302,684. They combined a constraint search for the semigroups that are not nilpotent of degree 3 with Distler and Mitchell's formulas for the degree-3 nilpotent ones (EJC 19(2) P51, 2012). Those formulas count up to equality, up to isomorphism, and up to isomorphism or anti-isomorphism. The count up to isomorphism alone, A027851(10) = 2*A001423(10) - A029851(10), is still missing because nobody has counted the self-converse semigroups of order 10 (A029851 stops at a(9) = 623,492,664, Distler 2011). The labeled count (associative operations on a 10-set, A023814) also stops at n = 9; it came from Distler and Kelsey's automorphism-group census (arXiv 1301.6023). For monoids, A058133(10) = 52,991,253,973,742 is known up to iso or anti-iso (Distler-Kelsey 2009). Self-converse monoids A058132 reached n = 9 only in Sep 2026 (Ben Spitz), and A058129 (monoids up to isomorphism) stops at a(9) = 3,685,886,630 (Cruttwell and Leblanc, added 2025). Related census entries: bands A058112 are known to n = 9 (Andrew Howroyd 2022), and inverse semigroups A001428 to n = 15 (Martin Malandro, Semigroup Forum 2019). All entries were re-fetched 2026-10-30.

## What counts as a win

Success means the exact value of A027851(10) (equivalently A029851(10)) or of A023814(10), re-fetched live and still missing immediately before claiming. The degree-3-nilpotent part must come from the Distler-Mitchell formulas, evaluated by two independent implementations that reproduce their published small values. The remaining part must come from a published search code that reproduces A029851(n) (resp. A023814(n)) for every n <= 9. A second independent method or code must agree on the non-nilpotent part, for example a constraint search for semigroups admitting an anti-automorphism versus a filter over a full enumeration. A literature search must find no earlier value.

## Partial wins

- **p1:** A058129(10), the number of monoids of order 10 up to isomorphism, obtained via A058132(10) = 2*A058133(10) - A058129(10). The pipeline must reproduce A058129(n), A058132(n) and A058133(n) for n <= 9 and A058133(10) = 52,991,253,973,742.
- **p2:** A058112(10), the number of bands (idempotent semigroups) of order 10, by code reproducing a(n) for n <= 9 and a second independent method agreeing.
- **p3:** A001428(16), the number of inverse semigroups of order 16 up to isomorphism or anti-isomorphism, by code reproducing Malandro's values for n <= 15 and a second independent method agreeing.

## How a win is checked

Re-evaluate the Distler-Mitchell formulas independently. Rerun the search code for n <= 9 against OEIS. For the new term, recompute a random sample of the search's work units (for example by fixed idempotent structure or minimal ideal) with independent code and compare the partial sums.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A027851>

## Sources

- <https://oeis.org/A027851>
- <https://oeis.org/A029851>
- <https://oeis.org/A001423>
- <https://oeis.org/A023814>
- <https://oeis.org/A058129>
- <https://oeis.org/A058132>
- <https://oeis.org/A058133>
- <https://oeis.org/A058112>
- <https://oeis.org/A001428>
- <https://doi.org/10.37236/2441>
- <https://doi.org/10.1007/978-3-642-33558-7_63>
- <https://arxiv.org/abs/1301.6023>
- <https://arxiv.org/abs/1312.7192>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search directly for order-10 semigroups together with an anti-automorphism (an involutive or finite-order bijection reversing products) as part of the constraint model; this space is far smaller than all non-nilpotent semigroups.
- Monoids with trivial group of units correspond to semigroups of order n-1 with an identity adjoined, so A058129(10) needs new search work only for monoids with nontrivial units.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Up to isomorphism (A027851) and up to iso or anti-iso (A001423) are different counts; check which one each formula gives.
- OEIS offsets: these entries start at n = 0 except A001428, which starts at n = 1.
- Nilpotent semigroups of degree 3 dominate the totals; a bug in the formula part swamps everything else.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/semigroups-order-10-up-to-isomorphism.md
```

Already set up? Say `run V3R1T4S on semigroups-order-10-up-to-isomorphism`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `semigroups-order-10-up-to-isomorphism`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
