# MOONSHOT - Erdős–Ginzburg–Ziv constant for odd n: refute s(C_n^3) = 9n-8 (smallest open n = 7) or beat 20n-19 in rank 4

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

s(G) is the least l such that every sequence of l elements of G has an n-term zero-sum subsequence, where n = exp(G). For odd n, Elsholtz (2004) proved s(C_n^3) >= 9n-8, Edel, Elsholtz, Geroldinger, Kubertin and Rackham (Q. J. Math. 2007) proved s(C_n^4) >= 20n-19, and Edel (Des. Codes Cryptogr. 47 (2008) 125-134) gave s(C_n^5) >= 42n-41 and s(C_n^6) >= 96n-95, the bounds quoted in arXiv:2610.35819. All these bounds come from point sets in {0,1,2}^r, each point taken n-1 times. The standing conjecture for odd n is s(C_n^3) = 9n-8 (Fan-Gao-Zhong, arXiv:1010.5101, J. Number Theory 2011; their Conjecture 4.2 states s(C_n^r) = a_3(r)(n-1)+1 in every rank, with cap sizes a_3(r) = 9, 20, 45, 112 for r = 3..6). It is proven for n = 3 (19) and n = 5 (37, Gao-Hou-Schmid-Thangadurai, Integers 2007), and so for every n = 3^a 5^b via s(C_mn^r) <= (s(C_m^r)-1)n + s(C_n^r). Fan-Gao-Zhong also prove it for n = 3^a 5^b 7^c 11^d 13^e when the 3^a 5^b factor is astronomically large, using a computer check that C_7^3, C_11^3 and C_13^3 have Property D0 with respect to 9: every sequence g T^(n-1) with |T| = 9 has an n-term zero-sum. In rank 4, s(C_3^4) = 41 = 20*3-19, and hence s(C_{3^a}^4) = 20*3^a-19. In October 2026 Wang-Zeng (arXiv:2610.25271) and Elsholtz (arXiv:2610.35819) broke the analogous Harborth bound for even non-power-of-two n in ranks >= 4. Elsholtz notes that for odd exponents no counterexample to Property C or D is known, and that Property D for C_15^3 is open. The smallest odd n for which s(C_n^3) is undetermined is n = 7 (9n-8 = 55). Find an odd n and an explicit sequence that beats one of these bounds.

## What counts as a win

Success means one of the following, verified by two independent programs. (a) An explicit sequence over C_n^3 of length 9n-8 with no zero-sum subsequence of exactly n terms, where n is odd and not of the form 3^a 5^b (for n = 7, length 55). (b) An explicit sequence over C_n^4 of length 20n-19 with no n-term zero-sum, where n is odd, n >= 5, n is not a power of 3 and n^4 <= 10^7 (for n = 5, length 81). In both cases |S|+1 must be STRICTLY GREATER (direction: max) than the best known lower bound for that (n, r) at verification time. That bound is 9n-8 or 20n-19 unless the latest arXiv:2610.35819, Edel et al. 2007, Edel 2008 or a fresh arXiv search shows a larger value for that n. The cell must not be one where s is proven equal to the bound, since that would contradict a theorem: n = 3^a 5^b in rank 3, the Fan-Gao-Zhong 2011 cases, or n = 3^a in rank 4. Check this first.

## Partial wins

- **p1:** Ranks 5 and 6: an explicit sequence over C_n^r with no n-term zero-sum, where n is odd, n >= 5, 3 does not divide n, r is 5 or 6 and n^r <= 10^7 (for example C_5^5, C_7^5, C_5^6). Its length L must satisfy L+1 strictly greater than the best known lower bound for that cell. That bound is the general 42n-41 or 96n-95 (Edel, Des. Codes Cryptogr. 2008, quoted in arXiv:2610.35819), or any larger value for that specific n in Edel 2008, Edel et al. 2007 or a fresh search. Multiples of 3 are excluded because the caps behind s(C_3^5) = 91 and s(C_3^6) = 225 can give larger bars there.
- **p2:** Property D for C_15^3, listed open in arXiv:2610.35819 (Remark 10(5)). The win is a sequence over C_15^3 of length 126 = s(C_15^3)-1 (s(C_15^3) = 127 is proven), verified by two programs, with no 15-term zero-sum subsequence and not of the form T^14: some element must occur between 1 and 13 times. Report the full multiplicity profile. If in addition no element occurs 14 times, the sequence also disproves the weak form of Property D (arXiv:2610.35819, Section 8).

## How a win is checked

Use a DP over subsequence size: R_0 = {0}, and for each term g, for j from n-1 down to 0, set R_{j+1} |= R_j + g. The claim is valid if and only if 0 is not in R_n. This costs O(|S| n^(r+1)), which is trivial for C_7^3 (55 * 7 * 343). For the second implementation, use a generating function grouped by distinct elements with multiplicity caps. Test both on the cap-based constructions: 9 points, each taken n-1 times, in rank 3 must pass, and adding any element must fail. For p2, also compute the multiplicity profile and confirm that some multiplicity is not 14. Then re-fetch arXiv:2610.35819 and search for new rank-3 to rank-6 values for that n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.35819>

## Sources

- <https://arxiv.org/abs/2610.35819>
- <https://arxiv.org/abs/1010.5101>
- <https://arxiv.org/abs/2610.25271>
- <https://doi.org/10.1007/s10623-007-9085-2>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Port the even-n mechanism (light terms replacing heavy multiplicity, Wang-Zeng blocks) to odd n. Elsholtz reports that heavy-to-light swaps fail for n = 9, 15, 21, 25 in rank 3. Record which supports were excluded before searching.
- For n = 7, move beyond {0,1,2}^3 supports: search over supports with entries in Z_7 using a lazy-cut ILP (solve, find a 7-term zero-sum with the DP, add a cut, repeat).
- For rank 5 with n = 5 or 7, try to lift 45-point caps from F_3^5 (which give s(C_3^5) = 91) to supports valid for general odd n. Elsholtz reports that 42-point-support searches with q = 5, 7 failed in a related setting.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For n = 3^a 5^b in rank 3 (and n = 3^a in rank 4) the bound is proven, so no sequence of length 9n-8 (resp. 20n-19) exists there. Choose n = 7, 11, 13, ... (rank 3) or n = 5, 7, 11, ... (rank 4).
- Fan-Gao-Zhong (1010.5101, Lemma 2.5) checked by computer that for n = 7, 11 and 13 every sequence g T^(n-1) with |T| = 9 over C_n^3 has an n-term zero-sum. A length-(9n-8) candidate therefore cannot be nine heavy (multiplicity n-1) terms plus one extra element.
- Off-by-one: a sequence of length L proves s >= L+1.
- Do not confuse s (exactly n terms) with eta (1..n terms) or with the Davenport constant (any length).
- Property D versus its weak form: a length-(s-1) sequence that is not T^(n-1) disproves Property D. Only one with no term of multiplicity n-1 disproves the weak form.
- Expect failure: no counterexample is known for any odd exponent. Report search coverage honestly as a negative result.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/egz-odd-exponent-rank3-9n-8.md
```

Already set up? Say `run V3R1T4S on egz-odd-exponent-rank3-9n-8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `egz-odd-exponent-rank3-9n-8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
