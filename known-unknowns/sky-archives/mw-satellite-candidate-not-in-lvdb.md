# New Milky Way satellite (ultra-faint dwarf or faint halo star cluster) in public DECam or Legacy Surveys catalogues, absent from the Local Volume Database

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-days (Astro Data Lab TAP queries of DELVE DR3 / Legacy Surveys DR10 healpix pixels; a full-footprint matched-filter scan covers a few hundred GB of catalogue rows) · open as of 2026-10-30

## The problem

The Local Volume Database (LVDB; Andrew B. Pace; Pace 2025, OJAp 8, 142, arXiv:2411.07424; github.com/apace7/local_volume_database, last commit 2026-10-29) lists 68 Milky Way dwarf satellites and candidates (dwarf_mw.csv) and 58 recently found Galactic star clusters (gc_mw_new.csv), plus ambiguous systems (gc_ambiguous), Harris globular clusters and Local Group dwarfs. Discoveries continue: 2026 brought Aquarius IV (Cerny et al., arXiv:2608.02601, found in Rubin Observatory Early Data Preview 2 and confirmed at ~6 sigma in archival DECam imaging) and DELVE 8 / Gemini I (Overdeck et al., arXiv:2606.09975, found in DELVE DR3), both already in the LVDB, alongside deep follow-ups of known systems such as Virgo III (Pai et al., arXiv:2607.25044) and Grus II / Horologium II (Prabhu et al., arXiv:2606.25058). Searches build on the DELVE survey (Drlica-Wagner and collaborators; DR3 on NOIRLab Astro Data Lab) and the DES/PS1 satellite census (Drlica-Wagner et al. 2020, ApJ 893, 47). Open task: find a resolved stellar overdensity in openly public catalogues that passes the community's search thresholds and is in no LVDB table and no paper.

## What counts as a win

A saved bundle (ADQL queries against delve_dr3.coadd_objects and/or ls_dr10.tractor on datalab.noirlab.edu, star/galaxy and quality cuts, matched-filter code, isochrone, member list, CMD and maps) where: (1) in one catalogue, the isochrone-weighted matched-filter ('simple'-style) Poisson significance is >= 6 sigma and a maximum-likelihood (ugali-style) fit gives TS >= 36; (2) an independent reduction gives >= 4 sigma at the same position: the other of DELVE DR3 / Legacy Surveys DR10, or DES DR2, Pan-STARRS1 DR2 or HSC-SSP PDR3 where deep enough; (3) an old metal-poor isochrone fits the CMD of stars within r_h better than the local field does (likelihood-ratio test reported); (4) the overdensity is made of point sources, lies outside bright-star and bad-region masks, and is not a galaxy cluster or background galaxy (no catalogued galaxy cluster or galaxy group within 3 arcmin); (5) there is no entry in any LVDB table (every CSV under data/ on the main branch: dwarf_mw, dwarf_local_field, dwarf_local_field_distant, dwarf_m31, gc_harris, gc_mw_new, gc_ambiguous, gc_other, gc_dwarf_hosted) within max(3 r_h, 3 arcmin), no SIMBAD object within 3 arcmin whose type is a dwarf galaxy, globular or open cluster, star cluster, association, or galaxy group or cluster (or a candidate of these), and no arXiv paper reports it (LVDB and arXiv re-fetched immediately before claiming). Unrelated background galaxies listed in SIMBAD do not by themselves disqualify a point-source overdensity that passes (4).

## Partial wins

- **p1:** Inside a declared footprint of >= 500 deg^2 containing >= 3 LVDB Milky Way satellites that the discovery papers detected in the same catalogue, the pipeline recovers >= 90% of them at >= 5 sigma, and reports its false-positive count after cuts (4).
- **p2:** A new overdensity meeting (3)-(5) with a matched-filter significance between 5 and 6 sigma, logged as a sub-threshold candidate.
- **p3:** For a new candidate meeting (1)-(5): >= 3 Gaia DR3 stars on the isochrone whose proper motions agree within 2 sigma and differ from the field mean.

## How a win is checked

Skeptic re-runs the saved ADQL on Astro Data Lab, recomputes the matched-filter map and likelihood with the saved code, checks masks and galaxy-cluster catalogues, and cross-matches the LVDB CSVs fetched from GitHub. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/apace7/local_volume_database>

## Sources

- <https://github.com/apace7/local_volume_database>
- <https://raw.githubusercontent.com/apace7/local_volume_database/main/data/dwarf_mw.csv>
- <https://raw.githubusercontent.com/apace7/local_volume_database/main/data/gc_mw_new.csv>
- <https://datalab.noirlab.edu/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT+table_name+FROM+tap_schema.tables+WHERE+schema_name='delve_dr3'>
- <https://www.legacysurvey.org/dr10/description/>
- <https://arxiv.org/abs/1912.03302>
- <https://arxiv.org/abs/2608.02601>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Regions with new deep coverage in DELVE DR3 or Legacy Surveys DR10/DR11 (northern DECam fields, low-latitude edges) that no published census has searched.
- Cross-domain import (particle physics): correct for the look-elsewhere effect by running the same pipeline on sky-rotated catalogues to calibrate the trials factor.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Distant galaxy clusters and compact groups mimic faint stellar overdensities when star/galaxy separation fails near the limit; check morphology and redshift catalogues.
- Survey-depth edges, chip gaps and bright-star halos produce 'overdensities'; work on depth-normalised maps.
- LVDB lists systems under many names and some only in the ambiguous tables; match by coordinates across every CSV.
- The LVDB lags new papers by weeks: Rubin-GC1 (arXiv:2609.15872, 2026-09-14) was in no LVDB CSV on 2026-10-30, so the arXiv check is not optional. The withdrawn Yasone-1 to -3 candidates (arXiv:2509.15345) are not in the LVDB either; re-detecting one is not a new discovery and must be stated.
- Rubin Observatory preview data are restricted to data-rights holders; use only catalogues that are openly public.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/mw-satellite-candidate-not-in-lvdb.md
```

Already set up? Say `run V3R1T4S on mw-satellite-candidate-not-in-lvdb`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mw-satellite-candidate-not-in-lvdb`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
