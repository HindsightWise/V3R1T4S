# Cometary activity in archival survey images of a main-belt asteroid with no cometary designation and no reported activity

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-hours (SSOIS / NOIRLab Astro Data Archive searches per object; DECam and ZTF cutouts are MB each) · open as of 2026-10-30

## The problem

Main-belt comets (Hsieh and Jewitt 2006) and other active asteroids number a few dozen. On 2026-10-30 the JPL SBDB lists 39 comet-designated objects (fragments counted separately) with 2.06 < a < 3.3 au, q > 1.6 au and T_J > 3.05, among them P/2025 W3 (Kresken), P/2025 W4 (PANSTARRS) and P/2026 N2. Some active asteroids have only an asteroid designation (e.g. (6478) Gault); others carry both (e.g. (7968) = 133P/Elst-Pizarro). Archival searches work: the Active Asteroids citizen-science project (Colin Chandler, Chad Trujillo, Henry Hsieh, William Oldroyd and volunteers) finds activity in public DECam images. Open task: show activity in public archival images of a main-belt asteroid that has no cometary designation and no published or MPC-reported activity.

## What counts as a win

A saved bundle (object designation, SBDB orbit, image list with archive URLs, cutouts, Horizons ephemerides, photometry and profile code) where: (1) the object has 2.064 < a < 3.3 au, q > 1.6 au, T_J > 3.05 and no cometary designation in SBDB; (2) on >= 2 nights ( > = 1 day apart), or in >= 2 different instruments, the source at the Horizons-predicted position (residual < 2 arcsec) shows extended emission: compared with a trailed PSF built from >= 5 field stars in the same image at the object's rate, its surface-brightness profile has excess flux beyond 2 FWHM at >= 5 sigma, and any tail lies within 30 deg of the projected anti-solar (PsAng) or anti-velocity (PsAMV) direction; (3) the same test on >= 20 inactive asteroids of similar magnitude in the same images gives no detection; (4) no background source lies under the object (checked in a deep stack of other epochs); (5) there is no activity report for the object in MPECs or the MPC database, SBDB, ATels, RNAAS, the Active Asteroids publications or arXiv, nor a CBET whose title on the public CBAT index names it (full CBET texts are subscription-only and are not required) (all re-fetched immediately before claiming).

## Partial wins

- **p1:** The pipeline detects activity, by test (2), in archival images of >= 5 known main-belt comets at epochs when activity was published, with zero detections on 100 inactive control asteroids.
- **p2:** Activity meeting (1)-(5) on a single night in one instrument, logged as a candidate.
- **p3:** A new active epoch (date and image) for a known active asteroid that no paper reports, meeting test (2), which constrains its recurrence.

## How a win is checked

Skeptic re-downloads the images from the stated archives, re-runs the profile and PSF comparison with the saved code, checks the Horizons ephemerides and the SBDB record, and searches MPC/arXiv by designation. About an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name%2Ca%2Ce%2Ci%2Cq%2Ct_jup&sb-kind=c&sb-cdata=%7B%22AND%22%3A%5B%22a%7CRG%7C2.06%7C3.3%22%2C%22t_jup%7CGT%7C3.05%22%2C%22q%7CGT%7C1.6%22%5D%7D>

## Sources

- <https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name%2Ca%2Ce%2Ci%2Cq%2Ct_jup&sb-kind=c&sb-cdata=%7B%22AND%22%3A%5B%22a%7CRG%7C2.06%7C3.3%22%2C%22t_jup%7CGT%7C3.05%22%2C%22q%7CGT%7C1.6%22%5D%7D>
- <https://www.zooniverse.org/projects/orionnau/active-asteroids>
- <https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/ssois/>
- <https://astroarchive.noirlab.edu/>
- <https://ssd.jpl.nasa.gov/horizons/>
- <https://irsa.ipac.caltech.edu/Missions/ztf.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prioritise outer-belt asteroids imaged near perihelion (true anomaly -60 to +90 deg), where sublimation-driven activity is seen.
- Members of the Themis and Beagle families and of the families of known MBC hosts.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Trailing of fast-moving objects and poor tracking mimic tails; compare with trailed PSFs at the same rate.
- Background galaxies and stars under the object, ghosts and satellite trails all produce false tails; check other epochs.
- Activity on a known active asteroid does not make a new active asteroid; check designations and the literature.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/main-belt-asteroid-new-activity-archival.md
```

Already set up? Say `run V3R1T4S on main-belt-asteroid-new-activity-archival`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `main-belt-asteroid-new-activity-archival`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
