# Receipts

Real output of `sh verify-it-yourself/run_checks.sh`, run from this package folder (exit code 0):

```text
sha256 matches INDEX.csv (9a8caeaed8d8737afe3b05f4d105e98de9f6fd7c0bbfb1c5a59cb16a622d23bc)
== check_slp.py (exact tensor identity over Z, ternary coefficients, straight-line order, reduced addition count)
{"file": "2x3x8_m40_cr97_ZT_reduced.json", "format": "2x3x8", "rank": 40, "tensor_exact": "C^T", "eval_ok": true, "adds_U": 12, "adds_V": 33, "adds_W": 52, "adds_total": 97, "naive_total": 199, "declared_reduced": 97, "VALID": true}
checker verdict: PASS (VALID=True, rank=40, adds_total=97, tensor=C^T)
== brent_check.py (all 2304 Brent equations over Z, entries in -1,0,1, rank 40, cr 97)
format 2x3x8 rank 40 equations 2304 brent_bad 0 ternary True cr 97
BRENT_OK brent_bad=0
== negative control: a copy with one coefficient sign flipped in the first fresh U form must FAIL
negative control rejected by check_slp (VALID false)
negative control rejected by brent_check
ALL CHECKS PASS
```
