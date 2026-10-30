# Number of legal chess positions: a provable upper bound well below Tromp's 8.7279e45 ranking

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-hours (exact combinatorial counting); validation runs on sampled positions are laptop-minutes · open as of 2026-10-30

## The problem

John Tromp's ChessPositionRanking (GitHub) defines an invertible ranking of 'urpositions', a computable superset of all legal chess positions (placement, side to move, castling rights, en passant). Its size is the best known rigorous upper bound on the number of legal positions. The README still gives N = 8726713169886222032347729969256422370854716254. On 2026-08-11 Michael Spece (GitHub MichaelSpece) reported a legal en-passant position that the ranking misses (issue #927, which Tromp accepted as the winning $256 bug report) and a related multiplicity error (#928). In a #927 comment of 2026-09-09 Tromp gave a fix that raises the size to 8727878536878208144190883427864082859392620550 (about 8.7279e45, 1.00013 times the old N). A commit 'fix incorrect ep counts bug' to src/CountChess.hs followed on 2026-09-29, and both issues were still open on 2026-10-30. Earlier bounds: Chinchalkar 1.77894e46 (1996), Allis 5e52 (1994). Tromp and Peter Osterlund (Texel proof-game engine) estimate the true count from 2 million random urpositions at (4.822 +- 0.028) x 10^44 (95% confidence), so the bound is about 18 times too large. The README notes that the ranking allows adjacent kings and that excluding them would gain only about 10%. In the initial classification of the 1M sample, 492,045 urpositions have both kings in check and 173,401 have the side not to move in check. Tromp writes that there is no hope of ever determining the exact number. Checked 2026-10-30: README, issues #927/#928 and the commit history read; no smaller rigorous bound found.

## What counts as a win

CONFIRMED: an exact integer U <= 4.0 x 10^45, together with (a) a precise definition of a set S of positions and the exact count |S| = U, computed by released counting code and recomputed exactly by an independently written counter, and (b) a written proof that every legal chess position (Labelle/Tromp definition: placement, side to move, castling rights, e.p. square only when an e.p. capture is legal) lies in S, where every excluded class is excluded by a stated, proven necessary condition for legality, and S has a membership test that accepts every certified-legal position in the validation set below. The bound must be strictly below the smallest rigorous bound published at verification time (8727878536878208144190883427864082859392620550 as of 2026-10-30).

## Partial wins

- **p1:** Any rigorous upper bound strictly below 8727878536878208144190883427864082859392620550 (for example by also excluding adjacent kings), meeting conditions (a) and (b) of the success criterion.
- **p2:** An independent exact recomputation of the post-fix size 8727878536878208144190883427864082859392620550 (or a demonstrated arithmetic error in it) by counting code that shares nothing with CountChess.hs. Legal but unrankable positions or wrong multiplicities fall under Tromp's bug bounties (held), not here.
- **p3:** A new estimate of the number of legal positions with a 95% half-width below 1.0e42 (current 2.75e42), from a sample whose seed was fixed in advance and published, where each legal sample position has a replayable proof game and each illegal one a reproducible illegality certificate; any unresolved position is counted as legal for the upper end and illegal for the lower end.

## How a win is checked

Run both counters and compare the exact integers. Check each exclusion rule's legality proof. Run the membership test on (i) the 112,754 legal urpositions with proof games in Tromp's Texel.out.* files, (ii) one million positions from random legal games (random moves, 1% stop chance per move, as in the README), including en-passant and castling edge cases such as the #927/#928 FENs. Every position must be accepted. For p3, replay every proof game with an independent legal-move generator, and recompute the estimator with Tromp's estimate.pl formula.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/tromp/ChessPositionRanking>

## Sources

- <https://github.com/tromp/ChessPositionRanking>
- <https://github.com/tromp/ChessPositionRanking/issues/927>
- <https://github.com/tromp/ChessPositionRanking/issues/928>
- <https://github.com/tromp/ChessPositionRanking/blob/main/src/CountChess.hs>
- <https://en.wikipedia.org/wiki/Shannon_number>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exclude 'side not to move is in check' exactly: for a fixed king square and attacker set, count arrangements with blocked rays by inclusion-exclusion over attacking lines; it removes the two largest illegal classes (66% of urpositions).
- Adjacent kings: condition the placement on the pair of king squares (3612 legal king pairs instead of 4032).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The README number is the pre-fix ranking, which missed legal en-passant positions; quote the post-fix value or a newer one.
- En passant, castling and promotions (up to 12 with 4 captures) are where supersets silently lose legal positions; test them explicitly.
- Tromp offers bug bounties on the ranking itself; those are a separate setter challenge (see held), not this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/chess-legal-positions-upper-bound.md
```

Already set up? Say `run V3R1T4S on chess-legal-positions-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chess-legal-positions-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
