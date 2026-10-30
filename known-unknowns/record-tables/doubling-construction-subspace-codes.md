# Doubling construction for mixed dimension subspace codes: decide whether A_q(2k+1,2k-1) = 2q^(k+1)+2 for (q,k) = (3,3) or (2,4)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT/ILP on the 82+82 or 33+33 structure) · open as of 2026-10-30

## The problem

Honold, Kiermaier and Kurz (Adv. Math. Commun. 2016) proved A_q(2k+1,2k-1) is 2q^(k+1)+1 or 2q^(k+1)+2 for mixed dimension subspace codes in F_q^(2k+1), and that the larger value needs a doubling construction: q^(k+1)+1 k-subspaces forming a maximum partial k-spread and q^(k+1)+1 (k+1)-subspaces forming the dual of one, with every k-subspace meeting every (k+1)-subspace in at most a point. It exists for k = 2 and for k = 3, q = 2 (A_2(7,5) = 34; the optimal codes were classified by Honold, Kiermaier and Kurz). Kurz's survey (arXiv 2112.11766, latest version 2025-12-20, Section 8) poses it as a research problem: does a doubling construction exist for k >= 4 or for k = 3 and q >= 3? The survey notes that a proven non-existence is also of interest, as it would improve an upper bound for A_q(2k,2k-2;k).

## What counts as a win

Either (a) an explicit doubling construction for (q,k) = (3,3) or (2,4) (or any other open pair: k >= 4, or k = 3 and q >= 3): 2q^(k+1)+2 subspaces of F_q^(2k+1) (164 subspaces of F_3^7: 82 of dimension 3 and 82 of dimension 4; or 66 subspaces of F_2^9: 33 of dimension 4 and 33 of dimension 5) with pairwise subspace distance >= 2k-1; or (b) a verifiable certificate that none exists for that (q,k) (exhaustive search with DRAT/LRAT or VIPR certificate and an audited encoding, or a formal proof). Compared against the open status in arXiv 2112.11766.

## Partial wins

- **p1:** For (q,k) = (3,3) or (2,4) and a stated nontrivial subgroup G of GL(2k+1,q): explicit G-invariant examples of BOTH halves separately (a G-invariant partial k-spread of size q^(k+1)+1 and a G-invariant set of q^(k+1)+1 (k+1)-spaces pairwise meeting in at most a point), together with a verifiable exhaustive certificate (re-runnable search plus DRAT/LRAT or VIPR certificate, encoding audited) that no G-invariant doubling construction exists; or an explicit G-invariant doubling construction, which is the full win.

## How a win is checked

RREF each generator matrix over F_q, check dimensions and distinctness, and for every pair compute d_S = dim U + dim W - 2 dim(U cap W) >= 2k-1 (equivalently: k-spaces pairwise trivial, (k+1)-spaces pairwise meeting in <= 1 dimension, mixed pairs meeting in <= 1 dimension). Re-read the survey and newer papers before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <https://arxiv.org/abs/2112.11766>
- <https://arxiv.org/abs/1512.06660>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fix the k-part as a known maximum partial spread (lifted MRD plus one) and search for a compatible dual partial spread by SAT with symmetry from the spread's stabilizer.
- Generalize the explicit q = 2, k = 3 doubling codes classified by Honold-Kiermaier-Kurz.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Both halves must be maximum (q^(k+1)+1 members); 2q^(k+1)+1 is always attainable and is not a win.
- Check every mixed pair, not only within each dimension.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/doubling-construction-subspace-codes.md
```

Already set up? Say `run V3R1T4S on doubling-construction-subspace-codes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `doubling-construction-subspace-codes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
