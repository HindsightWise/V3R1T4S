# RobustBench ImageNet Linf (eps 4/255): lower a listed model's robust accuracy below the best published value with a stronger attack

🛡️ **ML robustness** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (ResNet-18/50-sized models on the 5,000-image evaluation set at 224 px on CPU; the large Swin/ConvNeXt entries need a GPU); the ImageNet validation set must be obtained by the human under ImageNet's terms · open as of 2026-10-30

## The problem

RobustBench (Croce, Andriushchenko, Sehwag, Debenedetti, Flammarion, Chiang, Mittal and Hein; robustbench.github.io) lists 30 ImageNet models for the Linf threat model at eps = 4/255 (29 defended models plus the undefended Standard_R50). Each model_info JSON (model_info/imagenet/Linf/ < Model > .json) carries a 'clean_acc' and an 'autoattack_acc' from standard AutoAttack on RobustBench's fixed 5,000-image subset of the ImageNet validation set (robustbench.data.load_imagenet: at most 5,000 points from the list helper_files/imagenet_test_image_ids.txt, each model's own preprocessing such as Res256Crop224); only three carry an 'external' value from a stronger evaluation (Amini2024MeanSparse_ConvNeXt-L 59.64 -> 58.22, Amini2024MeanSparse_Swin-L 62.12 -> 58.92, Bai2024MixedNUTS 58.62 -> 58.50; checked 2026-10-28). The README invites any evaluation that yields a lower robust accuracy than AutoAttack, and warns that values, even clean accuracy, fluctuate with package versions such as torchvision. Published stronger evaluations not folded into the JSONs: AutoAE (Shengcai Liu, Fu Peng and Ke Tang, AAAI 2023, arXiv:2211.12713, Table 1; RobustBench's interface and fixed 5,000 images, with clean and AutoAttack columns equal to the JSON) lowers all five older ResNet entries: Salman2020Do_50_2 38.14 -> 37.96, Salman2020Do_R50 34.96 -> 34.36, Engstrom2019Robustness 29.22 -> 28.86, Wong2020Fast 26.24 -> 24.80 and Salman2020Do_R18 25.32 -> 25.00. Adaptive Auto Attack (A3, Liu et al., CVPR 2022, arXiv:2203.05154, Table 4) gives Salman's ResNet-18 AA 25.30 -> 25.16 and WRN-50-2 38.14 -> 38.12, and a ResNet-50 at AA 34.66 -> 34.64, whereas the Salman2020Do_R50 JSON says 34.96, so that row may be another checkpoint or preprocessing. MALT (Melamed, Yehudai and Shamir, NeurIPS 2024, arXiv:2407.02240, Table 2) lowers Liu2023 Swin-L, ConvNeXt-L and Swin-B and Singh2023 ConvNeXt-L/B by 0.02-0.06 points against its own AutoAttack runs, which sit 0.26-0.40 points above the JSON values (newer library versions, as MALT notes), so no MALT value is below a JSON value. PMA/PMA+ (Xie, Zheng, Huang, Ye and Ma, CVPR 2025, arXiv:2411.15210, Tables 2, 3 and 6) evaluate the top 11 ImageNet models, including Singh2023Revisiting_ConvNeXt-T-ConvStem (AA 47.60 -> PMA+ 47.56), but for 10 of the 11 models their AutoAttack column runs about 2 points below the JSON (49.46 for that model), so PMA used another image set or pipeline there. The exception is RWRN-101-2 (Peng2023Robust): clean 73.45 and AA 48.96 against the JSON's 73.44 and 48.94, a match, so its PMA+ value 48.93 (Table 6; PMA alone 49.06, Table 3) is the best published value for that model. AttackBench (Cinà et al., arXiv:2404.19460) attacks Wong2020Fast, a Salman2020Do model and a Debenedetti2022Light model on a random 5,000-image subset, not RobustBench's list. Laptop-sized entries with no published stronger evaluation on RobustBench's setup found: Chen2024Data_WRN_50_2 (40.60), Debenedetti2022Light_XCiT-S12 (41.78) and Singh2023Revisiting_ViT-S-ConvStem (48.08); Singh2023Revisiting_ConvNeXt-T-ConvStem (49.46) has only PMA's non-matching row. Known headroom is 0.02-0.14 points on modern adversarially trained models (A3, MALT, PMA+) but 0.18-1.44 points on the older ResNets (AutoAE). The result object is a tensor of 5,000 perturbed images.

## What counts as a win

Success means a saved set of adversarial inputs for the FULL RobustBench ImageNet evaluation set (the 5,000 images returned by robustbench.data.load_imagenet(n_examples=5000) with the model's own RobustBench preprocessing, in that order) against one ImageNet Linf model loaded unmodified via robustbench.utils.load_model(model_name, dataset='imagenet', threat_model='Linf') in eval mode, with weights downloaded fresh by the skeptic, such that (a) every perturbation satisfies max|x_adv - x| <= 4/255 (float64, tolerance 1e-6) in the preprocessed [0,1] input space and 0 <= x_adv <= 1; (b) the skeptic's own clean accuracy on the 5,000 images is within 0.04 points (2 images) of the live JSON clean_acc, showing that images, preprocessing and weights match RobustBench's evaluation (the skeptic pins package versions such as torch, torchvision, timm and Pillow until it matches; if no environment matches, the claim is PENDING); (c) the robust accuracy computed by the skeptic's own forward pass in that environment (clean prediction correct AND adversarial prediction still correct; argmax, ties count as not fooled) is STRICTLY LOWER (direction: min) than min(autoattack_acc, external) in the live https://raw.githubusercontent.com/RobustBench/robustbench/master/model_info/imagenet/Linf/ < Model > .json, re-fetched immediately before claiming, by at least 5 images (0.10 points); and (d) it is lower by at least 1 image than every robust accuracy already published for the same model (AutoAE arXiv:2211.12713 Table 1, A3 arXiv:2203.05154 Table 4, MALT arXiv:2407.02240 Table 2, PMA/PMA+ arXiv:2411.15210 Tables 3 and 6, and any paper or RobustBench issue of any date that the NOVELTY skeptic finds), a published row covering the model when its AutoAttack column matches the JSON autoattack_acc within 0.05. On 2026-10-28 this makes the bar AutoAE's value for Salman2020Do_50_2 (37.96), Salman2020Do_R50 (34.36), Engstrom2019Robustness (28.86), Wong2020Fast (24.80) and Salman2020Do_R18 (25.00), PMA+'s 48.93 for Peng2023Robust (0.01 below its JSON 48.94, so check (c) still binds there), and min(autoattack_acc, external) for the other listed models as far as found. How x_adv was produced is irrelevant; only the skeptic's plain forward pass on the unmodified deterministic model counts.

## Partial wins

- **p1:** A reproducible per-image attack-strength finding: at least 25 of the 5,000 images (indices listed), for one ResNet-18/50-sized model (Salman2020Do_R18, Salman2020Do_R50, Engstrom2019Robustness or Wong2020Fast), on which the skeptic's own run of standard AutoAttack (autoattack package, version='standard', seed 0, run on exactly those images, in an environment that passes check (b)) finds no adversarial example but the attacker's saved perturbations do (eps, box and misclassification checked by the skeptic). The attack must be one disclosed procedure with a stated compute budget: a union over AutoAttack seeds or restarts, or a re-run of a published ensemble with its published settings (AutoAE, A3, MALT, PMA+), does not qualify; the skeptic also reports how many of the listed images standard AutoAttack with seed 1 breaks. AutoAE's published totals are already 16-72 images below AutoAttack on these four models, so this is an attack-strength finding only, never a leaderboard change.

## How a win is checked

The human supplies the ImageNet validation set (ImageNet's terms; agents never accept them). Skeptic installs robustbench and autoattack in a fresh environment, loads the model by name into a fresh cache (never attacker-supplied weights), loads the 5,000 images with robustbench.data.load_imagenet and the model's preprocessing, compares a sha256 of the clean tensor with the attacker's manifest, and recomputes clean accuracy, which must be within 2 images of the JSON clean_acc; otherwise they pin older torch/torchvision/timm/Pillow versions and repeat, and report PENDING if no environment matches. Then they load x_adv (5000x3x224x224 float32), check the Linf bound and the box in float64, run clean and adversarial forward passes in batches on CPU (ResNet-50: tens of minutes), and count robust images as an integer out of 5,000. They re-fetch the live model_info JSON (quote URL and fetch time) and compare with min(autoattack_acc, external), then open AutoAE Table 1, A3 Table 4, MALT Table 2 and the PMA tables, apply the 0.05 matching rule, and search for newer evaluations and RobustBench 'New external evaluation(s)' issues. For p1 they read the attacker's code and run AutoAttack standard (seed 0, then seed 1) on the listed indices. If GitHub is unreachable the comparison is PENDING TABLE CHECK.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://robustbench.github.io/>

## Sources

- <https://robustbench.github.io/>
- <https://github.com/RobustBench/robustbench>
- <https://github.com/RobustBench/robustbench/tree/master/model_info/imagenet/Linf>
- <https://raw.githubusercontent.com/RobustBench/robustbench/master/robustbench/data.py>
- <https://arxiv.org/abs/2211.12713>
- <https://arxiv.org/abs/2203.05154>
- <https://arxiv.org/abs/2407.02240>
- <https://arxiv.org/abs/2411.15210>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Targeting is where ImageNet differs from CIFAR: AutoAttack's APGD-T tries only the top-9 classes out of 1,000. MALT's mesoscopic-linearity targeting (re-rank the top 100 candidate classes by a linear estimate and attack the most promising ones) found extra successes on large models; on ResNets an even wider candidate list is affordable on the ~25-35% of images that survive APGD-CE.
- Spend the whole budget on the robust residue: run APGD-CE once, keep the images it fails on, then use many restarts, longer schedules, margin/DLR/probability-margin (PMA) losses and per-image loss selection there.
- Transfer starts: perturbations from other RobustBench ImageNet models (same preprocessing) as initialisations for APGD on the target often succeed where random starts do not.
- Pick models with a large gap between clean and robust accuracy or a large APGD-CE vs APGD-T disagreement in a local run; both hint at loss-landscape pathologies.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Preprocessing: RobustBench perturbs the resized and centre-cropped [0,1] image; perturbing before resizing, or after normalisation, changes the threat model.
- Package-version drift: the README warns that values (even clean accuracy) fluctuate with torchvision versions; MALT's AutoAttack reruns differ from the JSON by up to 0.40 points (20 images) and its clean accuracies by up to 0.26 points (13 images), more than the 5-image margin. A robust count from an environment that does not reproduce clean_acc (check (b)) is not comparable with the JSON.
- Wrong subset or order of the 5,000 images, or images already misclassified counted as new successes.
- Novelty trap: AutoAE (2022) already lowers all five older ResNet entries below both the JSON and A3 (Wong2020Fast 24.80, Salman2020Do_R50 34.36, Engstrom2019Robustness 28.86, Salman2020Do_R18 25.00, Salman2020Do_50_2 37.96), so beating only the JSON value is not a record for them. A3's ResNet-50 row (AA 34.66) does not match the JSON (34.96) within 0.05, and PMA's ImageNet rows sit about 2 points below the JSON (another image set or pipeline) for 10 of its 11 models, so they do not cover those models under the matching rule; PMA's RWRN-101-2 row does match Peng2023Robust (AA 48.96 vs 48.94), so PMA+ 48.93 counts there; the NOVELTY skeptic must say which checkpoint and image set each published row uses.
- Seed noise: AutoAttack differs by a few images between runs; a difference below 5 images is not a record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/robustbench-imagenet-linf-beat-autoattack.md
```

Already set up? Say `run V3R1T4S on robustbench-imagenet-linf-beat-autoattack`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `robustbench-imagenet-linf-beat-autoattack`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
