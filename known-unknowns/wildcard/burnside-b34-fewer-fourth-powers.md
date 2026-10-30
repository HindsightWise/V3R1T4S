# Kourovka 20.36 (Havas-Newman): define B(3,4) with fewer than a million fourth powers

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (the 2-quotient half takes minutes in ANU pq; the finiteness certificate is the hard part, since a coset enumeration needs a subgroup whose own order is proved and indices beyond about 10^9 cosets are out of laptop reach) · open as of 2026-10-30

## The problem

The free Burnside group B(3,4) has order 2^69 (Bayes, Kautsky and Wamsley, 1974). Their proof uses Sanov's theorem, and Sanov's argument for B(3,4) uses more than 2^32 fourth powers. Havas and Newman (1980) showed that B(3,4) needs at least 105 relations. Kourovka Notebook problem 20.36 (G. Havas and M. F. Newman), still open in the 21st edition (arXiv 1401.0300v49, 20 Oct 2026), asks: (a) can B(3,4) be defined with fewer than a million fourth powers; (b) with fewer than a thousand; (c) what is the smallest number of fourth powers that define it?

## What counts as a win

Success means an explicit set S of fewer than 1,000,000 words in a, b, c together with a machine-verifiable proof that G = <a,b,c | w^4, w in S> is finite of order exactly 2^69, and hence equal to B(3,4). B(3,4) is a quotient of G, so |G| >= 2^69 is automatic and the proof must show |G| <= 2^69. An accepted proof is a 2-quotient (p-quotient with p = 2) computation showing the largest 2-quotient of G has order 2^69 (class 7, with the class-8 quotient equal to the class-7 one), plus a coset-enumeration or rewriting certificate that a referee can replay showing |G| <= 2^69. For example, the certificate can give the index [G:H] of a subgroup H together with a proof that |H| <= 2^69 / [G:H]. Fewer than 1,000 fourth powers (part b) is a stronger full win.

## Partial wins

- **p1:** An explicit set of fewer than 100,000,000 fourth powers with a full certificate that it defines a group of order exactly 2^69, which beats the more than 2^32 relations in Sanov's argument.

## How a win is checked

Re-run ANU NQ or GAP's pq on the presentation to confirm the 2-quotient of order 2^69 (class 7), then replay the coset-enumeration certificate (ACE) for finiteness. Independently confirm that every relator is a fourth power of a stated word and count them.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1401.0300>

## Sources

- <https://arxiv.org/abs/1401.0300>
- <https://www.math.auckland.ac.nz/~obrien/research/burnside.pdf>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A stable 2-quotient alone does not prove finiteness; a separate finiteness certificate is required.
- The 2-quotient half is routine and is not progress on 20.36. The ANU p-Quotient Program enforces exponent 4 by imposing explicit fourth powers, and Newman and O'Brien report 1016 fourth powers giving the 2-quotient of B(4,4), so a standard run yields a small set of fourth powers for B(3,4) with a stable 2-quotient of order 2^69. The whole difficulty is finiteness.
- Relators must be literally fourth powers w^4, not arbitrary consequences of the exponent law.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/burnside-b34-fewer-fourth-powers.md
```

Already set up? Say `run V3R1T4S on burnside-b34-fewer-fourth-powers`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `burnside-b34-fewer-fourth-powers`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
