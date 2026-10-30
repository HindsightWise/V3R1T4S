# Metamath pmproofs.txt: a strictly shorter condensed-detachment proof of a Principia Mathematica theorem

🗜️ **Compression and code golf** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (proof compression and bounded exhaustive search with pmGenerator-style tools; large RAM helps); checking a proof takes milliseconds · open as of 2026-10-30

## The problem

Metamath's 'Shortest known proofs of the propositional calculus theorems from Principia Mathematica' (pmproofs.txt, created by the late Norman Megill) gives D-proofs for the 193 propositional theorems of Principia Mathematica plus Meredith's single axiom, Peirce's axiom and biass: 196 entries in all. A D-proof is a Polish string of condensed-detachment steps over ax-1, ax-2 and ax-3 of Lukasiewicz's P2 system with modus ponens. The latest revision (26-Feb-2025) totals 24,460 steps. In it Samiro Discher found 38 shorter proofs with generative proof compression in pmGenerator 1.2.2, after 40 more in June 2024. Earlier improvers: Gregory Bush (2004), Scott Fenton (2010-13), George Szpiro (2018), Rohan Ridenour (2020) and Discher (2022-23). Proofs of up to 39 steps have been searched exhaustively, so the 68 entries of 39 steps or fewer are optimal. The 128 entries of 43 or more steps remain open. The longest are biass 1579, *5.32 621, *5.7 605, *5.53 551, *5.24 545, *4.38 527, *5.23 501, *5.18 491, *4.86 473 and *4.39 463. Seven entries sit at 43 steps (*2.42, *2.48, *2.51, *2.8, *4.74, *5.12, Peirce). An independent unification checker written for this entry re-derived the stated 'Result of proof' of all 196 entries from their proofs on 2026-10-30.

## What counts as a win

Success means, for one entry of https://us.metamath.org/mmsolitaire/pmproofs.txt (re-fetched live immediately before claiming), a string over {1,2,3,D} that is a well-formed D-proof in the file's Polish notation, STRICTLY SHORTER (direction: min) than the listed proof. Its most general conclusion, computed by condensed detachment with most-general unifiers (premises renamed apart, occurs check), must have that entry's 'Result of proof' formula as a substitution instance (equal up to renaming, or more general). The proof must be accepted by drule.c (us.metamath.org/downloads/drule.c) and by an independent checker. Proofs using other axioms, definitions, lemmas referenced by name or repeated-subproof sharing do not count: the length is the number of characters of the pure D-string.

## Partial wins

- **p1:** For one of the 128 entries with 43 or more steps, a D-proof of exactly the listed length whose most general conclusion is strictly more general than the listed 'Result of proof': the listed formula is a substitution instance of it but not a renaming.

## How a win is checked

Compile drule.c and run it on the single proof (one argument prints the conclusion in Polish notation). Independently, a short Python unifier: parse the D-string recursively, instantiate fresh axiom schemas, unify the antecedent of the major premise with the minor premise, and compare the conclusion against the parsed 'Result of proof' by one-way matching. Then check that the length is smaller than the live entry's step count.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://us.metamath.org/mmsolitaire/pmproofs.txt>

## Sources

- <https://us.metamath.org/mmsolitaire/pmproofs.txt>
- <https://us.metamath.org/mmsolitaire/mms.html>
- <https://us.metamath.org/downloads/drule.c>
- <https://github.com/xamidi/pmGenerator>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Long entries (biass, *5.32, *5.7, *4.38) are built from many lemmas. Re-route them through shorter proofs of the intermediate conclusions and reuse the best known D-subproofs of every formula they contain (the 'shortest proof of each subformula' table idea in pmGenerator).
- Generative compression: enumerate all most-general theorems up to 25-31 steps, index them by conclusion, then replace every subproof in an existing proof by the shortest proof of a formula at least as general.
- Search on the abbreviated forms. Several PM theorems differ only by v, ., = definitions, and a shorter proof of a sibling's result may specialise.
- Use the 2024 note that all proofs up to 39 steps are exhausted: improvements for the 43-step entries would need 41 steps, so target the long tail instead.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Length is the D-string length (odd numbers). Proofs that reuse a subproof by reference are explicitly excluded by the file's 23-Jan-2012 clarification.
- The conclusion must subsume the listed 'Result of proof', which is in the file's ASCII notation with ~ and ->. Parse it, do not eyeball it.
- The live file may have been updated after 26-Feb-2025. Re-fetch it, and check the pmGenerator repository and discussions for unmerged improvements before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/compression-and-golf/metamath-pmproofs-shorter-d-proof.md
```

Already set up? Say `run V3R1T4S on metamath-pmproofs-shorter-d-proof`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `metamath-pmproofs-shorter-d-proof`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
