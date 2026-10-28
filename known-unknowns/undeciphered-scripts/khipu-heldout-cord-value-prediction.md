# Inka khipus: frozen structural model that predicts masked cord values on khipus outside khipu.db (Open Khipu Repository)

📜 **Undeciphered scripts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Inka khipus record numbers in a decimal knot code (Locke 1912) and show many arithmetic relations, such as top cords or marker cords that sum groups of pendants (Marcia and Robert Ascher's databooks). What the rest of the structure encodes (colour, attachment direction, ply, cord ordering, grouping) remains undeciphered.

The Open Khipu Repository (OKR; Zenodo doi:10.5281/zenodo.18025748) is administered by the Open Khipu Research Laboratory under Mackinley FitzPatrick. Its advisory board is Carrie Brezine, Mackinley FitzPatrick, Ivan Ghezzi, Sabine Hyland, Manuel Medrano and Jeffrey Splitstoser. The repository holds data/khipu.db (619 khipus, 54,403 cords, 110,677 knots, OKR numbers KH0001-KH0630; counts re-checked 2026-10-28). Separate folders hold khipus outside khipu.db (KH numbers issued 2025-12-19, files added 2025-12-22):
- Excel recording sheets for KH0631-KH0632 (SH001.xlsx), KH0633-KH0635 (three sheets), KH0638-KH0652 (fifteen linked-khipu sheets from the MNAAHP), KH0676 (JS01) and KH0702 (R4303), about 22 khipus in all;
- only JPG images of recording sheets for KH0653-KH0663;
- only PDFs for KH0674-KH0675.
The folder KH0002_0010 holds re-recordings of khipus already in khipu.db.

Recent baselines:
- Medrano and Urton (2018) on the Santa Valley census khipus;
- Contreras (arXiv:2607.00185, 2026), which clusters OKR khipus and classifies provenance but does not predict cord values;
- Zenil & Uthamacumaran (arXiv:2610.08861, 2026), whose khipu test recovers concealed cord-attachment parents slightly above chance but does not predict cord values.

The open question: how much of a khipu's numeric content can a structural model predict from the rest of the khipu? This is a direct, checkable measure of how much of the recording system is understood. Structure prediction is not decipherment; readings or narrative interpretations never count.

## What counts as a win

Protocol (all frozen before touching held-out data):
1. Train only on data/khipu.db.
2. Held-out set: every khipu recorded in an .xlsx recording sheet in an OKR data/ folder numbered KH0631 or higher (these are not in khipu.db) with at least 20 valued cords. Excluded: image-only and PDF-only records (such as KH0653-KH0663 and KH0674-KH0675), the KH0002_0010 re-recordings, and any held-out khipu whose cord-value sequence matches a training khipu (the number removed is reported). A sheet covering two KH numbers is scored as one unit.
3. Parsing of the held-out sheets is validated by hand on at least 3 khipus, and the share of unparseable cords is reported.
4. For each held-out khipu, mask a random 20% of cords' total knot values with a published seed. The model sees everything else (other values, colours, structure).
5. Score = exact-match accuracy of predicted integer values on masked cords.
6. Baselines run on the same masks: (b1) the most common value in that khipu; (b2) an exact Ascher-style sum-relation solver that fills a masked cord only when an observed relation forces it; (b3) b2 plus the nearest-neighbour value within the cord group.
7. CONFIRMED if the frozen model beats the best baseline by at least 5 percentage points of exact-match accuracy, with a 95% bootstrap CI over khipus that excludes 0, AND the gain survives removing any single held-out collection.
8. The model hash, seeds, the OKR commit and the held-out file hashes are published before scoring.
9. Re-check the OKR repository live before claiming, to make sure the held-out khipus have not been merged into khipu.db with changed data.

## Partial wins

- **p1:** Pre-registered relation prediction: a rule set learned only from khipu.db (for example 'cords of colour pattern P at group position k sum the preceding group') that predicts, before inspection, at least 10 exact sum relations in held-out khipus, with fewer than 20% false predictions, beating a permutation null that shuffles cord positions within khipus at p < 0.01.
- **p2:** Non-numeric signal: a frozen model shows that a non-numeric feature (colour, attachment direction or ply) improves held-out masked-value accuracy over the same model without it by at least 2 points, CI excluding 0.

## How a win is checked

Clone the OKR repository at the recorded commit, hash khipu.db and the held-out spreadsheets, regenerate masks from the published seed, run the frozen model and the three baselines, and recompute accuracy and the bootstrap CI. Confirm by date and commit that no held-out file was used in training.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/khipulab/open-khipu-repository>

## Sources

- <https://github.com/khipulab/open-khipu-repository>
- <https://zenodo.org/records/18025748>
- <https://arxiv.org/abs/2607.00185>

## Ideas to start from

Left out on purpose, so this page never spoils the hunt.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/undeciphered-scripts/khipu-heldout-cord-value-prediction.md
```

Already set up? Say `run V3R1T4S on khipu-heldout-cord-value-prediction`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `khipu-heldout-cord-value-prediction`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
