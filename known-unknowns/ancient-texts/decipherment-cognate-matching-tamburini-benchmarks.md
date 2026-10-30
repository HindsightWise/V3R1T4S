# Automatic decipherment on known scripts: beat CSA_OptMatcher's mean cognate-matching accuracy on the seven Tamburini 2025 benchmarks (Ugaritic, Linear B, Cypriot, Phoenician, Luvian)

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (seven lexicon files of 136 to 4,442 lines; CSA_OptMatcher itself runs 16 parallel annealers) · open as of 2026-10-30

## The problem

Decipherment methods are validated on scripts that are already read: given an unpaired word list in the 'lost' script and one in a known related language, match each lost word to its cognate. Snyder, Barzilay and Knight (ACL 2010) introduced Ugaritic/Old Hebrew; Berg-Kirkpatrick and Klein (2011) reached 90.4% noiseless; Luo, Cao and Barzilay (NeuroDecipher, ACL 2019) added Linear B/Mycenaean Greek (919 pairs) and its names-only variant. Fabio Tamburini (Frontiers in AI 8, 2025, doi 10.3389/frai.2025.1581129; CAWL 2023 version) released all seven benchmarks in github.com/ftamburin/CSA_OptMatcher (GPL-3.0, last commit c2cb1626ca, 2025-09-15): U/OH noiseless (2,214 pairs), U/OH noisy (2,214 pairs plus 1,119 and 1,108 unpaired words), Ph/Ug (105 pairs, StarlingDB), LB/MG (919), LB/MG-names (455 pairs, 919 Linear B words), CS/AG Cypriot Syllabary/Arcadocypriot (693), Luv/Hit (59 gold rows in the file; the paper says 60). Table 3 gives mean (max) accuracy over four runs for CSA_OptMatcher: 95.5 (96.3), 74.7 (75.8), 80.5 (82.9), 89.4 (91.0), 83.4 (87.0), 86.3 (87.9), 47.5 (48.3); and for NeuroDecipher rerun by Tamburini without cognate counts: 90.4, 87.6 (88.26) on U/OH noisy, the best there, 71.2, 75.8, 67.9, 75.9, and 18.2 on Luv/Hit (that run was given the number of cognates). Luo 2019's own figures (93.5, 84.7, 67.3; 65.9 on a different noisy set) are below these bests; Born, Monroe, Kelley and Sarkar (CAWL 2024) report 46% top-1 on noisy U/OH. Status 2026-10-30: no later result on these files found (citations of Luo 2019 and Tamburini 2025 checked).

## What counts as a win

For a benchmark D among the seven .cog files at commit c2cb1626ca (sha256: uga-heb.no_speNL.cog 048eb1eab6921f6594fa2ba1035dd96ee3a95fb99ca6beb6b52e60480f0fdfb7; uga-heb.no_speNoisy.cog 0f73045a2d9e44ba6212c22fb21e15e98f16dacfe66bcc6d35590121881a2e65; StarlingDB_Ph-Ug.cog ff5b915afecfe844cc6cd278d64bfe64c1b494fa687708f0342a99b431219033; linear_b-greek.cog 270ff077e1300baf5e0b383a91cf3ab9fc84a981f6f08c780f3e7fa0fdfa9cff; linear_b-greek.names.cog ec09bb5d840051965e8d849f8fa643aecaa2d2a140177195d623c08540d035c6; csyl-greek.cog 60fd1818341dcc45bcf97a6cea0ba441c0d6488992a07a22e48c7955a6bc4b58; RWT2002_Luv-Hit.cog 4de4b31a7f487739a32653b210284d93df9645b140376172786ed5d577ae6523), the verifier splits D into a lost list (non-'_' cells of column 1) and a known list (non-'_' cells of column 2), shuffles each with a published seed, relabels every lost-side symbol by a random bijection to opaque codes, and gives the claimant only these two lists. The claimant's published code outputs a one-to-one partial matching (each lost entry to at most one known entry, each known entry used at most once). Accuracy = matched gold rows (both cells non-'_', lost and known entry from the same row; '|' variants belong to their entry) / number of gold rows. A full win: one fixed configuration, run with at least 4 seeds fixed in advance, all runs reported and none selected using gold, whose mean accuracy is strictly above the best published mean on at least two benchmarks, one of them noisy (U/OH noisy, Ph/Ug, LB/MG-names, Luv/Hit). Bars: 95.5, 87.6, 80.5, 89.4, 83.4, 86.3, 47.5 (Table 3, re-read before claiming). No gold pairs, cognate counts, sign values, external lexica or pretrained language models may be used; the verifier reruns at least one seed under a fresh shuffle and relabelling.

## Partial wins

- **p1:** Same protocol, mean accuracy over at least 4 seeds strictly above the best published mean on one of the seven benchmarks.
- **p2:** Same protocol, on LB/MG-names or Ph/Ug, the claimant's mean over at least 4 seeds is strictly above CSA_OptMatcher's best single run (87.0 and 82.9 respectively), not only its mean.
- **p3:** Same protocol, Luv/Hit (same script, different languages): mean accuracy of at least 55.0% (32.45 of 59 gold rows on average) without being told the number of cognates.

## How a win is checked

The verifier downloads the .cog files from the pinned commit and checks their sha256, builds the shuffled and relabelled lists with its own seed, runs the claimant's code (CPU, hours at most) for at least one seed and checks the output is a one-to-one matching, recomputes accuracy with its own scorer and compares with the claimed runs; it reads the code to confirm that no gold pairing, cognate count or external resource is used.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ftamburin/CSA_OptMatcher>

## Sources

- <https://github.com/ftamburin/CSA_OptMatcher>
- <https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1581129/full>
- <https://aclanthology.org/2023.cawl-1.10.pdf>
- <https://github.com/j-luo93/NeuroDecipher>
- <https://arxiv.org/abs/1906.06718>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Combine CSA's sign-mapping search with NeuroDecipher's neural edit model: anneal over mappings, score with a learned character alignment.
- Exploit frequency and positional statistics of sign n-grams to prune the mapping space before annealing.
- For noisy sets, add an explicit null-match option with a calibrated threshold so unpaired words are not forced into pairs.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The .cog rows are aligned pairs: reading both columns together is reading the answer. Only the verifier's shuffled, relabelled lists are legitimate input.
- Ugaritic and Hebrew are both transliterated in Latin letters in these files, so a system that trusts identical symbols gets a free prior; the relabelling removes it, and a claim that depends on it fails.
- Pretrained LLMs know Linear B sign values and Greek words; any use of them, or of a Linear B or Cypriot sign table, voids the claim.
- Tamburini scored with his EvalModel (any variant pair in the matching counts); this entry scores one-to-one entry matches, which can be slightly stricter. Report both.
- Tamburini and Luo note that NeuroDecipher needed restarts to converge; restarts chosen by gold accuracy are selection, and all runs count in the mean.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/decipherment-cognate-matching-tamburini-benchmarks.md
```

Already set up? Say `run V3R1T4S on decipherment-cognate-matching-tamburini-benchmarks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `decipherment-cognate-matching-tamburini-benchmarks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
