# Silesia corpus: beat the best per-file compressed size with a specialized open-source model

🗜️ **Compression and code golf** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Matt Mahoney's Silesia Open Source Compression Benchmark (programs as of Oct. 10, 2026) lists per-file compressed sizes (KB, truncated) for the 12 Silesia files. Per-file column minima today come from paq8px_v206/v217, precomp|cmix v21 and gleipnir 1.0.2 (sao). Several files are highly structured binaries where a format-specific model can plausibly beat general CM: sao (SAO star catalog, fixed 28-byte records), osdb (synthetic MySQL-style database), x-ray and mr (16-bit / DICOM medical images), nci (SMILES-like chemical database). Produce a byte-exact round trip on one file whose total (compressed file + zipped decompressor source) is strictly below that file's column minimum.

## What counts as a win

For one Silesia file (md5 as listed on https://mattmahoney.net/dc/silesia.html), an open-source compressor/decompressor where: decompress(compressed) reproduces the file byte-exactly (md5 match), run by a skeptic from a clean build; and size(compressed) + size(zip -9 of the decompressor source tree including any dictionaries/models) is strictly less than 1000 x (the minimum KB value in that file's column of the live table, re-fetched immediately before claiming). Decompressor must not embed file-specific data beyond what is counted in its zipped size; runtime <= 24 laptop-hours, RAM <= 32 GB.

## Partial wins

- **sao-specialized-beats-paq:** A specialized sao model beating every paq8px/cmix row (not necessarily gleipnir) by the same counted-size rule.
- **preprocessor-gain:** An open preprocessor (e.g. record transposition for osdb/sao, delta+bitplane for x-ray) that makes paq8px_v217 -12L output strictly smaller than its own listed size on that file, round-trip verified.
- **silesia-total:** Strictly beat the top Silesia total (27682006 bytes today, re-fetch) with the same per-file-counted rule - stretch.

## How a win is checked

Skeptic builds the decompressor from the zipped source, decompresses, md5sum compares against the corpus md5 on the page, then sums sizes. One run of a CM decompressor on a <=10 MB file is minutes to an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mattmahoney.net/dc/silesia.html>

## Sources

- <https://mattmahoney.net/dc/silesia.html>
- <https://mattmahoney.net/dc/text.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- sao: parse the fixed-length SAO star catalog records into fields (RA, Dec, magnitudes, spectral type, proper motions) and model each with field-specific contexts (sorted RA deltas, Dec correlation), mixing with a paq-style logistic mixer.
- osdb / nci: column/record transposition preprocessing then paq8px_v217 or cmix; tune column contexts.
- x-ray / mr: 16-bit lossless image models (CALIC/GraLIC-style gradient-adjusted prediction + context mixing on residual bitplanes), DICOM header handled separately.
- Cross-domain import (astronomy): exploit the sky-sorting structure of the star catalog - HEALPix/zone ordering of stars makes coordinates nearly monotone; model proper motions with priors from Gaia-like distributions (computed from the file itself, no external data).
- Cross-domain import (genomics/bioinformatics): SMILES-aware tokenization for nci, borrowing grammar-based compressors used for chemical/biological sequence data.
- Cross-domain import (medical imaging/MRI reconstruction): slice-to-slice motion-compensated prediction for the 3-D mr volume, like video codecs.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Table sizes are in KB truncated; compare total bytes to 1000 x KB minimum strictly (a value equal to the truncated KB could still be larger in bytes).
- Embedding file data in the decompressor: count the zipped decompressor source; a giant model file is counted too.
- Closed-source programs are not listed; the record is among open-source programs only - a closed program's better result does not move the table, but our claim must be open source.
- md5 must match the page's listed md5; some mirrors ship altered files (e.g. CRLF).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/compression-and-golf/silesia-per-file-specialized-record.md
```

Already set up? Say `run V3R1T4S on silesia-per-file-specialized-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `silesia-per-file-specialized-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
