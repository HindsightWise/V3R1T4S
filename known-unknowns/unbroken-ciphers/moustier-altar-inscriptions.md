# Moustier altar inscriptions (two 19th-century coded inscriptions, St Martin's Church, Belgium)

🔐 **Unbroken ciphers** · standard · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Two carved letter inscriptions on the side altars (St Mary's and St Martin's) of St Martin's Church in Moustier, Frasnes-lez-Anvaing, Hainaut, Belgium, which Klaus Schmeh dates to the 19th century (parish records mention altar repairs in 1836-1840). Each is set in ten lines (two blocks of five) of about 80 characters, one inscription four characters longer than the other, including special signs (^, [ and an HP/FHP group). Cryptologists learned of them through 'Secrets of the Altars' in the September 1974 issue of the NSA newsletter Cryptolog, which Nick Pelling (Cipher Mysteries) found in 2013. Pelling made the standard transcriptions. Schmeh photographed the altars in 2015 and lists them as no. 18 of his Top 50 unsolved encrypted messages. Jean Connart worked on them from 1961. His booklet's Trithemius-based Latin reading, Rudy Cambier's Nostradamus/consonant-script theory (from his book of about 2002, discussed by Pelling in 2013) and Philippe Connart's lettering theory (2016) are not accepted. Dirk Huylebrouck's 2022 EOS article reviews the proposals, with comments from Jarl Van Eycke, who notes that the lines repeat unusually few letters. Pelling and Schmeh both reported the inscriptions unsolved in April 2022. As of October 2026 no solution has been accepted by either. Unverified readings posted as blog comments (for example German-based readings in April 2026 and partial key claims by other commenters) have not been confirmed. Find the method and plaintext of either inscription.

## What counts as a win

CONFIRMED only if ALL hold. (1) A transcription is frozen and published before solving. It starts from Pelling's, is checked against Schmeh's 2015 photographs, and gives every ligature and special sign a declared reading. (2) One method, declared before solving together with a plaintext language and a lexicon for it named before solving (for example Whitaker's Words for Latin), decrypts every character of one inscription into text in which at least 90% of plaintext letters belong to words found in that lexicon. Abbreviations count as explained only if they come from a standard list for that language (for example an ecclesiastical abbreviation list), fixed before solving, and expand deterministically. At most 3 characters may be unexplained. A language model or a reader saying the text 'makes sense' is not evidence. (3) Key bits stay below 0.5 x length x 3.5. The same method family applied to the second inscription either decrypts it under the same rule or is shown to need a different key of the same form. (4) Under the same solver budget, 1,000 random strings with the same character frequencies never reach the lexicon-coverage score of the claimed plaintext. Re-fetch the status page live before claiming.

## Partial wins

- **p1:** Structural proof: a mechanically checkable demonstration that the two inscriptions share a key or a plaintext (for example aligned repeats, an isomorph, or one being a transposition of the other), with a shuffle null at p < 0.001.
- **p2:** Over-budget candidate: a method declared before solving that decrypts one full inscription with at least 90% lexicon coverage (as in criterion 2) and passes the 1,000-string null, but exceeds the key-bit limit by less than 50%. Reported as a candidate only.

## How a win is checked

Check the frozen transcription character by character against Schmeh's 2015 photographs and Pelling's transcription. Re-implement the method, decrypt, compute lexicon coverage against the named lexicon and abbreviation list, recompute key bits, and run the 1,000-string frequency-matched null with the same budget.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ciphermysteries.com/category/historical-ciphers/moustier-cryptograms>

## Sources

- <https://ciphermysteries.com/category/historical-ciphers/moustier-cryptograms>
- <https://ciphermysteries.com/2013/04/02/the-moustier-church-cryptograms>
- <https://scienceblogs.de/klausis-krypto-kolumne/news-about-the-moustier-inscriptions/>
- <https://scienceblogs.de/klausis-krypto-kolumne/2017/11/07/the-top-50-unsolved-encrypted-messages-18-the-moustier-altar-inscriptions/>
- <https://ciphermysteries.com/wp-content/uploads/sites/6/2022/04/Moustier_Eng.pdf>
- <https://klausschmeh.net/unsolved-crypto-mysteries/>
- <https://klausschmeh.net/category/solved-cryptogram/>

## Ideas to start from

Left out on purpose, so this page never spoils the hunt.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/unbroken-ciphers/moustier-altar-inscriptions.md
```

Already set up? Say `run V3R1T4S on moustier-altar-inscriptions`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `moustier-altar-inscriptions`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
