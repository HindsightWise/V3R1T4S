# First continuous gravitational-wave signal: a candidate in public LIGO data confirmed in an independent observing run

🔭 **Sky archives** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for broad all-sky searches (Einstein@Home scale); laptop-hours to days for targeted searches of known pulsars and for following a candidate up in narrow bands of GWOSC strain · open as of 2026-10-30

## The problem

Continuous gravitational waves (CWs) from spinning, deformed neutron stars have never been detected. In O4a data, the LVK targeted 45 known pulsars with three methods and found no signal (Abac et al., ApJ 983, 99, arXiv:2501.01495). Its upper limits beat the spin-down limit for 29 pulsars, and the lowest h0 limit, 6.4e-27, is for J0537-6910. An LVK narrowband search of 34 known pulsars in O4a+O4b data (arXiv:2603.25938) also found no signal; its tightest limit is about 2% of the Crab spin-down limit. LVK O4a searches toward 15 supernova remnants (arXiv:2603.25808), all-sky for isolated neutron stars from 20 to 2000 Hz (arXiv:2603.14168), all-sky for neutron stars in binaries (arXiv:2511.16863) and toward Scorpius X-1 (arXiv:2607.07765, whose outliers were ruled out with later O4 data) also found none. McGloughlin et al. (arXiv:2607.18219) searched public O4a data for J0435+3233 and set h0 < 5.8e-27. One Einstein@Home candidate survived the multi-stage follow-up of an O3a search with O3b and O4a data, O4a giving weaker evidence: the G347.3-0.5 outlier of Ming, Papa and collaborators (arXiv:2512.15672). Three pipelines then followed it up with the newly released O4b data and found no related standard CW signal in O4a or O4b (Mirasola et al., arXiv:2608.07662). Knee, Riles and Sun (arXiv:2608.07312) followed up 562 O4a radiometer candidates; none of their 21 outliers was recovered in O4b. GWOSC O4a and O4b data contain CW hardware injections for 18 simulated pulsars. Open task: a CW candidate in public data that is significant after trials in one run and predicted and recovered in an independent run.

## What counts as a win

A saved candidate (target: a known pulsar with its ephemeris, or a sky position; f0, f1 and any higher derivatives or binary parameters at a stated reference time; amplitude parameters) with the full search and follow-up code, such that: (1) in a pre-declared discovery data set from GWOSC (any of O3a, O3b, O4a or O4b), the candidate's detection statistic has false-alarm probability <= 1e-3 after the full trials factor of the declared search, with the noise distribution measured by running the identical pipeline on at least 1,000 off-source trials of the same data (bands shifted by at least 1 Hz, or sky positions at least 10 degrees away, avoiding instrumental lines); (2) in a later run not used for discovery (for example O4b after an O4a discovery), a coherent or semi-coherent follow-up at the parameters predicted from the discovery solution, with the prediction frozen before the data are analysed, recovers it with single-trial false-alarm probability <= 1e-3 against at least 1,000 off-source trials, and h0 agrees with the discovery value within 2 sigma; (3) H1-only and L1-only analyses each show the signal, with a ratio of detector SNRs within a factor 2 of the antenna-pattern expectation; (4) its frequency is not within 1 frequency bin of any line in the published LIGO line lists for those runs, and it matches none of the GWOSC hardware injections; and (5) it is not the G347.3-0.5 outlier or one of the 21 O4a radiometer outliers unless criterion (2) holds for it, and no published search has reported the same signal, with arXiv re-fetched live immediately before claiming.

## Partial wins

- **p1:** An outlier passing (1), (3) and (4) at post-trials false-alarm probability <= 1e-2 in one run, with the pre-registered follow-up in the second run reported whatever it shows.
- **p2:** For one of the 45 known pulsars of arXiv:2501.01495, a 95% upper limit on h0 from public O4a+O4b data that is lower (direction: min) than every published limit for that pulsar (the O4a targeted limit of arXiv:2501.01495 and, where one exists, the O4a+O4b narrowband limit of arXiv:2603.25938), calibrated with at least 200 software injections and checked by recovering the O4a hardware injection nearest in frequency.
- **p3:** Independent recovery of at least 15 of the 18 O4a CW hardware injections at their documented parameters from GWOSC strain, with a saved, re-runnable pipeline (method validation).

## How a win is checked

Skeptic downloads narrow bands of GWOSC strain around the candidate frequency for both runs (or builds SFTs from them with lalpulsar or PyFstat), reruns the saved coherent follow-up at the stated parameters with fresh off-source trials, checks the line lists and the hardware-injection table, and repeats the single-detector analyses. Hours for a follow-up; the discovery search itself is spot-checked, not rerun.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:%22continuous+gravitational%22&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://arxiv.org/abs/2501.01495>
- <https://arxiv.org/abs/2603.25938>
- <https://arxiv.org/abs/2512.15672>
- <https://arxiv.org/abs/2608.07662>
- <https://arxiv.org/abs/2608.07312>
- <https://arxiv.org/abs/2603.25808>
- <https://arxiv.org/abs/2603.14168>
- <https://arxiv.org/abs/2511.16863>
- <https://arxiv.org/abs/2607.07765>
- <https://arxiv.org/abs/2607.18219>
- <https://arxiv.org/abs/2508.18079>
- <https://arxiv.org/abs/2605.27090>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: targeted Bayesian, 5-vector or F-statistic searches on O4a+O4b together for pulsars with recent radio or X-ray timing that were not in the 45-pulsar O4a list.
- Follow up published outlier lists (Knee et al. 2026; Einstein@Home papers) in O4b with an independent pipeline.
- Cross-domain import (radio pulsar searching): acceleration searches and fast-folding ideas for CW sources in binaries.
- Cross-domain import (sonar narrowband tracking): hidden-Markov-model (Viterbi) tracking of spin wandering across long coherent segments.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- CW hardware injections are present in almost all O4a data (18 simulated pulsars); check the injection table first.
- Instrumental lines and combs dominate outlier lists; check the run's line list and single-detector consistency before anything else.
- The trials factor of a broad search is enormous; draw the off-source trials exactly as the search draws its templates, not from a quieter band.
- O4c strain is not public; a confirmation in O4b only counts if it was predicted from the O4a solution before the O4b data were analysed.
- Do not announce or post; the result is a candidate in a run report only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/first-continuous-gw-signal-confirmed-candidate.md
```

Already set up? Say `run V3R1T4S on first-continuous-gw-signal-confirmed-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `first-continuous-gw-signal-confirmed-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
