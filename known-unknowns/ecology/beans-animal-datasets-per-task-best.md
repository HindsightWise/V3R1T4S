# BEANS animal-sound benchmark: beat the best published test score on one of seven freely downloadable animal classification or detection datasets

🐦 **Ecology and bioacoustics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days per dataset (about 300 GB for all BEANS data; frozen-encoder probes run on CPU) · open as of 2026-10-30

## The problem

BEANS (Hagiwara, Hoffman, Liu, Cusimano, Effenberger, Zacarian; arXiv 2210.12300; github.com/earthspecies/beans) fixes train/validation/test splits and metrics over public animal-sound datasets: accuracy for classification, mAP for detection. Best published test values, collected on 2026-10-30 from the Perch 2.0 tables (arXiv 2508.04665, which also tabulate AVES-Bio and BioLingual fine-tuning), the AVEX study (Miron, Robinson, Alizadeh and colleagues, arXiv 2508.11845), the OpenBEATs full fine-tuning table (Bharadwaj, Cornell, Choi, Fukayama, Shim, Deshmukh, Watanabe; arXiv 2507.14129, Table 6) and the BioMamba comparison (Tang and Baskiyar, arXiv 2512.03563). Classification accuracy: watkins 0.935 (AVEX sl-BEATS-bio probe), bats 0.815 (Perch 2.0 peak-select prototype probe), dogs 0.971 (BioLingual fine-tuned; BEATs iter 1 and Dasheng 1.2B fine-tuned tie in OpenBEATs). Detection mAP: dcase 0.495 (OpenBEATs-Large iter 1 fine-tuned), enabirds 0.764 (Perch 2.0 peak-select PP), hiceas 0.713 (BEATs iter 1 fine-tuned, as run in the OpenBEATs paper; AVES fine-tuned 0.683 in the BioMamba paper), gibbons 0.516 (Perch 2.0 peak-select PP). The best mean over these four detection sets is 0.581 (Perch 2.0 peak-select PP: 0.457, 0.764, 0.585, 0.516; the best OpenBEATs row has 0.549). NatureLM-audio and BioMamba's own model report lower values. The 2026 attentive-probing paper (arXiv 2605.10494) gives its results only in figures, and BEANS-Next (arXiv 2610.10663) uses new tasks. Some papers compute mAP differently from the BEANS repository, so every claim is recomputed with the repository code. cbi and rfcx are left out because their download needs a human to accept Kaggle competition terms; ESC-50, Speech Commands and HumBugDB are left out too.

## What counts as a win

Pick one dataset D among watkins, bats, dogs, dcase, enabirds, hiceas and gibbons. The claim is a model trained only on D's BEANS train split (validation split for selection; declared pretraining allowed). Its test metric, computed with the BEANS repository's evaluation code as the mean over at least 3 seeds, must be STRICTLY GREATER (direction: max) than the value listed above for D by at least 0.005. It must also beat any test value for D in the BEANS paper, AVES, BioLingual, NatureLM-audio, Perch 2.0, AVEX, OpenBEATs, BioMamba, or any other paper from the last 24 months that the NOVELTY skeptic finds. Pretraining corpora must not contain D's test recordings (for example Watkins or Xeno-canto items reused by BEANS). Deliverables: code, seeds, saved test predictions and evaluation logs.

## Partial wins

- **p1:** With a frozen public encoder and only a linear or prototype probe, beat the best frozen-probe value for some dataset D (the Perch 2.0 LP/PP or AVEX probe columns), even if a fine-tuned model holds the overall record.
- **p2:** One model whose mean mAP over the four detection datasets dcase, enabirds, hiceas and gibbons exceeds 0.581 (Perch 2.0 peak-select PP), recomputed with the BEANS code.

## How a win is checked

The skeptic runs the BEANS download and preprocessing scripts (MD5 checked) and recomputes D's metric from the saved predictions with the repository code. They re-train one seed and check the pretraining corpora against D's source recordings.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:BEANS+AND+abs:bioacoustic&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://github.com/earthspecies/beans>
- <https://arxiv.org/abs/2210.12300>
- <https://arxiv.org/abs/2508.04665>
- <https://arxiv.org/abs/2508.11845>
- <https://github.com/earthspecies/avex>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multi-layer probing of several frozen encoders, then stacking their predictions.
- Cross-domain import (speaker verification): margin losses designed for individual identity, for the bats and dogs tasks (both identify individual animals).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- AVEX's pretraining mix lists Watkins; a pretrained model that saw Watkins test recordings cannot make a watkins claim.
- mAP implementations differ between papers; only the BEANS repository's computation counts.
- Single-seed differences of 0.01 on small test sets (dogs, bats) are noise.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/beans-animal-datasets-per-task-best.md
```

Already set up? Say `run V3R1T4S on beans-animal-datasets-per-task-best`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `beans-animal-datasets-per-task-best`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
