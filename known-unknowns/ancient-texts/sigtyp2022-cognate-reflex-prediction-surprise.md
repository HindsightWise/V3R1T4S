# Cognate reflex prediction (SIGTYP 2022 surprise data): beat FeVeT and CogTran on normalized edit distance and B-Cubed F at the 0.10, 0.30 and 0.50 test proportions

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (10 Lexibank wordlists, a few MB; small transformers train on CPU) · open as of 2026-10-30

## The problem

In the SIGTYP 2022 shared task (List, Vylomova, Forkel, Hill and Cotterell, 2022.sigtyp-1.7; github.com/sigtyp/ST2022, release v1.4) systems predict withheld words in cognate sets from their reflexes in related languages, on 10 surprise datasets (bremerberta, wangbai, beidazihui, hillburmish, deepadungpalaung, luangthongkumkaren, bodtkhobwa, birchallchapacuran, kesslersignificance, bantubvd) at five test proportions (0.10 to 0.50). Official scores (st2022 --evaluate): per dataset the mean over languages, then the mean over the 10 datasets, of edit distance (ED), normalized edit distance (NED), B-Cubed F (BCFS) and BLEU. Task winner Mockingbird-I1 (Kirov, Sproat and Gutkin): NED 0.2431 / 0.2648 / 0.2899 / 0.3162 / 0.3518 and BCFS 0.7673 / 0.7120 / 0.6717 / 0.6428 / 0.6050 at 0.10 to 0.50. Akavarapu and Bhattacharya's Cognate Transformer (EMNLP 2023) report CogTran-small NED 0.2421 / 0.2919 / 0.3332 and BCFS 0.7823 / 0.6954 / 0.6477 at 0.10 / 0.30 / 0.50 (their appendix per-family BCFS average to only 0.7628 / 0.6752 / 0.6257). Wientzek's FeVeT (Open Research Europe 2025, doi 10.12688/openreseurope.20647.1, v1 under review; github.com/TGH-2020/FeVeT) reports fine-tuned ED 0.7836 / 0.9589 / 1.1111, NED 0.205 / 0.2397 / 0.2825, BCFS 0.8041 / 0.7232 / 0.673, but these are means over 99 languages; its own per-dataset files average, in the official way, to ED 0.9064 / 1.1128 / 1.2725, NED 0.2289 / 0.2705 / 0.3111 and BCFS 0.7811 / 0.6941 / 0.6418. Bars used here: NED 0.2289, 0.2705, 0.3111 (FeVeT, official-style); BCFS 0.7823, 0.6954, 0.6477 (CogTran headline, the highest reported, kept as the conservative bar). Status 2026-10-30: no later result found (citations of the task paper, CogTran and FeVeT checked).

## What counts as a win

Frozen prediction files (hash committed before scoring) for all 10 surprise datasets at proportions 0.10, 0.30 and 0.50, each produced by published code that reads only that proportion's training-{P}.tsv and test-{P}.tsv from ST2022 tag v1.4 (other datasets' training partitions and generic phonetic feature tables such as CLTS are allowed; no Lexibank or CLDF source of the surprise languages, no solutions file, no other proportion's files of the same dataset). Scored with the ST2022 definitions as the mean over the 10 datasets, the claim must, at every one of the three proportions, have NED strictly below the bar (0.2289, 0.2705, 0.3111) and BCFS strictly above the bar (0.7823, 0.6954, 0.6477). Bars are re-read from the FeVeT family-result files and the CogTran paper before claiming, and any credible published official-style value found by the skeptic replaces them if better.

## Partial wins

- **p1:** Same rules, NED and BCFS both beat the bars at one of the three proportions 0.10, 0.30, 0.50.
- **p2:** Same rules at proportion 0.20 or 0.40 (where only shared-task runs are published): beat Mockingbird-I1 on all four official metrics (0.20: ED 1.0413, NED 0.2648, BCFS 0.7120, BLEU 0.6326; 0.40: ED 1.2725, NED 0.3162, BCFS 0.6428, BLEU 0.5724).
- **p3:** Same rules, NED strictly below FeVeT's headline averages (0.205, 0.2397, 0.2825) at all three proportions under the official mean over datasets.

## How a win is checked

The verifier fetches the v1.4 training, test and solutions files, checks the prediction files' hashes, scores them with its own implementation of the ST2022 metrics (cross-checked on the released Mockingbird-I1 outputs, which must reproduce the results/*.md values), and reads the code to confirm the data restrictions; one dataset and proportion may be re-run.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/TGH-2020/FeVeT/tree/main/results>

## Sources

- <https://github.com/sigtyp/ST2022>
- <https://aclanthology.org/2022.sigtyp-1.7/>
- <https://aclanthology.org/2022.sigtyp-1.9/>
- <https://arxiv.org/abs/2310.07487>
- <https://github.com/TGH-2020/FeVeT>
- <https://ore.eu/ore/article/view/972/version/1685>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble FeVeT-style feature-vector decoding with correspondence-pattern SVM predictions (the ST2022 baseline-SVM) and pick per cognate set by agreement.
- Pretrain on the other datasets' training partitions with language embeddings, then fine-tune per dataset as FeVeT does.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- FeVeT's headline averages (s2s_reflex_finetuned_avg.txt) are means over languages, not the official mean over datasets: its own family files give NED 0.2289 at 0.10, not 0.205. Compare like with like.
- Proportions are separate splits of the same wordlists: training-0.10.tsv contains most of the words withheld in test-0.50.tsv. Using any other proportion's files of the same dataset leaks the answers.
- Each data-surprise/ < dataset> folder of ST2022 also holds cognates.tsv, wordlist.tsv and solutions-{P}.tsv, which contain every withheld word; only training-{P}.tsv and test-{P}.tsv may be read.
- The full Lexibank CLDF datasets behind the surprise data are public and contain every withheld word.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/sigtyp2022-cognate-reflex-prediction-surprise.md
```

Already set up? Say `run V3R1T4S on sigtyp2022-cognate-reflex-prediction-surprise`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sigtyp2022-cognate-reflex-prediction-surprise`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
