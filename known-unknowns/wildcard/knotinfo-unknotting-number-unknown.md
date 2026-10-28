# KnotInfo: determine an unknotting number currently listed as an interval

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

KnotInfo (Charles Livingston and Allison Moore, knotinfo.org) lists unknotting numbers of prime knots up to 13 crossings. In database_knotinfo 2026.10.5 (the monthly mirror, released 2026-10-05), 4,991 of them are intervals: 10 with 10 crossings, 65 with 11, 548 with 12 and 4,368 with 13. The most common are [1,2] (2,577), [2,3] (1,607), [1,3] (416) and [3,4] (271), e.g. 10_6, 10_11 and 10_47 at [2,3]. Upper bounds come from explicit crossing-change sequences (Jablan-Sazdanović, Brittenham-Hermiller). Lower bounds come from signatures, Heegaard Floer obstructions, and the results of McCoy and Owens as applied by Kawano and Gebel-Pragley. KnotInfo's unknotting-number page says that Dranowski, Kabkov and Tubbenhauer (arXiv:2603.07955, 'RL unknotter, hard unknots and unknotting number', v4 2026-09-09) found new upper bounds on many unknotting numbers, and that 'This work is pending and the results are not installed.' Applebaum et al. (arXiv:2409.09032) also report reinforcement-learning upper bounds. Can an explicit unknotting sequence close an interval, or lower an upper bound below every published one?

## What counts as a win

For a knot K whose unknotting_number is an interval [a,b] in the live KnotInfo database (https://knotinfo.org/, or its database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a saved planar diagram code D of K, verified as K by SnapPy/Regina identification (mirror image and orientation handled), and a set of c crossings of D whose change gives a diagram that Regina's unknot recognition certifies as the unknot, where c is STRICTLY LESS (direction: min) than b and than every upper bound for K published in arXiv:2603.07955, arXiv:2409.09032 or any other source the skeptic finds. c = a closes the interval.

## Partial wins

- **p1:** Lower the KnotInfo upper bound b by at least 1 for an interval-valued knot (c < b) with the same certificate, even if c > a and even if a pending published result already matches c (say which).
- **p2:** For a knot listed as [1,2], a single crossing change in some diagram (not necessarily minimal) that Regina certifies yields the unknot. This closes the entry at 1, and is reported separately because it needs no published-bound comparison beyond KnotInfo and the two arXiv papers.
- **p3:** A demonstrated KnotInfo data inconsistency: a certified computation (e.g. |signature|/2, computed reproducibly in SnapPy or Sage from a verified diagram) that exceeds a listed upper bound, or a certified crossing-change sequence shorter than a listed lower bound, with the inputs saved.

## How a win is checked

Skeptic loads D in SnapPy/Regina, confirms identification as K (isometry of hyperbolic exteriors or Regina knot signature), applies the listed crossing changes, and runs Regina's unknot recognition. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/>

## Sources

- <https://knotinfo.org/>
- <https://knotinfo.org/descriptions/unknotting_number.html>
- <https://github.com/soehms/database_knotinfo>
- <https://pypi.org/project/database-knotinfo/>
- <https://arxiv.org/abs/2603.07955>
- <https://arxiv.org/abs/2409.09032>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: randomised Reidemeister-move diagram exploration (increase crossings, then search all crossing-change subsets) as in Brittenham-Hermiller.
- Conventional: crossing changes to a known knot with known u (u(K) <= 1 + u(K')) using KnotInfo's own table for K'.
- Cross-domain import (reinforcement learning / game search): MCTS over Reidemeister moves + crossing changes with a cheap value function (signature, determinant, hyperbolic volume).
- Cross-domain import (chemistry / molecular dynamics): simulate the knot as a polymer under energy minimisation (KnotPlot-like) to find simplifying diagrams.
- Cross-domain import (computer vision hashing): canonical diagram hashing to deduplicate the search space.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Diagram identification errors: mirror images and orientation matter for some invariants; verify the knot type with Regina/SnapPy, not by invariants alone.
- Pending published results (Dranowski-Kabkov-Tubbenhauer, arXiv:2603.07955; Applebaum et al., arXiv:2409.09032) may already match or beat your bound; the KnotInfo page says the former are not installed, so check the papers and their data before claiming.
- An upper bound equal to the listed lower bound is a win; an upper bound equal to the listed upper bound is not.
- Do not email KnotInfo maintainers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-unknotting-number-unknown.md
```

Already set up? Say `run V3R1T4S on knotinfo-unknotting-number-unknown`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-unknotting-number-unknown`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
