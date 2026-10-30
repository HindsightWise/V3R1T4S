# Latin named entity recognition (EvaLatin 2026, Ovid, Pliny, Tacitus): beat uOttawa's strict micro-F1 (0.908 coarse, 0.865 fine)

🏺 **Ancient texts and fragments** · standard · tractability ★★★☆☆ · compute: laptop-hours (26,308 test tokens in HIPE IOB format) · open as of 2026-10-30

## The problem

The EvaLatin 2026 named entity task (LT4HALA 2026 at LREC; task organisers Valeria Irene Boano, Eleonora Litta and Matteo Romanello, within the CIRCSE-run EvaLatin campaign of Passarotti and Sprugnoli) asks for proper names in Classical Latin, typed coarse (person, place, collective, creature, ...) and fine, in the HIPE IOB format, scored with the CLEF HIPE scorer as micro precision, recall and F1, strict (exact type and boundaries) and fuzzy. The test file evalatin2026-ner-v0.1-test.tsv (26,308 tokens; Ovid Metamorphoses 4 and 14, Pliny the Elder Naturalis Historia IV 1-85, Tacitus Germania; 2,665 scored coarse mentions, CC BY; gold uploaded 2026-02-27) and a small training sample are in github.com/CIRCSE/LT4HALA, 2026/data_and_doc, with the official results (EvaLatin_NERC_results.pdf, 27 February 2026). Best runs, both by Callum Chan (uOttawa) with few-shot prompting of commercial LLMs: NERC coarse strict uOttawa_nerc-coarse_2 (claude-sonnet-4-5) P 0.899 R 0.917 F1 0.908 (KULeuven 0.714, argo-navis 0.534); coarse fuzzy 0.941; NERC fine strict uOttawa_nerc-fine_1 (gemini-2.5-pro) 0.865; fine fuzzy 0.887. Any resource was allowed. The proceedings (11 May 2026) add only weaker post-campaign runs (uOttawa fine-tuned LaBERTa, coarse strict 0.749). Status 2026-10-30: no later result on this file was found.

## What counts as a win

A frozen prediction file in the HIPE IOB format of evalatin2026-ner-v0.1-test-masked.tsv (sha256 487a1c9e5fec675931f10582143a0ec185b4d8b56fa588d5964821e97f9f56af; output hash committed before scoring), scored against evalatin2026-ner-v0.1-test.tsv (sha256 e92227d40f2f4b7080a68091d99c34055c41602444684ae8bbb5ed89e6f96a26) with the HIPE scorer's micro F1, must reach NERC coarse strict F1 strictly above 0.908 AND NERC fine strict F1 strictly above 0.865. The gold file and any annotated copy of these four texts are excluded from training, prompting and tuning. Annotated means any token-level annotation, not only named entities: the Tacitus Germania portion of UD_Latin-CIRCSE (gold UPOS, PROPN) and the LASLA Opera Latina lemmatised files for these texts count. Language models may be used only if their training data predate 2026-02-01 (documented) or were trained locally on stated data; the training sample and other public NER data are allowed.

## Partial wins

- **p1:** Same rules, NERC coarse strict micro-F1 strictly above 0.908 alone.
- **p2:** Same rules, NERC fine strict micro-F1 strictly above 0.865 alone.

## How a win is checked

The verifier fetches the masked and gold files, checks hashes and that the tokens are unchanged, rescores with the HIPE scorer and with its own strict span-matching code, and reads the system description for the data and model-date restrictions; it may rerun the system on one document.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/CIRCSE/LT4HALA/tree/master/2026/data_and_doc>

## Sources

- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/EvaLatin.md>
- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/data_and_doc/EvaLatin_NERC_results.pdf>
- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/data_and_doc/EvaLatin_2026_guidelines_NER.pdf>
- <https://github.com/hipe-eval/HIPE-scorer>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Gazetteer features from Pleiades and Trismegistos place and person names (no annotated copies of the test texts).
- Self-consistency: Latin names inflect, so normalise by lemma and propagate a confident label to every case form in the same document.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The gold has been public since February 2026; a model trained on later web data may have seen it. Models with training data after 2026-02-01 are excluded.
- The gold has 2,696 coarse spans, 31 of them typed non-consecutive-entity; the official per-label totals (TP+FN = 2,665) leave those 31 out, and the NE-NESTED column is empty. Reproduce the official ALL and per-label TP/FP/FN counts in EvaLatin_NERC_results.pdf with your scorer setup before claiming.
- The four texts are classics; any named-entity annotation of them found online is an annotated copy and using it is leakage.
- Tacitus's Germania is in UD_Latin-CIRCSE (train, dev and test splits) with gold PROPN tags, and LASLA's Opera Latina lemmatises these texts. Both are annotated copies of test text: a POS tagger or Latin model trained on them has seen gold name boundaries for one test document. Exclude them, or train with every Germania sentence removed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/evalatin2026-latin-ner.md
```

Already set up? Say `run V3R1T4S on evalatin2026-latin-ner`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `evalatin2026-latin-ner`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
