# 🏺 Ancient texts and fragments

Unidentified papyri, tablet fragments, lacunae and sign detection, scored against held-out data.

**16 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★☆☆ | [Bamboo-slip fragment rejoining: beat WisePanda's Top-10 and Top-50 on the released Bamboo…](bamboo-slip-rejoining-wisepanda.md) | harvest | laptop-hours (fracture curves of 64 points; benchmark arrays under 20 MB) |
| ★★★☆☆ | [Cuneiform language and dialect identification (VarDial 2019 CLI): beat NRC-CNRC's macro-F…](cuneiform-language-identification-cli2019.md) | harvest | laptop-hours (about 5 MB of Unicode cuneiform lines) |
| ★★★☆☆ | [Cuneiform: fragment-to-fragment overlaps among UNIDENTIFIED eBL fragments (new witnesses…](ebl-unidentified-fragment-overlaps.md) | harvest | laptop-hours |
| ★★★☆☆ | [Latin dependency parsing (EvaLatin 2026): beat the best CLAS on Seneca's Phoenissae (74.0…](evalatin2026-latin-dependency-parsing.md) | standard | laptop-hours (two CoNLL-U files of about 4,150 words each; UD Latin treebanks for training) |
| ★★★☆☆ | [Latin named entity recognition (EvaLatin 2026, Ovid, Pliny, Tacitus): beat uOttawa's stri…](evalatin2026-latin-ner.md) | standard | laptop-hours (26,308 test tokens in HIPE IOB format) |
| ★★★☆☆ | [Medieval manuscript dating (ICDAR 2017 CLaMM tasks 3 and 4): beat 59.0% and 49.9% date-cl…](clamm2017-medieval-manuscript-dating.md) | harvest | laptop-days (about 12 GB of TIFF and JPEG page images; a GPU helps); scoring needs only two CSV files |
| ★★☆☆☆ | [Automatic decipherment on known scripts: beat CSA_OptMatcher's mean cognate-matching accu…](decipherment-cognate-matching-tamburini-benchmarks.md) | harvest | laptop-hours (seven lexicon files of 136 to 4,442 lines; CSA_OptMatcher itself runs 16 parallel annealers) |
| ★★☆☆☆ | [Cognate reflex prediction (SIGTYP 2022 surprise data): beat FeVeT and CogTran on normaliz…](sigtyp2022-cognate-reflex-prediction-surprise.md) | harvest | laptop-hours (10 Lexibank wordlists, a few MB; small transformers train on CPU) |
| ★★☆☆☆ | [Middle Chinese protoform reconstruction (WikiHan, WikiHan-aug, Hóu): beat the Lu-Wang-Mor…](sinitic-protoform-reconstruction-wikihan.md) | harvest | laptop-hours (5,165 cognate sets; GRU and Transformer models train on CPU or a small GPU) |
| ★★☆☆☆ | [Akkadian: restore masked/damaged signs in Oracc/eBL transliterations, beating the Lazar e…](akkadian-lacuna-restoration-heldout.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Cuneiform sign detection on the open MaiCuBeDa 3D-rendering benchmark: beat a reproduced…](cuneiform-sign-detection-maicubeda.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Greek inscriptions (I.PHI): beat Ithaca's region (70.8% top-1) and date (29.3 years) attr…](iphi-greek-inscription-attribution-ithaca.md) | harvest | laptop-days (178,551 inscriptions in a 217 MB JSON; released checkpoints about 0.2 GB each; a GPU helps) |
| ★★☆☆☆ | [Greek inscriptions: beat Stoicheia v2 (CER 15.5, top-1 74.5) on the frozen 3,000-gap file…](iphi-greek-restoration-stoicheia-frozen3000.md) | standard | laptop-days (a GPU helps; fine-tuning or reranking with a ~400M-parameter character model); test file 2.9 MB, public Greek corpora a few GB |
| ★★☆☆☆ | [Greek literary papyri: identify DCLP 'unidentified' fragments as witnesses of known works…](dclp-unidentified-literary-papyri.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Historical handwriting (READ 2016 Ratsprotokolle, line level): beat HTR-ConvText's 3.6% C…](read2016-ratsprotokolle-line-htr-closed.md) | standard | laptop-days (about 550 MB of page images; a GPU helps); scoring needs only text files |
| ★★☆☆☆ | [Latin inscriptions (LED): beat Aeneas on dating (13.4 years) and province attribution (72…](led-latin-inscription-attribution-aeneas.md) | harvest | laptop-days (180,205 inscriptions in a 62 MB JSON; released Aeneas checkpoint 146 MB; a GPU helps) |

← [All categories](../README.md)
