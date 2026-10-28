# WWII British censorship manual steganograms: locate the Morse code in the fashion drawing and recover the German text in the Amsterdam map

🔐 **Unbroken ciphers** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A 1939 British censorship training manual (UK National Archives KV 2/2424; Klaus Schmeh links a scan, and he photographed the original fashion drawing in high resolution at the archive and posted a high-resolution photo of the map) shows two pictures with hidden messages. It gives their meanings but not the full methods. (1) Fashion drawing, page 14: the hidden message is 'Heavy reinforcements for the enemy expected hourly. Before Arras.' The first part is said to be in Morse code and the second in shorthand (Schmeh calls it French shorthand). Blog reader Gerry read 'von aras' in German shorthand in the signature surname 'Shaw', and Schmeh accepted this reading ('Vor Arras') in May 2017. Where the Morse dots and dashes are hidden is still unknown. Commenter Thomas Ernst's 'EINE' reading of the collar is an unconfirmed guess. (2) Amsterdam city map, page 17: the manual says the message is in 'the morse alphabet (plus a transposition of 11 positions forward)' and gives it only in English: 'Oil has arrived, everything is ready. Gustav available for the appointed day.' The German original is not given. In October 2016 a reader called 'm' found pen-mark Morse below the dashed line along Raadhuisstraat, starting near Keizersgracht, with single strokes as dots and small filled boxes as dashes. The reading 'aathut' becomes 'llesfe' after the shift. 'm' also saw possible Morse between Kalverstraat and Rokin. Commenter Norbert reproduced 'llesfertig' and a few more fragments, and in September 2023 commenter Bugfish also read 'Alles Fertig' with only partial text around it. The full German original has not been recovered. Schmeh lists this as no. 33 of his Top 50 unsolved encrypted messages and calls the map result an 'almost solution'. No later solution appears on his blog, either the scienceblogs.de posts or klausschmeh.net since April 2026 (checked 2026-10-28). The plaintext meanings are known, so any solution can be checked mechanically.

## What counts as a win

Before reading, name one public image of each page (URL and SHA-256). For each page, state the reading rule: which strokes count as dots and dashes, and the reading order. Also state the Morse table, including any signs used for German umlauts and CH and how they are treated by the shift. (A) Map CONFIRMED if all hold: (1) a published mark list, with pixel bounding boxes on the page-17 image, each labelled dot, dash, letter gap or word gap and given in reading order, is decoded by a published script (the stated Morse table, then a forward shift of 11 on A-Z) into a German string; (2) the string contains a word for oil (OEL, OL or ÖL), FERTIG and GUSTAV in that order, and its 'llesfertig' part comes from the Raadhuisstraat marks; (3) it differs from a German sentence stated by the claimant by at most 3 symbol errors, and that sentence is a faithful translation of the manual's English text. (B) Fashion drawing CONFIRMED if a published mark list on the page-14 image, read under the stated rule, decodes by the stated Morse table to HEAVYREINFORCEMENTSFORTHEENEMYEXPECTEDHOURLY, or to a German translation stated before reading, with at most 2 symbol errors. For both: (i) the same rule applied to 20 control images of similar line density, chosen and hashed before reading, must never decode to a string with 3 or more consecutive dictionary words of 4 or more letters; (ii) a second reader given only the rule and the image must reproduce the mark list within the stated error allowance. Re-fetch the status page and Schmeh's solved-cryptogram category on klausschmeh.net before claiming.

## Partial wins

- **p1:** Map only: a published mark list on the page-17 image that the decoding script (stated Morse table, forward shift 11) turns into one contiguous German string of at least 30 letters, containing 'llesfertig' and at least one of OEL/OL/ÖL and GUSTAV, reproduced by a second reader from the rule and image alone.
- **p2:** Fashion drawing: a mark list under the pre-stated rule that decodes by the stated Morse table to HEAVYREINFORCEMENTSFOR (or the first three words of a German translation stated before reading) with at most 1 symbol error, reproduced by a second reader from the rule and image alone.

## How a win is checked

Fetch the named images and check their SHA-256. Overlay the claimed bounding boxes, re-label the marks blind under the stated rule, and run the published decoding script (Morse table, plus the shift of 11 for the map). Diff the output against the required keywords or the target string and count symbol errors. Run the same rule and script on the 20 pre-hashed control images and apply the dictionary-run threshold.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://scienceblogs.de/klausis-krypto-kolumne/2017/05/07/censorship-manual-steganograms-partially-solved/>

## Sources

- <https://scienceblogs.de/klausis-krypto-kolumne/2017/05/07/censorship-manual-steganograms-partially-solved/>
- <https://scienceblogs.de/klausis-krypto-kolumne/2017/05/03/the-top-50-unsolved-encrypted-messages-33-the-censorship-manual-steganograms>
- <https://scienceblogs.de/klausis-krypto-kolumne/2016/10/14/hidden-messages-in-a-letter-a-map-and-a-fashion-drawing/>
- <https://klausschmeh.net/category/solved-cryptogram/>

## Ideas to start from

Left out on purpose, so this page never spoils the hunt.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/unbroken-ciphers/censorship-manual-steganograms.md
```

Already set up? Say `run V3R1T4S on censorship-manual-steganograms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `censorship-manual-steganograms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
