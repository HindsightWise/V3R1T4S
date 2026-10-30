# First significant sub-solar-mass compact-binary candidate in public LIGO-Virgo strain (O1-O4b)

🔭 **Sky archives** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for a full search (sub-solar templates stay in band for minutes; Kacanja et al. needed about 25 million templates for O4a); laptop-hours to re-analyse the published outliers; laptop-days for a reduced bank over one month · open as of 2026-10-30

## The problem

Stellar evolution is not expected to make neutron stars or black holes below about 1 Msun, so a sub-solar-mass (SSM) merger would point to primordial black holes or dark-matter black holes. Searches of public strain have produced only marginal outliers. SSM200308 in O3b had search SNR 8.90 and FAR about 1 per 5 years (Prunier et al., arXiv:2311.16085). In O4a, the LVK (arXiv:2605.05444) and Kacanja, Soni, Akyuz and Nitz (arXiv:2602.12115, a public-data search with about 25 million templates) found no significant candidate. In O4b, the LVK search (arXiv:2610.20276, 2026-10-14; secondary 0.2-1 Msun, primary 0.2-10 Msun) reports two outliers that it judges consistent with noise. S240422ed (2024-04-22 21:35:13.42 UTC) has GstLAL SSM FAR 0.015/yr and was not confirmed by MBTA or PyCBC. S241229bq (2024-12-29 13:52:36.83 UTC) has MBTA FAR 0.0043/yr, about 2.8 sigma before trials, against 34/yr in GstLAL and 7.7/yr in PyCBC, and its SNR fell when the low-frequency cutoff was lowered. Table 1 of that paper also lists a third MBTA candidate (2025-01-02 09:44:02.30 UTC, FAR 1.3/yr, network SNR 10.6, a two-detector coincidence that includes Virgo) that the LVK judges consistent with noise. Christensen, Cornish, Kuhnel, Sakellariadou and Villares Guanga (arXiv:2607.23119) ran Bayesian PE on the seven most significant LVK O4a SSM triggers and on four triggers reported by other groups; several may contain a sub-solar component, but none is significant in its search. Kacanja, Soni and Nitz searched O4a+O4b public data (arXiv:2610.19329, 2026-10-14; primary 0.1-2 Msun, secondary 0.1-1 Msun, tidal deformabilities up to 7e5) and found no significant candidate (their most significant has FAR 0.6 per year). Miller (arXiv:2609.16238) found none for chirp masses 0.01-0.1 Msun in O4a+O4b. O4c strain is not public; it holds the SSM public alert S251112cm (MBTA SSM online FAR about 1 in 6 years, revised to about 1 in 4 years; GCN Circulars 42650 and 42690) and the sub-threshold SSM candidate S250818k. Open task: a sub-solar-mass candidate in public strain that stays significant after trials and that an independent second search recovers.

## What counts as a win

A saved candidate package (GPS time, detectors, template parameters, search code and configuration, trigger and time-slide background files, PE samples, and the excess-power scan of criterion (4)) for a candidate in GWOSC strain from any public run (O1 to O4b) such that: (1) the claimant's search, over a pre-declared span and template bank, gives FAR <= 1e-3 per year (IFAR >= 1000 yr) from an inclusive time-slide background with livetime at least 10 times that IFAR, after multiplying by the number of banks, spans and searches tried; (2) a second, independently implemented search of a different pipeline family (for example PyCBC-style vs GstLAL-style vs MBTA-style) recovers it within 0.05 s at FAR <= 1 per year; (3) Bayesian PE on the GWOSC strain gives a 90% upper bound on the secondary source-frame mass below 1.0 Msun, with a network SNR posterior median >= 8; (4) the time passes the GWOSC CBC_CAT1 bit in each detector used, no hardware injection is listed near it, no glitch with SNR > 8 lies in band within the template's last 10 s in either detector (checked with an Omicron or GWpy Q-transform scan of the GWOSC strain run by the claimant, and for O1-O3 times also against the Gravity Spy O1-O3 classifications, Zenodo 5649212; the O4a and O4b open-data papers describe no public O4 glitch list), and in each detector the SNR, as the low-frequency cutoff is lowered, follows the template's expected accumulation within 1 sigma (the check that weakened S241229bq); and (5) the claim states its relation to SSM200308, S240422ed, S241229bq, the other candidates in Table 1 of arXiv:2610.20276, the candidates in Table 1 of arXiv:2610.19329 and the O4a triggers analysed in arXiv:2607.23119, and exceeds every published significance for the same time, with arXiv:2610.20276, arXiv:2610.19329 and later SSM papers re-fetched live immediately before claiming.

## Partial wins

- **p1:** A candidate meeting criteria (2)-(5) with 100 yr <= IFAR < 1000 yr after trials in the claimant's search; once trials are counted, this already exceeds both LVK O4b outliers.
- **p2:** An independent re-analysis of public O4b strain that recovers both LVK O4b outliers (S240422ed and S241229bq) within 0.05 s, with network SNR within 10% of the Table 1 values of arXiv:2610.20276, and reports their FAR from its own inclusive background (a reproducibility check).

## How a win is checked

Skeptic downloads the GWOSC strain around the candidate (several minutes, since SSM templates are long), re-filters it with the saved template to reproduce SNR, chi-squared and the SNR-versus-cutoff behaviour, reruns the second search near the time, spot-checks the background by rerunning a subset of time slides with new offsets, reruns PE (relative binning or a reduced-order likelihood keeps this to hours), and compares with the LVK and Nitz-group tables. Hours to days.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=%28abs:%22sub-solar%22+OR+abs:subsolar%29+AND+%28abs:gravitational+OR+abs:LIGO%29&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://arxiv.org/abs/2610.20276>
- <https://arxiv.org/abs/2610.19329>
- <https://arxiv.org/abs/2605.05444>
- <https://arxiv.org/abs/2602.12115>
- <https://arxiv.org/abs/2311.16085>
- <https://arxiv.org/abs/2609.16238>
- <https://arxiv.org/abs/2607.23119>
- <https://gcn.nasa.gov/circulars/42690>
- <https://gwosc.org/eventapi/json/allevents/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a reduced SSM bank aimed at the region the LVK banks under-cover, for example the high aligned spins of S240422ed (the GstLAL low-latency SSM bank limits |chi| to 0.3), run with PyCBC and time slides.
- Hierarchical or ratio-filter de-chirping methods (Soni and Nitz, arXiv:2409.11317) make long templates affordable on one machine.
- Cross-domain import (sonar and radar long-pulse detection): stack-slide semi-coherent statistics over minutes-long chirps before a full coherent follow-up.
- Cross-domain import (particle physics look-elsewhere corrections): pre-register the bank and trials count, then compute a global p-value from toy backgrounds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- SSM templates stay in band for minutes, so non-stationary noise over that time drives the background; a short-segment PSD estimate inflates significance.
- S240422ed was first a stellar-mass candidate (chirp mass about 1.7 Msun, chi_eff above 0.75); a high-spin stellar-mass signal can land in an SSM bank with biased masses, and criterion (3) is what makes a candidate sub-solar.
- The LVK notes that an outlier's false-alarm probability rises by about an order of magnitude once several pipelines are considered; count every search and bank you ran.
- O4c alerts such as S251112cm cannot be analysed yet: O4c strain is not public (the GWOSC data-sets page lists O4a and O4b only).
- Do not post to GraceDB, GCN or social media; the result is a candidate in a run report only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/gwosc-o4-subsolar-mass-binary-candidate.md
```

Already set up? Say `run V3R1T4S on gwosc-o4-subsolar-mass-binary-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gwosc-o4-subsolar-mass-binary-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
