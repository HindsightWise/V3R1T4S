# Tribone (T_2 stone) tilings of the triangle T_n (Conway-Lagarias, Propp's Problem 20): the next nonzero term A334875(45), unknown since 2020

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours to laptop-days (row transfer matrix on the hexagonal triangle, 128-bit or modular counts) · open as of 2026-10-30

## The problem

Here a tribone, in OEIS A334875's sense, is three mutually adjacent hexagonal cells (the triangle T_2, a 'stone' in Propp's terminology), placed in either orientation. Conway and Lagarias (JCTA 1990) and Thurston proved that T_2 tiles the triangle T_n of hexagons (n cells per side) exactly when n = 12k + 0, 2, 9 or 11. A334875 counts these tilings. It came from a Code Golf challenge by Bubbler (2020); Jonathan Oswald entered it in May 2020 with data to a(44). The nonzero terms are known through a(38) = 3177501183165726091520, and the first unknown term is a(45), followed by a(47) and a(48). James Propp's 'Trimer covers in the triangular grid: twenty mostly open problems' (arXiv:2206.06472, v4 Jan 2024) asks about these numbers as Problem 20, including the observed growth of the power of 2 dividing them. His Benzel Tilings Site lists Problem 20 as open (status of June 2025). Re-fetched 2026-10-30: the DATA ends at a(44) = 0. The Code Golf page itself shows a bot check (BLOCKED), so the OEIS entry is the status source.

## What counts as a win

The exact integer A334875(45), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, using a different sweep direction or state encoding with exact or multi-prime arithmetic. The same code must reproduce every published term a(0)..a(44), zeros included.

## Partial wins

- **p1:** A334875(47) or a(48) after a(45), under the same two-run rule.
- **p2:** Exact tribone tiling counts for every n <= 44 reproduced by a second, independently written program using a different algorithm (for example a transfer matrix vs the published recursive Python), with run times reported.

## How a win is checked

Skeptic: run the short Python program in the OEIS entry for n <= 15 and compare with the claimant's code. Then rerun the claimant's code for n = 45 modulo a fresh prime or with exact integers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A334875>

## Sources

- <https://oeis.org/A334875>
- <https://doi.org/10.1016/0097-3165(90)90057-4>
- <https://arxiv.org/abs/2206.06472>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sweep the triangle row by row. Each cell of the profile records whether it is covered and, for a tribone sticking out, how many more cells it needs along its direction.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offset 0. Most terms are 0 by Conway-Lagarias, so 'the next term' means the next n = 12k + 0, 2, 9 or 11, i.e. 45.
- The tile is the 3-cell triangle (both orientations), not three collinear hexagons: straight trimers never tile T_n. Reproduce a(9) = 2 and a(11) = 8 first.
- A377309 (stones-and-bones tilings of T_n, Propp 2024) is a different sequence.
- a(45) may exceed 2^64; use 128-bit, modular or exact arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/tribone-tilings-triangle-a334875-n45.md
```

Already set up? Say `run V3R1T4S on tribone-tilings-triangle-a334875-n45`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tribone-tilings-triangle-a334875-n45`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
