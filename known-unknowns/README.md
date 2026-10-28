# 🗺 Known unknowns

The hills nobody has climbed yet: **445 open problems in 24 categories**. Each page says what the problem is, what counts as a win, how a win is checked, where to check it is still open, ideas to start from, and the traps that produced false wins before.

Pick one, then tell your agent:

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/<category>/<problem>.md
```

Or don't pick: your agent can roam anywhere, as long as a stranger's computer can check the answer.

| Category | Open | What's in it |
|---|---|---|
| 🕸️ [Graphs, games and automata](graphs-games-automata/README.md) | 59 | Graph records, puzzles, tilings and cellular automata. |
| 🧬 [Disease research](disease-research/README.md) | 51 | Cancer, rare and neglected diseases, antimicrobial resistance and outbreaks: public data, public scorers, computational claims only. |
| 📊 [Record tables](record-tables/README.md) | 44 | Codes, designs, packings and constructions measured against public tables. |
| 🔢 [Number hunts](number-hunts/README.md) | 30 | Certified bounds, exact searches and explicit solutions in number theory and computability. |
| 🦠 [Biology](biology/README.md) | 29 | Protein, DNA and evolution benchmarks and record tables with mechanical checkers. |
| ⚛️ [Physics](physics/README.md) | 28 | Statistical mechanics, lattice models, quantum information and materials: exact counts, certified bounds, constants to record precision and public leaderboards. |
| ✏️ [Erdős problems and proofs](erdos-and-proofs/README.md) | 23 | Erdős problems and relatives: counterexamples, small cases, machine-checked proofs. |
| 🚚 [Optimization benchmarks](optimization-benchmarks/README.md) | 23 | Best-known solutions on public routing, scheduling and MIP benchmark libraries. |
| 🔐 [Unbroken ciphers](unbroken-ciphers/README.md) | 20 | Historical and challenge ciphers nobody has read yet. |
| ⚪ [Packings and physics](packings-physics/README.md) | 19 | Circle, sphere and point configurations and energy minima vs live tables. |
| 🌍 [Earth and sky](earth-and-sky/README.md) | 18 | Missed events in open geophysical and space archives, checked against live catalogs. |
| 📜 [Undeciphered scripts](undeciphered-scripts/README.md) | 17 | Writing systems and corpora nobody can read; wins are frozen, checkable predictions, never interpretations. |
| 🔭 [Sky archives](sky-archives/README.md) | 16 | New vetted candidates in public astronomy archives (never 'a planet', only 'a candidate'). |
| ⚡ [Algorithms](algorithms/README.md) | 13 | Fast matrix multiplication schemes and other algorithmic records. |
| 💊 [Drug discovery](drug-discovery/README.md) | 13 | Molecular property, binding, docking and design leaderboards scored on official splits. |
| 🛡️ [ML robustness](ml-robustness/README.md) | 8 | Stronger attacks and soundness counterexamples on public, locally run benchmark models. |
| 🤖 [Machine learning](machine-learning/README.md) | 7 | Small leaderboards and efficiency records a laptop can top with open models run locally. |
| 🎲 [Recreational math](recreational-math/README.md) | 6 | Puzzle records, magic squares, dissections and sequences with public tables. |
| ✅ [Formal proofs](formal-proofs/README.md) | 6 | Statements waiting for a machine-checked proof: Lean's kernel is the referee. |
| 🏺 [Ancient texts and fragments](ancient-texts/README.md) | 4 | Unidentified papyri, tablet fragments, lacunae and sign detection, scored against held-out data. |
| 🌋 [Herculaneum scrolls](herculaneum-scrolls/README.md) | 4 | Ink detection and surface segmentation on the public Vesuvius Challenge data. |
| 🗜️ [Compression and code golf](compression-and-golf/README.md) | 4 | Byte-exact compression records and shortest-program tables. |
| 🃏 [Wildcard](wildcard/README.md) | 2 | Open, checkable problems from fields nobody else here covers. |
| 🗝️ [Crypto math](crypto-math/README.md) | 1 | Public challenges built to be attacked, and the mathematics of cryptographic primitives. |

Tractability, compute and status dates are guesses from the day each page was written; the status page linked on each problem is the only authority. Every page is generated from [`bank/targets.json`](../bank/targets.json): `python3 bank/build_known_unknowns.py`.
