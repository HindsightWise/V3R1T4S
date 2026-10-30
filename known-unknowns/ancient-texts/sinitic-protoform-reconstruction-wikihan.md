# Middle Chinese protoform reconstruction (WikiHan, WikiHan-aug, Hóu): beat the Lu-Wang-Mortensen 2024 reranked systems on accuracy and token edit distance

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (5,165 cognate sets; GRU and Transformer models train on CPU or a small GPU) · open as of 2026-10-30

## The problem

Supervised protoform reconstruction predicts the ancestral form of a cognate set from its daughter reflexes. WikiHan (Chang, Cui, Kim and Mortensen, COLING 2022, github.com/cmu-llab/wikihan, CC0) pairs Baxter-Sagart Middle Chinese with reflexes in 8 Sinitic varieties; with Chang et al.'s split it has 3,615 / 517 / 1,033 train / dev / test cognate sets. Lu, Wang and Mortensen (LREC-COLING 2024, arXiv 2403.18769; github.com/cmu-llab/reranked-reconstruction, last commit 2024-04-30) rerank beam-search reconstructions with a reflex prediction model and report, as means of 20 runs on the test sets (Table 3): WikiHan, GRU-BS + Transformer reranker, ACC 57.26%, token edit distance (TED) 0.7029, TER 0.1646, FER 0.0658, BCFS 0.7520; WikiHan-aug (Cui et al. 2022, training augmented with Mockingbird-I1 predictions, same test set) 58.58% and 0.6822 (GRU reranker); Hóu 2004 (39 varieties, Kim et al. 2023 split, 562 / 81 / 161) 42.08% and 0.9503 (Transformer reranker). Baselines: Meloni et al. 2021 GRU and Kim et al. 2023 Transformer (WikiHan 55.58% and 54.62%). The repository ships all three Sinitic splits (data/chinese_wikihan2022, chinese_wikihan2022_augmented, chinese_baxter). Status 2026-10-30: searches found no later supervised result above these on the same splits; the ACL 2024 semisupervised paper (arXiv 2406.05930) keeps only 5-30% of the training labels (main experiments at 10%), and the repository marks the Romance sets as unavailable.

## What counts as a win

On the WikiHan test split shipped in cmu-llab/reranked-reconstruction data/chinese_wikihan2022/test.pickle (sha256 b8d4e577bfc5c85f208f841b9d49c352607fec5f44499f0ce6782bf4a829898d; 1,033 cognate sets), a system trained only on the matching train.pickle (dev.pickle for tuning) produces frozen predictions (hash committed before scoring) from at least 10 independent seeds fixed in advance, all scored; a deterministic system may submit one run. The mean exact-match accuracy over runs (whole phoneme sequence including tone equals the gold Baxter protoform) must be strictly above 57.26% AND the mean token edit distance (Levenshtein over phoneme tokens, averaged over test sets) strictly below 0.7029. Inputs are the daughter reflexes and language labels only: the character keys of the pickles, any Middle Chinese or Old Chinese dictionary, WikiHan's full TSVs and any pretrained model that saw Chinese character readings are excluded.

## Partial wins

- **p1:** Same rules on WikiHan-aug (train from chinese_wikihan2022_augmented, same test set): mean ACC strictly above 58.58% and mean TED strictly below 0.6822.
- **p2:** Same rules on Hóu (chinese_baxter split, 161 test sets): mean ACC strictly above 42.08% and mean TED strictly below 0.9503.
- **p3:** Same rules on WikiHan: mean ACC strictly above 57.26% alone, with mean TED no worse than 0.7360 (the Meloni GRU baseline).

## How a win is checked

The verifier fetches the pickles, checks sha256, loads them with an unpickler that refuses all classes (each file is a tuple of a language list and a dict of cognate sets holding only dicts, lists and strings), checks the prediction hashes, and recomputes ACC and TED with its own code; it reads the training code for the input restrictions and may retrain one seed.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/cmu-llab/reranked-reconstruction>

## Sources

- <https://github.com/cmu-llab/reranked-reconstruction>
- <https://arxiv.org/abs/2403.18769>
- <https://aclanthology.org/2024.lrec-main.762>
- <https://github.com/cmu-llab/wikihan>
- <https://aclanthology.org/2022.coling-1.314/>
- <https://arxiv.org/abs/2307.01896>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Rerank larger beams with an ensemble of reflex predictors, as Lu et al. did, but score with PanPhon feature distance rather than exact reflex match.
- Cognate Transformer (Akavarapu and Bhattacharya 2023) style MSA encoders over aligned reflexes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The splits are Python pickles: never load them with a plain pickle.load; a class-refusing unpickler is enough.
- The pickle keys are Chinese characters with an index (e.g. 梆1), and a Middle Chinese reading is a dictionary lookup away; any use of the key, or of a model that knows character readings, is leakage.
- Lu et al.'s values are means of 20 runs: one lucky seed above 57.26% is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/sinitic-protoform-reconstruction-wikihan.md
```

Already set up? Say `run V3R1T4S on sinitic-protoform-reconstruction-wikihan`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sinitic-protoform-reconstruction-wikihan`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
