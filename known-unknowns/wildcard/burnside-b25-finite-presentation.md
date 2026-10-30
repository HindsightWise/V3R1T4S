# MOONSHOT - Burnside group B(2,5): finite or infinite? (with Kourovka 11.48, Kostrikin's fifth-power question)

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (coset enumeration or rewriting on candidate presentations), or pure thought · open as of 2026-10-30

## The problem

B(2,5) = F(x,y)/F^5 is the free 2-generator group of exponent 5. Whether it is finite is the smallest open case of the Burnside problem (Wikipedia, 'Burnside problem'). B(m,n) is finite for n = 2, 3, 4, 6 (Burnside, Sanov, M. Hall). It is infinite for odd n >= 665 (Novikov-Adian, improved by Adian) and for all n >= 8000 (Ivanov for large even n, then Lysenok). Kostrikin's solution of the restricted Burnside problem for prime exponent, with the Havas-Wall-Wamsley computation (1974), shows that the largest finite quotient R(2,5) has order 5^34. So B(2,5) is finite exactly when it equals R(2,5). Kourovka Notebook problem 11.48 (A. I. Kostrikin, still open in the 21st edition, arXiv 1401.0300v49, 20 Oct 2026) asks whether the commutator [x,y,y,y,y,y,y] is a product of fifth powers in the free group <x,y > . If it is not, B(2,5) is infinite.

## What counts as a win

Success means either (a) a finite set W of words in x, y with a machine-verifiable proof (coset-enumeration certificate, confluent rewriting system, or a formal proof in Lean, Coq or Isabelle) that G = <x,y | w^5, w in W> is finite. B(2,5) = G/G^5 is a quotient of G, so it is then finite and equal to R(2,5). As a consistency check, the certificate must also show that G/G^5 has order 5^34 (G itself may be larger). Or (b) a machine-checked formal proof that B(2,5) is infinite, for example a formally verified negative answer to Kourovka 11.48.

## Partial wins

- **p1:** A positive answer to Kourovka 11.48: an explicit list of words u_1..u_k in the free group on x, y such that u_1^5 u_2^5 ... u_k^5 freely reduces to the left-normed commutator [x,y,y,y,y,y,y], using the Kourovka convention [a,b] = a^-1 b^-1 a b and [a,b,c] = [[a,b],c].

## How a win is checked

For p1: freely reduce the product and compare it with the commutator word computed by a second implementation. For (a): replay the coset table or rewriting system (ACE, KBMAG or a formal-proof kernel) and confirm the order 5^34 (it should match the nilpotent quotient R(2,5) of class 12). For (b): run the proof assistant's checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1401.0300>

## Sources

- <https://en.wikipedia.org/wiki/Burnside_problem>
- <https://arxiv.org/abs/1401.0300>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Showing that some finite quotient has order 5^34 says nothing about B(2,5); only finiteness of a presentation that uses fifth powers alone counts.
- Commutator conventions differ ([a,b] = a b a^-1 b^-1 in some texts); state and use the Kourovka one.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/burnside-b25-finite-presentation.md
```

Already set up? Say `run V3R1T4S on burnside-b25-finite-presentation`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `burnside-b25-finite-presentation`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
