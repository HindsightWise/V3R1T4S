# New compact-binary merger candidate in public O4a/O4b LIGO-Virgo strain that GWTC-4.1, GWTC-5.0 and the community catalogs do not list

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-days for one month of data to needs cluster for a whole run (H1+L1 4 kHz strain is roughly 100 GB per month, our estimate from 4096-s HDF5 files; a broad BBH template bank over all of O4a and O4b is cluster-scale; re-ranking the released sub-threshold triggers needs only data around each one and takes laptop-hours) · open as of 2026-10-30

## The problem

The LIGO-Virgo-KAGRA (LVK) collaborations have released the strain from the first two parts of their fourth observing run through GWOSC: O4a (2023 May 24 to 2024 January 16, H1 and L1; open-data paper arXiv:2508.18079) and O4b (2024 April 10 to 2025 January 28, H1, L1 and V1; released 2026 May 26; open-data paper arXiv:2605.27090). GWTC-4.0 (arXiv:2508.18082) reported 128 new O4a candidates with p_astro >= 0.5; GWTC-4.1 updated the O4a results; and GWTC-5.0 (arXiv:2605.27225) added 161 O4b candidates, bringing the cumulative catalog to 390 candidates (391 rows in the GWOSC event-portal snapshot of 2026-05-27, Zenodo 20418856, still the latest snapshot version when checked). The LVK candidate data releases list every trigger with FAR < 2/day from GstLAL, MBTA, PyCBC and cWB, with p_astro and BAYESTAR skymaps: 1,456 for O4a (GWTC-4.1, Zenodo 20276095; 139 have p_terrestrial < 0.5 in at least one pipeline and no data-quality veto) and 1,886 for O4b (GWTC-5.0, Zenodo 20348004; 161 such). In O1-O3, independent searches of the same public strain found mergers the LVK had not listed: the IAS pipeline (Olsen et al. 2022; Mehta et al. 2025; Wadekar et al., arXiv:2312.06631), 4-OGC (Nitz et al. 2023) and AresGW (Koloniari et al. 2025). Malz, Russell, Ashton and Colombo (arXiv:2607.07272) re-rank the released sub-threshold candidates across the catalog and name the O4a and O4b candidates they up-rank. As of 2026-10-28 no independent catalog of new O4a or O4b mergers had appeared on arXiv, and the live GWOSC event list matched the 2026-05-27 snapshot event for event (671 entries). Open task: a two-detector compact-binary candidate in public O4a or O4b strain, found at FAR <= 1/yr by a search with its own time-slide background, that no LVK or community catalog lists.

## What counts as a win

A saved candidate package (GPS merger time to 0.01 s, detectors, best-fit template masses and aligned spins, SNR and reduced chi-squared per detector, the search code and configuration, the analysed segment list, the trigger and time-slide background files, and the excess-power scan of criterion (2)) such that: (1) the search covers a pre-declared span of at least 30 days of GWOSC O4a or O4b strain, and the candidate has FAR <= 1 per year from an inclusive background (the candidate's own single-detector triggers kept in the slides) built from at least 100 non-zero time slides, with background livetime at least 10 times the inverse of the claimed FAR, after multiplying by the number of searches, template banks and spans tried; (2) two detectors (H1 and L1, or two of H1, L1 and V1 in O4b) each have SNR >= 4.5 at the candidate with reduced chi-squared <= 2, the time lies inside the GWOSC data segments and passes the release's CBC_CAT1 data-quality bit in each detector used, no hardware injection is listed for that time, and, apart from the candidate's own chirp track, an Omicron or GWpy Q-transform scan of the GWOSC strain run by the claimant shows no excess-power trigger with SNR > 8 within 1 s in either detector (the O4a and O4b open-data papers describe no public Omicron or Gravity Spy trigger list); (3) Bayesian parameter estimation on the GWOSC strain (bilby or equivalent, with IMRPhenomXPHM or a newer model) gives a network matched-filter SNR posterior median >= 8; and (4) nothing lies within 1 s of it in the live GWOSC allevents list (https://gwosc.org/eventapi/json/allevents/, every catalog including marginal, discovery-paper and community lists), among the GWTC-4.1 and GWTC-5.0 candidate-release entries with p_terrestrial < 0.5 in any pipeline, or in any arXiv paper reporting O4 candidates (including the up-ranked candidates of arXiv:2607.07272), all re-fetched live immediately before claiming. A candidate listed in a candidate release with p_terrestrial >= 0.5 in every pipeline counts (a promotion), and the claim must say so.

## Partial wins

- **p1:** A candidate meeting criteria (2)-(4) with 1/yr < FAR <= 12/yr (once a month) in the claimant's search, the FAR coming from a background built by the rules of criterion (1), that is absent from all four LVK pipelines' FAR < 2/day candidate tables (a trigger every LVK search missed).
- **p2:** A new O3a or O3b candidate meeting criteria (1)-(4) on GWOSC O3 strain (with the O3 data-quality bits and hardware-injection lists in place of the O4 ones, and the glitch check also run against the Gravity Spy O1-O3 classifications, Zenodo 5649212), absent from GWOSC allevents, GWTC-2.1, GWTC-3 and their candidate releases, the IAS O3a, O3b and higher-harmonics catalogs (arXiv:2201.02252, 2311.06061, 2312.06631), 4-OGC (arXiv:2112.06878, including its sub-threshold list), AresGW (arXiv:2407.07820) and any other arXiv paper reporting O3 candidates (for example Kumar and Dent, arXiv:2403.10439), all re-fetched live immediately before claiming.
- **p3:** A saved, re-runnable search over at least 30 days of O4a or O4b strain that recovers at least 90% of the GWTC-4.1 or GWTC-5.0 candidates with FAR < 1/yr in that span at FAR <= 1/yr from its own time-slide background (method validation).

## How a win is checked

Skeptic downloads 4096 s of GWOSC 4 kHz strain around the candidate for each detector, re-filters it with the saved template (PyCBC or equivalent) to reproduce the per-detector SNR, chi-squared and time offset, reruns the saved pipeline's background on at least one week of the declared span with different slide offsets to check the FAR, checks the GWOSC segments, data-quality bits and hardware-injection list, reruns the excess-power scan around the time, reruns a short PE, and compares against the live GWOSC event list, both candidate releases and arXiv. Hours for the candidate checks; days for a full background rerun.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://gwosc.org/eventapi/json/allevents/>

## Sources

- <https://gwosc.org/eventapi/json/allevents/>
- <https://zenodo.org/records/20418856>
- <https://zenodo.org/records/20348004>
- <https://zenodo.org/records/20276095>
- <https://arxiv.org/abs/2605.27225>
- <https://arxiv.org/abs/2508.18082>
- <https://arxiv.org/abs/2508.18079>
- <https://arxiv.org/abs/2605.27090>
- <https://arxiv.org/abs/2607.07272>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a PyCBC-style matched-filter search with a bank aimed where LVK banks are coarse (high-mass, precessing or higher-mode BBHs), with time slides for background: the route by which the IAS pipeline found new O3 events.
- Re-rank the 3,342 released sub-threshold triggers (1,456 O4a + 1,886 O4b) with a coherent multi-detector statistic or a PE-based Bayes factor; a promotion needs only data around each trigger.
- Cross-domain import (radar CFAR detection): set thresholds per data-quality epoch from the local background instead of one global ranking statistic.
- Cross-domain import (ML ensembles, as in AresGW): an ML front end proposes triggers, matched filtering re-scores them, and time slides run on the combined statistic.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Use the inclusive background: removing the candidate's own triggers from the time slides inflates the significance of a loud trigger.
- Scattered-light and blip glitches mimic high-mass BBHs; check Gravity Spy/Omicron near the time and the shape of the SNR time series.
- In O4a, CAT2 flags were applied only to burst searches (arXiv:2508.18079); CBC_CAT1 is the release-defined bar for CBC times.
- gwosc.org did not resolve or answer from our network on 2026-10-29 (it answered about ten hours earlier); the Zenodo event-portal snapshots mirror the event list but lag updates by about a day.
- Do not post to GraceDB, GCN or social media; the result is a candidate in a run report only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/gwosc-o4-missed-cbc-candidate.md
```

Already set up? Say `run V3R1T4S on gwosc-o4-missed-cbc-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gwosc-o4-missed-cbc-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
