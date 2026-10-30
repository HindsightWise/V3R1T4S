# Greek inscriptions (I.PHI): beat Ithaca's region (70.8% top-1) and date (29.3 years) attribution on the PHI-digit-3 test split

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (178,551 inscriptions in a 217 MB JSON; released checkpoints about 0.2 GB each; a GPU helps) · open as of 2026-10-30

## The problem

Ithaca (Assael, Sommerschield, Shillingford, Bordbar, Pavlopoulos, Chatzipanagiotou, Androutsopoulos, Prag and de Freitas, Nature 603, 2022, doi 10.1038/s41586-022-04448-z) attributes Greek inscriptions to region and date. Table 1 (I.PHI test set, n = 7,811 inscriptions, PHI ids ending in 3): region top-1 70.8% / top-3 82.1% over 84 regions, date distance 29.3 years; onomastics baseline 21.2% / 26.5% and 144.4 years. No later system has beaten these on a shared protocol: Cullhed (arXiv 2409.13870v3; Digital Scholarship in the Humanities 41(1), 2026) reports 75.0% / 83.7% and 37.1 years on his own 95/5 split but lower attribution than Ithaca on a shared test set; Locaputo, Brunello, Saccomanno, Platanou and Serra ('Ithaca Revisited', LREC 2026) recompute Ithaca at 71.11% / 81.70% and 33.98 years on inputs with artificial gaps, against 59.02% / 69.66% and 44.78 years for GPT-5 with retrieval-augmented prompting; Stoicheia (arXiv 2608.07249) and Apollo Restore (arXiv 2609.22455) do restoration only. The current I.PHI release (storage.googleapis.com/ithaca-resources/models/iphi.json, 216,735,767 bytes, md5 7876f27fe7881bd5c1962e54f83cee1b, last modified 2025-06-24) holds 178,551 records, 17,789 with id % 10 == 3; it is not the 2022 snapshot (78,608 inscriptions), so Table 1's test set cannot be rebuilt exactly. Released checkpoints: Ithaca's checkpoint_v1.pkl (202,256,537 bytes, 2022-01-19) for github.com/google-deepmind/ithaca, and the Greek Aeneas-framework model ithaca_153143996_2.pkl (142,485,416 bytes, 2025-06-24) for predictingthepast, with no published attribution numbers. Status 2026-10-28: open; google-deepmind/ithaca last changed on 2026-10-27 (inference now lower-cases its input; the beam-search fix concerns restoration only).

## What counts as a win

On iphi.json (md5 7876f27fe7881bd5c1962e54f83cee1b), the test list T is every record with int(id) % 10 == 3 whose text, after deleting whitespace and the characters '-', '#' and '_', has at least 50 characters (7,684 records); the region list T_r is the records of T whose region_sub, mapped by region_name_filter of predictingthepast/util/region_names.py at a recorded commit, is one of the 82 names of train/data/iphi-region-sub.txt mapped the same way (7,464 records); the dating list T_d is the records of T with numeric date_min <= date_max, both inside [-800, 800] (4,682 records). The verifier recomputes all three lists. Every system reads only the record's text, in one of two preparations named before scoring: (G) as google-deepmind/ithaca train/dataloader.py prepares a record with char_use_guess=True, the setting behind Table 1: '[' and ']' deleted and the editorial supplements between them kept as letters; or (M) as predictingthepast train/dataloader.py prepares a test record: each [...] replaced by '-' of the same length, any remaining '[' or ']' deleted, then GreekAlphabet.filter. A frozen predictions file, whose hash is committed before scoring, ranks the 82 regions for every record of T_r and gives one point date for every record of T_d. Full win: region top-1 strictly above 70.8% AND mean date error strictly below 29.3 years (Ithaca, Nature 2022, Table 1, re-read before claiming; date error is 0 inside [date_min, date_max], else the distance to the nearer bound), AND, on each of the two metrics, strictly better than the better of the two released checkpoints on that metric. The claimant publishes the checkpoints' frozen predictions on the same lists (hashes committed before scoring), made as follows: checkpoint_v1.pkl with google-deepmind/ithaca on (G) and ithaca_153143996_2.pkl with predictingthepast on (M), commits recorded; a prepared text of 768 or more characters is cut to its first 767 characters, and one shorter than Ithaca's 50-character minimum is right-padded with '-' to 50 characters; predicted regions are mapped to the 82 names with region_name_filter, and unmappable predictions never count as correct; a checkpoint's point date is its predictive mean (date_pred_avg of predicted_dates in the repository's util/eval.py), the quantity Table 1 scores. Training uses only I.PHI records with id % 10 not in {3, 4} (digit 4 for model selection) plus public non-epigraphic Greek text, all listed with hashes; none of it may be a test record or a near-duplicate of one (same normalised text, or a shared run of 60 or more consecutive normalised characters with a record of T; normalised means the raw iphi.json text lower-cased, with whitespace and the characters '-', '#', '_', '[' and ']' deleted), so a model initialised from either released checkpoint cannot claim the full win; models whose pretraining data is undisclosed cannot claim the full win.

## Partial wins

- **p1:** One task only, same lists, preparations and baseline rules: region top-1 strictly above 70.8% with top-3 strictly above 82.1%, or mean date error strictly below 29.3 years, each named metric also strictly better than the better of the two released checkpoints on that metric on the same records.
- **p2:** Region top-1 at least 2 points above, or mean date error at least 2 years below, the better of the two released checkpoints on that metric on the same lists, with a paired bootstrap over inscriptions giving p < 0.01, same rules (the Table 1 value need not be beaten).

## How a win is checked

The verifier downloads iphi.json (md5 check) and, at the recorded predictingthepast commit, iphi-region-sub.txt and region_names.py; it regenerates T, T_r and T_d, checks the prediction files' hashes against the commitments, rescores region top-1 and top-3 and mean date error with independent code, re-runs both released checkpoints on a random 300 records in a sandbox, each with its stated preparation, the 767-character cut, the '-' padding and the predictive-mean date, to confirm the baseline files (CPU, under an hour), reads the claimant's code to confirm which preparation its system reads, and scans the published training manifest for test ids and near-duplicates. No retraining.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/ithaca>

## Sources

- <https://www.nature.com/articles/s41586-022-04448-z>
- <https://www.nature.com/articles/s41586-022-04448-z/tables/1>
- <https://github.com/google-deepmind/ithaca>
- <https://github.com/google-deepmind/predictingthepast>
- <https://storage.googleapis.com/ithaca-resources/models/iphi.json>
- <https://aclanthology.org/2026.lrec-1.82.pdf>
- <https://arxiv.org/abs/2409.13870>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fine-tune a public Greek character model with region and date heads; the documentary-clean Stoicheia backbone (Ericu950/Stoicheia-doc_clean) never saw documentary texts and is open.
- Dialect spellings, letter forms transcribed as spellings, formulae and personal names localise inscriptions; nearest-neighbour retrieval over the training digits by character n-grams is a strong baseline to ensemble with.
- For dating, predict a distribution over ten-year bins and output the year minimising expected distance to the true range.
- Use region_main (15 macro-regions) as an auxiliary target.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- iphi.json (2025) is not the 2022 I.PHI: Table 1's n = 7,811 cannot be rebuilt, so only checkpoints re-scored on the same lists make a beat meaningful.
- 6,131 of the 7,684 T texts carry editorial supplements in square brackets (27% of their non-space characters). Ithaca read them as letters (train/config.py char_use_guess=True, the setting behind Table 1); predictingthepast replaces them with '-'. A system that reads supplements set beside a baseline that masks them is not a like-for-like comparison, hence the fixed preparations (G) and (M). 210 T texts have unbalanced brackets, so apply each dataloader's steps literally.
- Both inference codes reject inputs of 768 or more characters ('Input text too long'): 662 T texts under (G), 663 under (M). Ithaca's also rejects inputs under 50 characters: 40 T texts under (G). The criterion fixes a 767-character cut and '-' padding so the baseline files are reproducible; the claimant's own system may read whole texts.
- checkpoint_v1.pkl predicts the 2022 subregions (84 regions in the paper; 88 entries in google-deepmind/ithaca train/data/iphi-region-sub.txt) while predictingthepast's iphi-region-sub.txt lists 82; map by name with region_name_filter and count unmappable predictions as misses, for the claimant too.
- Dates in the test digit run from -750 to 1881; records outside [-800, 800] are excluded from T_d.
- One stone can carry several PHI ids (re-editions): 201 T records have an exact textual twin under an id of another digit (172 in a training digit; 223 counting twins inside digit 3), which the released checkpoints may have been trained on (predictingthepast drops repeated texts, keeping the lowest id). Report results with and without them. Under the near-duplicate rule, with '[' and ']' deleted as the criterion's normalisation says, 5,577 training-digit records (3.9%) share a 60-character run with a record of T and 5,687 must be dropped in all (recounted 2026-10-30); keeping the brackets finds only 2,167, so normalise exactly as stated.
- PHI texts and their dates are on the open web; models with undisclosed pretraining may have memorised them.
- Ithaca Revisited's 71.11% and 33.98 years were measured on inputs with artificial gaps, not on full texts; don't mix protocols.
- Released checkpoints are Python pickles; load them only in a sandbox.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/iphi-greek-inscription-attribution-ithaca.md
```

Already set up? Say `run V3R1T4S on iphi-greek-inscription-attribution-ithaca`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iphi-greek-inscription-attribution-ithaca`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
