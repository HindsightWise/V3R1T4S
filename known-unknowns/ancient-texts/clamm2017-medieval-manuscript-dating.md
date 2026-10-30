# Medieval manuscript dating (ICDAR 2017 CLaMM tasks 3 and 4): beat 59.0% and 49.9% date-class accuracy on the released test sets

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (about 12 GB of TIFF and JPEG page images; a GPU helps); scoring needs only two CSV files · open as of 2026-10-30

## The problem

The ICDAR 2017 Competition on the Classification of Medieval Handwritings in Latin Script (CLaMM; Cloppet, Eglin, Helias-Baron, Kieu, Stutzmann and Vincent, ICDAR 2017, pp. 1371-1376, doi 10.1109/ICDAR.2017.224) set four tasks on a 3,540-image training set: script class (tasks 1 and 2) and date class (15 classes from 500 to 1600 CE; task 3 on 2,000 clean 300-dpi greyscale TIFFs, task 4 on 1,000 images of varied formats and resolutions). Best published accuracies, tasks 1 to 4: 85.2% (Tensmeyer, T-DeepCNN), 76.5% (Christlein and Kestemont, method 2), 59.0% (T-DeepCNN) and 49.9% (Christlein and Kestemont, method 2), as tabulated in the survey of Nikolaidou, Seuret, Mokayed and Liwicki (arXiv 2203.08504v3). The full dataset, with the test ground truth and all competitors' output matrices, is on Zenodo (record 5527690, doi 10.5281/zenodo.5527690, CC BY 4.0, deposited 2021-09-25 by Stutzmann and Helias-Baron). Re-scored on 2026-10-29 from those files (argmax of each belonging matrix, columns in header order where the file has a header): task 3, Tensmeyer's T-DeepCNN (a residual CNN on 227x227 patches averaged per image) 1,181 of 2,000 = 0.5905, adjacent-class 0.8865; Christlein and Kestemont method 2 0.5485 (method 1 0.5415, method 3 0.5255); Pondenkandath 0.4980. Task 4: Christlein and Kestemont method 2 499 of 1,000 = 0.499 (its matrix orders columns DATE_TYPE1, DATE_TYPE10, ..., DATE_TYPE9, as its header says), Tensmeyer 0.480. One task-3 ground-truth row names IRHT_P_009783.tif, but the zip ships that image as IRHT_P_009793.tif, the name all four task-3 output files use; Tensmeyer's prediction for it is wrong, so its 1,181 stands either way. Status 2026-10-28: no later result on the official task 3 or task 4 test sets was found. Later dating work on CLaMM data uses other splits or metrics (the 2024 'deep-dating' models on Hugging Face use 5-fold cross-validation; a 2023 DenseNet study by Boudraa and Bennour reports cumulative score and MAE; Studer et al., ICDAR 2019, reach at best 37.9% dating accuracy), and the ICDAR 2021 HDC dating task has its own test set scored by mean absolute error in years. The original site clamm.irht.cnrs.fr did not respond on 2026-10-29.

## What counts as a win

Frozen prediction files (one date class from 1 to 15 per test image, hashes committed before scoring) for all 2,000 images of ICDAR2017_CLaMM_task1_task3 and all 1,000 images of ICDAR2017_CLaMM_task2_task4, scored against the DATE_ICDAR column of the zips' own @ICDAR2017_CLaMM_task1_task3.csv (sha256 adf733bf867b61820c89cb37b0318b21e4edfecffd783277886d0af503081d55) and @ICDAR2017_CLaMM_task2_task4.csv (sha256 25e4d61e1d90d76953f5fb9c311c09c8b1b020874902647a45683816e85343ad), with file names matched on the lower-cased stem and the ground-truth row IRHT_P_009783.tif scored as the image IRHT_P_009793.tif, must reach plain per-image accuracy strictly above 0.5905 on task 3 (at least 1,182 of 2,000 correct; the record, Tensmeyer's T-DeepCNN, printed as 59.0%, re-scores to 1,181) AND strictly above 0.499 on task 4 (at least 500 of 1,000; Christlein and Kestemont method 2 re-scores to 499), both record values re-read from the competition paper or arXiv 2203.08504 and re-scored from the Zenodo output matrices before claiming. Training and model selection use only the ICDAR2017_CLaMM_Training images and labels; generic image models pretrained without any manuscript script or date labels are allowed and must be named; no test image is used for training or adaptation, and no other dated-manuscript collection (ICFHR 2016 CLaMM, ICDAR 2021 HDC, e-codices, IRHT or BnF metadata) may be used.

## Partial wins

- **p1:** Task 3 only: accuracy of at least 0.600 (1,200 of 2,000) on the 2,000 clean test images, same rules.
- **p2:** Task 4 only: accuracy of at least 0.510 (510 of 1,000) on the 1,000 varied test images, same rules.
- **p3:** Task 3: exact accuracy strictly above 0.5905 (at least 1,182 of 2,000) together with adjacent-class accuracy (prediction within one date class of the truth) strictly above 0.8865 (at least 1,774 of 2,000; Tensmeyer's re-scored value with the file-name mapping is 1,773), same rules.

## How a win is checked

The verifier fetches only the two ground-truth CSVs from the Zenodo zips by ranged GET (the central directory at the end of each zip gives the offsets; a few hundred kilobytes in all, no images), checks their sha256, checks the prediction files' hashes against the commitments, and recomputes exact and adjacent-class accuracy with independent code, matching file names on the lower-cased stem and scoring the ground-truth row IRHT_P_009783 as image IRHT_P_009793. It re-scores the competitors' matrices from ICDAR2017_CLaMM_outputs.zip (argmax per row, column order from each file's header where present) to confirm the record counts (task 3: 1,181 of 2,000; task 4: 499 of 1,000). Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zenodo.org/records/5527690>

## Sources

- <https://zenodo.org/records/5527690>
- <https://arxiv.org/abs/2203.08504>
- <https://huggingface.co/nikolai40/deep-dating>
- <https://lme.tf.fau.de/competitions/icdar-2021-competition-on-historical-document-classification/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Modern self-supervised vision backbones on text-region patches with per-image aggregation; the 2017 winner trained a residual CNN from scratch on 227x227 patches.
- Date classes are ordinal: train with ordinal losses or soft labels over neighbouring classes. Adjacent-class accuracy is already 0.886 on task 3, so most errors are one class off.
- Use the script labels in the same CSVs as an auxiliary task; script and date are strongly correlated.
- Task 4 images vary in format and colour: normalise resolution (estimate x-height) and convert to greyscale to match the training conditions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- File names differ in case and extension between ground truth and some outputs (.tif, .TIF, .jpg, .JPG): match on the lower-cased stem. One task-3 ground-truth row (IRHT_P_009783.tif) has no image of that name; the zip ships it as IRHT_P_009793.tif, which has no ground-truth row and which every 2017 task-3 output uses. Score the two as one image.
- The output matrices do not share a column order: Christlein and Kestemont's method 2 and 3 files carry a header in lexicographic class order. Read headers, or re-scored records come out wrong (method 2 on task 4 scores 0.105 read in natural order and 0.499 read by its header).
- Class sizes are uneven: class 10 has 352 of the 2,000 task-3 images, class 15 only 6 (4 in task 4).
- The competition paper speaks of accuracy 'per date'; plain per-image accuracy reproduces 59.0% for task 3 from the released matrix (1,181 of 2,000 = 0.5905), while mean per-class recall is 0.494. The criterion is plain accuracy, with thresholds at the re-scored counts: 1,181 correct on task 3 or 499 on task 4 only ties the record.
- Generic backbones pretrained on web images may have seen digitised pages of the same manuscripts, but never their labels; any model trained with manuscript date or script labels from outside the CLaMM 2017 training set is excluded.
- The task 3 and task 4 zips are 3.1 and 3.3 GB and the training zip 5.5 GB; scoring needs only the CSVs inside.
- ieeexplore.ieee.org (the competition paper) and link.springer.com answer plain fetches with an empty 202 or a JavaScript challenge; read the results in arXiv 2203.08504 or re-score the Zenodo matrices instead of getting around them. Two Springer chapters that cite the competition and date manuscript images could not be read for that reason: Boudraa and Bennour (ISPR 2023, reported elsewhere as cumulative score and MAE) and Sakout, Nait-Hamoud, Gahmousse, Djeddi and Ennaji ('Accurate Dating of Ancient Manuscripts with SIFT-CNN', 2025). Have a human check their protocols before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/clamm2017-medieval-manuscript-dating.md
```

Already set up? Say `run V3R1T4S on clamm2017-medieval-manuscript-dating`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `clamm2017-medieval-manuscript-dating`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
