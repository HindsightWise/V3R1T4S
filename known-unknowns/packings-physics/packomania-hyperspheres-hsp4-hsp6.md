# Packomania: equal 4D/5D/6D hyperspheres in a hypersphere (hsp4, hsp5, hsp6), beat a per-N record radius

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Packomania Section 4 lists the best known radius r(N) of N equal d-dimensional balls packed in the unit d-ball for d = 4 (N = 2..300), d = 5 (N = 2..300) and d = 6 (N = 2..250 on the page; txt/radius.txt also lists N = 251..259), with 12-decimal txt/radius.txt files and per-N coordinates inside txt/hsp<d>_coords.tar.gz (files hsp<d>-<N>.txt: first line radius, then N rows of an index and coordinates, 12 decimals). As of 2026-10-28 (archives unchanged since 2026-10-16) only the hsp4 files are complete: every hsp5 and hsp6 row carries 4 coordinates, not 5 or 6, and hsp6 has no file for N = 251-259, so the posted hsp5 and hsp6 coordinates are unavailable except at hsp5 N = 7 and 8 (see the success criterion). Last updates: hsp4 06-Jul-2025, hsp5 01-Aug-2025, hsp6 31-Jul-2025. Author files show these tables were built almost single-handedly by Specht (hsp4: 247/299 rows Specht, 30 Sloane-Hardin-Smith, 11 Mackay; hsp5: 263/299 Specht; hsp6: 258/258 Specht). None of hsp4/5/6 appears by name in the pending-requests list (2026-10-08 and 17-Oct-2026), but the tables are contested: the public collection of Moki & Julio (github.com/Hashirama1337s/moki-julio-circle-packing, MANIFEST.csv; balls in a ball since their v2.4 of 2026-09-26, commit 3036c50f5da0; first GitHub release v2.5, the same day) claims radii above the live tables by more than 1e-10 at 216 hsp4, 163 hsp5 and 71 hsp6 N (it lists 3 hsp5 and 54 hsp6 of its own records as superseded), and radii built from H. Cohn's table of spherical codes (spherical-codes.org) exceed the live tables at 4 hsp4, 70 hsp5 and 159 hsp6 N (2026-10-24; 65 and 155 on 2026-10-18; see pitfalls). The queued 26-Sep-2026 'many: 4666 candidates' bundle of Moki & Julio matches their earlier release v2.2, which has no hsp table (see pitfalls).

## What counts as a win

Success means N centers in R^d (d in {4,5,6}) for one N listed in the live https://packomania.com/hsp<d>/txt/radius.txt such that the FEASIBLE radius r* := min( min_{i<j} |c_i - c_j| / 2, 1 - max_i |c_i| ) (unit container ball centred at the origin), computed in mpmath at 50 digits directly from the submitted coordinates with no tolerance, is STRICTLY GREATER (direction: max) than that file's 12-decimal value for N re-fetched live immediately before claiming, by at least 1e-10 (the table carries 12 decimals; 1e-10 is 200x its rounding), AND, wherever the posted hsp<d>-<N>.txt reproduces its own header radius to 1e-11, the configuration is not isometric to that posted configuration (sorted pairwise-distance multisets differ by more than 1e-8 somewhere) and r* exceeds by at least 1e-9 the highest radius that the verifier's own local polishes of that posted file reach, each run until it stops improving, under several trust-region schedules, AND the configuration is not a relaxed copy of a posted packing, which is a trivial derivation however much it gains (a polish gain is an errata note for the table keeper, as in packomania-scu-spheres-in-cube since #605; the claim names any posted packing it started from), AND (d, N) does not appear in a History-of-updates entry on the live hsp<d>.html newer than the one the scout fetched. COORDINATES UNAVAILABLE (checked 2026-10-28): every hsp4 file reproduces its header radius, but the hsp5 and hsp6 rows carry 4 coordinates and hsp6 N = 251-259 have no file, so among hsp5 and hsp6 only hsp5 N = 7 and 8 can be compared or polished (see pitfalls); for every other hsp5 or hsp6 N the verdict must say 'posted coordinates unavailable', and the N must be re-checked against the posted file once Packomania posts complete coordinates. QUEUE RULE (Packomania, checked 2026-10-08): the N must NOT lie inside any range listed for this category on https://packomania.com/pending-requests.html re-fetched at verification time; a value that is already in Packomania's queue does not count as ours. The 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle is category-unspecified and cannot be resolved; the verdict must state this caveat and the N must be re-checked against the live table once that bundle disappears from the pending list. No submission (email) is ever made; the claim is for the verified construction only.

## Partial wins

- **p1:** A certified improvement for a row attributed to 'unknown' or 'A. L. Mackay' in txt/author.txt (hsp4), i.e. a row seeded from classical constructions rather than optimized.
- **p2:** An extension row: a certified packing for N = 301..310 (d = 4 or 5) or N = 260..270 (d = 6) that beats the obvious baseline of (best r(N-1) packing plus one ball at the largest cavity, re-jammed), reported with r* to 20 digits; not a record, but new data for an N the table does not list.
- **p3:** A certified contact-graph audit: for every listed N, re-derive r from the coordinates in the tarball and report any N where the posted coordinates do not achieve the posted 12-decimal radius (data-integrity finding). For the archives seen from 2026-10-16 to 2026-10-28 this is already reported (issue #232, see pitfalls): every hsp5 and hsp6 file except hsp5 N = 7 and 8 falls short because its rows carry 4 coordinates, hsp6 N = 251-259 have no file, and every hsp4 file reproduces its radius within 1.7e-12 (12-decimal rounding, not a finding); a new audit needs re-exported files.

## How a win is checked

Checker (minutes, plus the polishes, which take most of the time): curl the live hsp<d>/txt/radius.txt and parse row N; load the claimed centers; mpmath mp.dps=50; r* = min(half the minimum pairwise distance, 1 - maximum norm); assert r* - r_table >= 1e-10. Download txt/hsp<d>_coords.tar.gz (all three exist; hsp6 holds N = 2..250 only, checked 2026-10-28) and read hsp<d>-<N>.txt; count the numbers per row and recompute its r the same way (parser sanity: the hsp4 files must reproduce the table to 1e-11; all 299 do, within 1.7e-12). If the posted file reproduces its header radius to 1e-11, compare sorted distance multisets to rule out an isometric copy, then polish that file from its posted coordinates with your own local optimizer (for example sequential LP on the near contacts with a trust region) under at least three schedules (largest step 1e-2, 1e-3 and 1e-4), each until it stops improving, report every polished radius and assert r* exceeds the highest by at least 1e-9 (posted hsp4 files gain up to 3.3e-6 this way, see pitfalls), and read the claim's stated starting point: a relaxed copy of a posted packing is its derivation unless the claim documents real search beyond a relaxation; if the posted file does not reproduce its radius, or is missing, record 'posted coordinates unavailable' with the archive's sha256 (every hsp5 and hsp6 N except hsp5 N = 7 and 8 on 2026-10-28). Re-fetch hsp<d>.html (History of updates) and pending-requests.html and apply the queue rule. Report r* to 20 digits.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://packomania.com/hsp4/hsp4.html>

## Sources

- <https://packomania.com/hsp4/hsp4.html>
- <https://packomania.com/hsp4/txt/radius.txt>
- <https://packomania.com/hsp5/txt/radius.txt>
- <https://packomania.com/hsp6/txt/radius.txt>
- <https://packomania.com/hsp4/txt/author.txt>
- <https://packomania.com/hsp5/txt/author.txt>
- <https://packomania.com/hsp6/txt/author.txt>
- <https://packomania.com/hsp4/txt/hsp4_coords.tar.gz>
- <https://packomania.com/hsp5/txt/hsp5_coords.tar.gz>
- <https://packomania.com/hsp6/txt/hsp6_coords.tar.gz>
- <https://packomania.com/pending-requests.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Single-author tables are the softest: run a completely different optimizer than Specht's (event-driven LS compression in d dimensions from random starts, 10 cores x hundreds of restarts per N) over all N = 50..300; expect many small gains in 12-digit tables.
- Lattice shells: in 4D the D4 lattice (24-cell kissing) and in 6D the E6 lattice give dense shell structures; take shells around a center, cut to N, and relax; compare with txt/records.txt (density-record N) to find N where the table is NOT already a lattice shell.
- Kissing-configuration seeds: a central ball with a 24-ball (4D) or 40-ball (5D) or 72-ball (6D) shell plus a partial second shell is a natural template for N near 25, 41, 73 and N near the second-shell completions; the table's density-record lists hint at which are already found.
- Large-neighbourhood search on the posted coordinates: delete the 5 balls with the largest free volume (compute via random probing), re-insert at the deepest holes, re-jam; polish the active-contact KKT system with mpmath.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 12-decimal table: compare against the exact posted value with the criterion's 1e-10 margin; an improvement of 3e-12 is indistinguishable from the table's own rounding.
- Container convention: unit container ball (radius 1, centered at origin); the 'ratio' column is 1/r, not the objective.
- A new packing isometric to the posted one (rotated/reflected) with the same r is not a record; the checker compares distance multisets.
- Email submission needs explicit permission from the human and Packomania asks for no submissions in October 2026; claim the verified configuration only.
- Tables are 12-decimal, and the posted hsp4 coordinates certify their rows only to about 1e-12. Some posted hsp4 files are also short of their own local optimum: sequential-LP polishes of hsp4-88, -99, -115 and -117 end 2.0e-8, 8.5e-9, 7.2e-8 and 3.3e-6 above their rows (checked 2026-10-29). The 1e-10 margin covers rounding only, and a polished copy is not isometric to the posted file, so neither stops a polish. The non-isometry test and the criterion's polish floor apply wherever the posted file reproduces its radius (see COORDINATES UNAVAILABLE).
- The posted hsp5/hsp6 coordinates cannot serve the parser check or the non-isometry clause. In hsp5_coords.tar.gz (sha256 e3a7316a...20e5) and hsp6_coords.tar.gz (d36917c4...d15d), unchanged from 2026-10-16 to 2026-10-28, every row of all 299 hsp5 and 249 hsp6 files is an index plus 4 numbers; the radius they give is below the header radius in every file except hsp5 N = 7 and 8 (never above), as if the last coordinates were dropped (both N = 2 files put the two centres at the origin). hsp6 N = 251-259 are listed in radius.txt but have no file (HTTP 404), and the hsp6 page itself stops at N = 250 ('complete up to N = 250'). The 299 hsp4 files (hsp4_coords.tar.gz b929acc8...63df) reproduce their header radii within 1.7e-12. A new sha256 means a re-export: count the numbers per row again before using a file.
- Spherical-code constructions: an N-point spherical code with largest cosine c gives N balls of radius s/(2+s), s = sqrt(2 - 2c), in the unit ball (centres on the sphere of radius 1 - r), and N - 1 points plus a centre ball give min(1/3, s/(2+s)). With the codes on spherical-codes.org this exceeds the live hsp4, hsp5 and hsp6 tables at 4, 70 and 159 N, by up to 6.1e-6, 1.9e-3 and 2.9e-3 (2026-10-24; Cohn's table changes, so recompute), so compare a claim with these radii before calling it new.
- The queued 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle (pending-requests.html of 17-Oct-2026) matches their public release v2.2 (github.com/Hashirama1337s/moki-julio-circle-packing, commit 855d8f6838e9, 2026-09-25T22:41Z, '4,666 records in 15 tables'; its RESULTS_TABLE.md sums to 4,666 over the 2-D tables crt, ccq, cpd, cpt, crc_100 to crc_800, csc, csq and cxd). Balls in 4-, 5- and 6-D enter that repo only at v2.4 (commit 3036c50f5da0, 2026-09-26T08:05Z). The count and the timing agree, but the queued zip is not public: if it is v2.2, the queue holds no hsp candidate, while the later hsp records (220 hsp4, 169 hsp5, 77 hsp6 at commit fd6316dd, 2026-10-18) are public prior claims to compare against (checked 2026-10-19).
- No free cells (2026-10-20): in hsp4, hsp5 and hsp6 every row is the largest at any N' >= N, so deleting balls from a larger posted packing never beats a row (kit/propagated_bar.py, PR #573).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/packomania-hyperspheres-hsp4-hsp6.md
```

Already set up? Say `run V3R1T4S on packomania-hyperspheres-hsp4-hsp6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `packomania-hyperspheres-hsp4-hsp6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
