# HomFam multiple sequence alignment: beat learnMSA2's best 66.92% mean total-column score over the 94 HomFam families

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: laptop-days (94 families of 93 to 93,681 sequences; protein-language-model embeddings need a GPU or many CPU hours) · open as of 2026-10-30

## The problem

HomFam (Sievers et al., Clustal Omega, Mol Syst Biol 2011) embeds a structure-based reference subset of each of 94 Pfam families in up to 93,681 homologs. An aligner is scored only on how it aligns the reference sequences inside the full set: SP (correctly aligned residue pairs), TC (fully correct reference columns) and column score, computed with T-Coffee aln_compare. learnMSA2 (Felix Becker and Mario Stanke, Bioinformatics 2024) is a profile-HMM aligner fed with protein-language-model embeddings. The authors' public benchmark pipeline (github.com/felbecker/snakeMSA, one line per family) holds two sets of learnMSA2 runs. The main comparison (results/*.out) gives these means over the 94 HomFam families: learnMSA2 with language model 65.90 TC / 87.31 SP / 72.98 column; learnMSA without embeddings 63.12; FAMSA 60.07; MUSCLE5 59.09; MAFFT-sparsecore 58.70; Clustal Omega 58.20; MAGUS 56.77; regressive T-Coffee 56.57. The paper's hyperparameter search (lm_experiments/results, 54 runs over three language models, r, activation and C; ProtT5 runs average 66.00 TC / 87.30 SP as the paper reports) reaches the best HomFam mean: 66.92 TC / 87.65 SP / 73.67 column for ProtT5 with r = 32, softmax, C = 10. The paper's default (r = 16, sigmoid, C = 32) scores 66.70. On the largest extHomFam set ('huge', 62 families) the best TC is 44.17 (learnMSA2). FAMSA2 (Gudys, Zielezinski, Notredame and Deorowicz, Nature Biotechnology 2026) benchmarks on a new extHomFam v37.0 set rather than HomFam. ARIES (Hoang, Armour-Garb and Singh, Princeton, 2026), a protein-language-model aligner, reports results on BAliBASE, HOMSTRAD and QuanTest2 but not on HomFam.

## What counts as a win

Alignments of all 94 HomFam families, each aligning the full family (reference plus homologs) and produced by released deterministic code, whose mean TC score over the 94 reference subsets, computed with T-Coffee aln_compare exactly as in the snakeMSA pipeline, is STRICTLY GREATER than 66.92 (learnMSA2, ProtT5, r = 32, softmax, C = 10; direction: max), with mean SP of at least 87.65. The claim must also beat the best mean HomFam TC in both https://github.com/felbecker/snakeMSA/tree/main/results and https://github.com/felbecker/snakeMSA/tree/main/lm_experiments/results (re-fetched immediately before claiming) and any HomFam TC found by a novelty search. The method must not use the HomFam or Pfam-seed reference alignments, or structures of the reference sequences, as input, and its hyperparameters must be fixed before scoring, not selected on HomFam.

## Partial wins

- **p1:** extHomFam 'huge' (62 families): mean TC STRICTLY GREATER than 44.17 (learnMSA2) under the same scoring.
- **p2:** extHomFam 'large' (83 families): mean TC STRICTLY GREATER than 59.74 (learnMSA2) under the same scoring.
- **p3:** extHomFam 'xlarge' (67 families): mean TC STRICTLY GREATER than 52.51 (learnMSA2, the best in snakeMSA results) under the same scoring.

## How a win is checked

Skeptic extracts the reference sequences' rows from each claimed alignment, scores them against the HomFam references with T-Coffee aln_compare (SP, TC, column) as the snakeMSA Snakefile does, averages over the 94 families, and compares with the best mean in results/ and lm_experiments/results/. Minutes once the alignments exist.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/felbecker/snakeMSA/tree/main/results>

## Sources

- <https://github.com/felbecker/snakeMSA/tree/main/results>
- <https://github.com/Gaius-Augustus/learnMSA>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11373405/fullTextXML>
- <https://github.com/Singh-Lab/ARIES>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The language-model gain is largest at low identity and on large families, so ensemble or consensus approaches (for example learnMSA2 plus an embedding-similarity aligner) may add TC where the two disagree.
- ARIES's reciprocal embedding similarity could replace the HMM's emission signal for the hardest families.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Scores must come from aligning the full family; aligning only the reference subset is a different and easier task.
- learnMSA_paper.out in snakeMSA is an older learnMSA run (57.29 TC) and not the record.
- results/learnMSA_language2.out (65.90 TC) is not the best learnMSA2 run either: the hyperparameter grid in lm_experiments/results reaches 66.92 TC, and the paper's default configuration scores 66.70 there. Picking the best of many configurations on HomFam itself is how that bar was reached; a claim must fix its settings in advance.
- HOMSTRAD in the same pipeline is not a valid record to cite: ARIES 2026 claims to beat the listed tools there.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/homfam-msa-total-column-score.md
```

Already set up? Say `run V3R1T4S on homfam-msa-total-column-score`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `homfam-msa-total-column-score`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
