# Condorcet dimension 4: an election in which no three candidates form a Condorcet winning set (refutes Charikar et al. Conjecture 1)

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for SAT or local search over profiles; checking a claimed profile takes seconds (C(m,3) committees times m candidates times n voters) · open as of 2026-10-30

## The problem

In an election with n voters holding strict rankings of m candidates, a committee W is a Condorcet winning set (Elkind, Lang and Saffidine 2015) if, for every candidate c outside W, fewer than half of the voters rank c above every member of W. The Condorcet dimension is the size of the smallest such set. Elkind-Lang-Saffidine built elections of dimension 3 (Kronecker products of cyclic profiles), and Geist (arXiv:1402.4303, SAT search) found a minimal one with 6 voters and 6 candidates, but found nothing of dimension 4. Charikar, Lassota, Ramakrishnan, Vetta and Wang (arXiv:2411.03390) proved every election has dimension at most 6. Song, Nguyen and Lin (arXiv:2506.22133, v2 30 Jun 2025) lowered this to 5, and Charikar, Ramakrishnan and Wang wrote an exposition (arXiv:2606.14666). Charikar et al.'s Conjecture 1 says alpha-undominated committees of size k exist whenever alpha >= 2/(k+1). That would make 3 the maximum dimension. Epoch AI lists the dimension-4 question as unsolved (FrontierMath Open Problems, social choice). An arXiv search on 2026-10-30 found only restricted results: dimension at most 3 for planar l1 and l-infinity elections (arXiv:2608.27653) and at most 4 for planar l2. No dimension-4 profile has been published.

## What counts as a win

An explicit election: n lines, each a permutation of 1..m with m >= 4. For EVERY 3-element committee S there must be a candidate c not in S such that the number of voters ranking c above all three members of S is at least n/2, and the claimant must list that c for each S. This is the Elkind-Lang-Saffidine definition that Charikar et al. and the Epoch page use. Odd n is preferred, because then 'at least n/2' and 'a strict majority' coincide. With even n the claim must also state whether every overthrowing count is strictly above n/2. Supersets of winning sets are winning, so checking every 3-set settles that no set of size <= 3 wins. Direction: the existence of such a profile is the win. Before claiming, re-fetch the status source and arXiv; a published dimension-4 example dated earlier makes the claim a reproduction.

## Partial wins

- **p1:** Refute Conjecture 1 of arXiv:2411.03390 at k = 2: an explicit election in which every 2-element committee S has an outside candidate c ranked above both members of S by at least 2n/3 voters. Then no 2/3-undominated pair exists.
- **p2:** Refute Conjecture 1 at k = 4: an explicit election in which every 4-element committee S has an outside candidate ranked above all of S by at least 2n/5 voters.

## How a win is checked

Standard-library Python. Parse the rankings and check each line is a permutation of 1..m. For each voter precompute the position of each candidate. For every k-subset S (k = 3 for the full win, 2 or 4 for p1 and p2) and every c not in S, count the voters with pos(c) < min over s in S of pos(s). Compare the best count with the threshold using exact integer arithmetic: 2*count >= n for k = 3, 3*count >= 2n for k = 2, 5*count >= 2n for k = 4. Run negative controls first: Geist's 6x6 dimension-3 profile must show a winning 3-set, and the cyclic profile on 3 candidates must have dimension 2. Then re-fetch the Epoch page and the arXiv listings for 2411.03390 and 2506.22133.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://epoch.ai/frontiermath/open-problems/condorcet-winning-sets>

## Sources

- <https://epoch.ai/frontiermath/open-problems/condorcet-winning-sets>
- <https://arxiv.org/abs/2411.03390>
- <https://arxiv.org/abs/2506.22133>
- <https://arxiv.org/abs/2606.14666>
- <https://arxiv.org/abs/1402.4303>
- <https://arxiv.org/abs/2608.27653>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Kronecker and lexicographic products of cyclic profiles give dimension 3. Search products of three cyclic or tournament-derived profiles, then repair them locally with an exact objective: the number of 3-sets that still win.
- SAT/MaxSAT with voter types as variables, in the style of Geist's encoding, with the candidate count fixed at 8-12 and weighted voter types instead of individual voters.
- Charikar et al. tie the question to dominating sets in tournaments of high girth (their Question 2). Tournaments with no small dominating set are a source of candidate structures.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Elections with no winning set of size 2 are known (dimension 3). Do not claim those.
- With an even number of voters an overthrow at exactly n/2 is enough under the stated definition. A profile that only works through such ties is weaker, so report it as such.
- Planar l1, l-infinity and one-dimensional Euclidean elections are proven to have dimension <= 3. Do not search there.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/condorcet-dimension-four-profile.md
```

Already set up? Say `run V3R1T4S on condorcet-dimension-four-profile`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `condorcet-dimension-four-profile`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
