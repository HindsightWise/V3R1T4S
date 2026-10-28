# 🔭 Sky archives

New vetted candidates in public astronomy archives (never 'a planet', only 'a candidate').

**16 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [New periodic variable stars / eclipsing binaries absent from VSX, confirmed in two indepe…](new-periodic-variables-not-in-vsx.md) | harvest | laptop-hours (ZTF light curves are fetched per cone query, a few hundred KB each; TESScut 5x5-pixel cutouts are ~1 MB per sector; the CDS vsx.dat dump is 2.2 GB; Gaia and Chen+2020 catalogs are queried, not downloaded in full) |
| ★★★★☆ | [Reliable rotation periods for asteroids with no entry in the Asteroid Lightcurve Database…](asteroid-rotation-period-not-in-lcdb.md) | harvest | laptop-hours (per-object photometry is KB-MB; batch of thousands overnight) |
| ★★★☆☆ | [First true (dynamical) mass for an RV-detected companion from Hipparcos-Gaia acceleration…](hgca-rv-true-mass-unmeasured-companion.md) | harvest | laptop-hours (an orvara fit is minutes to an hour; data are KB) |
| ★★★☆☆ | [Hidden repeating FRB source among apparently one-off bursts in CHIME/FRB Catalog 2](chime-frb-cat2-hidden-repeater.md) | harvest | laptop-hours (catalog is a few MB; localisation maps tens of MB; Monte Carlo is minutes) |
| ★★★☆☆ | [New hierarchical triple from eclipse-timing variations of a TESS eclipsing binary](tess-eb-etv-new-hierarchical-triple.md) | harvest | laptop-hours (2-min and FFI light curves for a few thousand EBs; per-system timing is seconds) |
| ★★★☆☆ | [New microlensing event in public ZTF light curves absent from published ZTF, Gaia and OGL…](ztf-microlensing-event-uncatalogued.md) | harvest | laptop-hours to overnight (ZTF light-curve parquet files for selected fields are tens of GB) |
| ★★★☆☆ | [New vetted transit candidate in archival Kepler or K2 light curves (not in KOI/K2 candida…](kepler-k2-new-vetted-transit-candidate.md) | harvest | laptop-hours (do NOT fetch the full Kepler or K2 light-curve sets; restrict to a defined sub-sample under 200 GB, e.g. one K2 campaign (~20k targets, ~10 GB) or Kepler M dwarfs; pip install lightkurve transitleastsquares wotan triceratops astroquery) |
| ★★★☆☆ | [New vetted transiting-planet candidate in public TESS light curves (not in TOI/CTOI/Archi…](tess-new-vetted-transit-candidate.md) | harvest | laptop-hours (one sector of 2-min SPOC light curves is ~20,000 files / ~40 GB; keep any sub-sample under 200 GB, e.g. Tmag < 12 M dwarfs or a single sector; pip install lightkurve transitleastsquares wotan triceratops astroquery into a virtual environment first) |
| ★★★☆☆ | [Precovery of known asteroids in public ZTF / Pan-STARRS / DECam images, extending the obs…](asteroid-precovery-arc-extension.md) | harvest | laptop-hours (cutouts are ~1-10 MB each; orbit propagation is seconds; the limiting step is choosing objects whose back-propagated positions fall in archive coverage; MPCORB.DAT is 319 MB, NEA.txt is small) |
| ★★★☆☆ | [Unreported historical outburst (nova, dwarf nova or large-amplitude event) in DASCH DR7 c…](dasch-unreported-historical-outburst.md) | harvest | laptop-hours (API queries per field; cutouts are MB each) |
| ★★☆☆☆ | [New exocomet-transit candidate (asymmetric single dip) in public TESS light curves](tess-exocomet-dip-candidate.md) | harvest | laptop-hours (bright-star QLP/SPOC light curves for selected sectors are a few GB) |
| ★★☆☆☆ | [New single-/duo-transit long-period candidate in Kepler or TESS light curves](kepler-tess-single-transit-long-period-candidate.md) | harvest | laptop-hours (single-event search is cheap; the cost is downloading: use the tesscurl sector scripts for a defined bright sub-sample or Kepler PDCSAP for Teff < 6000 K dwarfs, well under 200 GB) |
| ★★☆☆☆ | [New white dwarf with transiting planetary debris in public ZTF or TESS light curves](wd-debris-transit-new-candidate.md) | harvest | laptop-hours (ZTF light curves for ~100k WDs is a few GB via the IRSA light-curve service; TESS for the brightest few thousand) |
| ★★☆☆☆ | [Gamma-ray pulsations from a known radio pulsar not yet on the public list of LAT-detected…](fermi-lat-pulsations-known-radio-pulsar.md) | standard | laptop-hours (LAT weekly photon files total ~100 GB for the mission; an ROI selection is far smaller) |
| ★★☆☆☆ | [New circumbinary transit candidate in a Kepler eclipsing binary (Villanova EB catalog)](kepler-eb-circumbinary-transit-candidate.md) | standard | laptop-hours to laptop-days (2878 EB light curves ~ 1.5 GB; the N-body stacking search is CPU-heavy, so restrict to detached EBs with morph < 0.5 and P_bin 5-60 d, ~ 700 systems) |
| ★☆☆☆☆ | [MOONSHOT - Planet Nine or a new extreme distant TNO candidate in public archival survey i…](planet-nine-distant-tno-archival-moonshot.md) | moonshot | laptop-hours to laptop-days (DECam frames are ~0.5-1 GB each; restrict to < 200 GB by selecting fields with >= 3 public epochs in the predicted Planet Nine region or ecliptic-latitude bands; shift-and-stack on 10 cores is feasible for a few square degrees per day) |

← [All categories](../README.md)
