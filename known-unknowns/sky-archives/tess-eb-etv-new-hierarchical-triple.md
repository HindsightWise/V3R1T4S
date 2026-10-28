# New hierarchical triple from eclipse-timing variations of a TESS eclipsing binary

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (2-min and FFI light curves for a few thousand EBs; per-system timing is seconds) · open as of 2026-10-28

## The problem

Eclipse-timing variations (light-travel-time and dynamical effects) reveal unseen third bodies around eclipsing binaries. TESS EBs have been searched in several ways:
- in and near the northern CVZ (Mitnyan et al. 2024, arXiv:2402.01486: >3,500 EBs searched, ETV solutions for 135 hierarchical triple candidates);
- for ~100 Villanova EBs (Marcadon & Prsa 2024, arXiv:2403.07694: ten new triple candidates);
- via Gaia DR3 non-single-star orbit cross-matches (Czavalinga et al. 2023, A&A 670, A75, arXiv:2212.02903);
- in the TESS Ten Thousand catalog (Kostov et al. 2025, arXiv:2506.05631).
Borkovits et al. 2025 (arXiv:2502.09480) extended the Kepler triples with TESS, and Borkovits, Rappaport and collaborators keep publishing TESS triply eclipsing triples (e.g. arXiv:2510.04565, 2609.25332, 2610.31200). Most of the 4,573 EBs in the live Villanova TESS EB catalog (counted 2026-10-28) outside the CVZs, and those in the southern CVZ, still have no published ETV solution. Open task: a statistically significant third-body ETV solution for a TESS EB not listed as a triple anywhere.

## What counts as a win

A saved bundle containing: the TIC ID, present in the live TESS EB catalog at https://tessebs.villanova.edu/ (re-fetched immediately before claiming); all eclipse mid-times with uncertainties measured from public TESS data, plus any archival ground-based times with their sources; and the fit code. In it:
(1) an LTTE (or LTTE+dynamical) model is preferred over a linear-plus-quadratic ephemeris by delta BIC > 20;
(2) primary and secondary ETVs are in phase, ruling out apsidal motion and spots;
(3) the fitted outer period is covered by >= 1.5 cycles, OR the amplitude is detected at > 10 sigma with phase coverage > 60%;
(4) the residual RMS is consistent with the timing errors;
(5) the system is absent from Mitnyan et al. 2024 (arXiv:2402.01486), Marcadon & Prsa 2024 (arXiv:2403.07694), Czavalinga et al. 2023 (arXiv:2212.02903), Kostov et al. 2025 (arXiv:2506.05631), Borkovits et al. 2025 (arXiv:2502.09480) and the Borkovits/Rappaport triply-eclipsing-triple series, and from ADS/arXiv by TIC/coordinate search.

## Partial wins

- **p1:** A third-body detection that meets every criterion but with outer-period coverage < 1.5 cycles (period lower limit only), with the anti-correlated/in-phase primary-secondary test passed.
- **p2:** Detection of a previously unreported tertiary eclipse in a TESS EB, confirmed by flux-centroid analysis to be on target.
- **p3:** A new apsidal-motion rate for an eccentric TESS EB not in published apsidal-motion compilations, with primary/secondary anti-correlated ETVs at > 10 sigma.

## How a win is checked

Skeptic re-extracts the TESS light curves (lightkurve/eleanor from MAST), re-measures a random subset of eclipse times with an independent template, refits the LTTE model and BIC comparison, and checks the catalogues by coordinates. Under an hour per system.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://tessebs.villanova.edu/>

## Sources

- <https://tessebs.villanova.edu/>
- <https://archive.stsci.edu/hlsp/tess-ebs>
- <https://archive.stsci.edu/>
- <https://arxiv.org/abs/2506.05631>
- <https://arxiv.org/abs/2502.09480>
- <https://arxiv.org/abs/2402.01486>
- <https://arxiv.org/abs/2403.07694>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: measure eclipse times per sector with a fixed per-system template, fit LTTE with an MCMC, and prioritise EBs with >= 6 sectors and long baselines (2018-2026).
- Add pre-TESS times from SuperWASP, KELT, ASAS-SN or Hipparcos epoch photometry to stretch the baseline for long outer periods.
- Cross-domain import (pulsar timing): use a timing-residual formalism with red-noise modelling (as in pulsar timing arrays) so spot-induced timing noise does not masquerade as a third body.
- Cross-domain import (geodesy / GNSS): treat eclipse times as a clock time series and use Allan-variance-style analysis to separate white timing noise from coherent signals.
- Use Gaia DR3 RUWE and astrometric acceleration solutions as independent priors pointing to triples.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Starspots shift measured eclipse times in anti-correlated fashion between primary and secondary; a third body produces in-phase runs.
- TESS sector-to-sector systematics and the 2-min vs 200-s/10-min cadence change can create offsets that a sparse ETV fit absorbs as signal.
- Blended EBs in large TESS pixels: the EB may not be the target star; centroid tests needed before any physical interpretation.
- Many TESS EB triples are already in Mitnyan 2024 / Zasche 2022 / the Gaia-NSS cross-match under a TIC ID or a GCVS/ASAS name; search by coordinates.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/tess-eb-etv-new-hierarchical-triple.md
```

Already set up? Say `run V3R1T4S on tess-eb-etv-new-hierarchical-triple`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tess-eb-etv-new-hierarchical-triple`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
