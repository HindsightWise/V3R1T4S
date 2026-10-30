# Legendre pairs: settle an open odd length below 200 (115, 145, 159, 161, 169, 175, 177, 185, 187, 195)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (compression, PSD filtering and SAT lifting; checking is instant) · open as of 2026-10-30

## The problem

A Legendre pair of odd length l is a pair of +-1 sequences A, B with PAF_A(s) + PAF_B(s) = -2 for every s = 1..l-1 (periodic autocorrelation); it gives a Hadamard matrix of order 2l + 2 (Fletcher, Gysin and Seberry), and one is conjectured to exist for every odd l. Balonin and Đoković (arXiv:2010.02829, 2020) listed the open l < 200 as 77, 85, 87, 91, 93, 115, 117, 123, 129, 133, 145, 147, 159, 161, 169, 175, 177, 185, 187, 195 and settled three; Turner, Kotsireas, Bulutoglu and Geyer found l = 77 (arXiv:2101.10918), Kotsireas and Koutschan 117, 129, 133 and 147 (arXiv:2101.03116), and Kotsireas, Koutschan, Bulutoglu, Arquette, Turner and Ryan 85 and 87 (arXiv:2111.02105 v3, 8 Apr 2024), leaving ten open values below 200: 115, 145, 159, 161, 169, 175, 177, 185, 187, 195; their two structured searches at 115 found nothing. Kotsireas, Koutschan and Winterhof (arXiv:2408.16318 v2, 2025) give 115 as the smallest unsettled length, and Egan, Kotsireas, London and Ó Catháin (arXiv:2610.27175, Oct 2026) list existence at every odd length as their Problem 1. Ramos, Hulak and de Queiroz (arXiv:2607.20765) studied l = 333 (order 668), an order since settled by other means.

## What counts as a win

Success means explicit +-1 sequences A, B of a length l in {115, 145, 159, 161, 169, 175, 177, 185, 187, 195} with PAF_A(s) + PAF_B(s) = -2 for every s = 1..l-1, computed exactly by two independent programs, where no Legendre pair of that length is reported at claim time in a fresh arXiv search for 'Legendre pair' (direction: none; existence target).

## Partial wins

- **p1:** A certified exclusion of Legendre pairs of length 115 (or another listed length) in which both sequences are invariant under a stated nontrivial subgroup H of Z_l^*, or have a stated compression, where that exclusion is not already published (Section 4 of arXiv:2111.02105 reports two non-exhaustive searches at 115); delivered as code and logs the skeptic re-runs to the same empty result, or as a DRAT/LRAT certificate.

## How a win is checked

Check both sequences have length l and entries +-1; compute PAF_X(s) = sum_j x_j x_{j+s mod l} in integers for every s and require PAF_A(s) + PAF_B(s) = -2 for s = 1..l-1. Sanity check: (sum A)^2 + (sum B)^2 = 2, so both row sums are +-1. The value 2l + 2 is the PSD sum at nonzero frequencies, not at frequency 0. Calibrate the checker on two copies of the Legendre sequence of a prime p = 3 mod 4. Optionally negate the sequences so both row sums are 1, build the bordered two-circulant Hadamard matrix of order 2l + 2 (Fletcher, Gysin and Seberry; Theorem 4 of arXiv:2610.27175) and verify H H^T. Use two independent checkers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2111.02105>

## Sources

- <https://arxiv.org/abs/2111.02105>
- <https://arxiv.org/abs/2010.02829>
- <https://arxiv.org/abs/2408.16318>
- <https://arxiv.org/abs/2610.27175>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Compression: for l = m*d the d-compressions of A and B satisfy derived PAF and PSD conditions; enumerate compressed pairs and lift (115 = 5*23, 145 = 5*29, 159 = 3*53, 161 = 7*23, 169 = 13^2, 175 = 5^2*7, 177 = 3*59, 185 = 5*37, 187 = 11*17, 195 = 3*5*13).
- Multiplier groups: assume invariance under a subgroup of Z_l^* (85 was found this way) and the balance conjecture of arXiv:2111.02105 for lengths divisible by 5.
- PSD test: PSD_A(k) + PSD_B(k) = 2l + 2 at every nonzero frequency, used as a filter before exact checks.
- Kotsireas' Problem 2 in arXiv:2610.27175 (uncompressing Legendre-symbol sequences of length p to a pair of length p*q^2) gives a structured route for l = 175 = 7*5^2.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- l = 333 corresponds to order 668, which is settled; it is not part of this entry.
- Quaternary Legendre pairs and generalised Legendre pairs of even length are different objects (see the quaternary entry).
- PSD values computed in floating point are filters only; the final PAF check must be exact.
- The J. Symbolic Comput. paper by Kotsireas, Gallardo-Cava, Gómez and Gómez-Pérez on Legendre pairs of length pq^2 (reference [60] of arXiv:2610.27175) was not read for this entry; check it for l = 175 = 7*5^2 and the other listed lengths before claiming.
- DCP's crowd-sourced, prize-pool Legendre-pair hunts (jobs.dcp.dev/legendre117, finished; legendre153.dcp.dev, structured pairs of length 153) are live challenges at other lengths and are not part of this entry. Joining or submitting to them is an action only the human may take.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/legendre-pairs-open-odd-lengths.md
```

Already set up? Say `run V3R1T4S on legendre-pairs-open-odd-lengths`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `legendre-pairs-open-odd-lengths`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
