# New coherent X-ray periodicity in an archival XMM-Newton or Chandra source (5XMM-DR15 / CSC 2.2), confirmed independently and absent from period catalogues

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (pipeline event lists are tens to hundreds of MB per observation from the XMM-Newton Science Archive and the Chandra Data Archive) · open as of 2026-10-30

## The problem

5XMM-DR15 (XMM-Newton Survey Science Centre; HEASARC table xmmssc) has 818,656 unique sources from 14,616 EPIC observations made 2000-01-19 to 2024-10-14, almost half of them with more than one detection. The Chandra Source Catalog 2.2 (Chandra X-ray Center, released 2026 October) has 432,713 sources from ACIS and HRC-I observations public to the end of 2023. The EXTraS project (De Luca et al. 2021, A&A 650, A167) searched EPIC data up to 2012 for pulsations and found, e.g., the ~1 s pulsations of NGC 5907 ULX-1 (Israel et al. 2017). Its public archive v2.0 now carries only aperiodic variability (to 2020), and the original periodicity products are available only on request. No public catalogue-wide periodicity product was found for EPIC data after 2012 or for CSC 2.2. Single-source papers and ATels still report many periods, so absence must be checked source by source. Open task: find a coherent periodicity (spin or orbital) in the archival event data of a catalogued source that no catalogue or paper reports.

## What counts as a win

A saved bundle (ObsIDs, event-file names, source and background regions, barycentred times, search grid, code) where: (1) a Z^2_n (n <= 4) or Rayleigh search gives post-trial significance >= 4.5 sigma, with red-noise-aware significance (power-law noise model fitted to the source's own power spectrum) and trials = frequencies x harmonics x sources searched, declared before the search; (2) the same period (within 3 sigma, allowing a declared |Pdot|) is found at >= 3 sigma single-trial in an independent dataset: another observation, or a different detector (EPIC-pn vs MOS for P > 5.2 s; Chandra vs XMM); (3) the period is not within 0.5% of a harmonic of the instrument frame time, of the Chandra dither periods for Chandra data (ACIS 707 s and 1000 s; HRC 768 s and 1087 s), or of the spacecraft orbit, and it is absent in the background region and in a nearby comparable source; (4) no counterpart within max(3 sigma position error, 5 arcsec) has a period within 1% (or a harmonic of one) in SIMBAD, VSX, ATNF psrcat, the Ritter and Kolb CV catalogue, or the Fortin et al. 2023 HMXB and Neumann et al. 2023 LMXB catalogues, and no arXiv or ATel report exists (re-fetched immediately before claiming).

## Partial wins

- **p1:** Pipeline recovers >= 20 known periodic X-ray sources (pulsars, intermediate polars, polars, eclipsing binaries) from archival event files at their catalogued periods, and shows < 1 false detection per 1000 sources on time-scrambled events.
- **p2:** A candidate meeting (1), (3) and (4) in one dataset without independent confirmation.
- **p3:** First X-ray detection of a period already known at other wavelengths (e.g. the optical or TESS period of a CV candidate in VSX), meeting (1)-(3), with no X-ray period reported before.

## How a win is checked

Skeptic downloads the event files from the XSA or the Chandra Data Archive, re-runs barycentring (barycen / axbary) and the Z^2 search with an independent code (e.g. Stingray or HENDRICS), recomputes the trials and checks the period catalogues. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://heasarc.gsfc.nasa.gov/W3Browse/xmm-newton/xmmssc.html>

## Sources

- <https://heasarc.gsfc.nasa.gov/W3Browse/xmm-newton/xmmssc.html>
- <https://www.cosmos.esa.int/web/xmm-newton/xsa>
- <https://cxc.cfa.harvard.edu/csc/>
- <https://extras.inaf.it>
- <https://www.aanda.org/articles/aa/full_html/2021/06/aa39783-20/aa39783-20.html>
- <https://cda.harvard.edu/chaser/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Galactic-plane sources with hard spectra and >= 500 counts in post-2012 EPIC-pn data: the intermediate-polar and HMXB population that EXTraS-era searches did not cover.
- Stack repeat observations semi-coherently for faint sources with many detections in 5XMM-DR15.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Chandra dither (ACIS 707 s and 1000 s; HRC 768 s and 1087 s) and XMM attitude or frame-time effects produce spurious periods; test the background and the neighbours.
- Red noise from aperiodic variability makes white-noise false-alarm probabilities far too optimistic.
- Many periods are published only in ATels or in papers on single sources; search by coordinates, not names.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/xmm-chandra-archival-new-xray-periodicity.md
```

Already set up? Say `run V3R1T4S on xmm-chandra-archival-new-xray-periodicity`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `xmm-chandra-archival-new-xray-periodicity`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
