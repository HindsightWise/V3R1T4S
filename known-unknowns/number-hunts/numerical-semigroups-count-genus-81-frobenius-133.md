# Numerical semigroups: the next exact count by genus (n_81, OEIS A007323) or by Frobenius number (N_133, OEIS A124506)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (n_81: about 1.6 x the 231,300 core-hours Bras-Amoros and Torra spent on n_80; N_133 is far cheaper but still roughly double N_131, which took almost 115 hours in their cluster runs) · open as of 2026-10-30

## The problem

n_g counts the numerical semigroups of genus g (OEIS A007323). N_F counts those with Frobenius number F (A124506). Maria Bras-Amoros and Vicenc Torra (arXiv 2607.23111, v3 10 Sep 2026) ran the seeds algorithm on genus- and Frobenius-leaf-discriminating trees, which are pruned so that their leaves are exactly the objects counted. They obtained n_78, n_79 and n_80 = 199583757387067387, using 231,300 core-hours on the Kebnekaise and Tetralith clusters. They also got N_F for every F <= 132 (N_132 = 92876546429911575576; N_131 took about 115 hours) and irreducible-semigroup counts up to F = 132. They prove a closed formula for the semigroups with m >= (F+1)/3, so only small-multiplicity nodes need exploring. Earlier records: Fromentin and Hivert (to 70, github hivert/NumericMonoid), Fernandez-Gonzalez and Bras-Amoros (71-72), Delgado, Eliahou and Fromentin (73-75, 2023), and Bras-Amoros's unleaved tree (76-77, 2025). Martin Fuller computed A124506 terms 40-100. Both OEIS b-files, re-fetched 2026-10-30, stop at g = 80 and F = 132. A new term also extends the checked range of Bras-Amoros's conjectured Fibonacci-like growth n_g >= n_{g-1} + n_{g-2}. The same holds for monotonicity n_{g+1} >= n_g, which Zhai proved only for large g.

## What counts as a win

Success means the exact value of A007323(81) or A124506(133), or a later term: the first index beyond the live b-file, re-fetched immediately before claiming. Two independent methods or independently written codes must agree exactly, for example a seeds/leaf-discriminating-tree count against a Kunz-coordinate or Fromentin-Hivert decomposition count. The code must reproduce every published term for g <= 60 (resp. F <= 110) and the Bras-Amoros-Torra per-multiplicity decomposition wherever they publish it. The per-work-unit counts (split by multiplicity and first jumps) must be published so a skeptic can recompute random units. A literature search must find no earlier value.

## Partial wins

- **p1:** The number of irreducible numerical semigroups with Frobenius number 133 (OEIS A158206; Bras-Amoros and Torra 2026 report them through F = 132). Because 133 is odd, these are exactly the symmetric numerical semigroups with F = 133 (genus 67). The value must come from code that reproduces the published A158206 values for a contiguous range of F ending at 132, and a second, independently written code using a different method (for example a direct enumeration of symmetric semigroups through Kunz coordinates or Apery sets) must agree exactly.
- **p2:** An independent recomputation of n_78, n_79 or n_80 by a different algorithm and code, agreeing exactly with Bras-Amoros and Torra's value (each of these terms has a single published computation). A confirmed discrepancy would be a major finding and needs a third run.

## How a win is checked

Rerun the claimant's code for small g/F (seconds to minutes) and compare with the b-files. Recompute a random sample of the published work units (multiplicity / first-jumps splits) with independent code and check that the partial sums match. Sum the units and compare with the claim. Check the Bras-Amoros-Torra closed formula for the m >= (F+1)/3 part independently.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A007323/b007323.txt>

## Sources

- <https://oeis.org/A007323>
- <https://oeis.org/A007323/b007323.txt>
- <https://oeis.org/A124506>
- <https://oeis.org/A124506/b124506.txt>
- <https://arxiv.org/abs/2607.23111>
- <https://arxiv.org/abs/2503.14664>
- <https://arxiv.org/abs/2310.07742>
- <https://github.com/hivert/NumericMonoid>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Count the m >= (F+1)/3 part by the Bras-Amoros-Torra formula and enumerate only the small-multiplicity remainder; the Frobenius tree explores about 0.03% of the full tree.
- Use Fromentin-Hivert's SIMD decomposition representation with 192/256-bit gap masks (the 64-bit limit is what stopped earlier codes).
- Kunz-coordinate counting (Bernardini; Kaplan) for fixed multiplicity as an independent second method on low-multiplicity slices.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offsets: A007323 starts at g = 0, while A124506 starts at F = 1 and counts by Frobenius number, not genus.
- Bitset width: genus above 64 overflows 64-bit gap masks silently.
- Cluster-scale runs need checkpointed, independently checkable work units; an unsplit single total cannot be spot-checked.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/numerical-semigroups-count-genus-81-frobenius-133.md
```

Already set up? Say `run V3R1T4S on numerical-semigroups-count-genus-81-frobenius-133`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `numerical-semigroups-count-genus-81-frobenius-133`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
