# Kourovka 20.21 (Verret/Conder): isomorphic normal subgroups K and L of index 12 with G/K = C12 and G/L = A4

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-days (GAP search over SmallGroups and extensions, filtering groups with both a C12 and an A4 quotient) · open as of 2026-10-30

## The problem

Kourovka Notebook problem 20.21 (posed by G. Verret, submitted by M. Conder, 20th issue 2022), still unanswered in the 21st edition (arXiv 1401.0300v49, 20 Oct 2026): does there exist a finite group G with two normal subgroups K and L, each of index 12, such that K is isomorphic to L but G/K is cyclic of order 12 while G/L is the alternating group A4? A positive answer is a finite object that anyone can check.

## What counts as a win

Success means an explicit finite group G (as a permutation group or a pc-presentation), explicit generators of normal subgroups K and L, and an explicit isomorphism K -> L, such that a GAP or Magma check confirms: K and L are normal in G, |G:K| = |G:L| = 12, the map is an isomorphism, G/K is cyclic of order 12, and G/L is isomorphic to A4. A machine-checked proof that no such G exists also counts.

## Partial wins

- **p1:** A re-runnable exhaustive certificate that no such G exists with |G| <= 1000, covering every order divisible by 12 in the SmallGroups library (pre-filtering to groups with both a C12 quotient and an A4 quotient is allowed), with the code and the run log.

## How a win is checked

Load G in GAP; check IsNormal for K and L, the indices, IdGroup or StructureDescription of G/K and G/L (C12 versus A4), and that the given generator map extends to an isomorphism K -> L (GroupHomomorphismByImages plus IsBijective).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1401.0300>

## Sources

- <https://arxiv.org/abs/1401.0300>
- <https://kourovkanotebookorg.wordpress.com/>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- K and L must be isomorphic as abstract groups, not conjugate or equal; a map that is not a homomorphism fails.
- Re-check the latest Notebook version: AI-proposed solutions are being posted (♯ marks), and only ∗ marks mean confirmed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/kourovka-20-21-isomorphic-normal-subgroups-c12-a4.md
```

Already set up? Say `run V3R1T4S on kourovka-20-21-isomorphic-normal-subgroups-c12-a4`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kourovka-20-21-isomorphic-normal-subgroups-c12-a4`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
