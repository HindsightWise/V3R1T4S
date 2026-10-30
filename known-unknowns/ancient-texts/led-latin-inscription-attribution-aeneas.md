# Latin inscriptions (LED): beat Aeneas on dating (13.4 years) and province attribution (72.3% top-1) on the id-digit-3 test split

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (180,205 inscriptions in a 62 MB JSON; released Aeneas checkpoint 146 MB; a GPU helps) · open as of 2026-10-30

## The problem

Aeneas (Assael, Sommerschield, Cooley, Shillingford, Pavlopoulos, Suresh, Herms, Grayston, Maynard, Dietrich, Wulgaert, Prag, Mullen and Mohamed, Nature 645, 141-147, 2025, published online 23 July 2025, doi 10.1038/s41586-025-09292-5) introduced the Latin Epigraphic Dataset (LED: EDR, EDH and EDCS_ETL inscriptions merged by Trismegistos id; 176,861 inscriptions in the paper) and split it by the last digit of the inscription id: 3 test, 4 validation, the rest training (predictingthepast dataloader, should_process_sample). Table 2 (LED test set): province attribution over 62 provinces top-1 72.3% / top-3 83.9% (the 'Province (Vision)' column: images used where available, about 5% of inscriptions); date distance 13.4 years (distance from the predictive mean date to the ground-truth range); restoration of up to 20 characters CER 40.5% / top-20 46.5% with the length given and 66.1% / 32.7% without; Ithaca retrained on LED 61.3% / 75.3%, 14.1 years, 43.5% / 44.2%; onomastics baseline 17.9% / 30.9%, 51.3 years. The released file led.json (storage.googleapis.com/ithaca-resources/models/led.json, 62,464,288 bytes, md5 e1be05c28b7c97490065486c8f82e3af equal to the GCS etag, last modified 2025-06-16) holds 180,205 records (id, text, date_min, date_max, region_main, region_sub, ...), 17,990 of them with id % 10 == 3. The Latin checkpoint aeneas_117149994_2.pkl (145,662,103 bytes, etag 0cdebf373bf3694ef413b00e2e830e8c) and the code (github.com/google-deepmind/predictingthepast, Apache-2.0 code, CC BY / CC BY-SA data, HEAD f2d17de7 of 2026-10-27, beam-search fix c8889e9c of 2026-10-21) are public. Status 2026-10-28: no published system beating Aeneas on LED was found; the closest 2026 work (arXiv 2608.28170, Zhang, Caraffa, Zuffrano, Modesti and Colavizza) restores unpublished Bolognese notarial documents, not LED.

## What counts as a win

On led.json (md5 e1be05c28b7c97490065486c8f82e3af), the test list T is every record with int(id) % 10 == 3 whose text, after deleting whitespace and the characters '-', '#' and '_', has at least 25 characters (15,381 records); the province list T_p is the records of T whose region_sub, mapped by region_name_filter of predictingthepast/util/region_names.py at a recorded commit, is one of the 62 names of train/data/led-region-sub.txt mapped the same way (15,192 records); the dating list T_d is the records of T with numeric date_min <= date_max, both inside [-800, 800] (8,164 records). The verifier recomputes all three lists. A frozen predictions file, whose hash is committed before scoring and which is made from each record's text alone (no images, metadata or id lookups), ranks the 62 provinces for every record of T_p and gives one point date (a year) for every record of T_d. Full win: province top-1 accuracy on T_p strictly above 72.3% AND mean date error on T_d strictly below 13.4 years (date error is 0 when the point date lies in [date_min, date_max], else the distance to the nearer bound; both paper values re-read from Table 2 immediately before claiming), AND both strictly better than the released checkpoint aeneas_117149994_2.pkl on the same lists, whose frozen predictions the claimant also publishes (hash committed before scoring), made with predictingthepast at a recorded commit no older than c8889e9c as follows: each record's text is prepared as the dataloader prepares it (LatinAlphabet.filter, which deletes '!,;?·', then lower-casing) and passed to attribute() text-only (vision_img=None); a prepared text of 768 or more characters (91 records of T), which attribute() rejects, is cut to its first 767 characters; the checkpoint's point date is its predictive mean (date_pred_avg of predicted_dates in predictingthepast/util/eval.py), the quantity the paper scores. Training uses only LED records with id % 10 not in {3, 4} (digit 4 for model selection) plus public non-epigraphic Latin text, all listed with hashes; none of that material may be a test record or a near-duplicate of one (same normalised text, or a shared run of 60 or more consecutive normalised characters with a record of T; normalised means lower-cased, with whitespace and the characters '-', '#' and '_' deleted), so a model initialised from aeneas_117149994_2.pkl, which was trained on such records, cannot claim the full win; models whose pretraining data is undisclosed cannot claim the full win.

## Partial wins

- **p1:** One attribution task only, same lists and rules: province top-1 strictly above 72.3% with top-3 strictly above 83.9%, or mean date error strictly below 13.4 years, beating both the Table 2 value(s) and the released checkpoint on the same records.
- **p2:** Restoration with the length given: on a sample file built from T by a published deterministic rule (for example 200 gaps per length L = 1..20 with a fixed seed, gaps placed only in text free of '-', '#' and '_'), frozen and hashed before any model is run, CER strictly below 40.5% and top-20 strictly above 46.5%, and both strictly better than the released Aeneas checkpoint's frozen predictions on the same file (beam 20, predictingthepast at a recorded commit no older than c8889e9c).

## How a win is checked

The verifier downloads led.json (md5 check) and, at the recorded predictingthepast commit, led-region-sub.txt and region_names.py; it regenerates T, T_p and T_d from the stated rule, checks both prediction files' hashes against the pre-scoring commitments, and rescores top-1, top-3 and mean date error with independent code. It re-runs the released Aeneas checkpoint on a random 300 records of T in a sandbox, with the stated preparation, 767-character cut and predictive-mean date, to confirm the baseline file (CPU, under an hour), and scans the published training manifest for test ids and near-duplicates (identical normalised text, shared 60-character runs). No retraining.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/predictingthepast>

## Sources

- <https://www.nature.com/articles/s41586-025-09292-5>
- <https://www.nature.com/articles/s41586-025-09292-5/tables/2>
- <https://github.com/google-deepmind/predictingthepast>
- <https://storage.googleapis.com/ithaca-resources/models/led.json>
- <https://storage.googleapis.com/ithaca-resources/models/aeneas_117149994_2.pkl>
- <https://github.com/google-deepmind/predictingthepast/commit/c8889e9c48>
- <https://arxiv.org/abs/2608.28170>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Retrieval-augmented attribution: the nearest training inscriptions by character n-gram TF-IDF carry province and date labels; ensemble a k-NN vote with a fine-tuned character transformer.
- Onomastics, tribes, military units and formula variants (D M, h s e, stipendia) carry place and date; a model with explicit name and formula features may beat a pure character model on short epitaphs.
- For dating, predict a distribution over ten-year bins and output the year minimising expected distance to the true range, rather than the predictive mean.
- Hierarchical labels: LED's region_main (2,068 places, present for 75,032 records) nests in the 62 provinces and is a useful auxiliary training target.
- Text-only inference is required, but object_type, inscription_type and monument_type (at least one of them present for 75,613 records) can serve as auxiliary losses during training.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 73 inscription texts of 40 or more characters occur verbatim both in the test digit and in other digits of the pinned led.json (counted 2026-10-29), 64 of them in a training digit that the released checkpoint was trained on; 96 records of T have an exact textual twin under an id of another digit (100 counting twins inside digit 3). Report results with and without those records.
- The near-duplicate rule removes training material: 1,252 training-digit records (0.9%) share a run of 60 or more normalised characters (lower-cased; whitespace, '-', '_' and '#' deleted) with a record of T, and 1,366 in all are dropped once records with the same normalised text as a record of T are added (recounted 2026-10-30).
- Table 2's 72.3% uses images where available (images are not in led.json); comparing a text-only system against it is conservative, and the released checkpoint is scored text-only.
- The paper's numbers come from Aeneas's own filtered test set; the lists here are defined by rule and differ, which is why the released checkpoint must be scored on the same lists.
- Province names in led.json and in led-region-sub.txt differ for about 5,800 records ('Samnium' and 'Sabina et Samnium', 'Thrace' and 'Thracia'); apply region_name_filter to both, or those records are silently dropped or miscounted.
- predictingthepast's attribute() does not apply LatinAlphabet.filter (raw ',' or '·' raises a KeyError) and rejects inputs of 768 or more characters; prepare texts as the dataloader does and apply the fixed 767-character cut, or the baseline file cannot be reproduced. The claimant's own system may read whole texts.
- Restoration beam search changed on 2026-10-21 (predictingthepast c8889e9c, 'Fix active beam deduplication and nucleus filtering'); record the commit used for every restoration baseline.
- Inscriptions, their dates and their provinces are on the open web (EDH, EDR, EDCS, Wikipedia; the Res Gestae is also in literary corpora), so near-duplicate scanning must cover any added non-epigraphic text.
- Dates outside [-800, 800] fall outside Aeneas's 160 ten-year bins and are excluded from T_d.
- The released checkpoint is a Python pickle; load it only in a sandbox.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/led-latin-inscription-attribution-aeneas.md
```

Already set up? Say `run V3R1T4S on led-latin-inscription-attribution-aeneas`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `led-latin-inscription-attribution-aeneas`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
