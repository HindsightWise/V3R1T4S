# Three-Player Texas Hold'em Jam/Fold SnG Solver

## What
Stationary strategy profile for 3-player Texas Hold'em Jam/Fold SnG (Ganzfried-Sandholm) across all 946 nonterminal stack vectors with exact preflop equities, linear system residual < 1e-9, and certified ex-post exploitability epsilon = $0.074891 (Convention ii) and $0.089075 (Convention i).

## Check it yourself
Run the standalone checker from this package folder:
```sh
sh verify-it-yourself/run_checks.sh
```
Expected output:
```
Preflop 2-way equity table validated (685,464 bytes).
Convention (ii) strategy profile verified: 946 states, epsilon = $0.074891.
Convention (i) strategy profile verified: 946 states, epsilon = $0.089075.
ALL THREE-PLAYER JAM/FOLD ARTIFACTS VERIFIED: PASS
PASS
```

## Compared to
| Metric | Incumbent Benchmark | Our Strategy Profile | Status |
|---|---|---|---|
| Nonterminal States | 946 | 946 | Complete |
| Linear System Residual | <= 1e-6 | < 1e-9 | Exact conservation |
| Convention (ii) Exploitability | <= $0.1000 | **$0.074891** | 99.6% states < $0.0488 |
| Convention (i) Exploitability | <= $0.1000 | **$0.089075** | 96.3% states < $0.0488 |

## Not claimed
- We do not claim full global convergence below the $0.0488 partial win threshold (epsilon = $0.074891 exceeds $0.0488 on 4 extreme short-stack states).
- This submission is designated as a Heuristic Advance / PROMISING Epsilon Bound.

## Credits
- Sam Ganzfried and Tuomas Sandholm (2013) for the formulation of 3-player Jam/Fold SnG stochastic games.
- Noam Brown and Tuomas Sandholm for CFR+ algorithms.
