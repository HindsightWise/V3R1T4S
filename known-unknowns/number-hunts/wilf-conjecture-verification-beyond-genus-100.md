# Wilf's conjecture on numerical semigroups: extend the computer verification beyond genus 100, or find a counterexample

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (the genus-100 run used up to 1500 cores for two weeks); smarter trimming may bring a few extra genera within laptop-days · open as of 2026-10-30

## The problem

Wilf's conjecture (1978) says that every numerical semigroup S with conductor c, embedding dimension e and genus g satisfies e(c - g) >= c. Manuel Delgado, Shalom Eliahou and Jean Fromentin (arXiv 2310.07742, 2023; published in J. Algebra) verified it for every semigroup of genus g <= 100; the previous record was g <= 66 (Maria Bras-Amorós, 2023), after g <= 65 (Bras-Amorós and Rodríguez, 2021), g <= 60 (Fromentin and Hivert, 2016) and g <= 50 (Bras-Amorós). They combined three things: Eliahou's 2020 theorem settling the case e >= m/3; trimming the tree of numerical semigroups of subtrees that cannot hold a counterexample (the trimmed tree T_100(3) has about 4.5e15 nodes, with per-genus counts t_g published in Section 5.1); and a parallel exploration on up to 1500 cores of the CALCULCO platform over two weeks in summer 2023 (code: github.com/jfromentin/trim_tree_semigroups). For semigroups with m dividing c they reached g <= 120. Later results add sufficient conditions but do not extend the exhaustive range. Delgado, Kumar and Marion (arXiv 2501.04417, v3 1 Oct 2026) show that Wilf holds when |S n (m, 2m)| >= sqrt(2m) and for almost all semigroups with large maximum primitive. Delgado's 2026 IMNS overview still names the genus-100 verification as the strongest published result, and reports that all semigroups with Frobenius number <= 111 or maximum primitive <= 100 are Wilf. Bras-Amoros and Torra (arXiv 2607.23111, v3 10 Sep 2026) count semigroups up to genus 80 with a seeds-based tree but do not extend the Wilf verification. The conjecture is open and no counterexample is known.

## What counts as a win

Success means EITHER (a) an explicit numerical semigroup, given by minimal generators, with e(c - g) < c, confirmed by two independent exact checkers (for example GAP NumericalSgps and an independent Apery-set computation); OR (b) a computer verification that every numerical semigroup of genus g <= G satisfies Wilf's inequality, for some G >= 101. Option (b) requires: published code; every trimming rule justified by a cited theorem whose statement is reproduced; per-genus node counts from a run of the same code with G = 100 (the trimmed tree T_G(3) depends on G), truncated at some genus >= 66, that exactly reproduce Delgado-Eliahou-Fromentin's published t_g table for T_100(3) (Section 5.1 of arXiv 2310.07742) up to that genus; and an independent re-run of at least a random 5% of the work units with separately written code, agreeing exactly. In both cases a literature search immediately before claiming must find no earlier counterexample or published verification beyond genus 100.

## Partial wins

- **p1:** Verification of Wilf's conjecture for all numerical semigroups with m dividing c up to genus G >= 121 (Delgado-Eliahou-Fromentin reached 120), to the same evidence standard as option (b).
- **p2:** An independent re-verification of the genus <= 100 result with code written from scratch, reproducing the published per-genus counts of the trimmed tree.

## How a win is checked

Counterexample: compute the Apery set, the conductor, the genus and the minimal generators exactly, then check the inequality (seconds). Verification run: rebuild the trimmed tree to small genus and compare node counts with the published table; recompute random work units with independent code; check each pruning rule against the cited theorem.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2310.07742>

## Sources

- <https://arxiv.org/abs/2310.07742>
- <https://github.com/jfromentin/trim_tree_semigroups>
- <https://arxiv.org/abs/2501.04417>
- <https://arxiv.org/abs/2607.23111>
- <https://imns2026.org/upload/1784622557_Manuel-Delgado.pdf>
- <https://oeis.org/A007323>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Add the new Delgado-Kumar-Marion sufficient condition (|S n (m,2m)| >= sqrt(2m)) as an extra pruning rule; it was proved after the 2023 run.
- Port the Bras-Amoros-Torra seeds/leaf-discriminating tree (which descends only three levels above the leaves) to the Wilf-trimmed tree.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Embedding dimension means the number of minimal generators, not of all small elements.
- A pruning rule needs a theorem behind it; a heuristic prune voids the verification.
- Gaps can be as large as 2g - 1, so 64-bit gap masks overflow from genus 33 on; codes in the Fromentin-Hivert style need wider (for example SIMD) representations.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wilf-conjecture-verification-beyond-genus-100.md
```

Already set up? Say `run V3R1T4S on wilf-conjecture-verification-beyond-genus-100`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wilf-conjecture-verification-beyond-genus-100`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
