# Classic online bin packing: a deterministic lower bound above Balogh-Bekesi-Dosa-Epstein-Levin's 1.54278, or an algorithm at most 1.57821 (Advanced Harmonic, retuned by Martin in 2026 to 1.5782147)

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact LPs over packing patterns and weight-function checks; the hard part is designing the adversary or algorithm, not the computation) · open as of 2026-10-30

## The problem

In online bin packing, items of rational size in (0,1] arrive one by one and must be packed irrevocably into unit bins. The measure is the asymptotic competitive ratio of deterministic algorithms. Lower bounds follow Yao (1980), Brown and Liang (1.53635) and van Vliet (1.5401474). Balogh, Bekesi and Galambos (TCS 2012) found a better batched sequence of identical items, giving 248/161 ~ 1.5403726. Balogh, Bekesi, Dosa, Epstein and Levin (BBDEL; arXiv:1807.05554, Algorithmica 2021) used branching inputs, fully adaptive item sizes and a weight-based analysis. Their bound is R >= (1363 - sqrt(1387369))/120 ~ 1.5427809 (their Theorem 9). The same five authors designed Advanced Harmonic (AH; arXiv:1707.01728, ESA 2018), proved at most 1.57829. It was the first algorithm below 1.58, the barrier that had held Super Harmonic-type algorithms such as Seiden's Harmonic++ (1.58889). In October 2026 Karyamsetty Martin (arXiv:2610.32367, unrefereed) re-certified AH as an exact optimisation over its dual parameters. Re-tuning its proportion parameters gave the certified exact rational 1.5782147437..., with code and certificates public. That paper also reports that natural batch extensions of the BBDEL adversary do not raise the lower bound. The optimal ratio therefore lies in [1.5427809..., 1.5782147...]. Credit: the authors named above.

## What counts as a win

Either of the following counts. (a) Lower bound: a complete proof that every deterministic online algorithm has asymptotic competitive ratio at least R, with R STRICTLY GREATER than (1363 - sqrt(1387369))/120 ~ 1.5427809 (BBDEL Thm 9), the comparison made exactly. The proof must be a machine-checked formal proof, or a written proof whose numerical content consists of finitely many explicit inequalities and LPs. Those must come with exact rational dual certificates and be re-checked by an independent program. (b) Upper bound: an online algorithm with asymptotic competitive ratio at most R', with R' <= 1.57821 (exact rational comparison). That is a margin of about 4.7e-6 below 1.5782147437..., the exact rational of Martin (arXiv:2610.32367, Thm 3.2). That paper reports that resuming its own coordinate descent still accepts smaller moves, so re-running its public harness for longer is not a win. If Martin's certificate fails independent re-verification, the bar reverts to AH's published certificate 1.5782895555... (cited as 1.57829) with the same margin, i.e. R' <= 1.57828. The analysis must reduce to finitely many weighting-function and knapsack checks, in the style of the Super Harmonic or AH analyses, verified by an independent program in exact arithmetic. In both cases re-check arXiv and recent SODA/ESA/ICALP/Algorithmica papers for newer bounds before claiming. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** A non-branching input in the Brown-Liang-van Vliet framework: a fixed list of item sizes presented in batches of identical items, where the adversary only chooses where to stop. Its exact LP value must be strictly greater than 248/161, the Balogh-Bekesi-Galambos record for this class. It is verified by an exact rational LP with a dual certificate.

## How a win is checked

For (a) and p1, write the van Vliet LP: variables are the numbers of bins the algorithm opens with each packing pattern of the batched sizes; constraints are item counts and, for each stopping point, ALG <= R * OPT_LP with OPT computed exactly. Solve it in exact rationals (SoPlex exact or QSopt_ex) and check the dual. Calibrate on the Brown-Liang sequence (1.53635), van Vliet (1.5401474) and BBG (248/161) first. For branching and adaptive proofs, check every case inequality of the written proof with exact arithmetic. For (b), enumerate the finitely many knapsack instances of the weighting system exactly and confirm that the maximum weight is at most R'. Calibrate on Harmonic++ (1.58889) and on the AH certificate (1.57829).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.32367>

## Sources

- <https://arxiv.org/abs/1807.05554>
- <https://arxiv.org/abs/1707.01728>
- <https://arxiv.org/abs/2610.32367>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- BBDEL's gain over 248/161 came from branching plus full adaptivity (Theorem 1 of arXiv:1807.05554, borrowed from the cardinality-constrained work). Searching over branching trees of batched sizes with LP leaves is a finite search in which every leaf is an exact LP.
- For p1, search sequences of the form 1/k_i + eps in a larger space than the greedy Sylvester-like one (BBG showed greedy is not optimal), and score each with the exact LP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The lower-bound side concerns all deterministic algorithms. Lower bounds for restricted classes (Harmonic-type algorithms: 1.58333 of Ramanan et al.; the Heydrich-van Stee fixed-fraction floor, 1.5762 in the full version per Martin) or for randomized algorithms (best 1.5403) are different cells.
- Asymptotic, not absolute, ratio. The absolute ratio is settled at 5/3 and is not this target.
- Martin's 2026 bar is unrefereed. Re-run its public certificate before treating it as the incumbent. A further retune inside AH's own proportion family is what that paper already optimised to a local optimum; tiny descent gains from its harness fall inside the 1.57821 margin and do not count.
- Floating-point LP solutions are not certificates; give exact rational duals.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/classic-online-bin-packing-asymptotic-ratio.md
```

Already set up? Say `run V3R1T4S on classic-online-bin-packing-asymptotic-ratio`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `classic-online-bin-packing-asymptotic-ratio`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
