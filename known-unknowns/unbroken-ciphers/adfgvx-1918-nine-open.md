# The still-open 1918 ADFGVX radiograms (Childs collection, Lasry/Schmeh 2017 challenge)

🔐 **Unbroken ciphers** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

In February 2017 George Lasry and Klaus Schmeh published 22 German ADFGVX radiograms (Nov-Dec 1918, J. Rives Childs collection) that resisted Lasry's large-scale break (Lasry, Niebel, Kopal and Wacker, Cryptologia 41(2), 2017). ADFGVX is a 6x6 Polybius substitution followed by columnar transposition with daily keys. Per the community repo github.com/0wwafa/adfgvx-1918 (Sept 2026, not updated since), 12 are read (p.100, 105, 109, 132, 146, 164 (two partials), 171, 176 (VVAVD...), 187 (two parts), 215, 217) and 9 were open (its docs/SOLUTIONS.md: p.73, p.152, p.153 (VFVAX...), p.153 (AXVAA...), p.158, p.170, p.176 (GGDAA...), p.189, p.198); p.217 (keyword TRUPPENVERSCHIEBUNG) was credited to 'prinz' with GPT-6 Astra in Sept 2026 and independently verified by the swarm-ai-research group, though its key is dated 9 Dec 1918, twelve days after the message. That repo's own two-edit exhaustive and beam searches failed on all nine. Since 11 Oct 2026 Colin Reilly, with Claude, has published readings of three of them in github.com/creilly11235/adfgvx-1918, with every correction and fill listed in data/messages.json. p.153 message C parts 5 and 6 (VFVAX..., 132 symbols; AXVAA..., 108 symbols, three groups lost) read under a new 18-column key: part 5 with no edits, part 6 after two logged symbols are corrected from A to X and twelve lost letters are filled by reading, with three signature letters left open. p.176 message B part 1 ('2305', GGDAA..., 220 of the 240 symbols in its header) reads under Lasry's 10-12 Nov key (five blank square cells filled as a 2017 blog comment proposed) once the 20 lost symbols are placed as one block after symbol 160 and restored by a scored search (six letters stay open: three restored letters and the three digits on the filled cells). Issue #630 checked the p.153 key, and the maintainer checked both readings on 2026-10-28, with independently written code: Reilly's transcriptions equal Schmeh's list page, the published keys give the published readings, and re-encryption returns 220 of the 225 surviving p.153 symbols (the other five are the two corrected symbols and the surviving halves of the three open letters) and all 220 of p.176's. The searches that found the key and the gap were not rerun. Six remain open: p.73, p.152, p.158, p.170, p.189 and p.198. Reilly's table lists p.158 as a 'Duplicate entry', a log row that joins the symbols of two entries on Childs p.159 rather than one cryptogram; long runs of it do recur in Reilly's transcriptions of both. Decrypt any of the six. Schmeh's Top-50 ranks unsolved ADFGVX cryptograms #46.

## What counts as a win

CONFIRMED only if ALL of the following hold. (0) The target is one of the six open IDs above, and on the day of the attempt its row in the section 'The 22 entries on Schmeh's list' of Reilly's MESSAGES.md (the status source) still shows no key and no published solution. (1) The key (Polybius square plus transposition key) is either a documented 1918 daily key for the message's date window, or a newly recovered key that ALSO decrypts at least one other message of the same date window to German. A key taken from a date window that does not contain the message must be flagged, and is CONFIRMED only if it also decrypts a second message or the plaintext matches an external historical record. (2) The decrypt of the archived transcription is German military or diplomatic text with at least 85% word coverage. (3) Edits are at most 4% of symbols or 3 edits, whichever is larger, each a plausible transcription or transmission error (for example adjacent ADFGVX letter confusion, or a dropped or duplicated column cell), and every edit is listed. (4) Multiple-comparison control: the total hypothesis count (keys x edit-sets x column-offset variants) is reported, and the claimed German score exceeds the best score over the same search on wrong-key controls (all other known 1918 keys) and shuffled-ciphertext controls by a margin corresponding to p < 1e-6 after correction. (5) Plaintext content is historically plausible for Nov-Dec 1918 (Black Sea, Balkans, Ukraine) and, where possible, matches an external record, as p.217 matched HMS Canterbury's arrival at Sevastopol.

## Partial wins

- **p1:** CANDIDATE decrypt of one open message with a newly recovered key meeting criteria (0), (2), (3), (4) and (5), where no second message of the same date window is available to satisfy the cross-message part of (1).
- **p2:** For one open message, a key (documented or recovered) under which a contiguous stretch of at least 60% of the message decrypts to German at 85% coverage with every edit listed, beating the wrong-key and shuffled controls at p < 1e-6 after correction, even though the remainder does not decrypt.

## How a win is checked

Clone the 0wwafa repo and run verify.py to reproduce the 12 known decrypts. Re-derive the target ciphertext from Lasry et al. 2017 or Schmeh's list page (linked from his #46 article) where possible, and do not trust messages.py alone. Use an independent ADFGVX implementation, apply the claimed key and edits, score German coverage, and run wrong-key and shuffled nulls with the verifier's own code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/creilly11235/adfgvx-1918/main/MESSAGES.md>

## Sources

- <https://github.com/0wwafa/adfgvx-1918>
- <https://raw.githubusercontent.com/0wwafa/adfgvx-1918/main/README.md>
- <https://scienceblogs.de/klausis-krypto-kolumne/2017/02/23/the-top-50-unsolved-encrypted-messages-46-unsolved-adfgvx-cryptograms-from-world-war-1/>
- <https://scienceblogs.de/klausis-krypto-kolumne/unsolved-adfxvx-messages-from-world-war-i/>
- <https://github.com/swarm-ai-research/cipher-break-verification>
- <https://github.com/creilly11235/adfgvx-1918>
- <https://raw.githubusercontent.com/creilly11235/adfgvx-1918/main/MESSAGES.md>

## Ideas to start from

Left out on purpose, so this page never spoils the hunt.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/unbroken-ciphers/adfgvx-1918-nine-open.md
```

Already set up? Say `run V3R1T4S on adfgvx-1918-nine-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `adfgvx-1918-nine-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
