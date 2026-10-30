# SpikeForest ground-truth spike sorting: beat the best average accuracy in the SpikeForest table on the paired Boyden recordings (and the hybrid Janelia studies)

🧠 **Neuroscience** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per study (DANDI 000618 holds 125 NWB files, 145 GB in all; paired_boyden32c is 19 recordings of 32 channels) · open as of 2026-10-30

## The problem

SpikeForest (Magland, Jun, Lovero, Morley, Hurwitz, Buccino, Garcia, Barnett; eLife 2020) benchmarks spike sorters against ground truth. It scores the accuracy of each ground-truth unit, matches/(matches+false positives+false negatives), and averages over units with SNR >= 8. Its website now serves a frozen static table (dateUpdated 2019-12-11) of 2019-era sorters. The ground-truth recordings of the paired juxtacellular Boyden, Kampff and English sets and of the Janelia hybrid sets are public on DANDI as dandiset 000618. The best table values per study are: paired_boyden32c 0.678 (IronClust; JRClust 0.593); hybrid_drift_siprobe 0.903 (IronClust; KiloSort2 0.879); hybrid_static_siprobe 0.962 (KiloSort2); hybrid_drift_tetrode 0.837 (IronClust); hybrid_static_tetrode 0.927 (IronClust). On paired_boyden32c, KiloSort2 failed on 5 of the 19 recordings; averaged over the 6 SNR >= 8 units it did sort it reaches 0.813, so 0.678 is the best among sorters that completed every recording. Newer sorters (Kilosort4, MountainSort5, SpykingCircus2) are not in the table, and paired_boyden32c, with real ground truth, is the least saturated study.

## What counts as a win

Sortings of all 19 recordings of paired_boyden32c from dandiset 000618, produced by one sorter with one fixed parameter set chosen without the ground-truth units. The skeptic computes per-unit accuracy, matches/(matches+false positives+false negatives), against the NWB ground truth with SpikeInterface compare_sorter_to_ground_truth at the SpikeForest matching tolerance. The tolerance is calibrated by rerunning one open-source sorter from the table (for example SpykingCircus or MountainSort4) and reproducing its table cell within 0.02. The skeptic averages over the 10 units with true SNR >= 8 as listed in the table's trueSnrs, counting a failed recording as accuracy 0. The average must be STRICTLY HIGHER (direction: max), by at least 0.03, than both 0.678, the best table value among sorters that completed all recordings (re-fetched from spikeforest.flatironinstitute.org/api/studyanalysisresults/PAIRED_BOYDEN.json immediately before claiming), and any SpikeForest-protocol value for this study found by the NOVELTY check. In addition, its average over the 6 of those units that KiloSort2 sorted must be at least KiloSort2's 0.813.

## Partial wins

- **p1:** The same kind of win on hybrid_drift_siprobe: one fixed-parameter sorter's average accuracy over SNR >= 8 units strictly above 0.903 by at least 0.01.
- **p2:** The same kind of win on hybrid_drift_tetrode: strictly above 0.837 by at least 0.02.
- **p3:** Beat the table best on both hybrid static studies (0.962 siprobe, 0.927 tetrode) with one parameter set, by at least 0.005 each.

## How a win is checked

The skeptic downloads the relevant NWB assets from DANDI 000618 with the dandi client (no login), reruns the declared sorter and parameters (or loads the submitted sortings), recomputes the per-unit accuracies, checks the SNR filter against the table's trueSnrs, and compares the result with the static SpikeForest JSON. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://spikeforest.flatironinstitute.org/api/studyanalysisresults/PAIRED_BOYDEN.json>

## Sources

- <https://spikeforest.flatironinstitute.org/>
- <https://spikeforest.flatironinstitute.org/api/studyanalysisresults/PAIRED_BOYDEN.json>
- <https://dandiarchive.org/dandiset/000618>
- <https://elifesciences.org/articles/55167>
- <https://github.com/flatironinstitute/spikeforest>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run current Kilosort4, MountainSort5 and SpykingCircus2 with defaults first: no SpikeForest-protocol numbers for them appear in the table, and they may already clear the bars.
- Ensemble sorting (consensus across sorters) and drift correction (DREDge-style motion estimation) suit the drift hybrids.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- paired_boyden32c has only 10 units with SNR >= 8, so a single unit moves the average by about 0.1; report per-unit values.
- KiloSort2's paired_boyden32c entry has null accuracies on 5 recordings; the site may display its 0.813 partial average next to IronClust's complete 0.678. Compare like with like, as the criterion states.
- Tuning the sorter parameters per recording against the ground truth is leakage; one parameter set per study.
- The CRCNS hc-1 and MEA64C paired sets in the table are not on DANDI 000618 (CRCNS requires an account), so they are out of scope.
- The spikeforest Python package loads the stored 2019 sorting outputs through kachery-cloud, which requires a Google sign-in. Agents must not sign up; calibrate by rerunning an open-source sorter on the DANDI data instead.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/spikeforest-paired-hybrid-sorter-accuracy.md
```

Already set up? Say `run V3R1T4S on spikeforest-paired-hybrid-sorter-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spikeforest-paired-hybrid-sorter-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
