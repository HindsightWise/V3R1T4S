# MOONSHOT - The tenth Dedekind number D(10) (OEIS A000372(10)) or inequivalent monotone Boolean functions of 10 variables (A003182(10))

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (D(9) took FPGA supercomputing; D(10) is many orders of magnitude beyond) · open as of 2026-10-30

## The problem

Dedekind numbers count monotone Boolean functions (antichains of subsets) of n variables. D(8) came from Wiedemann (1991). D(9) = 286386577668298411128469151667598498812366 was computed independently in 2023 by Christian Jaekel (J. Comput. Algebra) and by Lennart Van Hirtum, Patrick De Causmaecker et al. (FPGA supercomputing, arXiv 2304.03039). Inequivalent monotone functions A003182 reached n = 9 through Bartlomiej Pawelski (2023). Alex Fihman, Lennart Van Hirtum and Christian Plessl (arXiv 2607.08446, July 2026) estimate D(10) to about 4 significant digits; no exact value exists. OEIS checked live 2026-10-30: A000372 and A003182 end at n = 9, keyword 'more', no pending drafts.

## What counts as a win

Success means the exact integer D(10) = A000372(10), or the exact A003182(10). It must be computed by two independent methods that agree exactly: a different decomposition (for example interval-based vs pair-matching formula) and different arithmetic. The code must reproduce D(0..9), respectively A003182(0..9). The value must be consistent with every published congruence (Pawelski-Szepietowski). As a sanity check, it is also compared with Fihman-Van Hirtum-Plessl's 4-digit estimate.

## Partial wins

- **p1:** D(10) modulo a prime or prime power not determined by published congruences (Pawelski-Szepietowski, arXiv 2302.04615). Two independent implementations must agree and must also reproduce D(9) modulo the same number.

## How a win is checked

Skeptic: rerun the claimant's code at n = 7, 8 (minutes) and n = 9 modulo a small prime; recompute the claimed residue for n = 10 with an independent implementation; for a full claim compare several modular residues from independent runs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000372>

## Sources

- <https://oeis.org/A000372>
- <https://oeis.org/A003182>
- <https://arxiv.org/abs/2304.00895>
- <https://arxiv.org/abs/2304.03039>
- <https://arxiv.org/abs/2607.08446>
- <https://arxiv.org/abs/2302.04615>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The parity and some other residues of D(n) follow from known congruences; a residue implied by Pawelski-Szepietowski is not a new partial.
- A000372 counts all monotone functions, including the two constants; A003182 counts orbits under variable permutations.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/dedekind-number-d10.md
```

Already set up? Say `run V3R1T4S on dedekind-number-d10`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dedekind-number-d10`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
