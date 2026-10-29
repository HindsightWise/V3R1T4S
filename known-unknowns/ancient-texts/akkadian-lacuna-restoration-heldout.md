# Akkadian: restore masked/damaged signs in Oracc/eBL transliterations, beating the Lazar et al. 2021 held-out benchmark with frozen predictions

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Lazar, Saret, Yehudai, Horowitz, Wasserman and Stanovsky (EMNLP 2021, arXiv 2109.04513) framed filling gaps in Akkadian transliterations as masked language modelling on about 1M words / 2.3M signs scraped from Oracc. Their best model (MBERT+Akk, greedy decoding) reports hit@5 = 0.89 and MRR = 0.83 on a 20% held-out split with 15% random masking. These are token-level (BERT word-piece) scores: the paper says 'Table 2 compares token level evaluation', and the repository's evaluate_bert.py masks and scores each word piece separately (positions with label_ids != -100); multi-sign and word prediction is evaluated separately (its Figure 3). They released code and the scraped data (github.com/SLAB-NLP/Akk, MIT, data/akk_from_jsons.jsonl 21 MB, last commit 2022-11-10). The paper's split is a random 80/20 split by text (about 8K train / 2K test texts, its Table 1). The code fixes the seed (preprocessing/main_preprocess.py: SEED = 2, train_test_split(test_size=0.2, random_state=SEED)), but it splits a fresh Oracc scrape written to data/raw/akk_jsons.jsonl, which is not in the repository; the shipped data/akk_from_jsons.jsonl is not referenced by the code and holds 23,211 records, more than Table 1 reports, so the paper's exact test set is not known to be reproducible. The shipped data file (data/akk_from_jsons.jsonl, 21.2 MB, repository commit dfd2a66d of 2022-11-10) is the frozen corpus. Vetter re-check 2026-10-08: two literature searches found no later work reporting hit@k/MRR on this task (later Akkadian work is NMT: Gutherz et al. 2023, TabletCraft 2026). The real-world task is restoring the editorial gaps ('x', [...]) that remain unrestored in Oracc and eBL editions; eBL alone has 625,844 transliterated lines, a large fraction containing bracketed editorial restorations that can serve as a natural held-out test.

## What counts as a win

On the SLAB-NLP/Akk released data (data/akk_from_jsons.jsonl at commit dfd2a66d or a later recorded commit), with an 80/20 split by text, the frozen list of masked positions published (hash) before any model is trained, and the token-level protocol of the paper's Table 2 and the repository's evaluate_bert.py reproduced with a documented fixed seed (the masked units are word-piece tokens, not whole words): every text is preprocessed as the repository's main_preprocess.py does with the flags its README names for the paper's models (--remove_subscripts --remove_superscripts; no --remove_hyphens, --use_pseudo_words or --remove_missing, so hyphens and the '...' break marks stay in the text; every 'x', gap mark or not, becomes the missing-sign character U+1F607, which the repository injects as a token and never masks; the code also turns '+' into '-' and deletes every 'o', every 'v' and backslash codes such as \t); each test text is then tokenized with the MBERT+Akk tokenizer that the repository code builds from the training split (the tokens it puts into M-BERT's 99 free slots published, with the sha256 of the resulting vocab.txt) and truncated to 128 tokens including [CLS] and [SEP], as ORACCDataset does; every token except the special tokens and the missing-sign token (U+1F607) is masked independently with probability 0.15 and then shown as [MASK] (80%), a random token (10%) or unchanged (10%), as DataCollatorForLanguageModelingAkkadian does, and the frozen list records what is shown at each masked position, so that every system sees the identical input; each masked token, whichever of the three it shows, is scored by exact match with its original word piece (the positions with label_ids != -100, as compute_mrr_and_all_hit_ks does): (1) the claimant retrains the paper's MBERT+Akk baseline with the repository code and default hyperparameters on the same frozen split and freezes its top-5 predictions (hash) - its hit@5 must land within 0.02 of 0.89 on the frozen masked positions, otherwise the split is not comparable and no full win is possible; (2) a prediction file (top-5 per masked token) for the new system, frozen (hash) before scoring and trained/tuned ONLY on the training split, scores BOTH hit@5 and MRR strictly above the paper's values (re-read from the arXiv/ACL paper immediately before claiming) AND strictly above the reproduced baseline on the identical masked positions. A whole-word or whole-sign score is a different unit and is never compared with 0.89 or 0.83. Any use of test documents, of eBL/Oracc texts that duplicate test documents (same P/Q number or same composition), or of a corpus fetched after the split was frozen voids the claim.

## Partial wins

- **p1:** Same protocol as the full criterion (including the reproduced baseline), beating only hit@5 or only MRR by at least 1 absolute point over both the paper's value and the reproduced baseline; or beating both metrics on a genre subset for which the paper reports a per-genre number (re-read from the paper's per-genre table/figure; genre defined by Oracc project as in the paper).
- **p2:** Natural-lacuna holdout: a permanent held-out set of at least 2,000 editorially restored signs (text inside [ ] in eBL fragments with joins == [] and no corpus-chapter manuscript link, sampled by a published deterministic rule from fragments fetched on a recorded date, hashed before training) is masked and predicted with frozen top-5 predictions. All training material must exclude any line sharing 6 or more consecutive signs with the 20-sign context window around any holdout gap (parallel/duplicate exclusion, re-checked by the verifier). hit@1 at least 0.50 and hit@5 at least 0.75, with BOTH a unigram-frequency baseline and a k-NN retrieval baseline over the filtered training set reported alongside and beaten by at least 20 absolute points on hit@1.

## How a win is checked

The verifier re-creates the split, the preprocessing, the word-piece tokenization (M-BERT's vocabulary with the published injected tokens) and the masks from the published seed/rule on the recorded data commit, checks the hashes of both frozen prediction files (baseline and new system) against the hashes committed before training (timestamps from the pre-registered holdout protocol), rescores hit@k/MRR for both with independent code on the identical masked positions, and checks that no test document or duplicate (same Oracc P/Q number, composition, or eBL museum number) appears in the training material. Rescoring is minutes; the verifier never retrains.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/SLAB-NLP/Akk>

## Sources

- <https://github.com/SLAB-NLP/Akk>
- <https://arxiv.org/abs/2109.04513>
- <https://ar5iv.labs.arxiv.org/html/2109.04513>
- <https://www.ebl.lmu.de/api/statistics>
- <https://oracc.museum.upenn.edu/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Character/sign-level n-gram or small transformer LMs trained from scratch on signs with genre tags, predicting the frozen word-piece positions. Note that the 2021 models already work below the word (the paper's M-BERT tokens split a-na into 'a', '-', 'na'), and its from-scratch BERT+AKK(mono) reached 0.60 hit@5 (Table 2).
- Retrieval-augmented restoration: Akkadian royal inscriptions and omens are highly formulaic, so k-NN over duplicate passages in the training split can restore many gaps exactly.
- Ensemble a forward and backward sign LM with a lexicon constraint (only attested sign sequences for the word), which directly targets MRR.
- Build the natural-lacuna holdout (p2) from eBL bracketed restorations, stratified by genre and gap length, and seal it before any training.
- Report per-gap-length curves; long gaps dominate the real editorial need and are where the 2021 model fails.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 0.89 and 0.83 are token-level scores, and a token is not a word. M-BERT splits off every sign delimiter: in the 1,882 test documents that main_bert.py --do_eval keeps under the SEED = 2 split of the shipped file, at least 62% of the 174,632 words are two or more tokens (76% with the plain M-BERT vocabulary), and a third to two fifths of the maskable tokens are '-' or '.' (33% with the plain vocabulary, at most 41%); about two thirds of these inside the 128-token window (three quarters over whole documents) are sign delimiters, the rest the dots of the '...' break marks that the preprocessing keeps. The repository's 80/10/10 rule also leaves the original token in place at a tenth of the masked positions. Masking whole words or signs is a much harder task: the paper's Figure 3 puts one masked sign at about 0.55 hit@5, against about 0.9 for one token (read off the chart). Never compare such a score with 0.89 or 0.83.
- The 2021 split is produced by code (SEED = 2) on a fresh Oracc scrape, not shipped as files; a different scrape yields a different test set. Only the reproduced-baseline control makes a beat meaningful.
- Massive duplication in Oracc (parallel manuscripts of the same composition, RINAP duplicates) leaks test text into training; deduplicate by composition/Q number or report leakage.
- data/akk_from_jsons.jsonl repeats records: 5,666 id_text values occur 2 to 5 times (8,781 extra records; 8,691 lines are exact repeats), although the repository's scraper skips an id_text it has already written. Splitting this file as the repository's --do_preprocessing path does (preprocess_akk_file keeps all 23,211 records in order, then train_test_split(test_size=0.2, random_state=2)) gives 18,568 train / 4,643 test records and puts a byte-identical copy of 2,606 of the 4,643 test documents (56.1%) in training. The repository's evaluation (main_bert.py --do_eval) then scores only test documents whose id_text is neither in training nor earlier in the test file: it drops 2,761 (2,616 with the id_text in training, 145 repeats within the test set) and scores 1,882. Remove repeated records (same id_text) before splitting, or apply the same id filter, and report how many were removed.
- Exact-match filters (same id_text, same text) do not remove composition-level duplicates: under the SEED = 2 split of the shipped file, test documents can be largely covered by a composite text (Q number) in train. Example: test record P229143 (19 words) shares 10 to 11 of its 12 distinct word 8-grams with Q002268 in train, depending on how editorial marks are normalised. Compute each test document's n-gram share against train before accepting a claim, and report it.
- Editorial restorations are themselves often made from parallels: hit rates on bracketed text overstate performance on truly unknown gaps.
- LLM-judged 'plausibility' of restorations is not a criterion; only frozen top-k predictions scored against held-out text count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/akkadian-lacuna-restoration-heldout.md
```

Already set up? Say `run V3R1T4S on akkadian-lacuna-restoration-heldout`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `akkadian-lacuna-restoration-heldout`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
