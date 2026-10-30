# 💥 Particle physics

Open-data and simulation benchmarks from high-energy physics: tagging, tracking, anomaly detection and fast simulation, scored against released truth.

**5 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★☆☆☆ | [Fundamental limit of jet tagging (GPT-generated top/QCD jets with known likelihood ratio)…](jet-tagging-fundamental-limit-gpt-jets-gap.md) | standard | needs cluster (Zenodo 14824930 is a 24.4 GB zip, about 154 GB unpacked; the reference taggers train on 10M jets per class on GPUs) |
| ★★☆☆☆ | [Pythia quark-gluon jet tagging (Komiske-Metodiev-Thaler dataset): beat PELICAN's AUC 0.92…](quark-gluon-pythia-tagging-auc-record.md) | standard | laptop-days (2M jets in 20 files, about 2.1 GB; a single GPU brings training down to a few hours) |
| ★★☆☆☆ | [Community top-tagging dataset (Kasieczka et al.): beat OmniLearned-l's background rejecti…](top-tagging-landscape-rejection-record.md) | standard | laptop-days (about 1.2M training jets, 1.7 GB in all; a GPU strongly advised; external pre-training on large public jet sets is allowed for the full win but needs cluster time) |
| ★★☆☆☆ | [Dark Machines unsupervised anomaly detection: beat the best median total improvement (15.…](darkmachines-unsupervised-median-total-improvement.md) | standard | laptop-days (four channels; channel 3 has 8.5M background events; the hackathon archive is 2.1 GB) |
| ★☆☆☆☆ | [JetClass 10-class jet tagging: beat L-GATr's 0.866 accuracy and 0.9885 macro AUC on the 2…](jetclass-ten-class-accuracy-auc.md) | moonshot | needs cluster (100M training jets in about 152 GB of files, 190 GB with validation and test; reference models train for days on multiple GPUs) |

← [All categories](../README.md)
