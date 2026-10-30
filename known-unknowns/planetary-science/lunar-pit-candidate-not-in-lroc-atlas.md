# New lunar pit (steep-walled collapse feature) in public LROC NAC images, absent from the LROC Pits Atlas

🪐 **Planets and moons** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (LROC NAC EDR/CDR frames are 100-500 MB each; searches restricted to mare, impact-melt and highland target areas) · open as of 2026-10-30

## The problem

Lunar pits are steep-walled collapse pits, some opening into voids, first recognised in SELENE and LROC images (Haruyama et al. 2009; Robinson et al. 2012; Wagner and Robinson 2014). The LROC team (R. V. Wagner, M. S. Robinson and the LROC Science Operations Center, ASU) maintains the LROC Pits Atlas, whose list page on 2026-10-30 has 278 entries, with host feature, coordinates, funnel and inner diameters, azimuth and depth; every entry gives a depth, but 40 depths are only lower bounds (" > ") and 12 entries have no inner diameter. Most are small pits in impact-melt deposits; the mare pits (Mare Tranquillitatis, Marius Hills, Mare Ingenii and others) are candidate cave entrances for exploration. LRO has imaged most of the Moon at 0.5-1.5 m/pixel under several illumination angles, and all NAC images are public through the PDS. Open task: a pit that the atlas does not list, with its depth measured from shadows in two images.

## What counts as a win

A saved bundle (NAC product IDs, map-projected cutouts, illumination geometry from the PDS labels, shadow measurements and code) where: (1) the feature is seen in >= 2 NAC images whose solar incidence angles differ by >= 10 deg; (2) its inner (steep-walled) opening has a maximum diameter >= 5 m and spans >= 5 pixels in each of those images; (3) in each image the shadow edge falls on the pit floor (not on the far wall), and the depth estimates from the shadow length (depth = shadow length x tan(90 deg - incidence), corrected for local slope from the SLDEM2015 or a NAC DTM where available) agree within 30%, with depth / inner diameter >= 0.3, deeper than fresh simple impact craters of that size (about 0.2); (4) the feature has no raised rim or ejecta blanket (described with a radial brightness profile in each image); (5) no entry on https://lroc.im-ldi.com/atlases/pits/list (re-fetched immediately before claiming) lies within 200 m, and no published pit or cave-candidate list found by search (including Le Corre et al. 2025, Icarus 441, 116675) gives it.

## Partial wins

- **p1:** A detector that, on NAC images of >= 30 atlas pits not used to tune it, recovers >= 80% of them with <= 1 false candidate per 10 km^2 of searched area, with all candidates saved.
- **p2:** A candidate meeting (2), (4) and (5) in a single NAC image, with a single-image depth estimate giving depth / diameter >= 0.3.
- **p3:** A depth for an atlas pit whose depth is listed only as a lower bound (" > "), measured as in (3) from two NAC images in which the shadow edge falls on the pit floor, larger than the listed bound, with the result saved.

## How a win is checked

Skeptic downloads the NAC products from the PDS, re-projects the cutouts, re-measures the shadow lengths and incidence angles from the labels, recomputes depth and diameter, and checks the live atlas list for entries within 200 m. Under an hour per candidate.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://lroc.im-ldi.com/atlases/pits/list>

## Sources

- <https://lroc.im-ldi.com/atlases/pits/list>
- <https://lroc.im-ldi.com/atlases/pits>
- <https://pds.lroc.im-ldi.com/>
- <https://ode.rsl.wustl.edu/moon/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: search mare and impact-melt regions with a small CNN trained on atlas pits, then confirm with shadow geometry.
- Use the incidence-angle diversity: a pit's shadow fraction grows much faster with incidence than a bowl crater's, which is a cheap physical discriminator.
- Cross-domain import (karst and sinkhole mapping on Earth): sinkhole detectors trained on lidar and imagery use closed-depression and wall-steepness features that carry over.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Small fresh craters, boulder shadows and image noise can mimic pits at high incidence; the two-image depth agreement in (3) is the main safeguard.
- Several atlas entries share host features and have close coordinates; check distance to every entry, not only to entries with the same host name.
- Published pits are not all in the atlas: Le Corre et al. (2025, Icarus 441, 116675) report the South Marius Hills Pit and the Bel'kovich A Pit, found with a Mask R-CNN on NAC images, and other machine-learning pit searches have published candidate lists; search for them before claiming.
- At high incidence the shadow of a deep pit often ends on the far wall, which gives only a lower bound on depth; use the lower-incidence image or a DTM for the floor.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/lunar-pit-candidate-not-in-lroc-atlas.md
```

Already set up? Say `run V3R1T4S on lunar-pit-candidate-not-in-lroc-atlas`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lunar-pit-candidate-not-in-lroc-atlas`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
