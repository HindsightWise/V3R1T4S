# Prove a listed PRP prime in Luhn's generalized repunit, generalized Wagstaff or generalized Mersenne tables (at least 10 000 digits)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (ECPP of a 10 000-digit number takes a few CPU-days with CM or Primo; the 3 500-6 000-digit entries take hours) · open as of 2026-10-30

## The problem

Norman Luhn's tables list every known (probable) prime of at least 1000 digits of three forms, each marked Prime or PRP from its factordb or PrimePages status. (b^n-1)/(b-1) has 3873 entries, 3069 of them PRP (updated 29 Oct 2026). (b^n+1)/(b+1) has 1385 entries, 767 PRP (26 Oct 2026). b^n-(b-1)^n has 4335 entries, 1750 PRP (29 Oct 2026). The smallest PRPs are recent finds by Richard Fischer: 638^1237-637^1237 (3470 digits, Jul 2026), (506^1433+1)/507 (3873 digits, Jul 2026) and (1004^1951-1)/1003 (5854 digits, Aug 2026). Among the smallest PRPs of at least 10 000 digits are (4813^2719-1)/4812 (10009 digits, Bernardo Boncompagni, 2010), (172^4483+1)/173 (10020 digits, 2000) and 19365^2333-19364^2333 (10001 digits, Lelio R Paula, 2008). The base-3 repunits (3^49681-1)/2 (23704 digits) and (3^57917-1)/2 (27634 digits) have been PRPs since Henri Lifchitz found them in 2003. The largest proven entries reach 141416 digits ((124750^27751-1)/124749, Tom Wu, CM). Credit goes to Luhn (tables), Fischer, Andy Steward, Tom Wu, Boncompagni, Lifchitz and the provers.

## What counts as a win

CONFIRMED (full win) for a number with at least 10 000 digits that is marked PRP on one of the three live Luhn tables (TableRepunitGen.php, TableWagstaffGen.php, TableMersenneGen.php, re-fetched immediately before the claim). The claim needs a complete primality certificate for exactly that number that an independent verifier checks as valid: a Primo certificate, a CM or PARI/GP ECPP certificate, or an N-1/N+1 (Pocklington/BLS/Coppersmith-Howgrave-Graham) proof whose factored part has every prime factor proven. Each newly proven entry counts (direction: min on the number of PRP entries of at least 10 000 digits).

## Partial wins

- **p1:** A verified primality certificate for any entry marked PRP on one of the three live tables, of any size (the smallest is 3470 digits).

## How a win is checked

Rebuild N from the expression and compare it with the certificate's N. Check Primo certificates with an independent Primo-certificate verifier, PARI/GP certificates with primecertisvalid, and CM certificates with CM's checker. For N-1/N+1 proofs rerun PFGW -tp/-tm with the factor helper file, or Broadhurst's chgcertd.gp for CHG, on the verifier's own install. Confirm the entry is still PRP on the live table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/Primetables/TableRepunitGen.php>

## Sources

- <https://pzktupel.de/Primetables/TableRepunitGen.php>
- <https://pzktupel.de/Primetables/TableWagstaffGen.php>
- <https://pzktupel.de/Primetables/TableMersenneGen.php>
- <https://pzktupel.de/Primetables/TableRepunitGenS.php>
- <http://www.fermatquotient.com/PrimSerien/GenRepu.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For (b^n-1)/(b-1) with n prime, N-1 = b(b^(n-1)-1)/(b-1) splits into cyclotomic pieces Phi_d(b), d | n-1. Pick entries where n-1 is smooth and the small Phi_d(b) are fully factored (Cunningham-style tables). Then a BLS (1/3) or CHG (about 30%) proof replaces ECPP.
- For b^n-(b-1)^n and Wagstaff-type entries, N-1 or N+1 rarely factor well, so plan on ECPP: CM (Enge's FastECPP) scales better than Primo above 10 000 digits.
- Sort the 1666 generalized repunit PRPs of 10 000-20 000 digits by size and start with the smallest.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Luhn takes the status from factordb, which can lag: someone else may already have uploaded a certificate. Check factordb (in a browser) before spending CPU-days. Uploading a certificate to factordb is an action for the human.
- A certificate for (b^n-1) or b^n+1 instead of the divided form, or for the wrong n, is worthless. Compare N digit by digit.
- A PRP test, however strong, is not a proof.
- The proven-versus-PRP marks also cover numbers of 1000-3470 digits found earlier. Only entries currently marked PRP count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/luhn-repunit-family-prp-primality-proofs.md
```

Already set up? Say `run V3R1T4S on luhn-repunit-family-prp-primality-proofs`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `luhn-repunit-family-prp-primality-proofs`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
