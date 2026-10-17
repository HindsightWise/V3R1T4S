# Run it yourself

From this package folder, in a fresh shell (python3 3.8 or later, standard library only):

```sh
sh verify-it-yourself/run_checks.sh
```

Expected: sha256 matches `INDEX.csv`; `check_slp.py` prints JSON with `"VALID": true`, `"rank": 40`, `"adds_total": 97`; `brent_check.py` prints `brent_bad 0` and `BRENT_OK` (all 2304 Brent equations over Z, entries in -1,0,1); a copy with one sign flipped is rejected by both; last line `ALL CHECKS PASS`.

Individually:

```sh
python3 verify-it-yourself/check_slp.py object/2x3x8_m40_cr97_ZT_reduced.json
python3 verify-it-yourself/brent_check.py object/2x3x8_m40_cr97_ZT_reduced.json 97 40
```

To recount the reference, download Perminov's file named in `the-record-we-beat/README.md` and run `check_slp.py` on it; it reports 98 (`adds_U: 13, adds_V: 33, adds_W: 52`).
