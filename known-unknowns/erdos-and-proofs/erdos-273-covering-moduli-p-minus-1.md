# Erdős #273: a covering system with distinct moduli of the form p - 1, p >= 5 prime

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact covering search; lcm candidates in the 10^7 range) · open as of 2026-10-30

## The problem

Is there a covering system all of whose (distinct) moduli are of the form p - 1 with p >= 5 prime (Erdős-Graham [ErGr80, p.24])? Selfridge found one using divisors of 360 when p = 3 (modulus 2) is allowed. Progress (forum and proof-claims): R. Zeraoulia (2026-07-27, doi:10.5281/zenodo.21613011) proved any such covering has lcm L >= 393120; veljjanoski (forum 2026-09-24/28, github.com/veljjanoski/erdos273) pushed this, with two independent exact searches, to L >= 4e6 and then L >= 8e6 (all 420 counting-admissible candidates in [4e6, 8e6) have no covering). A forum comment by ideal_ombrer (2026-07-12) states that the 149 moduli with p <= 877 cannot cover Z alone (BBMST distortion sieve, exact rational check). Greedy plus local search with the full pool leaves 10-14% of residues uncovered at lcm 55440 to 1.66e6. Status: open on erdosproblems.com.

## What counts as a win

CONFIRMED: an explicit finite list of pairs (a_i, m_i) with distinct m_i, each m_i = p_i - 1 for a prime p_i >= 5, such that every integer is congruent to some a_i mod m_i. Checked by enumerating all residues modulo L = lcm(m_i) (or by an exact CRT-structured check when L is large) with two independent programs, and by proving each p_i = m_i + 1 prime. Alternatively a complete proof that no such covering exists (checkable line by line or in Lean).

## Partial wins

- **p1:** A reproducible exact proof (two independent searches, as in the forum) that no such covering has lcm L < 1.6e7, strictly above the best bound posted on the #273 thread or proof-claims page at verification time (L >= 8e6 on 2026-10-30).
- **p2:** A system of congruences with distinct moduli p - 1 (p >= 5 prime) whose exactly computed uncovered density modulo its lcm is below 0.08, strictly better than the best value posted on the thread at verification time (about 0.10 on 2026-10-30).

## How a win is checked

Recompute L, the full set of residues mod L, and the coverage with an independent sieve; verify primality of each p_i = m_i + 1. For p1, reproduce the counting test (sum of 1/m over admissible divisors m of L) for every candidate L and rerun the exact search on a verifier-chosen sample of candidates plus all borderline ones.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/273>

## Sources

- <https://www.erdosproblems.com/273>
- <https://www.erdosproblems.com/forum/thread/273>
- <https://www.erdosproblems.com/forum/thread/273/proof-claims>
- <https://github.com/veljjanoski/erdos273>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- All moduli are even: a covering splits into two coverings of Z by moduli (p-1)/2, one of which cannot use 2 (forum observation); attack the harder half first.
- Use the Balister-Bollobás-Morris-Sahasrabudhe-Tiba distortion method as a filter to discard lcm candidates before search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Modulus 2 (p = 3) is excluded; with it Selfridge's 360 example already works.
- Moduli must be distinct.
- Below lcm 8e6 is already excluded; do not re-announce weaker bounds.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-273-covering-moduli-p-minus-1.md
```

Already set up? Say `run V3R1T4S on erdos-273-covering-moduli-p-minus-1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-273-covering-moduli-p-minus-1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
