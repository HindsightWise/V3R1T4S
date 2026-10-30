# KnotInfo Turaev genus: a Turaev-genus-1 diagram for one of the 25 non-alternating knots (11n_118 and 24 at 12 crossings) listed [1,2]

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

For a diagram D with c crossings whose all-A and all-B smoothings have s_A and s_B circles, the Turaev surface has genus g_T(D) = (2 + c - s_A - s_B)/2. The Turaev genus of K is the minimum over diagrams, and it is 0 exactly for alternating knots. KnotInfo (Livingston and Moore) records it from several sources: Abe-Kishimoto (arXiv:0808.0573) for non-alternating knots under 12 crossings (except 11n_95 and 11n_118), Jablan's 154 almost-alternating 12-crossing knots (arXiv:1404.4967), Howie's unpublished bound of 2 for the rest, and Dasbach-Lowrance's genus-2 results (arXiv:1604.03501), with lower bounds from Khovanov and knot Floer width (Manturov, Lowrance). In database_knotinfo 2026.10.5, 25 knots are [1,2]: 11n_118 and 12n_285, 12n_318, 12n_328, 12n_358, 12n_370, 12n_371, 12n_407, 12n_426, 12n_439, 12n_443, 12n_451, 12n_462, 12n_487, 12n_488, 12n_591, 12n_730, 12n_749, 12n_750, 12n_801, 12n_807, 12n_809, 12n_830, 12n_835 and 12n_838. Non-alternating knots have g_T >= 1, so a Turaev-genus-1 diagram of any of them closes it at 1.

## What counts as a win

For a knot K whose turaev_genus is [1,2] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a PD code D (of any crossing number) that SnapPy and Regina identify as K (mirror allowed), with g_T(D) = (2 + c(D) - s_A(D) - s_B(D))/2 = 1, where s_A and s_B are the numbers of circles in the all-A and all-B Kauffman states, computed by the skeptic.

## Partial wins

- **p1:** For one of the 25 knots, a reproducible computation showing that it meets the hypotheses of a published theorem implying Turaev genus >= 2: for example Khovanov width at least 4 (g_T >= w_Kh - 2, Manturov / Champanerkar-Kofman-Stoltzfus), knot Floer width at least 3 (g_T >= w_HF - 1, Lowrance arXiv:0709.0720), or a Turaev-genus-one obstruction from Dasbach-Lowrance (arXiv:1604.03501). It counts only if neither KnotInfo nor any paper the skeptic finds has already applied that theorem to K, and it must name the theorem and save every input, with each invariant recomputed from a verified diagram.
- **p2:** An almost-alternating diagram (one crossing change from alternating) verified as one of the 25 knots. This implies g_T = 1 and is reported separately because almost-alternating status is of independent interest.

## How a win is checked

Skeptic identifies D as K with SnapPy/Regina and counts the all-A and all-B state circles in D directly from the PD code. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/turaev_genus.html>

## Sources

- <https://knotinfo.org/descriptions/turaev_genus.html>
- <https://arxiv.org/abs/1604.03501>
- <https://arxiv.org/abs/1404.4967>
- <https://arxiv.org/abs/0808.0573>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: random Reidemeister and flype walks that increase the crossing number, evaluating g_T(D) on each diagram (minimisers need not be minimal-crossing).
- Conventional: build almost-alternating and Turaev-genus-1 diagrams from Dasbach-Lowrance's classification of Turaev genus one diagrams, and match them by HOMFLY before identifying.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The KnotInfo description text says Jablan's work leaves 37 knots without values (before Dasbach-Lowrance's genus-2 results), while the 2026.10.5 data has 25 [1,2] entries. Go by the live data entry.
- Identify the diagram with SnapPy/Regina, not by Jones or HOMFLY alone (12-crossing knots share polynomials).
- Some of these knots may genuinely have g_T = 2. Check for 2024-2026 preprints on Turaev genus of 12-crossing knots before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-turaev-genus-twelve-crossing.md
```

Already set up? Say `run V3R1T4S on knotinfo-turaev-genus-twelve-crossing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-turaev-genus-twelve-crossing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
