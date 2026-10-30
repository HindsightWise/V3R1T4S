# Totally symmetric alternating sign matrices: a rigorous count A005164(25) (order 51), and an exact-enumeration check of the terms that rest on a conjectured formula

🎲 **Recreational math** · standard · tractability ★★★★☆ · compute: laptop-hours (transfer matrix on the 1/8 fundamental domain, modular arithmetic plus CRT) · open as of 2026-10-30

## The problem

A005164 counts (2n+1) x (2n+1) alternating sign matrices invariant under all eight symmetries of the square (TSASMs). Besides DSASM and even-order DASASM, it is the only ASM symmetry class with no product formula. Robbins (Symmetry classes of ASMs, 2000) and Stanley (A baker's dozen of conjectures, 1986) list it, and Bousquet-Melou and Habsieger computed early terms. OEIS DATA runs to a(24) (order 49). Jean Lienardy added a(14)-a(19) in Aug 2020 and a(20)-a(24) in Sep 2022, next to his note that Hagendorf and Lienardy (arXiv:2008.03220) give a CONJECTURED multiple-contour-integral formula. That paper's abstract presents the TSASM link as a conjecture, so the terms from a(14) on may rest on it. Keyword 'more'; unchanged since 2022, re-fetched 2026-10-30. In October 2026 James Guillochon pushed the neighbouring class A005162 (ASMs symmetric about both diagonals) to n = 62 with a transfer matrix on the fundamental triangle (github guillochon/oeis-results). That suggests a direct enumeration of TSASMs to order 51 and beyond is a laptop computation.

## What counts as a win

The exact integer A005164(25) (TSASMs of order 51), obtained by an exact enumeration (a transfer matrix, a DP or an equivalent count of the matrices themselves), not by evaluating the Hagendorf-Lienardy conjectured formula. The same program must reproduce a(0)..a(13) exactly. It must also either reproduce a(14)..a(24) or report each disagreement, and a second independent program must confirm every disagreement. Two independent runs must agree on a(25), using different prime sets or exact big integers and a different sweep order or state encoding. It counts only if a(25) is not in the DATA or a b-file of A005164 when re-fetched immediately before claiming.

## Partial wins

- **p1:** An exact enumeration (not the conjectured formula) that reproduces every term a(14)..a(24) of A005164, with code and per-term residues published, so the existing terms no longer depend on a conjecture.
- **p2:** An exact enumeration that reproduces a(0)..a(19) and finds a disagreement with a published term, confirmed by a brute-force count for that order or by a second independent program.

## How a win is checked

Skeptic (under an hour): brute-force the TSASMs of orders 1..9 (a(0)..a(4) = 1,1,1,2,4) and compare with the program. Rerun the claimant's code modulo one fresh 62-bit prime for a(25) and check that the program also reproduces a(24). A second independent implementation can follow.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005164>

## Sources

- <https://oeis.org/A005164>
- <https://arxiv.org/abs/2008.03220>
- <https://arxiv.org/abs/math/0008045>
- <https://oeis.org/A005162>
- <https://github.com/guillochon/oeis-results/tree/main/A005162>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Six-vertex (square ice) encoding with reflecting boundaries along the symmetry axes: sweep the 1/8 wedge row by row, as Guillochon did for DASASM on the fundamental triangle.
- Count modulo several 62-bit primes and recombine by CRT. a(25) is about 3 x 10^34 (a(24) = 5.3e31 and the ratio of consecutive terms is about 420 and rising), so two primes suffice and a third serves as a check.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offset 0 and odd order: a(n) is order 2n+1, so a(24) is order 49 and the target a(25) is order 51.
- A value computed from the conjectured contour-integral formula is not a win under this entry.
- Guillochon is actively extending ASM symmetry classes in 2026; re-fetch A005164 and its history right before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/tsasm-a005164-order-51-exact.md
```

Already set up? Say `run V3R1T4S on tsasm-a005164-order-51-exact`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsasm-a005164-order-51-exact`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
