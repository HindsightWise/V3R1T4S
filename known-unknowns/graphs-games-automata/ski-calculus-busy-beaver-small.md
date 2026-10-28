# Busy Beaver for SKI combinator calculus: beat a listed lower bound for size 7..11, or settle Xi_0(7) exactly

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Xi_0(n) is the largest normal-form size of a terminating SKI combinator term with n combinators (leaves), reduction rules Sfgx = fx(gx), Kfx = f, Ix = x. The bbchallenge Busy Beaver wiki's 'SKI Calculus' page (last edited 2026-10-23) lists exact values for n <= 6 (Xi_0(6) = 17, SSS(SI)S) and only lower bounds above: n = 7: >= 41 (SSS(S(SS))S), 8: >= 80 (SSK(S(SS)S)S), 9: >= 1561 (S(SI)(SS)(SS)SS), 10: >= 1562, 11: >= 1563, then astronomically large lower bounds from n = 12. It also tabulates the SK-only calculus (exact through n = 7, Xi = 41; then 8: >= 80, 9: >= 169, 10: >= 1561, ...) and BCKW (exact through n = 5 = 47; n = 6 is already astronomically large). The small sizes are enumerable on a laptop: there are Catalan(n-1)*3^n SKI terms of size n (about 2.9e5 for n = 7, 2.8e6 for n = 8, 2.8e7 for n = 9, 2.9e8 for n = 10). Open targets: a terminating term of size n in 7..11 whose normal form is STRICTLY larger than the listed bound, or an exact value Xi_0(7) (or 8) with every non-terminating term certified.

## What counts as a win

Success means (a) an SKI term with exactly n combinator leaves, 7 <= n <= 11, that reaches a normal form under leftmost-outermost (normal-order) reduction, whose normal form has STRICTLY more combinator leaves than the lower bound listed for that n on https://wiki.bbchallenge.org/wiki/SKI_Calculus re-fetched live immediately before claiming (same size convention as the page: size = number of S/K/I leaves); or (b) an exact value: a complete enumeration of all SKI terms of size n (n = 7 or 8) in which every term is either normalised (with its normal-form size recorded) or carries a machine-checkable non-termination certificate, the maximum normalised size matching the page's listed champion, while the page still shows '>=' for that n. The same rules apply, reported separately, to the SK-only table for 8 <= n <= 12, where the page lists a lower bound.

## Partial wins

- **p1:** Exact Xi_0(7) for SKI (expected 41 if the listed champion is optimal), with all non-normalising size-7 terms certified.
- **p2:** Exact Xi_0 for the SK-only calculus at n = 8 (all size-8 SK terms classified with certificates), if the page still lists '>= 80'.
- **p3:** A complete classification of size-8 SKI terms leaving at most 20 unresolved holdouts, with the holdout list published for others.

## How a win is checked

Parse the term, reduce with an independent normal-order reducer (graph reduction with sharing is fine, but the normal form must be printed in full and its leaves counted). Confirm the normal form has no redex (no S with 3 args, K with 2, I with 1). For exact-value claims: re-run the enumeration with an independently written enumerator, confirm the count Catalan(n-1)*3^n, and re-check each non-termination certificate (e.g. a reduction sequence from t to a term containing an instance of t in head position, or a proven-looping pattern like SII(SII) reached).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/SKI_Calculus>

## Sources

- <https://wiki.bbchallenge.org/wiki/SKI_Calculus>
- <https://wiki.bbchallenge.org/wiki/Busy_Beaver_for_lambda_calculus>
- <https://oeis.org/A333479>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exhaustive enumeration with memoised reduction: reduce every subterm bottom-up once, hash-cons normal forms, and reuse results across the Catalan shapes; sizes 7-9 take minutes.
- Non-termination certificates borrowed from Busy Beaver Turing-machine deciders: cycle detection, 'translated cycler' style growth detection (term t reduces to C[t'] with t' an instance of t), and loop-pattern libraries (omega-like subterms SII(SII), S(SI)(SI)...).
- Import from term rewriting: use AProVE/TTT2-style termination provers on the non-normalising holdouts (dependency pairs, matrix interpretations) to certify non-termination or termination automatically.
- Import from program synthesis: search sizes 10-11 by genetic programming over term trees with fitness = normal-form size under a step budget, seeded with the champions of sizes 8-9 (champions tend to be extensions of smaller ones).
- Use the SK-only and BCKW tables as cross-checks: an SK term with I replaced by SKK is size-inflated, so champions transfer between tables in a known way.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Size is the number of combinator leaves, not the number of characters or applications; normal-form size is counted the same way.
- Applicative-order (innermost) reduction can loop on terms that DO have a normal form; only normal-order reduction is complete. A term judged non-terminating because an innermost reducer looped is a classic error.
- Terms that grow without bound but never reach a normal form are not terminating, however large they get.
- The page was edited repeatedly in October 2026 (footer: last edited 2026-10-23), and the n = 9..11 SKI bounds now read 1561-1563; champions change often. Re-fetch before claiming.
- Do not mix the SKI, SK-only and BCKW tables; each has its own size convention and champions (BCKW is out of reach beyond n = 5).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/ski-calculus-busy-beaver-small.md
```

Already set up? Say `run V3R1T4S on ski-calculus-busy-beaver-small`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ski-calculus-busy-beaver-small`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
