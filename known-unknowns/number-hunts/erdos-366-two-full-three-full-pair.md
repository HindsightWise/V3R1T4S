# Erdős #366: a 2-full n with n+1 3-full (or two consecutive 3-full integers)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (enumerate 3-full numbers to ~1e27 and test neighbours for powerfulness) · open as of 2026-10-30

## The problem

Are there 2-full n with n+1 3-full (every prime dividing n divides it at least twice, every prime dividing n+1 at least three times)? Erdős-Graham [ErGr80, p.68] note (8,9) and ask whether it is the only consecutive pair with one 3-full and one 2-full; Ralf Stephan observed 12167 = 23^3, 12168 = 2^3 3^2 13^2 (known to Golomb 1970). Both known pairs have the 3-full number first; no n with n 2-full and n+1 3-full is known. By OEIS A060355 there are no other such pairs below 10^22 (site page, edited 2026-07-16). Erdős also asked whether two consecutive 3-full integers exist (Guy B16); none is known. David Turturean (forum 2026-04-14) notes abc implies finitely many; a proof claim (Theofil Xeff, 2026-07-22) bounds n < 10^16136778163 assuming Baker's explicit abc. Status: open.

## What counts as a win

CONFIRMED: an integer n with complete PROVEN prime factorisations of n and n+1 showing that n is 2-full and n+1 is 3-full (every prime dividing n divides it at least twice, every prime dividing n+1 divides it at least three times). Two consecutive 3-full integers (in either order) also count, since they answer Erdős's weaker question in [Er76d] and Guy B16.

## Partial wins

- **p1:** A third consecutive pair in the other direction: n 3-full and n+1 2-full with (n, n+1) not (8, 9) or (12167, 12168), with complete proven factorisations (the site records none other below 10^22).
- **p2:** A reproducible exhaustive search (code plus logs, rerun by the verifier on sampled ranges) proving there is no pair of either type (2-full next to 3-full, in either order) below 10^25 other than (8,9) and (12167,12168), extending the 10^22 bound stated on the #366 page.

## How a win is checked

Factor n and n+1 completely (the 3-full side is enumerable as a^3 b^4 c^5 forms); prove each prime factor prime; check exponents. For p2, recount 3-full numbers up to the bound (asymptotically about 4.66 x^{1/3}) and audit the powerfulness test of each neighbour on verifier-chosen subranges.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/366>

## Sources

- <https://www.erdosproblems.com/366>
- <https://www.erdosproblems.com/forum/thread/366>
- <https://oeis.org/A060355>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Enumerate 3-full m = a^3 b^4 c^5 (b, c squarefree, coprime) up to X; there are only about 4.66 X^{1/3} of them, so X = 1e27 means ~5e9 candidates. Test m-1 and m+1 for powerfulness by trial division to X^{1/5} and exact square/cube/a^2 b^3 tests on the cofactor.
- Pell-type families x^2 - D y^3 = +-1 parametrise many candidates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Direction matters: both known examples are (3-full, 2-full); the title asks for (2-full, 3-full).
- A060355 lists consecutive powerful pairs, not 3-full ones; filter it rather than citing it as the answer.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/erdos-366-two-full-three-full-pair.md
```

Already set up? Say `run V3R1T4S on erdos-366-two-full-three-full-pair`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-366-two-full-three-full-pair`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
