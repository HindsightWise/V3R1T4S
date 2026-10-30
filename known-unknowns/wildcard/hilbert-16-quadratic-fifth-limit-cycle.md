# MOONSHOT - Hilbert's 16th problem for quadratic systems: a quadratic vector field with five limit cycles (H(2) >= 4 since Shi 1980)

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours per candidate (validated integration); the search itself is open-ended · open as of 2026-10-30

## The problem

The second part of Hilbert's 16th problem asks for H(n), the maximal number of limit cycles of planar polynomial vector fields of degree n. Even the finiteness of H(2) was long open. An unrefereed OpenAI draft ('Uniform bounds for planar polynomial limit cycles', dated 24 Sep 2026, released 6 Oct 2026, cited in the closing remark of Qin-Sun) claims that H(d) is finite for every d. Finiteness, even if correct, does not decide whether a quadratic system can have five cycles. Since Chen Lansun and Wang Mingshu (1979) and Shi Songling (Scientia Sinica 23 (1980) 153-158), quadratic systems with four limit cycles in the (3,1) distribution have been known, and no quadratic system with five has ever been found. Bautin proved that at most three small-amplitude cycles bifurcate from one quadratic focus. Table 1 of Chaoyang Qin and Xiaoming Sun (arXiv 2610.12218, 8 Oct 2026) still lists H(2) >= 4 (Shi 1980) as the best explicit lower bound. Wikipedia's Hilbert's sixteenth problem page records the same state, citing Ilyashenko's 2002 survey and the narrow basins that make numerical counting unreliable (Kuznetsov-Kuznetsova-Leonov 2011, Leonov-Kuznetsov 2013).

## What counts as a win

An explicit quadratic system x' = P(x,y), y' = Q(x,y) (degree <= 2, rational coefficients) with at least 5 limit cycles (direction: more than the current 4), certified in one of two ways. (a) Validated numerics: for each cycle, a transversal segment on which an interval-arithmetic validated Poincaré return map shows the displacement changing sign between two points, with the segments and orbit enclosures showing that the 5 sign changes belong to 5 distinct closed orbits. A sign change excludes a period annulus, so each is a limit cycle by analyticity. (b) A one-parameter family plus an exact-arithmetic check of every hypothesis of a cited bifurcation theorem (Lyapunov constants, Melnikov or Abelian integrals) that yields 5 limit cycles for all small enough parameter values.

## Partial wins

- **p1:** A validated-numerics certificate (rule (a)) of four limit cycles in one explicit quadratic system with rational coefficients of absolute value <= 10, all four certified at that single parameter value (no 'for epsilon small enough' argument), such that no validated-numerics certificate of four limit cycles in a quadratic system is found by a literature search.

## How a win is checked

Skeptic: re-run the validated integrator (for example CAPD or arb-based Taylor models) from each segment endpoint, confirm the displacement signs and the disjointness of the orbit enclosures, and check that the system has degree 2. For (b), recompute the Lyapunov or Melnikov quantities in exact rational arithmetic and confirm the theorem's rank or zero conditions. Minutes to hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.12218>

## Sources

- <https://arxiv.org/abs/2610.12218>
- <https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem>
- <https://en.wikipedia.org/wiki/Smale%27s_problems>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Plots and floating-point integration routinely miss or invent nested cycles with tiny basins; only interval-validated return maps or exact bifurcation certificates count.
- Known theory restricts the configurations: at most 3 small cycles around one focus (Bautin), and four-cycle examples have the (3,1) distribution; check a candidate's nests against these results before a long computation.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/hilbert-16-quadratic-fifth-limit-cycle.md
```

Already set up? Say `run V3R1T4S on hilbert-16-quadratic-fifth-limit-cycle`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hilbert-16-quadratic-fifth-limit-cycle`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
