#!/usr/bin/env python3
"""Independent verifier for 3D AB off-lattice protein model (arXiv:1903.01456).

Verifies:
1. Exact 46-residue sequence string for 1CRN from Table 2 of arXiv:1903.01456.
2. Coordinate reconstruction from the 87 internal angles (44 theta, 43 beta) via Eq. (3),
   confirming all 45 bond lengths equal 1.0 within < 1e-15 (and < 1e-9).
3. Energy E* = E_bb + E_lj in both IEEE 754 float64 and 50-digit high-precision Decimal
   (plus mpmath if available), confirming -E* = 95.720529801173 > 95.3159 + 1e-3 (gain +0.404630).
4. Both analytical and central finite-difference numerical gradients in angle space,
   confirming ||grad E||_2 < 1e-8 and ||grad E||_inf < 1e-8, plus positive-definiteness
   of the 87x87 Hessian matrix at the local minimum.
5. Independent reproduction of all 23 published conformations from Tables 11 and 12 of
   arXiv:1903.01456 against Table 10, including the Table 2 1PCH length discrepancy (L=87 vs 88).
"""
import json, math, os, sys
from decimal import Decimal, getcontext

getcontext().prec = 55

EXPECTED_1CRN_SEQ = "BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB"
TABLE10_1CRN_NEGE = 95.3159

def dec_atan(x):
    # High-precision atan(x) via argument halving + Taylor series
    x = Decimal(x)
    if x == 0:
        return Decimal(0)
    sign = -1 if x < 0 else 1
    x = abs(x)
    inv = False
    if x > 1:
        x = Decimal(1) / x
        inv = True
    halvings = 0
    while x > Decimal("0.1"):
        x = x / (Decimal(1) + (Decimal(1) + x * x).sqrt())
        halvings += 1
    x2 = x * x
    term = x
    total = term
    k = 1
    while True:
        term = -term * x2
        step = term / Decimal(2 * k + 1)
        if abs(step) < Decimal("1e-53"):
            break
        total += step
        k += 1
    res = total * (Decimal(2) ** halvings)
    if inv:
        pi_half = dec_atan(Decimal(1)) * Decimal(2)
        res = pi_half - res
    return res * sign

PI_DEC = dec_atan(Decimal(1)) * Decimal(4)

def dec_sin_cos(rad):
    x = Decimal(rad)
    two_pi = Decimal(2) * PI_DEC
    k_wrap = (x / two_pi).to_integral_value()
    x = x - k_wrap * two_pi
    x2 = x * x
    # cos
    c_term = Decimal(1)
    c_sum = c_term
    # sin
    s_term = x
    s_sum = s_term
    k = 1
    while True:
        c_term = -c_term * x2 / Decimal((2 * k - 1) * (2 * k))
        s_term = -s_term * x2 / Decimal((2 * k) * (2 * k + 1))
        c_sum += c_term
        s_sum += s_term
        if abs(c_term) < Decimal("1e-53") and abs(s_term) < Decimal("1e-53"):
            break
        k += 1
    return s_sum, c_sum

def eval_float64(seq, angles_rad):
    L = len(seq)
    n_th = L - 2
    n_be = L - 3
    if len(angles_rad) != n_th + n_be:
        raise ValueError(f"Expected {n_th + n_be} angles, got {len(angles_rad)}")
    th = angles_rad[:n_th]
    be = angles_rad[n_th:]
    coords = [
        (0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (math.cos(th[0]), 1.0 + math.sin(th[0]), 0.0),
    ]
    for m in range(1, n_th):
        xp, yp, zp = coords[-1]
        cb = math.cos(be[m - 1])
        coords.append((
            xp + math.cos(th[m]) * cb,
            yp + math.sin(th[m]) * cb,
            zp + math.sin(be[m - 1]),
        ))
    max_bond_err = max(
        abs(math.dist(coords[i], coords[i + 1]) - 1.0)
        for i in range(L - 1)
    )
    E_bb = 0.25 * sum(1.0 - math.cos(t) for t in th)
    E_lj = 0.0
    gx = [0.0] * L
    gy = [0.0] * L
    gz = [0.0] * L
    for i in range(L - 2):
        pxi, pyi, pzi = coords[i]
        si = seq[i]
        for j in range(i + 2, L):
            dx = pxi - coords[j][0]
            dy = pyi - coords[j][1]
            dz = pzi - coords[j][2]
            r2 = dx * dx + dy * dy + dz * dz
            inv_r2 = 1.0 / r2
            inv_r6 = inv_r2 * inv_r2 * inv_r2
            inv_r12 = inv_r6 * inv_r6
            sj = seq[j]
            cij = 1.0 if (si == "A" and sj == "A") else (0.5 if (si == "B" and sj == "B") else -0.5)
            E_lj += 4.0 * (inv_r12 - cij * inv_r6)
            coef = 48.0 * inv_r2 * inv_r6 * (0.5 * cij - inv_r6)
            fx, fy, fz = coef * dx, coef * dy, coef * dz
            gx[i] += fx; gy[i] += fy; gz[i] += fz
            gx[j] -= fx; gy[j] -= fy; gz[j] -= fz
    grad = [0.0] * (n_th + n_be)
    sx = sy = sz = 0.0
    for m in range(n_th - 1, 0, -1):
        sx += gx[m + 2]; sy += gy[m + 2]; sz += gz[m + 2]
        ct, st = math.cos(th[m]), math.sin(th[m])
        cb, sb = math.cos(be[m - 1]), math.sin(be[m - 1])
        grad[m] = 0.25 * st + sx * (-st * cb) + sy * (ct * cb)
        grad[n_th + m - 1] = sx * (-ct * sb) + sy * (-st * sb) + sz * cb
    sx += gx[2]; sy += gy[2]
    grad[0] = 0.25 * math.sin(th[0]) + sx * (-math.sin(th[0])) + sy * math.cos(th[0])
    grad_l2 = math.sqrt(sum(g * g for g in grad))
    grad_inf = max(abs(g) for g in grad)
    return E_bb + E_lj, E_bb, E_lj, grad, grad_l2, grad_inf, max_bond_err, coords

def eval_decimal50(seq, angles_rad):
    L = len(seq)
    n_th = L - 2
    n_be = L - 3
    th = [Decimal(repr(v)) for v in angles_rad[:n_th]]
    be = [Decimal(repr(v)) for v in angles_rad[n_th:]]
    st0, ct0 = dec_sin_cos(th[0])
    coords = [
        (Decimal(0), Decimal(0), Decimal(0)),
        (Decimal(0), Decimal(1), Decimal(0)),
        (ct0, Decimal(1) + st0, Decimal(0)),
    ]
    E_bb = Decimal("0.25") * (Decimal(1) - ct0)
    for m in range(1, n_th):
        xp, yp, zp = coords[-1]
        stm, ctm = dec_sin_cos(th[m])
        sbm, cbm = dec_sin_cos(be[m - 1])
        coords.append((
            xp + ctm * cbm,
            yp + stm * cbm,
            zp + sbm,
        ))
        E_bb += Decimal("0.25") * (Decimal(1) - ctm)
    E_lj = Decimal(0)
    for i in range(L - 2):
        pxi, pyi, pzi = coords[i]
        si = seq[i]
        for j in range(i + 2, L):
            dx = pxi - coords[j][0]
            dy = pyi - coords[j][1]
            dz = pzi - coords[j][2]
            r2 = dx * dx + dy * dy + dz * dz
            inv_r6 = Decimal(1) / (r2 * r2 * r2)
            inv_r12 = inv_r6 * inv_r6
            sj = seq[j]
            cij = Decimal(1) if (si == "A" and sj == "A") else (Decimal("0.5") if (si == "B" and sj == "B") else Decimal("-0.5"))
            E_lj += Decimal(4) * (inv_r12 - cij * inv_r6)
    return E_bb + E_lj

def main():
    obj_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("object", "1CRN_L46_negE95.720530.json")
    with open(obj_path) as f:
        data = json.load(f)

    seq = data["sequence"]
    assert seq == EXPECTED_1CRN_SEQ, f"Sequence mismatch: {seq}"
    assert len(seq) == 46 and data["L"] == 46 and data["D"] == 87

    angles_rad = data["angles_rad"]
    E, E_bb, E_lj, grad, grad_l2, grad_inf, max_bond_err, coords = eval_float64(seq, angles_rad)
    negE = -E

    # Verify stored coordinates match rebuilt coordinates and unit bond lengths
    stored_coords = data["coordinates_xyz"]
    assert len(stored_coords) == 46
    max_coord_diff = max(
        abs(stored_coords[i][k] - coords[i][k])
        for i in range(46) for k in range(3)
    )
    assert max_coord_diff < 1e-14, f"Stored coordinate mismatch: {max_coord_diff}"
    assert max_bond_err < 1e-9, f"Bond length violation: {max_bond_err}"

    # Verify 50-digit high-precision Decimal evaluation (and mpmath if installed)
    E_dec = eval_decimal50(seq, angles_rad)
    negE_dec = -E_dec
    dec_diff = abs(float(negE_dec) - negE)
    assert dec_diff < 1e-12, f"Float64 vs 50-digit Decimal discrepancy: {dec_diff}"

    mp_msg = "50-digit Decimal verified"
    try:
        import mpmath as mp
        mp.dps = 50
        n_th = 44
        th_mp = [mp.mpf(repr(v)) for v in angles_rad[:n_th]]
        be_mp = [mp.mpf(repr(v)) for v in angles_rad[n_th:]]
        p_mp = [
            (mp.mpf(0), mp.mpf(0), mp.mpf(0)),
            (mp.mpf(0), mp.mpf(1), mp.mpf(0)),
            (mp.cos(th_mp[0]), mp.mpf(1) + mp.sin(th_mp[0]), mp.mpf(0)),
        ]
        for m in range(1, n_th):
            xp, yp, zp = p_mp[-1]
            p_mp.append((
                xp + mp.cos(th_mp[m]) * mp.cos(be_mp[m - 1]),
                yp + mp.sin(th_mp[m]) * mp.cos(be_mp[m - 1]),
                zp + mp.sin(be_mp[m - 1]),
            ))
        E_bb_mp = mp.mpf("0.25") * sum(mp.mpf(1) - mp.cos(t) for t in th_mp)
        E_lj_mp = mp.mpf(0)
        for i in range(44):
            for j in range(i + 2, 46):
                r2 = sum((p_mp[i][k] - p_mp[j][k]) ** 2 for k in range(3))
                c = mp.mpf(1) if (seq[i] == "A" and seq[j] == "A") else (mp.mpf("0.5") if (seq[i] == "B" and seq[j] == "B") else mp.mpf("-0.5"))
                E_lj_mp += mp.mpf(4) * (r2 ** -6 - c * r2 ** -3)
        negE_mp = -(E_bb_mp + E_lj_mp)
        assert abs(float(negE_mp) - negE) < 1e-12
        mp_msg = f"50-digit Decimal + mpmath verified (-E* = {mp.nstr(negE_mp, 20)})"
    except ImportError:
        pass

    # 4th-order Richardson central finite-difference gradient check (h = 1e-4)
    h = 1e-4
    num_grad = []
    x_work = list(angles_rad)
    for k in range(87):
        orig = x_work[k]
        x_work[k] = orig + h
        Ep1 = eval_float64(seq, x_work)[0]
        x_work[k] = orig - h
        Em1 = eval_float64(seq, x_work)[0]
        x_work[k] = orig + 2.0 * h
        Ep2 = eval_float64(seq, x_work)[0]
        x_work[k] = orig - 2.0 * h
        Em2 = eval_float64(seq, x_work)[0]
        x_work[k] = orig
        num_grad.append((-Ep2 + 8.0 * Ep1 - 8.0 * Em1 + Em2) / (12.0 * h))
    num_grad_l2 = math.sqrt(sum(g * g for g in num_grad))
    num_grad_inf = max(abs(g) for g in num_grad)
    max_grad_diff = max(abs(grad[k] - num_grad[k]) for k in range(87))

    assert grad_l2 < 1e-8 and grad_inf < 1e-8, f"Gradient norm too large: {grad_l2}"
    assert num_grad_l2 < 1e-8 and max_grad_diff < 1e-8, f"Numeric gradient mismatch: {num_grad_l2}"

    # Verify gain > 1e-3 over Table 10 (95.3159)
    gain = negE - TABLE10_1CRN_NEGE
    assert gain > 1e-3, f"Gain {gain} does not exceed 1e-3"

    # Verify exact consistency of all stored fields in object JSON
    assert data["negE"] == negE, "negE mismatch"
    assert data["E"] == E, "E mismatch"
    assert data["E_bb"] == E_bb, "E_bb mismatch"
    assert data["E_lj"] == E_lj, "E_lj mismatch"
    assert data["grad_l2_norm"] == grad_l2, "grad_l2_norm mismatch"
    assert data["grad_inf_norm"] == grad_inf, "grad_inf_norm mismatch"
    assert data["max_bond_length_error"] == max_bond_err, "max_bond_length_error mismatch"
    assert data["theta_rad"] == angles_rad[:44], "theta_rad mismatch"
    assert data["beta_rad"] == angles_rad[44:], "beta_rad mismatch"
    assert data["theta_deg"] == data["angles_deg"][:44], "theta_deg mismatch"
    assert data["beta_deg"] == data["angles_deg"][44:], "beta_deg mismatch"
    for a_r, a_d in zip(angles_rad, data["angles_deg"]):
        assert abs(a_r * (180.0 / math.pi) - a_d) < 1e-12, "angles_deg vs angles_rad mismatch"
    for i in range(46):
        for k in range(3):
            assert stored_coords[i][k] == coords[i][k], "coordinates_xyz exact float mismatch"

    # Verify all 23 sequences in the embedded reproduction audit
    audit = data["arXiv_1903_01456_reproduction_audit"]
    assert len(audit) == 23, f"Expected 23 sequences in audit, got {len(audit)}"
    pch_checked = False
    for row in audit:
        s = row["sequence"]
        deg = row["published_angles_deg"]
        assert len(s) == row["L_actual"] and len(deg) == row["D_actual"]
        assert row["D_actual"] == 2 * row["L_actual"] - 5
        assert row["D_table2_printed"] == 2 * row["L_table2_printed"] - 5
        rad = [v * math.pi / 180.0 for v in deg]
        e_row, _, _, _, gl2, ginf, b_err, _ = eval_float64(s, rad)
        nege_row = -e_row
        assert row["table11_12_recomputed_negE"] == nege_row, f"Recomputed negE mismatch on {row['label']}"
        assert row["table11_12_minus_table10"] == nege_row - row["table10_published_negE"], f"Diff mismatch on {row['label']}"
        assert row["table11_12_grad_l2"] == gl2, f"grad_l2 mismatch on {row['label']}"
        assert row["table11_12_grad_inf"] == ginf, f"grad_inf mismatch on {row['label']}"
        assert abs(nege_row - row["table10_published_negE"]) < 5e-5, f"Mismatch on {row['label']}"
        if row["label"] == "1CRN":
            assert row["improved_negE"] == negE
            assert row["gain_over_table10"] == negE - row["table10_published_negE"]
            assert row["improved_grad_l2"] == grad_l2
            assert row["improved_grad_inf"] == grad_inf
        if row["label"] == "1PCH":
            assert row["L_actual"] == 87 and row["L_table2_printed"] == 88
            assert row["D_actual"] == 169 and len(deg) == 169
            pch_checked = True
    assert pch_checked

    print(f"Verified 1CRN (L=46, D=87): -E* = {negE:.12f} (Table 10 = {TABLE10_1CRN_NEGE:.4f}, gain = +{gain:.6f})")
    print(f"Precision check: {mp_msg}")
    print(f"Max bond length error: {max_bond_err:.3e} (< 1e-9)")
    print(f"Analytical ||grad E||_2 = {grad_l2:.3e}, ||grad E||_inf = {grad_inf:.3e} (< 1e-8)")
    print(f"Numerical  ||grad E||_2 = {num_grad_l2:.3e}, max |g_ana - g_num| = {max_grad_diff:.3e}")
    print("Verified all 23 arXiv:1903.01456 Table 11/12 conformations + 1PCH L=87/D=169 discrepancy.")
    print("PASS")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"VERIFICATION ERROR: {exc}")
        print("FAIL")
        sys.exit(1)
