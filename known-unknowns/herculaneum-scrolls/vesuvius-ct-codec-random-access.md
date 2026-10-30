# Scroll CT compression with random access: beat volcomp's rate-distortion on its 54 held-out PHerc. Paris 4 2.4 µm 128³ chunks while every chunk stays independently decodable

🌋 **Herculaneum scrolls** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (CPU only; the held-out set is 54 raw uint8 128³ chunks, 108 MiB, read directly from the public S3 zarr) · open as of 2026-10-30

> 🔒 **Live puzzle with a living setter.** Solve it, but never publish the answer: it goes privately to the setter, and only a salted hash goes in this repo. See [DONT_SPOIL_THE_HUNT.md](../../DONT_SPOIL_THE_HUNT.md).

## The problem

Data scale is a named bottleneck on scrollprize.org/2026_open_problems: large scroll volumes reach dozens of terabytes. At level 0 the PHercParis4 2.4 µm masked volume alone is 75784 x 32693 x 32693 uint8 voxels, stored as raw uncompressed 128³ zarr v2 chunks (.zarray fetched 2026-10-29). volcomp (Forrest McDonald; github.com/SuperOptimizer/volume-compressor, MIT; the README introduces the C library as version 1.3.0, format revision 4, while head 81f6519 of 2026-10-13 also documents format revision 5 / volcomp 1.4.0 typed chunks for non-u8 data, with the u8 tANS tables unchanged) won a September 2026 Progress Prize as 'a chunked compressor for scroll CT and model predictions, now supported in VC3D'. It codes 16³ blocks with a 3-D DCT, a dead-zone quantiser and tANS into independently decodable 128³ chunks inside zarr v3 shards, and its mirror of all 39 samples is at dl.ash2txt.org/community-uploads/forrest/volcomp/. Its docs/BENCHMARKS.md (lossy 2026-09-01, lossless 2026-09-07; unchanged at head commit 81f6519, fetched 2026-10-29) uses two sets of 54 chunks. A tune set serves every design choice. A held-out set (corpus/manifest_heldout.tsv: 41 chunks at level 0, 9 at level 1, 4 at level 2, including one contiguous 2x2x2 octet) is touched only for the published numbers. Held-out ratio / PSNR / SSIM at q 2, 4, 8, 16, 32: 17.56 / 41.33 dB / .9840; 30.05 / 38.04 / .9700; 52.92 / 35.00 / .9463; 95.58 / 32.22 / .9088; 176.5 / 29.67 / .8532 (one thread, AVX2; decode 702-2484 MB/s). The optional volcomp_deblock() post-filter adds up to 0.42 dB (q8: 35.17 dB / .9494). The predecessor codec c5d is 0.6-6.9% larger at the same q. The open part comes from the interim comparison in docs/SUBMISSION_2026-09.md section 5 (four 512³ cubes, contended timings). Inter-frame video codecs need fewer bits at 35 dB: SVT-AV1 0.53-0.86x volcomp's bits (0.69x on the 2.40 µm cube), x265 0.71-0.99x, aom 0.75-0.90x. They get there only by giving up 128³ random access: reading one chunk means reading a 128-frame GOP, with 6-21x more bytes and 14-179x slower decoding. Every random-access codec tested needs 1.5-31x more bits than volcomp: SZ3, ZFP, JPEG 2000, JPEG XL, AVIF, WebP and all-intra video. On those four cubes no tested codec beats volcomp while keeping chunk random access (docs/bench/README.md is still marked interim: sizes and quality final, timings contended). No third-party codec has been run on the 54 held-out chunks; Gate A measures only volcomp there. CREDITS: Forrest McDonald (volcomp, c5d, the benchmark and the mirror); the Vesuvius Challenge team and ESRF (PHercParis4 2.4 µm / 78 keV scan 20260411134726). DATA: CC BY-NC 4.0 open data plus the dl.ash2txt.org terms. A human must accept the terms before any download; chunks are never redistributed.

## What counts as a win

SCORER (pinned). score_codec.py is written by the scout and frozen by sha256 in METRIC.sha256 before the baseline run. (1) Fetch: the 54 held-out chunks listed in manifest_heldout.tsv @ 81f6519, from https://vesuvius-challenge-open-data.s3.us-east-1.amazonaws.com/PHercParis4/volumes/20260411134726-2.400um-0.2m-78keV-masked.zarr/ < level > / < cz > / < cy > / < cx> (2,097,152 bytes each). Their sha256 is recorded on first fetch, and any later mismatch aborts. (2) Decode: each submitted chunk stream is decoded in its own fresh process, in a seeded random order, from that stream plus the codec's static side data only. (3) Report: total bytes (the sum of the 54 streams plus all static side data such as tables, dictionaries or weights, counted once in full); pooled PSNR = 10 log10(255^2 / MSE over all 54 x 128^3 voxels); mean SSIM (2-D, 7 x 7 Gaussian window, data_range 255, averaged over all z-planes of all chunks); max absolute error; single-thread CPU decode throughput (decoded bytes per wall second, in-memory stream to uint8 output, median of 3 runs). GATE A. The scout builds volcomp @ 81f6519 and stores in a hash-locked BASELINE.json its bytes, PSNR, SSIM and decode throughput at q 2, 8 and 32, both plain and with volcomp_deblock(). At each q the baseline variant is the one with the higher pooled PSNR (ties: higher mean SSIM); its bytes, PSNR, SSIM and single-thread decode throughput (decode plus filter for the deblock variant) are the reference values. The run should reproduce the BENCHMARKS.md ratios within 0.5% and PSNR within 0.02 dB; otherwise the measured values stand and the discrepancy is reported. GATE B. Codec design, parameters and any learned weights use no byte of the 54 held-out chunks and no byte of any chunk at another level that covers the same voxels (the level-1 and level-2 chunks containing a held-out level-0 chunk, and the level-0 and level-1 chunks inside a held-out level-1 or level-2 chunk); leak audit over training and tuning logs and hashes. The tune set and any other data are allowed. SUCCESS requires all of the following, at each of three operating points matched to volcomp q2, q8 and q32: pooled PSNR >= the baseline's; mean SSIM >= the baseline's; total bytes <= 0.85 x the baseline's at q8 and <= 0.90 x at q2 and q32; every chunk decodes independently and bit-exactly across two runs; single-thread decode throughput >= 0.25 x the baseline variant's throughput measured at the same point on the same machine; decoder source supplied and built by the verifier. This is an internal benchmark. It is credited officially only if scrollprize.org/winners credits a Progress Prize submission made by the human.

## Partial wins

- **p1:** One operating point. At q8-matched quality (pooled PSNR and mean SSIM >= volcomp q8's, taking the better of plain decode and deblock), total bytes <= 0.85 x the baseline's. The same independence, decode-speed and leakage rules apply.
- **p2:** Lossless. Byte-exact, independently decodable chunks whose total bytes are <= 0.90 x the smallest of three codecs on the same 54 chunks: volcomp q = 0, per-chunk zstd -19 and per-chunk blosc-zstd level 5, all measured by the scout in Gate A. Single-thread decode must reach >= 0.25 x the fastest of those three.
- **p3:** Speed at equal size. Total bytes <= 1.01 x the q8 baseline variant's (Gate A), pooled PSNR and mean SSIM at least that variant's, and single-thread decode throughput >= 2 x that variant's measured q8 throughput on the same machine. The same independence and leakage rules apply.

## How a win is checked

The verifier: (1) fetches the 54 chunks (108 MiB) and checks them against the scout's sha256 list; (2) builds the claimant's decoder from source, with static side data supplied separately and counted; (3) decodes every chunk in its own process in a seeded random order (a chunk that needs another chunk's bytes fails); (4) recomputes bytes, PSNR, SSIM and max error with score_codec.py, which takes seconds; (5) rebuilds volcomp @ 81f6519 and re-encodes 5 seeded chunks at q8 to confirm the BASELINE.json byte counts exactly; (6) times both decoders on the same machine (median of 3); (7) re-reads volcomp's BENCHMARKS.md and docs/bench tables, and villa's VC3D codec support, for newer records.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/SuperOptimizer/volume-compressor/blob/main/docs/BENCHMARKS.md>

## Sources

- <https://github.com/SuperOptimizer/volume-compressor>
- <https://github.com/SuperOptimizer/volume-compressor/blob/main/docs/BENCHMARKS.md>
- <https://github.com/SuperOptimizer/volume-compressor/blob/main/corpus/manifest_heldout.tsv>
- <https://github.com/SuperOptimizer/volume-compressor/blob/main/docs/SUBMISSION_2026-09.md>
- <https://vesuvius-challenge-open-data.s3.us-east-1.amazonaws.com/PHercParis4/volumes/20260411134726-2.400um-0.2m-78keV-masked.zarr/0/.zarray>
- <https://dl.ash2txt.org/community-uploads/forrest/volcomp/>
- <https://scrollprize.org/winners>
- <https://scrollprize.org/2026_open_problems>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Chunk-closed inter-slice prediction: treat each 128³ chunk as its own 128-frame sequence, with motion or affine prediction between z-slices as inter-frame video codecs do across a 512² GOP. Random access then survives at chunk granularity.
- Adaptive context modelling with arithmetic or rANS coding across blocks inside a chunk, trellis or rate-distortion-optimised quantisation, and in-format deblocking.
- Learned transforms or priors fitted on the tune set and other scroll data, shipped as counted static side data.
- Exploit the masked-air fill value and the near-periodic sheet structure (winding pitch) for prediction.
- Report results per chunk class (dense interior, smooth papyrus, boundary, air), as volcomp does.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Inter-frame video codecs already beat volcomp on bits at 35 dB by giving up random access. A stream that needs neighbouring chunks or a 512-wide GOP does not count.
- PSNR alone rewards smoothing that erases ink-scale texture. The success needs both PSNR and SSIM, and max-error tails should be reported.
- Never tune on the held-out chunks; the tune manifest exists for that. Held-out chunk hashes appearing in tuning logs void the attempt.
- Static side data (dictionaries, weights, tables) counts in full. Amortising it over a larger corpus is not allowed.
- Timing noise is about +-10% under WSL2. Compare decoders on the same machine and use medians.
- Data terms: chunks come straight from the public bucket, only after the human has accepted the terms, and they are never redistributed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/herculaneum-scrolls/vesuvius-ct-codec-random-access.md
```

Already set up? Say `run V3R1T4S on vesuvius-ct-codec-random-access`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vesuvius-ct-codec-random-access`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
