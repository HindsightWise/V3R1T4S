# Polycubes: the number of 23-cell polycubes (next term of OEIS A001931 fixed and A000162 / A038119 free, open since Phillip Thompson's n = 22 in 2024)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (or many laptop-weeks: about 2.4e18 fixed polycubes at n = 23 with a Redelmeier-type counter; symmetric classes are far cheaper) · open as of 2026-10-30

## The problem

Fixed polycubes are face-connected sets of n unit cubes up to translation: simple-cubic lattice animals, OEIS A001931. Free polycubes are A000162 (rotations only) and A038119 (rotations and reflections). Earlier terms came from Redelmeier, Lunnon, Mertens (1990), Aleksandrowicz and Barequet (2006), and Luther and Mertens (2011). Stanley Dodds computed a(20) in Aug 2023 with a streamlined Redelmeier implementation in C#, now on OEIS with comments by Guenter Rote. Phillip Thompson's Rust port of Dodds's algorithm gave a(21) and a(22) = 306405169166373418 (Feb 2024; the n = 22 run took about 10 days on a 64-thread machine). The free counts reach n = 22 too: A000162 from Dodds and Thompson, A038119 extended by John Mason (2024). John Mason's per-symmetry-class sequences (A376964-A377131, Oct 2024) reach n = 22 for most classes and further for a few (e.g., class A, A376965, to n = 24). OEIS checked live 2026-10-30: all three sequences end at n = 22 (data field only, no separate b-file), all three carry keyword 'more', and there are no pending drafts. The higher-dimensional lattice-animal entry of the bank covers d >= 4; this target is the 3D cubic lattice only.

## What counts as a win

Success means the exact value of a(23) of A001931 (fixed), or of A000162 or A038119 at n = 23 (free, which also needs the symmetric-polycube counts at 23), with N re-read from the live b-files before claiming. The value must be computed by two independent programs, or by one program plus an independent check of a stated partition of the count (for example by the first growth steps or by bounding-box class) recomputed separately, and they must agree exactly. The same code must reproduce every published term for n <= 22.

## Partial wins

- **p1:** The number of 23-cell polycubes with a nontrivial rotational symmetry (the correction term needed to pass from A001931(23) to A000162(23)), by two methods that agree and reproduce the published symmetric data for n <= 22.
- **p2:** An exact count of 23-cell fixed polycubes inside a stated bounded box class (for example all with bounding-box height at most 3), computed by two methods, presented as a certified lower bound.

## How a win is checked

Skeptic: rerun the claimant's code for n <= 18 (minutes) against the b-file; recompute several randomly chosen subtrees of the Redelmeier search (or bounding-box classes) for n = 23 and compare subtotals; check the growth ratio a(23)/a(22) against the trend (about 7.8).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001931>

## Sources

- <https://oeis.org/A001931>
- <https://oeis.org/A000162>
- <https://oeis.org/A038119>
- <https://arxiv.org/abs/1106.1078>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A000162 identifies rotations only (mirror pairs counted twice); A038119 also identifies reflections. Do not mix them.
- 64-bit overflow: a(23) is about 2.4e18, within a factor of 4 of the signed 64-bit limit (about 9.2e18). Any weighted subtotal (symmetry multipliers, Burnside weights such as 24 or 48 times a class count) can overflow; use 128-bit or checked accumulators.
- Stephen Pursey (2026) corrected some published polycube-with-cavity counts; check that the sub-counts you rely on are the corrected ones.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/polycubes-3d-next-term-n23.md
```

Already set up? Say `run V3R1T4S on polycubes-3d-next-term-n23`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `polycubes-3d-next-term-n23`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
