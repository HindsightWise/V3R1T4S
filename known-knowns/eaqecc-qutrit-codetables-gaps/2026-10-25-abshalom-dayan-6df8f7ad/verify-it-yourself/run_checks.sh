#!/bin/sh
# Run from the package folder: sh verify-it-yourself/run_checks.sh   (last line: PASS or FAIL)
# Needs python3 (standard library only) and a C compiler (cc). About 5 seconds (3 parallel parts of the
# information-set test, then a 1-second theorem-based check: Goppa bound plus Construction X, goppa_x.py).
V=verify-it-yourself; O=object/eaqecc_33_3_20_18.json; W="$V/tmp_work"; rm -rf "$W"; mkdir -p "$W"
fail() { echo "$1"; rm -rf "$W"; echo FAIL; exit 1; }
cc -O3 -o "$W/infoset" "$V/infoset.c" || fail "could not compile infoset.c"
python3 "$V/gf3prep.py" "$O" "$W/basis.txt" > "$W/results.txt" || fail "gf3prep failed (object malformed?)"
python3 "$V/check_eaqecc.py" prepare "$O" "$W/enum_basis.txt" >> "$W/results.txt" || fail "GF(9) check failed (object malformed?)"
python3 "$V/gf9info.py" prep "$O" "$W/G9.txt" >> "$W/results.txt" || fail "GF(9) recovery failed (object malformed?)"
M=$(python3 -c "import json,sys; o=json.load(open(sys.argv[1])); print(o['n'] - o['d'] + 1)" "$O") || fail "no claimed d"
for p in 0 1 2; do "$W/infoset" $M $p 3 < "$W/G9.txt" > "$W/part$p.out" & done; wait
cat "$W/part0.out" "$W/part1.out" "$W/part2.out" >> "$W/results.txt"
python3 "$V/witness.py" "$O" 0,1,2,3,4,5,6,7,9,11,18,19,21,22,23,24,26,28,30,31 >> "$W/results.txt" || fail "witness check failed"
WORD=5,1,3,2,5,8,1,6,0,1,0,1,0,0,0,0,0,0,1,3,0,1,3,7,5,0,6,0,1,0,5,1,0
python3 "$V/goppa_x.py" "$O" 4 -1 "$WORD" > "$W/goppa.txt" 2>&1 || fail "theorem-based check failed to run (object malformed?)"
cat "$W/goppa.txt" >> "$W/results.txt"
cat "$W/results.txt"
D=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['d'])" "$O")
grep -q "^RESULT: d_EA = $D exactly (theorem-based; no distance search): True$" "$W/goppa.txt" || fail "theorem-based check (Goppa bound + Construction X) does not give d = $D"
python3 "$V/verdict.py" "$O" "$W/results.txt" || fail "parameters do not match the claim"
rm -rf "$W"; echo PASS
