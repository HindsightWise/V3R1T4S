# Historical handwriting (READ 2016 Ratsprotokolle, line level): beat HTR-ConvText's 3.6% CER and 15.7% WER on the 1,138 test lines without external data

🏺 **Ancient texts and fragments** · standard · tractability ★★☆☆☆ · compute: laptop-days (about 550 MB of page images; a GPU helps); scoring needs only text files · open as of 2026-10-30

## The problem

The ICFHR 2016 READ competition dataset (Sánchez, Romero, Toselli and Vidal, ICFHR 2016; Zenodo record 1297399, CC BY 4.0, 2018) holds pages of the Ratsprotokolle council minutes (1470 to 1805, Early Modern German) with line-level PAGE ground truth: the test archive Test-ICFHR-2016.tgz (md5 894063b8abbe2f671dbb07a144738300) has 50 pages with 1,138 transcribed lines, matching the 8,349 / 1,040 / 1,138 line split used in the line-level literature. Lowest published line-level test CER without external data, pretraining or language models: HTR-ConvText (arXiv 2512.05021v1, December 2025, code and checkpoints at github.com/DAIR-Group/HTR-ConvText) 3.6% CER / 15.7% WER; before it HTR-VT (Li et al., Pattern Recognition 2024) 3.9 / 16.5, VAN and DAN (Coquenet et al.) 4.1, and Spike-HTR (arXiv 2608.01646, August 2026) 3.9. With external resources, HAND (arXiv 2412.18981, github.com/MHHamdan/HAND) reports 2.71 / 10.98 after pretraining on synthetic lines rendered from 103 fonts and 1.65 / 4.95 with an mT5 post-corrector. Page-level results (DAN 3.43) are a different task. Status 2026-10-30: searches found no closed-setting line-level result below 3.6.

## What counts as a win

A frozen transcription file (one line of text per test line id, hash committed before scoring) for all 1,138 transcribed lines of Test-ICFHR-2016.tgz, with line images cut by a published deterministic rule from the PAGE coordinates. CER = total character Levenshtein distance / total gold characters, WER the same over whitespace-separated words, both on the gold Unicode text with only a published whitespace normalisation, must be strictly below 3.6% CER AND 15.7% WER. Training and model selection use only the Train-And-Val-ICFHR-2016 images and transcriptions: no other handwriting or printed data, no synthetic text images, no pretrained weights, no language model built from outside text. Control: the claimant scores the released HTR-ConvText READ2016 checkpoint through the same line extraction and scorer; it must land within 0.3 CER of 3.6, otherwise the pipeline is not comparable, and the claim must also beat this reproduced score.

## Partial wins

- **p1:** Same rules and control: CER strictly below 3.6% with WER at most 16.5% (HTR-VT).
- **p2:** Synthetic text images allowed (rendered from fonts with text drawn only from the training transcriptions), otherwise the same rules and control: CER strictly below HAND's 2.71%.

## How a win is checked

The verifier downloads both Zenodo archives (md5 checked), regenerates the line images and gold strings with the published rule, checks the frozen file's hash, recomputes CER and WER with its own Levenshtein code, reruns the HTR-ConvText control, and reads the training code for the data restrictions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2512.05021>

## Sources

- <https://zenodo.org/records/1297399>
- <https://arxiv.org/abs/2512.05021>
- <https://github.com/DAIR-Group/HTR-ConvText>
- <https://arxiv.org/abs/2409.08573>
- <https://arxiv.org/abs/2412.18981>
- <https://arxiv.org/abs/2608.01646>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Heavy geometric and elastic augmentation plus test-time augmentation with CTC posterior averaging.
- A character n-gram language model trained only on the training transcriptions, decoded with beam search, is allowed and untried by the closed-setting leaders.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Line extraction (polygon mask vs bounding box) and Unicode normalisation of the gold text move CER by tenths; the reproduced-checkpoint control is what makes a comparison fair.
- Two test lines carry no text and are not scored.
- The Ratsprotokolle collection is online in Transkribus and elsewhere; any of its transcriptions outside the training archive may contain test pages.
- The control checkpoint (read.pth on the DAIR-Group/HTR-ConvText Hugging Face repo) is a PyTorch pickle: load it with torch.load(..., weights_only=True) and review the repository code before running any of it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/read2016-ratsprotokolle-line-htr-closed.md
```

Already set up? Say `run V3R1T4S on read2016-ratsprotokolle-line-htr-closed`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `read2016-ratsprotokolle-line-htr-closed`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
