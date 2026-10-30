# Confluence Competition: certified YES/NO for a first-order TRS in ARI-COPS that no CoCo tool has answered since 2019

✅ **Formal proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours (CSI, Hakusan, CONFident, ACP-style decomposition, critical-pair analysis); CeTA checks seconds · open as of 2026-10-30

## The problem

The Confluence Competition (CoCo 2026, 15th edition, run live at IWC 2026 / FLoC 2026, Lisbon, 24 July 2026; steering committee Naoki Nishida, Teppei Saito, Rene Thiemann, Sarah Winkler, assisted by Nao Hirokawa for ARI-COPS) runs all tools on the ARI-COPS problem database. In the 2026 TRS full run (444 problems; AProVE, CO3, CONFident, CSI, CSI2025, CSI+CeTA, CeTA-Prover+CeTA, FORT-h, FORT-h+FORTify, Hakusan, Hakusan+CeTA) 32 problems got no YES or NO. Cross-checking the 2019-2025 full runs (2019-2023 tables use COPS numbers, 2024-2026 ARI numbers, mapped by each ARI file's @cops tag) leaves 18 that no tool has ever answered: ARI 51, 53, 55, 56, 57 (Aoto-Yoshida-Toyama extensions of combinatory logic S, K, I: a conditional B, Dh z z -> z, Dk z z -> E z, Klop's Ds z z -> E, and surjective pairing D, D0, D1), 108 (relation-algebra rules), 124 (one rule f(f(x,y),z) -> f(f(x,z),f(y,z)), a self-distributivity variation), 239 (Suzuki-Aoto-Toyama), 448 and 449 (Middeldorp: binary arithmetic with associativity, and max with associativity and commutativity), 465 (van Oostrom 2016), 507 (Aoto), 987 (Shintani, secret 2019), 1014 (Ogawa: d x x -> x, f x -> d x (f x), a -> f a), 1133, 1135, 1136 (Zantema braid-like systems) and 1621 (Felicissimo-Jouannaud, secret 2025). Klop showed by hand that CL with Ds z z -> E and CL with surjective pairing are not confluent, so 56 and 57 are known NO yet have no automated or certified proof.

## What counts as a win

For one of ARI-COPS problems 51, 53, 55, 56, 57, 108, 124, 239, 448, 449, 465, 507, 987, 1014, 1133, 1135, 1136, 1621 (file from https://ari-cops.uibk.ac.at/ARI/, hashed), still without a YES or NO in the latest CoCo full run of the TRS category at claim time: a confluence (YES) or non-confluence (NO) proof in CPF format accepted by the current CeTA release. For NO, an explicit peak t ->* s1, t ->* s2 with every rewrite step listed and a CeTA-checked argument that s1 and s2 have no common reduct also counts. A tool's bare YES/NO, or a hand proof, does not win.

## Partial wins

- **p1:** An uncertified YES/NO for one of the 18 problems from a tool whose proof is written out step by step and independently re-checked by a second tool or a short script (for NO: the peak and a non-joinability argument by tree automata or by distinct normal forms of a terminating sub-system), labelled uncertified.
- **p2:** A CeTA-certified YES/NO for one of the 13 other TRS problems unanswered in the CoCo 2026 full run that have never had a certified answer: ARI 27, 88, 158, 166, 167, 169, 223, 394, 395, 397, 418, 444 (answered without certification, mostly by ACP, in 2019-2025) and 1134 (answered NO without certification by ACP in 2022 only). ARI 246 already has an ACP+CeTA certified NO and does not count.

## How a win is checked

Fetch https://ari-cops.uibk.ac.at/CoCo/2026/full-run/TRS/ and the older full-run pages (/CoCo/ < year > /full-run/TRS/). For 2024-2026, look up the ARI number; for 2019-2023, look up the COPS number given by the @cops line of the ARI file. Confirm that no row has a YES or NO cell. Run CeTA (cl-informatik.uibk.ac.at/software/ceta) on the ARI problem and the CPF proof; accept only CERTIFIED. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ari-cops.uibk.ac.at/CoCo/2026/full-run/TRS/>

## Sources

- <https://project-coco.uibk.ac.at/2026/>
- <https://ari-cops.uibk.ac.at/CoCo/2026/full-run/TRS/>
- <https://ari-cops.uibk.ac.at/>
- <https://ari-cops.uibk.ac.at/CoCo/2025/full-run/TRS/>
- <http://cl-informatik.uibk.ac.at/software/ceta/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For 56 and 57, formalise Klop's counterexample term for CL with Ds / surjective pairing as an explicit peak and look for a certifiable non-joinability argument (for example an ordering or interpretation showing the two reducts lie in disjoint closed sets).
- Non-left-linear systems (51, 53, 55, 448, 449, 987, 1014, 1621) defeat critical-pair methods; try decreasing diagrams with relative termination, or layer-preserving decomposition.
- For 1133, 1135 and 1136 (braid-like rules, some with p -> a p), the word problem view may give a direct confluence modulo argument or a counterexample peak.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Problem numbers are ARI ids, which differ from the old COPS numbers (problem 56 is COPS 57, 1134 is COPS 1282); the 2019-2023 full-run tables are indexed by COPS number, so compare via the @cops tag.
- The other 14 problems unanswered in 2026 were answered by earlier tools (mostly ACP); they count only under p2, with a certificate, and 246 is already certified.
- A hand proof in the literature is not a certified answer.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/coco-trs-never-answered-confluence.md
```

Already set up? Say `run V3R1T4S on coco-trs-never-answered-confluence`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `coco-trs-never-answered-confluence`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
