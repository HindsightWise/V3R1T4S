# Latin dependency parsing (EvaLatin 2026): beat the best CLAS on Seneca's Phoenissae (74.03) and Aquinas's Summa (83.14) under the official scorer

🏺 **Ancient texts and fragments** · standard · tractability ★★★☆☆ · compute: laptop-hours (two CoNLL-U files of about 4,150 words each; UD Latin treebanks for training) · open as of 2026-10-30

## The problem

EvaLatin 2026 (LT4HALA 2026 at LREC; parsing task run by Federica Iurescia, Marco Passarotti and Rachele Sprugnoli of CIRCSE, Università Cattolica del Sacro Cuore) set Universal Dependencies parsing of two unseen Latin texts with gold tokenisation, lemmas, POS and features given: poetry, Seneca's Phoenissae (308 sentences, 4,156 syntactic words plus 86 multiword tokens, from LASLA's Opera Latina, converted, pre-parsed and revised by an expert) and prose, a portion of Thomas Aquinas's Summa Theologiae from the Index Thomisticus (203 sentences, 4,151 words). No training set was imposed: any data or model could be used. Gold files (uploaded 2026-02-20), scorers, all submitted runs (EvaLatin_2026_runs) and ranking are in github.com/CIRCSE/LT4HALA, 2026/data_and_doc. Best CLAS with subtypes: poetry THIVLVC_2 (Pommeret, Wagret and Deret) 74.03, prose UppsalaNLP_1 (Sara Stymne) 83.14 (UDPipe baseline 56.94 and 79.41); CLAS without subtypes 76.08 (THIVLVC_2) and 86.88 (UppsalaNLP_1); LAS with subtypes 72.88 and 84.41; LAS without subtypes 77.60 and 87.93 (both THIVLVC_2). The proceedings (11 May 2026) add contrastive runs (Uppsala ITTB-only prose CLAS+s 82.77, LAS+s 84.43) that do not move the CLAS-with-subtypes records. Since then UD_Latin-CIRCSE has added the whole of Phoenissae (new text added April 2026, merged to master 6 May 2026): all 308 poetry test sentences, 306 of them with the same HEAD and DEPREL as the EvaLatin gold (our check, 2026-10-30). Status 2026-10-30: no later result on these files was found.

## What counts as a win

Frozen CoNLL-U outputs (HEAD and DEPREL filled, all other columns as in the released test files EvaLatin_2026_poetry_test_data.conllu, sha256 b9fe2d95717976e4bcd5617edc71449890d032621fd6de841e55cf4cf3aeba4f, and EvaLatin_2026_prose_test_data.conllu, sha256 29cef94d9afca54ea488b1875d983465e3dc712f9f5e9afd124283e7902d533d; output hashes committed before scoring), scored against EvaLatin_2026_poetry_gold.conllu (sha256 0584cc804f6fd0cae200cd0640f0f391af2099bae5f450edc5239d0aadfb3842) and EvaLatin_2026_prose_gold.conllu (sha256 59ac041f12d9d30da5cc1f20122ea6a0c87748722caaf714383112cf71811f60) with the official scorer, meaning data_and_doc/conll18_ud_eval_with_subtypes-EvaLatin2026.py run with --subtypes (not the _modified version), which counts a word for CLAS only when its full DEPREL is in the plain UD content list and reproduces 74.03 on the released THIVLVC_2 poetry run and 83.14 on the released UppsalaNLP_1 prose run, must reach CLAS with subtypes strictly above 74.03 on poetry AND strictly above 83.14 on prose. The gold files, the released runs and any copy of these test sentences are excluded from training and tuning. That includes the Seneca Phoenissae sentences in UD_Latin-CIRCSE (all 308 poetry test sentences are there since the May 2026 release; drop every Phoenissae sentence from every split) and any UD Latin-ITTB or Opera Latina sentence that matches a test sentence (verifier checks overlap). Language models may be used only if their training data predate 2026-02-01 (documented release) or were trained locally on stated data. One system and configuration covers both files.

## Partial wins

- **p1:** Same rules, CLAS with subtypes strictly above the record on one of the two files.
- **p2:** Same rules, LAS without subtypes strictly above 77.60 (poetry) and 87.93 (prose).

## How a win is checked

The verifier fetches the gold and test files, both scorer versions and the released runs from CIRCSE/LT4HALA and checks hashes. It confirms that conll18_ud_eval_with_subtypes-EvaLatin2026.py --subtypes reproduces 74.03 (THIVLVC_2 poetry) and 83.14 (UppsalaNLP_1 prose) on the released runs, or its own reimplementation of that rule does. It checks that the outputs keep the given tokenisation and annotation, then rescores them with that scorer and with its own CLAS code. It checks the training data for overlap with the test sentences (exact and near-duplicate sentence match), in particular that no Phoenissae sentence from UD_Latin-CIRCSE and no matching ITTB or Opera Latina sentence was used.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/CIRCSE/LT4HALA/tree/master/2026/data_and_doc>

## Sources

- <https://github.com/CIRCSE/LT4HALA/tree/master/2026>
- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/EvaLatin.md>
- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/data_and_doc/EvaLatin_2026_Ranking_DEP.pdf>
- <https://github.com/CIRCSE/LT4HALA/blob/master/2026/data_and_doc/EvaLatin_2026_guidelines_DEP_V11.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Train on a harmonised mix of the UD Latin treebanks (Perseus, and UD_Latin-CIRCSE's other Seneca tragedies Hercules Furens, Agamemnon and Oedipus for poetry, with every Phoenissae sentence removed; ITTB for Aquinas) with treebank embeddings, as the guidelines suggest.
- Use the gold morphology in the input: feature-rich biaffine parsers gain most from it on poetry.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- UD_Latin-CIRCSE (master since 6 May 2026, UD release of May 2026) contains Seneca's Phoenissae in its train, dev and test splits: all 308 poetry test sentences, 306 with gold-identical trees. Any model trained on a UD_Latin-CIRCSE release from 2026 or later, or a pretrained Latin parser whose training set includes it, has seen the answer key. Filter by sent_id (SenPhoen-P-17-* or Latin_SenecaYounger_Phoen_poetry-*) and by text match.
- UD Latin-ITTB is built from Aquinas and may contain the Summa test passage; remove any overlap before training (our check found 1 exact sentence match and 2 sentences sharing an 8-gram).
- The gold has been public since February 2026: a language model trained on later web data may have seen it. Models with training data after 2026-02-01 are excluded.
- Rankings with and without subtypes differ; this entry's bar is CLAS with subtypes, under the unmodified scorer. The _modified scorer in the same folder counts subtyped relations as content words and gives different numbers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/evalatin2026-latin-dependency-parsing.md
```

Already set up? Say `run V3R1T4S on evalatin2026-latin-dependency-parsing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `evalatin2026-latin-dependency-parsing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
