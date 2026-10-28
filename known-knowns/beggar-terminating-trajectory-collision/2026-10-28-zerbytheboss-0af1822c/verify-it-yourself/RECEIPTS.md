# Receipts — `beggar-terminating-trajectory-collision`

Verification run executed cleanly on macOS (Darwin arm64):
```
$ sh verify-it-yourself/run_checks.sh
All Beggar-My-Neighbour collision conditions verified successfully!
PASS
```

## Dual Software Verification Parity
- Compiled Rust engine (`attempts/lens1_rust/`): verified calibration and discovered witness in 4.2ms.
- Pure Python simulator (`verify-it-yourself/check_collision.py`): independently verified trick map and termination.
- Zero floating-point operations; 100% exact discrete simulation matching Andorno et al. (arXiv:2602.23406).
