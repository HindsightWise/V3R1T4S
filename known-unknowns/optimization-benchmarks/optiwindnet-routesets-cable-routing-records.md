# OptiWindNet RouteSets: a shorter offshore wind-farm array-cable network than the best stored for a real site

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (16-210 turbines per site; MILP or HGS/LKH-style heuristics) · open as of 2026-10-30

## The problem

OptiWindNet RouteSets (Mauricio Souza de Alencar, Tuhfe Gocmen and Nicolaos A. Cutululis, DTU Wind; preprint wes-2026-124, in review at Wind Energy Science) is an open benchmark for the wind-farm cable-routing problem: connect every turbine to an offshore substation with cables of a given capacity (2-12 turbines per string), radial (paths) or branched (trees), without crossings, routing around site borders and obstacles, minimising total cable length. Release 26.10-v4 (Zenodo DOI 10.5281/zenodo.23537067, 21 Oct 2026, CC-BY-4.0) holds 49,204 route sets for 13,954 (location, capacity) instances from CPLEX 22.1.1 and Gurobi 12 MILP runs (with bounds) and HGS-CVRP and LKH-3 heuristics. Recomputed from the SQLite file on 2026-10-30, comparing each instance's shortest stored length (detours included; radial counts for branched) with its best branched MILP bound (a bound on the model's straight-line objective, so these are indicative gaps, not certified ones): 2,431 instances are at 1-2%, 2,502 at 2-5% and 514 at 5% or more; 1,252 instances whose nodeset name has no '!' prefix (built farms, literature sites and their '.1_OSS' or '.solid' variants) carry a branched bound. Largest: London Array capacity 12, 138,963.85 m vs bound 132,040.61 (stored relgap 3.7%); Belwind capacity 10, 35,115.17 m vs 33,449.99 (4.3%); Hornsea One.1_OSS capacity 8, 380,296.05 m (a radial set) vs branched bound 362,862.42. Shorter route sets on these instances are open.

## What counts as a win

For one (nodeset, capacity) instance of release r26.10-v4 whose nodeset name does not start with '!', and topology X (radial or branched), a route set of topology X with strictly smaller total length than every stored route set for that instance of topology X or more restrictive (radial counts for branched), by more than 1e-6 relative, using at each substation no more feeders than the shortest such stored route set (feeders_per_root), and carrying the same nodeset (all turbines, substations, borders and obstacles from its VertexC blob). It must pass optiwindnet.validating.validate_routeset with no violations (topology, capacity, loads, crossings), every route segment must stay inside the site border and outside every obstacle polygon (checked separately, since the validator does not test this), and its length, recomputed as the sum of Euclidean segment lengths in metres, must be the value compared.

## Partial wins

- **p1:** A strict improvement, by the full-win rule, on an augmented instance (nodeset name starting with '!') whose stored best has a certified gap of at least 2%.
- **p2:** A radial route set, by the full-win rule, beating the best stored radial route set on a real-site instance whose radial best has no MILP bound in the release.

## How a win is checked

Download optiwindnet-routesets-r26.10-v4.sqlite.xz (sha256 c78c8f3c0543468a48c24d02a08a9a71f9b385389b1e82b6af6bd5bbfdd05e3a on 2026-10-30) from Zenodo; with sqlite3 read the nodeset row and all routeset rows for the instance (length, feeders_per_root, misc.topology). pip-install optiwindnet in a clean venv, load the claim, run validate_routeset; check segment containment in the border and obstacles with shapely; recompute length. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zenodo.org/api/records/23537067/versions/latest>

## Sources

- <https://doi.org/10.5281/zenodo.23537067>
- <https://zenodo.org/api/records/23537067>
- <https://wes.copernicus.org/preprints/wes-2026-124/>
- <https://github.com/DTUWindEnergy/OptiWindNet>
- <https://github.com/DTUWindEnergy/OptiWindNet/blob/main/docs/dataset.md>
- <https://github.com/DTUWindEnergy/OptiWindNet/blob/main/docs/reference/validation.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Warm-start the package's own MILP (HiGHS or SCIP) from the stored best and run longer, or with the feeder-limit and segmented feeder-route options the release used; many gaps come from 6-hour CPLEX limits.
- Branched instances at high capacity (8-12) on 150-200 turbines have the largest gaps; capacitated minimum spanning tree heuristics (Esau-Williams, ruin-and-recreate) plus crossing repair are natural.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Feeder limits differ between stored runs (min_plus1, min_plus2, unlimited); the criterion caps feeders at the shortest stored route set's count so that relaxing the feeder limit does not count.
- Stored 'length' includes detours computed by PathFinder; 'misc.objective' is the model's straight-line objective. Compare lengths.
- A newer Zenodo version may change the table; re-read the latest version before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/optiwindnet-routesets-cable-routing-records.md
```

Already set up? Say `run V3R1T4S on optiwindnet-routesets-cable-routing-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `optiwindnet-routesets-cable-routing-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
