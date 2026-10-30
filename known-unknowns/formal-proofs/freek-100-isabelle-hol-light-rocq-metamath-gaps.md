# Freek Wiedijk's 100 theorems: fill a gap in Isabelle, HOL Light, Rocq, Metamath or Mizar (Lean is complete)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: pure thought plus laptop-hours of proof-assistant builds · open as of 2026-10-30

## The problem

Freek Wiedijk (Radboud University) maintains 'Formalizing 100 Theorems'. The page (last modified 2026-10-29) shows 100% formalised overall: Lean has all 100 (the four colour theorem as a Lean port of Gonthier's proof by Chris Emery and Robert D. Barish, Fermat's Last Theorem by Anthropic). Its other counts are HOL Light 95, Isabelle 95, Rocq 80, Metamath 74 (the Metamath 100 page of David A. Wheeler and Norman Megill says 75) and Mizar 71. John Harrison's HOL Light repository is ahead of the page: commit d30e823 (2026-10-20) added Claude-autoformalised Puiseux's theorem, independence of CH and AC from ZF, and a port of the four colour theorem, leaving only #16 (Abel-Ruffini, insolvability of the general quintic) and #33 (FLT) open in HOL Light. Isabelle lacks #16, #28 Pascal's hexagon theorem, #32 four colour, #33 FLT and #43 the isoperimetric theorem, and no AFP entry proves any of them. Larry Paulson's New_Algebra development in the Isabelle repository (since 2026-09-06) already proves the finite Galois correspondence and the non-solvability half of Abel-Ruffini; the radical-extension half is only begun. Rocq lacks 20, among them PNT, trisection, the area of a circle, the parallel postulate, Green, Brouwer, Pell, Minkowski, isoperimetric, partitions, CLT, Dirichlet, Platonic solids, Fourier series, Pick, Buffon and Descartes' rule of signs. Metamath's own to-do list has 25 items (including Goedel's incompleteness, the polyhedron formula, Brouwer, CLT, pi transcendental, Morley, Pick and Buffon). Mizar lacks 29. Every gap is a fixed, famous statement whose proof one system's kernel can check.

## What counts as a win

A complete formalisation, in the target system, of a theorem from the list for which neither Freek's page nor that system's own sources show a formalisation at claim time. The sources are: the HOL Light repository (100/, Autoformalization/, 4CT/), the Isabelle distribution and its development repository and the AFP, Rocq's opam/contrib ecosystem, set.mm, and the MML. The full win is a cell in HOL Light (#16 or #33) or Isabelle/HOL (#16, #28, #32, #33 or #43). The statement must be at least as strong as the Lean, HOL Light or Rocq statement linked from Freek's page for that theorem, using the system's standard library notions; no new axioms. The development must be checked by the system's kernel, with no sorry/oops (Isabelle), no cheat or new_axiom and axioms() unchanged (HOL Light), no Admitted/Axiom (Rocq), and no ? steps (Metamath). A Rocq, Metamath or Mizar cell counts as a partial win (below).

## Partial wins

- **p1:** A Rocq (Coq) formalisation, with Print Assumptions showing only the standard library's classical axioms if any, of one of the 20 theorems Freek's page lists without a Rocq entry, where no Rocq development of it is already public.
- **p2:** A set.mm proof of one of the 25 theorems on the Metamath 100 to-do list, accepted by metamath-exe 'verify proof *' and by one other verifier (metamath-knife or checkmm).
- **p3:** A Mizar article proving one of the 29 theorems with no Mizar entry on Freek's page, accepted by the current Mizar verifier against the current MML.

## How a win is checked

The skeptic builds the development with the stated system version (isabelle build -D; a HOL Light loads run followed by axioms() showing only the three standard axioms; coqc plus Print Assumptions; metamath-exe plus a second verifier; or the Mizar verifier). They grep for sorry, oops, cheat, Admitted and new_axiom, and compare the final statement with the Lean, HOL Light or Rocq statement linked from Freek's page. They also re-check Freek's page, the system's repository and library (for Isabelle, the development repository as well as the AFP) that the cell was still empty. 1 to 4 hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.cs.ru.nl/~freek/100/>

## Sources

- <https://www.cs.ru.nl/~freek/100/>
- <https://us.metamath.org/mm_100.html>
- <https://github.com/jrh13/hol-light/tree/master/100>
- <https://github.com/jrh13/hol-light/tree/master/Autoformalization>
- <https://www.isa-afp.org/>
- <https://leanprover-community.github.io/100.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Pascal and the isoperimetric theorem in Isabelle can be ported from HOL Light's 100/pascal.ml and 100/isoperimetric.ml; Isabelle HOL-Analysis shares much of HOL Light's multivariate library.
- Rocq gaps such as Descartes' rule of signs, Pick's theorem and the number of Platonic solids rest on mathcomp and mathcomp-analysis; translate the Isabelle or HOL Light proofs.
- Abel-Ruffini: follow Lean's AbelRuffini.exists_not_solvable_by_rad (Thomas Browning) or Rocq's Bernard-Cohen-Mahboubi-Strub development.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Freek's page lags the systems (HOL Light's 2026-10-20 additions of Puiseux, CH independence and 4CT were not on it on 2026-10-29); check the system's repository and AFP before starting.
- Isabelle #16 is in active development: Paulson's src/HOL/New_Algebra (Abel_Ruffini.thy, Radical_Extension.thy, Galois_Finite_Correspondence.thy) may finish it in the Isabelle repository before the next release; check it right before claiming.
- The AFP's Projective_Geometry/Pascal_Property.thy (Anthony Bordg) proves that Pascal's property of an abstract projective plane is equivalent to Pappus's property; that is not Pascal's hexagon theorem for conics and does not fill #28.
- AI-assisted autoformalisation is filling cells fast in 2026; re-check right before claiming.
- A weaker statement (special cases, extra hypotheses, a different notion of solvability by radicals) does not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/freek-100-isabelle-hol-light-rocq-metamath-gaps.md
```

Already set up? Say `run V3R1T4S on freek-100-isabelle-hol-light-rocq-metamath-gaps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `freek-100-isabelle-hol-light-rocq-metamath-gaps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
