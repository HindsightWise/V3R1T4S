# Bamboo-slip fragment rejoining: beat WisePanda's Top-10 and Top-50 on the released Bamboo1350 fracture-curve benchmark without using real pairs

🏺 **Ancient texts and fragments** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (fracture curves of 64 points; benchmark arrays under 20 MB) · open as of 2026-10-30

## The problem

Zhu, Zhao, Lei, Wang, Lu, Li, Tang, Shen, Xia, Du and Xu (Nature Communications 17, article 3550, published 2026-03-06, doi 10.1038/s41467-026-70361-y; arXiv 2505.08601v2) rejoin transversely broken Western Han bamboo slips (Tomb 77, Shuihudi, Yunmeng, 179-157 BCE, not yet published) by ranking fracture-curve matches. Their WisePanda network is trained only on physics-simulated fracture curves, never on real pairs. The benchmark data are public at github.com/zhujinchi/wisepanda (HEAD af79b052 of 2026-09-30; the README licenses the code under Apache 2.0 and names no data licence, and the repository has no LICENSE file; the notebook loads the arrays from algorithm/ as dataset/...): algorithm/dataset/vector_real_118_patch.npy (118 expert-verified pairs, float64 118x4x64, sha256 94a4ffbc1f0a75b1417f85e0a67ac234e28ce5e1ec0caa138a31b3ae605feaab; the evaluation uses channels 2:4 as top and bottom curves), algorithm/dataset/interference_data_bamboo.npy (1,114 unrelated real curves, 1114x64, sha256 9f32f60c1f0f398cc21fee4c0956c782f1d186467463531094375b2be2c8b17a), algorithm/dataset/wood/vector_real_335_patch.npy (335 wooden-slip pairs, sha256 45173a322e802bfd3ed3052a929001d8fa89dce2ef9259cf15afbd7f5456a03f), algorithm/dataset/wood/interference_data_wood.npy (2,259 curves, sha256 b0eeb885f282f51ae1b01bbf1110b1844302e5e7ec0f426a8c5c51e6d48ee7e3), the synthetic training set algorithm/dataset/vector_reallike_6000.npy, cropped edge images of Bamboo236 (real-world_dataset/Bamboo236), and three trained weight pairs per method (algorithm/models/normal). Scoring (algorithm/method_comparison.ipynb, get_topk_accuracy_with_extend): every real top curve ranks all bottom candidates and every real bottom ranks all top candidates, and Top-k = hits / 236. Table 1, mean of 3 runs (%), Top-1 / 5 / 10 / 20 / 50 / 100: Bamboo236 (118 pairs) WisePanda 13.42 / 37.15 / 50.85 / 66.81 / 91.81 / 100.00; Bamboo1350 (118 pairs plus 1,114 interference curves) WisePanda 5.37 / 16.53 / 25.42 / 37.57 / 52.54 / 64.40, best Top-1 SIS 7.34, next-best Top-50 seriesGAN 38.28; Wood670 (335 pairs) WisePanda 1.89 / 10.14 / 17.25 / 24.31 / 31.24 / 35.61, best Top-1 Event-DTW 2.84. Eleven curve-matching and generative baselines are compared (DTW, FMM, SIS, Event-DTW, Drop-DTW, Modified COW, two-stage DTW, GAN, seriesGAN, DDPM, Diffusion-TS). Status 2026-10-28: no later result on these sets was found; the bamboo-slip papers of Sept-Oct 2026 work on other material (ordering of excavated Chu slips, point-cloud registration).

## What counts as a win

On Bamboo1350 built exactly as get_topk_accuracy_with_extend in algorithm/method_comparison.ipynb at commit af79b052 but with extend_number = 1114 for every method (all 1,114 interference curves, so 1,232 candidates on each side), a frozen 1,232 x 1,232 distance matrix D, whose hash is committed before scoring, in the notebook's order (row i is top candidate i: the 118 real top curves, channel 2 of vector_real_118_patch.npy, then the 1,114 rows of interference_data_bamboo.npy; column j is bottom candidate j: the 118 real bottom curves, channel 3, then the same 1,114 curves; a smaller D[i][j] means a better match, as in the notebook's ascending sort), must give two-direction Top-10 strictly above 25.42% AND Top-50 strictly above 52.54% (WisePanda, Nat. Commun. 2026, Table 1, re-read before claiming), with ties broken pessimistically (a true mate tied with other candidates is ranked after all of them), AND both strictly above the verifier's pessimistic-tie re-score of the three released WisePanda weight pairs (algorithm/models/normal/f_model_wisepanda{1,2,3}.pth with c_model_wisepanda{1,2,3}.pth) at extend_number = 1114, averaged over the three. The method never uses the real pairing: no training, tuning, threshold choice or model selection may use any information about which real top curve belongs to which real bottom curve (vector_real_118_patch.npy, vector_real_335_patch.npy, the Bamboo236 images and file names). Real curves may be used without pair information, synthetic data (vector_reallike_6000.npy or the claimant's own generator) freely.

## Partial wins

- **p1:** Wood670 (vector_real_335_patch.npy, no interference curves, 670 two-direction queries): Top-10 strictly above 17.25% and Top-50 strictly above 31.24%, same no-pairing rule and pessimistic ties.
- **p2:** Bamboo1350 at extend_number = 1114: Top-1 strictly above 7.34% (SIS, the best Top-1 in Table 1) and Top-5 strictly above 16.53% (WisePanda), same rules.
- **p3:** Bamboo236 (no interference curves): Top-20 strictly above 66.81% and Top-50 strictly above 91.81%, same rules.

## How a win is checked

The verifier clones github.com/zhujinchi/wisepanda at the recorded commit, checks the sha256 of the .npy files, rebuilds the candidate pools from the notebook's recipe (channels 2:4 of the real array, interference curves appended to both sides), checks the matrix hash against the commitment, and recomputes two-direction Top-k with pessimistic tie-breaking with independent code. It re-scores the released WisePanda weights the same way (torch.load with weights_only=True, in a sandbox) and reads the claimant's code to confirm no pair information enters training or selection. Minutes on a laptop.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/zhujinchi/wisepanda>

## Sources

- <https://www.nature.com/articles/s41467-026-70361-y>
- <https://www.nature.com/articles/s41467-026-70361-y/tables/1>
- <https://github.com/zhujinchi/wisepanda>
- <https://raw.githubusercontent.com/zhujinchi/wisepanda/af79b05247a0f961f1c3971ea2ffec704303e9bf/algorithm/method_comparison.ipynb>
- <https://arxiv.org/abs/2505.08601>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble the learned similarity with classical curve matchers: SIS has the best Top-1 on Bamboo1350 and Modified COW the best classical Top-50 on Bamboo236, so their errors differ from WisePanda's.
- Global assignment: each real top has at most one bottom, so a bipartite matching (Hungarian or Sinkhorn) over the score matrix, re-ranked by its marginals, can suppress interference curves that attract many queries.
- Hubness reduction (CSLS or mutual-nearest-neighbour scaling) on the distance matrix is cheap and often lifts Top-k in large candidate pools.
- Improve the synthetic generator: fit the fracture-model parameters to real curve statistics without pair information (allowed), as the paper's genetic_param module does.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The notebook's ranking is optimistic on ties (the true distance's index in the sorted list): a constant matrix scores 100%. The criterion uses pessimistic ties; re-score every baseline that way.
- In the released notebook the WisePanda cell builds 'Bamboo1350' with extend_number = 1000 while every other method uses 1114; the stored WisePanda numbers (52.54 Top-50) may therefore come from a 1,118-candidate pool (the notebook keeps no execution counts to tell). The criterion uses 1114 for all methods and re-scores the released WisePanda weights at 1114.
- Wood3833 cannot be rebuilt from the repository: it ships 2,259 wood interference curves, while the paper uses 3,163.
- Pair identity is encoded in the array index (row i top matches row i bottom) and in the Bamboo236 file names (N_1.png, N_2.png); any training or selection on those rows is label use.
- Orientation (upper or lower part) is given by the archaeologists; no other metadata may be used.
- There are only 118 bamboo pairs: one extra hit moves two-direction Top-k by 0.42 points, so report bootstrap intervals over pairs.
- The .pth weights are pickles; load them with weights_only=True in a sandbox.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ancient-texts/bamboo-slip-rejoining-wisepanda.md
```

Already set up? Say `run V3R1T4S on bamboo-slip-rejoining-wisepanda`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bamboo-slip-rejoining-wisepanda`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
