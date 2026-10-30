# Hausdorff dimension of the Apollonian gasket: more than Vytnova-Wormell's 128 rigorous decimals

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (the 128-decimal run took about 90 hours on 30 cores; public Julia code) · open as of 2026-10-30

## The problem

The residual set of the Apollonian circle packing has Hausdorff dimension delta_A = 1.3056867... (OEIS A052483). No closed form is known. delta_A also governs circle counting: the number of circles of curvature at most x grows like c x^delta_A (Kontorovich-Oh). The value was estimated by Boyd, McMullen (1998), Manna-Herrmann (1991) and Thomas-Dhar (1994), and extended by Bai and Finch (Fractals 2018, 30 non-rigorous decimals). Polina Vytnova and Caroline Wormell ('Hausdorff dimension of the Apollonian gasket', arXiv 2406.04922, Invent. Math. 239 (2025) 909-946) developed an efficient method for parabolic limit sets with rigorously justified error bounds and computed delta_A to 128 decimal places (Theorem 1.1 prints 129 digits with radius 10^-129). Their run used precision 2^-447 and took about 90 hours on 30 cores. Their Julia code is public (github.com/wormell/apollonian), and they estimate that doubling the digit count costs about 100 times more computing. OEIS A052483 lists 110 terms from their work (extension of Nov 2023). The parabolic fixed points make the transfer-operator problem harder than for uniformly hyperbolic Cantor sets, so this is a strong benchmark for certified dimension computation, and the authors expect the method to extend.

## What counts as a win

Success means a rigorous enclosure of delta_A of radius at most 10^-(D+1), the convention of Vytnova-Wormell's Theorem 1.1 (128 decimals, radius 10^-129), with D STRICTLY GREATER (direction: max) than 128 and than any certified digit count found in a literature/OEIS search re-run immediately before claiming. A 129-decimal win therefore needs radius at most 10^-130. The enclosure must be consistent with Vytnova-Wormell's 128 decimals. The certificate is a program in rigorous arithmetic (Arb or similar) plus a written account of the error bounds (transfer-operator discretisation, treatment of the parabolic cusps, and the bisection in the dimension parameter) that a skeptic reruns and checks.

## Partial wins

- **p1:** A non-rigorous computation of delta_A to at least 200 decimals by two independent methods (for example a Vytnova-Wormell-style discretisation and a periodic-orbit or cycle-expansion method), agreeing on all 200, with the first 128 matching Vytnova-Wormell.

## How a win is checked

Skeptic: rerun the certified program at two precisions and check that the enclosure of the leading eigenvalue of the transfer operator brackets 1 on either side of the dimension interval. Check the parabolic-cusp error terms against the written argument. Compare the leading 128 decimals with the published value. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A052483>

## Sources

- <https://arxiv.org/abs/2406.04922>
- <https://oeis.org/A052483>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Induce on the cusps: replace the parabolic maps by their first-return (infinite-alphabet, uniformly expanding) system, whose transfer operator has explicitly summable tails (zeta-type sums), then use Chebyshev or Lagrange collocation with a posteriori bounds.
- Reuse certified-spectral techniques for the Gauss map (Nisoli 2026) on the induced operator.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Digits of agreement between two non-rigorous runs do not count for the main win.
- Different 'Apollonian' sets (the gasket, the strip packing, packings with other root quadruples) share the dimension only when they are Moebius-equivalent; state which limit set is computed.
- The OEIS lists 110 terms but the record to beat is 128 certified decimals; Theorem 1.1 prints a 129th digit only inside its radius 10^-129, so that digit is not certified.
- Rerunning the public Vytnova-Wormell code at higher precision is allowed, but cost grows roughly like (digits)^6.5; even a few extra digits need a multi-core server for days, not a laptop.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/apollonian-gasket-dimension-certified-digits.md
```

Already set up? Say `run V3R1T4S on apollonian-gasket-dimension-certified-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `apollonian-gasket-dimension-certified-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
