# ECC Inversion Addition Chains — New Records for M-383 and M-511

## What
Partial Win p1 (M-383 at 395 and M-511 at 524)

Specifically:
- M-383 (Curve383187) inversion exponent $2^{383} - 187$: certified addition chain of length 395 (382 squarings, 13 additions), beating the previous known record of 396 by 1 multiplication step.
- M-511 inversion exponent $2^{511} - 187$: certified addition chain of length 524 (510 squarings, 14 additions), beating the previous known record of 525 by 1 multiplication step.

## Check it yourself
Run the standalone checker from this package directory:
```sh
sh verify-it-yourself/run_checks.sh
```
- Expected last line: `PASS`
- Rough laptop time: < 1 second (pure Python standard library)

## Compared to
- **Table / Source**: https://raw.githubusercontent.com/mmcloughlin/addchain/master/doc/results.md
- **Cell**: M-383 (396) and M-511 (525)
- **Published Values**:
  - M-383: 396 steps (382 squarings, 14 additions)
  - M-511: 525 steps (510 squarings, 15 additions)
- **Fetch Time**: 2026-10-29T08:08:00Z (HTTP 200, SHA256: `c805367ced12810d221ac3513ca3ccd0d329382dac2a8ec7b54f2f272e167357`)

## Not claimed
- Full win / main curve beats (only p1 secondary curve improvements).
- We do not claim any improvements on primary curves where the incumbent addition chain matches the theoretical lower bound (e.g. Curve25519 at 265, NIST P-256 at 266, NIST P-384 at 396).

## Credits
- Michael McLoughlin (`addchain` algorithm and documentation)
- Brian Smith (survey of cryptographic inversion addition chains)
- Peter L. Montgomery (modular inversion and addition chain heuristics)
