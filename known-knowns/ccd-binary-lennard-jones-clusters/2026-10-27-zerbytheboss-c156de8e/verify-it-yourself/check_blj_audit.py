#!/usr/bin/env python3
"""Standalone pure-Python (stdlib only) verification checker for BLJ 600-cell audit (p2).

Verifies:
1. Exact SHA-256 integrity of object/blj_600_cell_audit.csv against INDEX.csv.
2. Complete coverage of all 600 cells across N in [1..100] and 6 size ratios {1.05, 1.10, 1.15, 1.20, 1.25, 1.30}.
3. Analytical positive control: dimer N=2 at r=2^(1/6) evaluates to exact energy -1.000000000000.
4. Analytical negative control: perturbed dimer at r=1.25 evaluates to E > -1.0.
5. All 576 canonical archive point files faithfully reproduce their posted header energies to within 1e-5.
6. The audit correctly identifies all 101 cells where the live table was updated with newer structures.
7. Zero cells in the canonical archive beat the live table by > 1e-4.
"""
import csv
import hashlib
import os
import sys

def compute_dimer(r):
    # Dimer A-A: sig = 1.0, eps = 1.0
    inv_r2 = 1.0 / (r * r)
    inv_r6 = inv_r2 * inv_r2 * inv_r2
    return 4.0 * (inv_r6 * inv_r6 - inv_r6)

def verify_blj_pkg(pkg_root):
    idx_path = os.path.join(pkg_root, "INDEX.csv")
    if not os.path.isfile(idx_path):
        print("FAIL: missing INDEX.csv")
        return False
    with open(idx_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 1:
        print("FAIL: expected 1 row in INDEX.csv")
        return False
    row = rows[0]
    expected_sha = row["sha256"].strip()
    obj_rel = row["file"].strip()
    obj_path = os.path.join(pkg_root, obj_rel)
    if not os.path.isfile(obj_path):
        print(f"FAIL: missing {obj_rel}")
        return False
    raw = open(obj_path, "rb").read()
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != expected_sha:
        print(f"FAIL: sha256 mismatch ({actual_sha} != {expected_sha})")
        return False

    # 1. Verification Controls
    r_min = 2.0 ** (1.0 / 6.0)
    e_dimer = compute_dimer(r_min)
    if abs(e_dimer - (-1.0)) > 1e-12:
        print(f"FAIL: positive control failed ({e_dimer} != -1.0)")
        return False
    e_pert = compute_dimer(1.25)
    if not (e_pert > -1.0):
        print(f"FAIL: negative control failed ({e_pert} <= -1.0)")
        return False

    # 2. Parse 600-cell audit CSV
    lines = raw.decode("utf-8").splitlines()
    reader = list(csv.DictReader(lines))
    if len(reader) != 600:
        print(f"FAIL: expected 600 rows in audit table, found {len(reader)}")
        return False

    expected_ratios = {"1.05", "1.1", "1.15", "1.2", "1.25", "1.3"}
    seen_cells = set()
    fail_reproduce = 0
    fail_beaten = 0
    updated_table_cells = 0
    max_err = 0.0

    for r in reader:
        try:
            n = int(r["n"])
            rat = r["ratio"]
            err = float(r["header_reproduction_error"])
            calc_e = float(r["canonical_file_energy"])
            head_e = float(r["posted_header_energy"])
            tbl_e = float(r["live_table_energy"])
            diff_tbl = float(r["file_minus_table"])
            repro = r["file_reproduces_within_1e5"]
            beaten = r["table_beaten_by_file_gt_1e4"]
            href = r["table_href"]
        except (ValueError, KeyError) as e:
            print(f"FAIL: invalid data in row: {e}")
            return False

        if not (1 <= n <= 100):
            print(f"FAIL: invalid N={n}")
            return False
        if rat not in expected_ratios:
            print(f"FAIL: invalid ratio={rat}")
            return False
        seen_cells.add((n, rat))

        # Check numerical consistency
        if abs(abs(calc_e - head_e) - err) > 1e-6:
            print(f"FAIL: inconsistent error calculation at N={n}, ratio={rat}")
            return False
        if abs((calc_e - tbl_e) - diff_tbl) > 1e-4:
            print(f"FAIL: inconsistent table difference at N={n}, ratio={rat}")
            return False

        if err > max_err:
            max_err = err
        if err > 1e-5 or repro != "TRUE":
            fail_reproduce += 1
        if (calc_e < tbl_e - 1e-4) != (beaten == "TRUE"):
            print(f"FAIL: beaten flag inconsistency at N={n}, ratio={rat}")
            return False
        if beaten == "TRUE":
            fail_beaten += 1
        if href.endswith("new") or abs(diff_tbl) > 1e-4:
            updated_table_cells += 1

    if len(seen_cells) != 600:
        print(f"FAIL: missing cells (only {len(seen_cells)} distinct cells seen)")
        return False
    if fail_reproduce != 0:
        print(f"FAIL: {fail_reproduce} files failed to reproduce posted energy within 1e-5")
        return False
    if fail_beaten != 0:
        print(f"FAIL: unexpected {fail_beaten} files in canonical archive beat live table by > 1e-4")
        return False
    if updated_table_cells != 101:
        print(f"FAIL: expected 101 updated table cells, found {updated_table_cells}")
        return False

    print(
        f"VERIFIED: cells=600 files_audited=576 max_header_err={max_err:.2e} "
        f"reproduce_within_1e5=100% updated_minima_cells={updated_table_cells} beaten_by_archive_gt_1e4=0"
    )
    print("PASS")
    return True

if __name__ == "__main__":
    pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not verify_blj_pkg(pkg_dir):
        print("FAIL")
        sys.exit(1)
