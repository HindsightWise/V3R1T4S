# Receipts

Real output of `sh verify-it-yourself/run_checks.sh`, run from this package folder (exit code 0):

```text
sha256 matches INDEX.csv (e718ab34db2e1aa72f391e9d2b538c49f6d11e2bb051de3a6a7aa4cdd04d94d9)
== check_slp.py (exact tensor identity over Z, ternary coefficients, straight-line order, reduced addition count)
{"file": "2x4x7_m45_cr166_ZT_reduced.json", "format": "2x4x7", "rank": 45, "tensor_exact": "C^T", "eval_ok": true, "adds_U": 35, "adds_V": 60, "adds_W": 71, "adds_total": 166, "naive_total": 336, "declared_reduced": 166, "VALID": true}
checker verdict: PASS (VALID=True, rank=45, adds_total=166, tensor=C^T)
== brent_check.py (all 3136 Brent equations over Z, entries in -1,0,1, rank 45, cr 166)
format 2x4x7 rank 45 equations 3136 brent_bad 0 ternary True cr 166
BRENT_OK brent_bad=0
== negative control: a copy with one coefficient sign flipped in the first fresh U form must FAIL
negative control rejected by check_slp (VALID false)
negative control rejected by brent_check
ALL CHECKS PASS
```
