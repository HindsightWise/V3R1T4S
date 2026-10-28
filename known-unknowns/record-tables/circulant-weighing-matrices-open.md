# Circulant weighing matrices: settle an 'Open' CW(n,k) in Gordon's La Jolla repository

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A circulant weighing matrix CW(n,s^2) is an n x n circulant matrix with entries in {-1,0,1} and W W^T = s^2 I; equivalently a {-1,0,1} sequence of length n with s(s+1)/2 entries +1, s(s-1)/2 entries -1 and zero periodic autocorrelation. Daniel Gordon's La Jolla Circulant Weighing Matrices Repository (Zenodo v1.3, 2026-04-24; GitHub dmgordo/circulant-weighing-matrices) records the existence status of proper CW(n,k) (not contained in a coset of a proper subgroup) for n < 1000 and k <= 19^2. Its data file cwm.json (keys written CW(n,s), i.e. weight k = s^2; last commit 2026-04-24) lists 2,773 parameter pairs with status 'Open' on 2026-10-28; the project page itself only shows the summary table of known proper CWs. cwm.json lags the literature: Ming Ming Tan (arXiv:2608.18468, v2 1 Sep 2026) proves that CW(105,36), CW(140,36), CW(116,49), CW(120,49), CW(192,49), CW(140,64), CW(180,64) and CW(196,64) do not exist, and seven of these are still 'Open' in cwm.json, leaving 2,766 pairs open. The smallest-weight open cases include CW(155,25), CW(165,25), CW(186,25); for k = 36: CW(96,36), CW(112,36), CW(117,36), CW(180,36); for k = 49: CW(228,49), CW(240,49). Construct a proper CW for an open pair, or prove non-existence with a checkable certificate.

## What counts as a win

Success means a first row w in {-1,0,1}^n with exactly k nonzeros, zero periodic autocorrelation at every nonzero shift (so W W^T = kI), that is proper (its support is not contained in a coset of a proper subgroup of Z_n), verified by two independent programs, for an (n,k) whose status is 'Open' in the live La Jolla repository (https://dmgordon.org/circulant-weighing-matrices/ and the latest cwm.json on GitHub dmgordo/circulant-weighing-matrices or Zenodo, re-fetched live immediately before claiming) and that is not settled in the literature (not among the non-existence results of Tan, arXiv:2608.18468, and with no existence or non-existence result found by a fresh arXiv search for that CW(n,k)).

## Partial wins

- **p1:** A non-existence proof for a CW(n,k) that is 'Open' in the live cwm.json and not already settled in the literature (e.g. not one of the eight cases of Tan, arXiv:2608.18468), delivered as a checkable certificate (an exhaustive search with a DRAT/LRAT-verified UNSAT proof, or an explicit multiplier/field-descent argument whose computational part a skeptic re-runs).
- **p2:** A new signed or relative difference set for a parameter set listed as open in Gordon's La Jolla signed difference set or relative difference set repositories (same site), verified by the group-ring equation.

## How a win is checked

Load the sequence, check entries are in {-1,0,1} and the counts of +1 and -1 are s(s+1)/2 and s(s-1)/2. Compute the periodic autocorrelation sum_i w_i w_{i+t mod n} for every t = 1..n-1 and require all zero (or W W^T = kI directly). Check properness by testing, for each proper divisor d of n, whether the support lies in one coset of dZ_n. Use two independently written checkers; the repository's is_cwm in cwm_code.py may be read as a reference for the conventions but downloaded code is not executed. Then confirm the pair is 'Open' in the live data and not settled by Tan (arXiv:2608.18468) or a newer paper.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/dmgordo/circulant-weighing-matrices/blob/main/cwm.json>

## Sources

- <https://dmgordon.org/circulant-weighing-matrices/>
- <https://github.com/dmgordo/circulant-weighing-matrices>
- <https://zenodo.org/api/records/19741187>
- <https://dmgordon.org/signed-difference-sets/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multiplier orbits: assume the support is a union of orbits of a multiplier group (x -> t*x mod n) and solve the reduced autocorrelation equations exactly with SAT or ILP; this is how many sporadic CWs were found.
- Spectral filtering from signal processing: a CW has flat periodic power spectrum |DFT(w)|^2 = k at every frequency. Use this as a strong pruning test in backtracking (partial sums cannot exceed the bound), as in perfect-sequence searches.
- Compression (Djokovic-Kotsireas): project the sequence to Z_m for m | n, enumerate compressed sequences satisfying the compressed autocorrelation, then lift with SAT. This turns length-150 searches into length-30 searches plus lifting.
- Product and RDS constructions: check whether an Open pair follows from combining known CWs or relative difference sets in ways not yet recorded in cwm.json, then verify the explicit matrix.
- Field descent and character sums (Schmidt): for non-existence, compute the necessary conditions for each Open pair automatically to find ones that are actually excluded.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Improper matrices: a CW whose support lies in a coset of a proper subgroup is derived from a smaller one and does not settle the Open entry for proper CWs.
- Confusing periodic and aperiodic autocorrelation. CW needs periodic (cyclic) autocorrelation zero.
- Weight convention: the repository uses k = s^2; CW(n,s) versus CW(n,s^2) mix-ups lead to the wrong row.
- The repository is updated (v1.3 in April 2026). Re-download cwm.json and check the status of the exact pair before claiming.
- cwm.json lags the literature: Tan (arXiv:2608.18468, Sep 2026) proves non-existence of CW(105,36), CW(140,36), CW(120,49), CW(192,49), CW(140,64), CW(180,64), CW(196,64), all still 'Open' in the April 2026 json. Search arXiv for the exact pair before claiming either direction.
- A 'non-existence' result from an unverified search run without a certificate is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/circulant-weighing-matrices-open.md
```

Already set up? Say `run V3R1T4S on circulant-weighing-matrices-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `circulant-weighing-matrices-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
