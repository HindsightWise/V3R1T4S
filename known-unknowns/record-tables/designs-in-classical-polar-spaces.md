# Designs in finite classical polar spaces: a new realizable 2-(r,k,lambda)_Q design (or the first one in a Hermitian polar space)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (Kramer-Mesner with prescribed groups, e.g. solvediophant or ILP) · open as of 2026-10-30

## The problem

A t-(r,k,lambda)_Q design is a set of k-dimensional totally isotropic/singular subspaces (blocks) of a polar space Q of rank r over F_q such that every t-dimensional subspace of Q lies in exactly lambda blocks. Kiermaier, Schmidt and Wassermann (Designs in finite classical polar spaces, arXiv 2403.11188, v3 2025-10-01) give admissibility conditions (step Delta_lambda, lambda_max, Lemma 15 bound) and Table 3: the known realizable lambda for q = 2, 3 in Omega^-(2r+2,q), Omega(2r+1,q), Omega^+(2r,q) and Sp(2r,q), over 140 new parameter sets, with data on Zenodo (doi 10.5281/zenodo.13353388). Earlier designs are due to De Bruyn and Vanhove and to Bamberg and Lansdown. No designs with t >= 2 have been found in Hermitian polar spaces. For example in Omega^-(10,2) with k = 4 only lambda in {9,11,12,14,15,16,18,19,21} are known (lambda = 1 impossible).

## What counts as a win

An explicit 2-(r,k,lambda)_Q design (block list as generator matrices plus the form defining Q) for one of the (Q, q, r, k) rows of Table 3 of arXiv 2403.11188 (q in {2,3}), with lambda a multiple of that row's Delta_lambda, 1 <= lambda <= floor(lambda_max/2), lambda not in the row's 'does not exist' column, and neither lambda nor lambda_max - lambda listed as realizable in that row (including italic and asterisked entries), in the Zenodo dataset doi 10.5281/zenodo.13353388, or in any newer paper. Direction: a new realizable parameter set in a row of Table 3 (for example Omega^-(10,2), k = 4, lambda in {2,...,8,10,13,17,20,22}).

## Partial wins

- **p1:** The first 2-design (t = 2, non-trivial: 1 <= lambda < lambda_max, with parameters admissible by the integrality conditions of arXiv 2403.11188) in any Hermitian polar space H(2r-1,q^2) or H(2r,q^2) with r >= 3, verified as in the full criterion; the paper reports none found.
- **p2:** An exhaustive non-existence certificate (complete search with a checkable certificate, encoding audited) for an admissible parameter set in a row of Table 3 of arXiv 2403.11188 that is not yet listed as realizable or as 'does not exist'.

## How a win is checked

Build the form and check it is non-degenerate. In the orthogonal cases (Omega^-, Omega, Omega^+) check that every block is totally singular for the quadratic form: in characteristic 2 vanishing of the bilinear form alone is not enough. In Sp(2r,q) check that every block is totally isotropic for the alternating form. Check that each block has dimension k and that the blocks are distinct after reduced-echelon canonicalisation. Enumerate all t-dimensional totally singular/isotropic subspaces of Q, checking their number against the paper's counting formulas, and count incident blocks, asserting each count equals lambda. Confirm the parameter set is absent from Table 3, the Zenodo data and the complement. Re-read arXiv 2403.11188 (latest version) before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2403.11188>

## Sources

- <https://arxiv.org/abs/2403.11188>
- <https://doi.org/10.5281/zenodo.13353388>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prescribe cyclic subgroups of the polar space's isometry group and their normalizers, as the authors did, but try larger or non-cyclic groups and a modern ILP/SAT backend.
- Use Theorem 9 of the paper (derived/reduced designs) to turn a new design into further new parameter sets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Some table entries (in italics) come from Theorem 9 and are already realized even though they were not found by search. Italics are lost in text extraction, so read the rendered PDF.
- lambda and lambda_max - lambda are equivalent; Latin-Greek halvings give trivial-looking cases marked with an asterisk.
- For even q, Omega(2r+1,q) and Sp(2r,q) are the same polar space (Table 3 lists Sp(2r,2) as 'see Omega(2r+1,2)'); a design counts once, not under both names.
- Over GF(2), totally isotropic for the bilinear form is not the same as totally singular for the quadratic form; blocks of an orthogonal design must be totally singular.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/designs-in-classical-polar-spaces.md
```

Already set up? Say `run V3R1T4S on designs-in-classical-polar-spaces`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `designs-in-classical-polar-spaces`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
