# Normal-play Sprouts: settle the 63-spot game or another open n <= 105 (SPOTS frontier, 2026)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (SPOTS solved its hardest position in 24 days on 512 cores; n = 0 or 3 mod 6 are the hardest classes); a proof checker is laptop-hours · open as of 2026-10-30

## The problem

Sprouts (Conway and Paterson, 1967) starts with n spots in the plane. A move joins two spots (or a spot to itself) with a curve that crosses nothing and puts a new spot on it; no spot may have more than 3 lines. In normal play the last player to move wins. Conway, Mollison and Applegate, Jacobson and Sleator (1991) settled n <= 11, Purinton n = 12-14 (2006), and Lemoine and Viennot's Glop (2007-2011) all n <= 44 plus 46, 47 and 53. In 2025-2026 Cizek, Balko and Schmid's massively parallel proof-number solver SPOTS (arXiv:2511.10339, v2 9 Feb 2026, AAAI 2026; code github.com/cizektom/spots) added 42 outcomes: all n <= 62 and the 27 least complex cases with 63 <= n <= 104, 89 known in all. The 32 outcomes from its sequential solver were fully verified with Lemoine and Viennot's procedure; the README says the 10 from the parallel solver could not be fully verified and were only spot-checked on simpler positions. Wikipedia's Sprouts table and Table 2 of the paper (re-read 2026-10-30) still leave 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 101, 102 and 105 unknown. The Sprouts conjecture (the first player wins exactly when n = 3, 4 or 5 mod 6) predicts wins at 63, 69, ..., 99, 101 and 105 and losses at 66, 72, ..., 102. Lemoine and Viennot's extended conjecture says the n-spot Grundy number is 0 for n = 0, 1, 2 mod 6 and 1 otherwise. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem C2) still asks for the analysis to be extended. Settle any one open n.

## What counts as a win

CONFIRMED: the normal-play outcome (first-player win or loss) of the n-spot starting position in the plane, for one n that is unknown at verification time in Wikipedia's Sprouts table and in the SPOTS repository and paper (on 2026-10-30: 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 101, 102, 105), with both of the following. (1) A certificate (a solution tree, or a database of proven Grundy numbers in a documented format as SPOTS publishes) accepted by a checker that shares no code with the solver. The checker regenerates the full child list at every node where all children must be refuted, and recomputes every Grundy-number or land-splitting reduction it uses. (2) The outcome reproduced by a second, independent program (for example Lemoine and Viennot's verifier, or Glop/SPOTS run on the certificate). An outcome that contradicts the Sprouts conjecture is an equally full win.

## Partial wins

- **p1:** The first fully independent re-verification of one of the ten outcomes obtained only by parallel SPOTS, which the SPOTS README says could not be fully verified (shaded in Table 2 of arXiv:2511.10339v2; they appear to be the ten entries with proof size 1e9: n = 57, 60, 89, 94, 95, 97, 98, 100, 103, 104). The checker shares no code with SPOTS or Glop, walks the published certificate with its own move generator and agrees with the published outcome; a demonstration that one of these outcomes is wrong also counts.

## How a win is checked

Write an independent Sprouts move generator in Lemoine-Viennot string notation. Test it by reproducing the outcomes for n <= 14 from scratch, and compare child counts of random small positions against Glop or SPOTS. Then walk the certificate: at each node where the player to move must lose, regenerate every child and check that each is a proven win; at each winning node, check that the named child is legal and proven lost. Recompute any Grundy number used to replace a land (normal-play Sprague-Grundy sums are valid). Finally, confirm the outcome with a second program and check that n is still listed as unknown.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Sprouts_(game)>

## Sources

- <https://en.wikipedia.org/wiki/Sprouts_(game)>
- <https://arxiv.org/abs/2511.10339>
- <https://github.com/cizektom/spots>
- <http://sprouts.tuxfamily.org/wiki/doku.php?id=records>
- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Odd n = 5 mod 6 such as 101 needs only one proven-losing child at the root. Try first the child that links one spot to itself and splits the rest into two equal regions, the move that worked for earlier refutations.
- Warm-start from the SPOTS Grundy-number databases, so every land already solved for n <= 104 costs nothing.
- SPOTS reports that n = 3 mod 6 positions are the most complex. Among the open cases, the 0 mod 6 losses (66, 72, ...) need every root child refuted: order the children by Lemoine-Viennot 'lives' and share a transposition table.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Normal play only: Grundy-number reductions are valid here but not in the misere game (misere-sprouts-21-spots is a separate target).
- The Glop records page lags behind SPOTS; use Wikipedia's table and the SPOTS repository as the authority for which n are open.
- A single solver run proves nothing, because a move-generator bug gives a wrong outcome. Two independent implementations are required.
- Crowding: the SPOTS team is actively extending these results. Re-check arXiv and the repository before and after a run.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/sprouts-normal-play-63-spots.md
```

Already set up? Say `run V3R1T4S on sprouts-normal-play-63-spots`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sprouts-normal-play-63-spots`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
