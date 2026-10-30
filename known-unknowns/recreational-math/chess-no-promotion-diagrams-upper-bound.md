# Legal chess diagrams without promotion: beat Gourion's upper bound of 3.7422e37

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (Gourion's 25-men cases took up to 1.6 hours each in MatLab on a desktop) · open as of 2026-10-30

## The problem

A diagram is the contents of the 64 squares (no side to move, castling or e.p.). How many diagrams can be reached in a legal game with no promotion? Shannon's rough count was 64!/(32!(8!)^2(2!)^6), about 4.63e42. Stefan Steinerberger (Int. J. Game Theory 44, 2015) proved an upper bound of about 1.53e40 (2e40 in Gourion's abstract). Tromp's ChessPositionRanking README improves this to 2891398339895958031893456691621753206624 (about 2.9e39) by limiting unopposed pawns. Daniel Gourion (ICGA Journal, DOI 10.3233/ICG-220210, 2022; arXiv:2112.09386v2, revised 16 January 2025) reached 3.7422... x 10^37, using a graph on capture quadruplets and classes of legal pawn arrangements; his MatLab code is at github.com/DanielGourion/ChessDiagrams. He conjectures the true count lies between 1e37 and 3.5e37, probably close to 3e37. He names two possible gains: forbidding adjacent kings also for 24 or more men (about 10%; he already does so for 23 or fewer), and better bishop counting (his method loses up to 13% in the worst case). Checked 2026-10-30: arXiv v2 (2025) is the latest version, and Wikipedia's Shannon number article still gives 4e37 (Steinerberger, Gourion) as the upper bound for positions without promotion.

## What counts as a win

CONFIRMED: an exact integer or rigorous decimal upper bound U <= 3.5 x 10^37 on the number of legal chess diagrams reachable without promotion (Gourion's definition), with (a) released counting code whose result an independently written counter reproduces exactly, and (b) a proof that every excluded diagram is illegal without promotion. A membership test of the counted superset must accept every diagram in the validation set described under verification_method. The bound must also be strictly below the smallest bound published at verification time (Gourion's 3.7422... x 10^37 as of 2026-10-30).

## Partial wins

- **p1:** An independent recomputation of Gourion's per-men upper bounds for 24 to 32 men (his Table 4, for example 4.93e32 at 32 men and 1.08e37 at 26 men) to the printed digits, by code that shares nothing with his MatLab repository, or a demonstration of an error in one of them.
- **p2:** A sampled estimate of the number of legal diagrams without promotion with a 95% confidence half-width below 10% of the estimate, from a published-seed sample of an exactly rankable superset, where legal sample diagrams carry replayable promotion-free proof games and unresolved ones are counted both ways.
- **p3:** Any rigorous upper bound strictly below 3.7422 x 10^37 (for example by removing illegal pawn-arrangement classes of the kind Gourion describes in his section 5.1), meeting conditions (a) and (b) of the success criterion and the membership test, and below any smaller bound published at verification time.

## How a win is checked

Recompute the claimed bound with both counters and compare. Check the illegality proof of each added exclusion. Generate one million diagrams from random promotion-free legal games, plus every diagram along those games, and confirm the claimant's superset membership test accepts all of them. For p2, replay each proof game with an independent move generator, check that no promotion occurs, and recompute the estimator.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.09386>

## Sources

- <https://arxiv.org/abs/2112.09386>
- <https://github.com/DanielGourion/ChessDiagrams>
- <https://link.springer.com/article/10.1007/s00182-014-0453-7>
- <https://github.com/tromp/ChessPositionRanking>
- <https://en.wikipedia.org/wiki/Shannon_number>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend the adjacent-kings exclusion to 24 or more men by conditioning on the king pair before placing the other pieces.
- Use exact counting of bishops on each colour per class instead of Gourion's worst-case bishop handling.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'Without promotion' means reachable by a game with no promotion. Counting all diagrams that merely contain no extra pieces is a different set.
- Diagrams are not positions: do not compare with Tromp's position counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/chess-no-promotion-diagrams-upper-bound.md
```

Already set up? Say `run V3R1T4S on chess-no-promotion-diagrams-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chess-no-promotion-diagrams-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
