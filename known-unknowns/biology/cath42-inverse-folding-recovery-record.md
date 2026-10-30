# CATH 4.2 inverse folding: beat the best published sequence recovery (0.63, Refold) on the standard test split

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (GPU helps; the CATH 4.2 split is a few hundred MB) · open as of 2026-10-30

## The problem

The standard table for protein inverse folding is sequence recovery on the CATH 4.2 test split used by GraphTrans, GVP, ProteinMPNN and PiFold. As compiled by Zhangyang Gao, Cheng Tan and Stan Z. Li in Knowledge-Design (arXiv:2305.15151), the published recoveries on the full test set are StructGNN 35.91, GraphTrans 35.82, GCA 37.64, ESM-IF 38.3, GVP 39.47, AlphaDesign 41.31, ProteinMPNN 45.96, PiFold 51.66, LM-Design 55.65 and Knowledge-Design 60.77 percent, with 44.66 on the short subset, 45.45 on the single-chain subset, and TS50 62.79 and TS500 69.19 for the same model. Refold (Yiran Zhu, Changxi Chi, Hongxin Xiang, Wenjie Du, Xiaoqi Wang and Jun Xia, arXiv:2603.14350) reports higher recovery on the same benchmark through the ProteinInvBench framework: 0.63 on the CATH 4.2 full test set and 0.51 on the short subset for Refold (Joint), and 0.61 full for Refold (Frozen); its figures are given to two decimals only and the paper does not name the split file. Credit for the current state belongs to those authors and to the ProteinMPNN (Justas Dauparas and co-authors) and PiFold lines of work the table is built on. More than a third of residues are still predicted wrongly given the backbone, and the splits, data pipelines and evaluation (per-chain recovery over the test chains) are public in the ProteinInvBench / PiFold repositories, so the benchmark runs on one GPU or a patient CPU.

## What counts as a win

Designed sequences for every chain of the CATH 4.2 test split exactly as distributed by the public pipeline used in the published table (PiFold / ProteinInvBench data loaders; the split file hash must be stated), one sequence per chain from a single frozen model with declared sampling temperature, such that the recovery computed by the skeptic with that repository's evaluation code (same aggregation as the published table) is STRICTLY HIGHER (direction: max) than 63.5 percent - above Refold (Joint)'s reported 0.63 on CATH 4.2 (arXiv:2603.14350, re-fetched live immediately before claiming) with its two-decimal rounding absorbed - and higher than any later recovery for the same split found by the novelty check, with the short-subset recovery also reported; training must respect the CATH 4.2 split and every pretraining corpus must be declared and filtered so that no test chain (and no chain above a stated sequence-identity threshold to a test chain) appears in it. A full-test recovery above 60.77 but at or below 63.5 percent counts only as partial win p4.

## Partial wins

- **p1:** Short-subset recovery strictly above 51.5 percent (absorbing the rounding on Refold (Joint)'s reported 0.51) with the full-test recovery also reported from the same frozen model and the same corpus audit.
- **p2:** With the same frozen model, TS50 recovery strictly above 62.79 percent or TS500 strictly above 69.19 percent (Knowledge-Design) by at least 0.5 points, with the CATH 4.2 numbers reported alongside, provided the novelty check finds no higher published value for those sets.
- **p3:** Matching the published 60.77 percent within 1 point using a model of at most 10M parameters trained from scratch on the CATH 4.2 training split alone, with training logs and the harness published.
- **p4:** Full-test recovery strictly above 60.77 percent (Knowledge-Design) by at least 0.5 points under the same split, frozen-model and corpus-audit rules, reported as beating the Knowledge-Design row and not as the record.

## How a win is checked

Skeptic obtains the CATH 4.2 split through the public loaders, checks the split hash and that the submission covers each test chain exactly once, recomputes recovery with the repository's evaluation code (and independently as per-chain identity, median and mean both reported), reruns the attacker's inference from the released checkpoint and seed, and audits the declared training and pretraining corpora for test chains and near-identical homologues. An hour or two plus the attacker's training cost.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2305.15151v2>

## Sources

- <https://arxiv.org/html/2305.15151v2>
- <https://arxiv.org/abs/2603.14350>
- <https://github.com/A4Bio/ProteinInvBench>
- <https://github.com/dauparas/ProteinMPNN>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Most of the remaining error is in loops and surface positions; a model with an explicit burial/secondary-structure prior, or a two-stage core-then-surface decoder, attacks exactly where the gap is.
- Cross-domain import (sequence modelling): recovery is a per-position classification with strong neighbourhood structure, so iterative refinement decoding (mask-predict, as in non-autoregressive translation) fits better than one-shot decoding.
- Pair a structure encoder with a protein language model as a prior, but freeze the language model and declare its corpus, since that is where leakage hides.
- Report designability (self-consistency TM-score) alongside recovery: a recovery gain that lowers designability is not progress, and the extra number costs little.
- Check the easy wins first: ensembling several public models and voting per position often moves recovery by a point, which calibrates how much a new architecture is really worth.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several CATH splits circulate (4.2 vs 4.3, different chain lists); numbers are only comparable within one split, so the split file hash must be stated.
- Protein language models pretrained on recent UniRef or PDB snapshots may have seen the test chains; without a declared and filtered corpus the number is unverifiable.
- Recovery is reported as median or mean over chains in different papers, and sampling temperature changes it; pin both and report both.
- Sequence recovery is not a measure of whether a designed protein works; a win is a benchmark result only.
- TS50 and TS500 are small sets with their own conventions; a TS50 number quoted against the CATH bar is a category error.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/cath42-inverse-folding-recovery-record.md
```

Already set up? Say `run V3R1T4S on cath42-inverse-folding-recovery-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cath42-inverse-folding-recovery-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
