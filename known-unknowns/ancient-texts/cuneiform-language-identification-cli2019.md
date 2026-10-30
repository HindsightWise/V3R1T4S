# Cuneiform language and dialect identification (VarDial 2019 CLI): beat NRC-CNRC's macro-F1 0.7695 on the released test set, closed track

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (about 5 MB of Unicode cuneiform lines) · open as of 2026-10-30

## The problem

The Cuneiform Language Identification shared task (VarDial 2019; organiser Tommi Jauhiainen, dataset by Jauhiainen, Jauhiainen, Alstola and Linden, W19-1409; campaign report Zampieri et al., W19-1401) asks which of seven varieties a line of Unicode cuneiform belongs to: Sumerian or one of six Akkadian dialects (Old Babylonian, Middle Babylonian peripheral, Standard Babylonian, Neo-Babylonian, Late Babylonian, Neo-Assyrian), built from Oracc transliterations. The data (github.com/tosaja/CLI2019, commit 2f82d58b of 2019-07-08; CLIdata.zip git blob ce86e5a4, sha256 9fe02f82e76a53c51638079291406b9e24fb5977f03aad55ba678c45ee32b7e1; CC BY-SA 3.0) hold 139,421 training lines, 4,676 development lines and a balanced test set of 6,895 lines (985 per variety) with gold labels (gold.txt, gold.labels). Official metric: macro-averaged F1 over the seven classes. Record: NRC-CNRC (Bernier-Colborne, Goutte and Leger, W19-1402; code github.com/gbcolborne/lang_id), a character-level BERT pretrained on the task data with a second unsupervised pretraining phase on the unlabelled test lines, macro-F1 0.7695 (accuracy 0.7711); runner-up tearsofjoy (linear SVM with language-model adaptation) 0.7632; best non-adaptive run 0.7511. Status 2026-10-28: no closed-track result above 0.7695 on the official test set was found; SharifCL's 2020 write-up (arXiv 2009.10794) reports 0.7210, and an IJICT 2024 paper's 96% is on its own oversampled random re-split, not on the official test set.

## What counts as a win

A frozen label file for all 6,895 lines of CLIdata/test.txt (order preserved, hash committed before scoring) with macro-F1 strictly above 0.7695 against CLIdata/gold.labels (sklearn f1_score with average='macro' over the seven labels), under the 2019 closed-track rules: training and tuning use only CLIdata train.txt and dev.txt; the unlabelled test lines may be used for unsupervised adaptation, as the 2019 winner did, but no gold label is read before the file is frozen; no external data of any kind, including Oracc, CDLI, eBL or ePSD texts (the test lines come from Oracc) and any pretrained model trained on anything other than CLIdata. Code and seeds are published.

## Partial wins

- **p1:** Non-transductive: macro-F1 strictly above 0.7632 (the runner-up's test-adapted SVM) without using the test lines in any way before the label file is frozen, same closed-track rules.
- **p2:** Hardest classes: F1 strictly above NRC-CNRC's class-wise F1 on both Standard Babylonian (0.5705) and Neo-Babylonian (0.6500) (Table 3 of W19-1402), with overall macro-F1 of at least 0.7600, same rules.

## How a win is checked

The verifier fetches CLIdata.zip from github.com/tosaja/CLI2019 (checks the blob id and sha256), checks the label file's hash against the commitment, and recomputes macro-F1 and per-class F1 with sklearn and with independent code. It reads the published code to confirm that only CLIdata train and dev (and, for the full win, unlabelled test text) are used, and may re-train once (laptop-hours) to confirm the frozen file comes from the stated system. Scoring takes seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/tosaja/CLI2019>

## Sources

- <https://github.com/tosaja/CLI2019>
- <https://aclanthology.org/W19-1401/>
- <https://aclanthology.org/W19-1402/>
- <https://aclanthology.org/W19-1409/>
- <https://github.com/gbcolborne/lang_id>
- <https://arxiv.org/abs/2009.10794>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Character n-gram SVM and naive Bayes ensembles with test-set language-model adaptation (tearsofjoy, 0.7632) are within 0.007 of the record; combine them with a small character transformer and calibrate the ensemble on dev.
- Deduplicate the training lines first (NRC did): many lines repeat across varieties, so keep label distributions for duplicates rather than one label.
- Short lines dominate the error: 1,922 test lines have 5 signs or fewer; back off to dev-tuned class priors for very short lines.
- Unsupervised adaptation on the unlabelled test lines (allowed for the full win) gave NRC most of its margin over non-adaptive runs.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 638 of the 6,895 test lines occur verbatim in train or dev, and 104 of those carry a different or additional label there; 12 distinct test texts occur twice in the test set with different gold labels, so 100% is unreachable.
- External cuneiform corpora contain the test lines (all from Oracc); using them, or a pretrained model that saw them, breaks the closed track and leaks labels.
- Dev and test contain no line shorter than 3 signs while train has 31,706 such lines, and dev is balanced while train is not (38% Sumerian); NRC found cross-validation on train plus dev, with folds built to match, more reliable than the official dev set alone.
- Random re-splits with oversampling inflate scores (IJICT 2024 reports 96%); only the official test labels count.
- The criterion is macro-F1 over seven balanced classes, not accuracy.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/cuneiform-language-identification-cli2019.md
```

Already set up? Say `run V3R1T4S on cuneiform-language-identification-cli2019`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cuneiform-language-identification-cli2019`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
