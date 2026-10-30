# Kourovka 16.46 (Conder): does the index-8 subgroup K of an amalgam acting on the 3-valent tree have a non-trivial finite quotient?

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-hours (low-index subgroups, homomorphism searches into simple groups) · open as of 2026-10-30

## The problem

Among the finitely presented groups that act arc-transitively on the 3-valent tree with finite vertex stabiliser are G3 and G4 (Djokovic-Miller types), each containing PSL(2,Z) = <h,a | h^3, a^2> with finite index. Their free product with <h,a> amalgamated has a normal subgroup K of index 8 with presentation K = <A,B,C,D,E,F | A^3, B^3, C^2, D^2, E^2, F^2, (AC)^3, (AD)^3, (AE)^3, (AF)^3, (BC)^3, (BD)^3, (BE)^3, (BF)^3, (ABA^-1C)^2, (ABA^-1D)^2, (A^-1BAE)^2, (A^-1BAF)^2, (BAB^-1C)^2, (B^-1ABD)^2, (BAB^-1E)^2, (B^-1ABF)^2 > . Kourovka Notebook problem 16.46 (M. Conder), still open with no comment in the 21st edition (arXiv 1401.0300v49, 20 Oct 2026), asks whether K has a non-trivial finite quotient. Our quick hand check: K's abelianisation is trivial, so any finite quotient is non-abelian.

## What counts as a win

Success means an explicit non-trivial homomorphism from K to a finite group: images of A, B, C, D, E, F as permutations in some S_n (or matrices over a finite field), not all the identity, that satisfy all 22 relators exactly. A machine-checked proof that K has no non-trivial finite quotient also counts.

## Partial wins

- **p1:** A re-runnable exhaustive low-index-subgroups certificate (for example GAP LowIndexSubgroupsFpGroup, cross-checked by an independent implementation) that K has no proper subgroup of index at most 30, published with code and run log.

## How a win is checked

Substitute the permutation or matrix images into each of the 22 relators and check that each gives the identity, and that at least one generator image is non-trivial. Re-type the presentation from the Kourovka PDF independently, because a transcription error makes the check meaningless.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1401.0300>

## Sources

- <https://arxiv.org/abs/1401.0300>
- <https://kourovkanotebookorg.wordpress.com/>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Problems marked ♯ in the Notebook have unverified AI solutions and those marked ∗ are solved; 16.46 has neither mark as of v49, but re-check the latest version.
- Check relator orientation (A^-1 B A versus A B A^-1) against the PDF; the two are not interchangeable.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/kourovka-16-46-conder-finite-quotient.md
```

Already set up? Say `run V3R1T4S on kourovka-16-46-conder-finite-quotient`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kourovka-16-46-conder-finite-quotient`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
