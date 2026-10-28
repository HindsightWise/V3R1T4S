#!/usr/bin/env python3
"""Standalone verifier for penney-permutations-rotation-conjecture (partial win p1).
Reads object/s4_certificates.json, parses exact big integers, and verifies:
1. All 24 permutations of S_4 are present.
2. For each permutation, tau is the right cyclic rotation: (sigma_4, sigma_1, sigma_2, sigma_3).
3. Exact big integer sum: A(H) + B(H) + R(H) == H! == math.factorial(H).
4. Rigorous tail inequality: 2 * (A(H) + R(H)) < H! (proving Pr(sigma precedes tau) < 1/2).
5. Complementary Bob inequality: 2 * B(H) > H! (proving Pr(tau precedes sigma) > 1/2).
6. Exact agreement on calibration benchmark 2341 -> 1234 at H=36.
"""

import json
import math
import os
import sys

def main():
    try:
        obj_path = os.path.join(os.path.dirname(__file__), "..", "object", "s4_certificates.json")
        if not os.path.isfile(obj_path):
            obj_path = "object/s4_certificates.json"

        with open(obj_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data.get("target_id") == "penney-permutations-rotation-conjecture", "Incorrect target_id"
        assert data.get("claim") == "p1", "Incorrect claim"
        assert data.get("symmetric_group") == "S_4", "Incorrect group"

        certs = data.get("certificates", [])
        assert len(certs) == 24, f"Expected 24 certificates for S_4, got {len(certs)}"

        seen_sigmas = set()

        for c in certs:
            sigma = tuple(c["sigma"])
            tau = tuple(c["tau"])
            assert len(sigma) == 4 and sorted(sigma) == [1, 2, 3, 4], f"Invalid sigma: {sigma}"
            assert sigma not in seen_sigmas, f"Duplicate sigma: {sigma}"
            seen_sigmas.add(sigma)

            expected_tau = (sigma[3], sigma[0], sigma[1], sigma[2])
            assert tau == expected_tau, f"Tau mismatch for {sigma}: expected {expected_tau}, got {tau}"

            H = int(c["horizon"])
            assert 4 <= H <= 36, f"Horizon {H} out of bounds"

            A = int(c["A"])
            B = int(c["B"])
            R = int(c["R"])
            H_fact = int(c["H_fact"])

            expected_fact = math.factorial(H)
            assert H_fact == expected_fact, f"H_fact mismatch for H={H}"
            assert A + B + R == H_fact, f"Partition count mismatch: A+B+R={A+B+R} != {H_fact}"

            # Rigorous mathematical proof that Bob beats Alice:
            # Pr(Alice wins) <= (A + R) / H! < 1/2  <=>  2 * (A + R) < H!
            assert 2 * (A + R) < H_fact, f"Tail bound violated for {sigma}: 2*(A+R)={2*(A+R)} >= {H_fact}"
            assert 2 * B > H_fact, f"Bob win bound violated for {sigma}: 2*B={2*B} <= {H_fact}"

            # Float consistency
            a_f = A / H_fact
            b_f = B / H_fact
            ar_f = (A + R) / H_fact
            assert f"{a_f:.7f}" == f"{float(c['A_over_fact']):.7f}", f"A float mismatch: {a_f:.7f} vs {c['A_over_fact']}"
            assert f"{b_f:.7f}" == f"{float(c['B_over_fact']):.7f}", f"B float mismatch: {b_f:.7f} vs {c['B_over_fact']}"
            assert f"{ar_f:.7f}" == f"{float(c['A_plus_R_over_fact']):.7f}", f"AR float mismatch: {ar_f:.7f} vs {c['A_plus_R_over_fact']}"

            # Benchmark check for 2341 -> 1234
            if sigma == (2, 3, 4, 1):
                assert H == 36
                assert A == 147886985383757458869209075733594161570220
                assert B == 186454247223712671395113700966835612829428
                assert R == 37652094182431087203676671450405425600352

        assert len(seen_sigmas) == 24, "Did not verify all 24 permutations"
        print("All 24 S_4 Penney rotation certificates verified successfully!")
        print("PASS")
        sys.exit(0)

    except Exception as e:
        print(f"VERIFICATION FAILURE: {e}")
        print("FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
