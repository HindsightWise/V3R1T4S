# HWMCC'25: first certified answer for a hardware model-checking benchmark that no participant solved

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days per benchmark (IC3/PDR, BMC, k-induction portfolios; a 16-core machine helps); certificate checking takes minutes to hours · open as of 2026-10-30

## The problem

HWMCC'25 was the 13th Hardware Model Checking Competition, at FMCAD'25, organised by Mathias Preiner, Nils Froleyks and Armin Biere; benchmarks, raw CSVs, logs and certificates are on Zenodo 17428464. Tracks (1 h on a 16-core node): bit-level safety, 330 AIGER 1.9 bit-blastings of the word-level BV benchmarks (ric3, ric3-multi, super-prove, supercar, aic3, avy, ncip, voiraig); bit-level liveness, 264 (nuxmv, super-prove); word-level BV, 330 BTOR2 (ric3, supercar, btor2-select, avr, pono, ic3-ng, btormc); word-level arrays, 310 (pono, btor2-select, avr, btormc). Only BTOR2 counterexamples were checked at word level, so word-level unsat answers are uncertified. In the raw CSVs no configuration answered sat or unsat on 46 bit-level safety, 40 liveness, 39 BV and 132 array benchmarks. The safety lists overlap: 14 of the 46 were answered at word level (e.g. 2019/goel cal157-cal211 and mul1 unsat by avr, xsokoban level_5 sat by ric3) and 7 of the 39 at bit level. 32 designs have no answer in either track: 2019/beem/pgm_protocol.8.prop6; 2020/mann fifo-p0 and rast-p17; eight 2024/hkust/refinement_checking ISA checks (ILA_Flute_*, ILA_Piccolo_*, ILA_Ridecore_JAL); 2024/hkust/x-epic/a16-p75; three 2025/hkust miters (examples 10, 82, 95); seven 2025/ntu/sat/xsokoban levels (10, 20, 27, 48, 66, 73, 90); yosyshq cv32e40x p228 and p530; eight SoSy-Lab translations of SV-COMP tasks (eca-rers2012, nla-digbench, float-benchs, loops-crafted). Of these, only ILA_Flute_XORI_sanity has an answer in the HWMCC'24 CSVs (unsat by ncip-minicraig, uncertified), leaving 31. hwmcc.github.io/2026 returns 404 on 2026-10-30. Families were contributed by HKUST, NTU, SoSy-Lab (LMU), YosysHQ, Goel, Mann and others.

## What counts as a win

Success means one of the 31 designs named in the statement (no sat/unsat answer from any configuration in hwmcc25-bitlevel-safety.csv or hwmcc25-wordlevel-bv.csv on Zenodo 17428464, and none in the HWMCC'24 CSVs at hwmcc.github.io/2024 or any earlier edition's results), its file taken from the track tarball and matched by SHA-256, plus a certificate in the HWMCC'25 formats. For sat, a counterexample accepted by aigsim on the bit-level .aig or by btorsim on the word-level .btor2. For unsat, an AIGER safety certificate for the bit-level .aig accepted by Certifaiger (a word-level unsat claim is certified only through this bit-level translation). The design must not be reported solved in the HWMCC'25 slides or logs, a later HWMCC or a paper. Uncertified answers do not count.

## Partial wins

- **p1:** A sat witness accepted by btorsim for one of the 132 word-level array benchmarks that no HWMCC'25 participant solved, other than 2019/mann/safe/arbitrated_fifos_n2d8w8 (answered unsat by nuxmv in HWMCC'24): 131 eligible on 2026-10-30 against the HWMCC'24 CSVs. The benchmark must also have no sat/unsat answer in the HWMCC'20 or HWMCC'19 results, matched by file name.
- **p2:** A certified answer (aigsim or Certifaiger for bit-level safety, btorsim for a word-level sat witness, the checker behind hwmcc25-bitlevel-live-cert.csv for liveness) for one of the 6 benchmarks answered by some tool but never certified: cal222, 2020/mann/stack-p0 and yosyshq veer-p7 (bit-level safety, unsat claimed in HWMCC'25), ILA_Flute_XORI_sanity (unsat claimed in HWMCC'24 only), 6s364j00000 (liveness, sat claimed by super-prove) and array-examples/standard_init3_ground-1 (arrays, sat claimed by btor2-select).
- **p3:** For one of the 40 unsolved bit-level liveness benchmarks, a lasso counterexample accepted by aigsim, or a certificate accepted by the checker used for hwmcc25-bitlevel-live-cert.csv.
- **p4:** A Certifaiger-accepted unsat certificate for the bit-level .aig of one of the 12 designs that HWMCC'25 answered unsat only at word level (uncertified) and not at bit level: 2019/goel/industry cal157, cal188, cal191, cal206, cal211 and mul1; 2024/hkust/seq/gcd_2_4/gcd_bit_width_large; SoSy-Lab pals_lcr.3.ufo.BOUNDED-6.pals+Problem12_label01, eca-rers2012 Problem17_label44 and Problem19_label01, and loop-lit jm2006.c.i.v+cfa-reducer; 2025/hkust example_52_miter_miter.

## How a win is checked

Fetch the track tarball from Zenodo 17428464, extract the benchmark and hash it. Run aigsim or btorsim on the witness, or Certifaiger (github.com/Froleyks/certifaiger) on the AIGER certificate against the bit-level benchmark, recording versions and the accepting output. Re-read the bit-level safety and word-level BV CSVs together (plus the liveness, array and *-cert CSVs for partial wins) to confirm the design had no sat/unsat answer in either track, match it by file name in the HWMCC'24 CSVs at hwmcc.github.io/2024 and earlier editions, and check hwmcc.github.io for a newer edition.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zenodo.org/records/17428464>

## Sources

- <https://hwmcc.github.io/>
- <https://hwmcc.github.io/2025/>
- <https://zenodo.org/records/17428464>
- <https://github.com/Froleyks/certifaiger>
- <https://github.com/arminbiere/aiger>
- <https://github.com/hwmcc/btor2tools/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Miters (2025/hkust *_miter_miter) and ISA refinement checks are equivalence problems: structural hashing, SAT sweeping and induction over internal equivalences (ABC dprove/&cec style) often beat generic IC3.
- xsokoban levels sit under a 'sat' folder: a Sokoban solver can produce the move sequence, which is then encoded as an input trace and checked with aigsim/btorsim.
- SoSy-Lab tasks come from SV-COMP programs whose verdicts are in sv-benchmarks. Use the program-level invariant to build a hardware inductive invariant, then a Certifaiger certificate.
- For p4, avr and pono proved the goel industry cases at word level: a word-level inductive invariant from those tools, bit-blasted, is a starting point for a Certifaiger certificate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several families have answers known by construction (xsokoban 'sat', SV-COMP-derived tasks with known verdicts). The win is the first certified solve, not a new truth, so state that.
- The bit-level safety track is the bit-blasted BV track: always check both CSVs (and both cert CSVs). A design unsolved in one track may be solved, even certified, in the other.
- AIGER 1.9 reset functions: a witness must respect them, and older aigsim versions may mishandle them.
- The word-level unsat path goes through the bit-level translation. Make sure the two are the same benchmark name and property.
- HWMCC'24 used the folder name 2024/hku where HWMCC'25 uses 2024/hkust: match earlier editions by file name.
- Check the HWMCC'25 slides, earlier editions and later papers (and any HWMCC'26 if one is announced) before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/hwmcc25-unsolved-first-certified.md
```

Already set up? Say `run V3R1T4S on hwmcc25-unsolved-first-certified`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hwmcc25-unsolved-first-certified`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
