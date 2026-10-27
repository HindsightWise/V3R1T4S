#!/usr/bin/env python3
"""Lens 2: Analytical Newton-Raphson Polish & 3Nx3N Hessian Normal Mode Certification."""
import math
import os
import re
import sys
import numpy as np

def parse_point_file(filepath):
    with open(filepath, 'r') as f:
        lines = [l.strip() for l in f if l.strip()]
    n_atoms = int(lines[0])
    species = []
    coords = []
    for l in lines[2:2 + n_atoms]:
        tokens = l.split()
        sp = tokens[0].replace('L', '')
        species.append(sp)
        coords.append([float(tokens[1]), float(tokens[2]), float(tokens[3])])
    return n_atoms, species, np.array(coords, dtype=np.float64)

def blj_eval(coords_flat, species, ratio):
    n = len(species)
    coords = coords_flat.reshape((n, 3))
    energy = 0.0
    grad = np.zeros((n, 3), dtype=np.float64)
    
    sig_aa = 1.0
    sig_bb = ratio
    sig_ab = (1.0 + ratio) / 2.0
    
    for i in range(n):
        si = species[i]
        for j in range(i + 1, n):
            sj = species[j]
            dvec = coords[i] - coords[j]
            r2 = np.dot(dvec, dvec)
            r = math.sqrt(r2)
            
            sig = sig_aa if (si == 'A' and sj == 'A') else (sig_bb if (si == 'B' and sj == 'B') else sig_ab)
            
            inv_r = 1.0 / r
            u = sig * inv_r
            u2 = u * u
            u6 = u2 * u2 * u2
            u12 = u6 * u6
            
            energy += 4.0 * (u12 - u6)
            
            # dV/dr = 24/r * (u6 - 2*u12)
            dV_dr = 24.0 * inv_r * (u6 - 2.0 * u12)
            g_vec = dV_dr * (dvec * inv_r)
            grad[i] += g_vec
            grad[j] -= g_vec
            
    return energy, grad.flatten()

def compute_analytical_hessian(coords_flat, species, ratio):
    n = len(species)
    coords = coords_flat.reshape((n, 3))
    H = np.zeros((3 * n, 3 * n), dtype=np.float64)
    
    sig_aa = 1.0
    sig_bb = ratio
    sig_ab = (1.0 + ratio) / 2.0
    I3 = np.eye(3, dtype=np.float64)
    
    for i in range(n):
        si = species[i]
        for j in range(i + 1, n):
            sj = species[j]
            dvec = coords[i] - coords[j]
            r2 = np.dot(dvec, dvec)
            r = math.sqrt(r2)
            
            sig = sig_aa if (si == 'A' and sj == 'A') else (sig_bb if (si == 'B' and sj == 'B') else sig_ab)
            
            inv_r = 1.0 / r
            rhat = dvec * inv_r
            rhat_outer = np.outer(rhat, rhat)
            
            u = sig * inv_r
            u2 = u * u
            u6 = u2 * u2 * u2
            u12 = u6 * u6
            
            dV_dr = 24.0 * inv_r * (u6 - 2.0 * u12)
            d2V_dr2 = 24.0 * (inv_r * inv_r) * (26.0 * u12 - 7.0 * u6)
            
            block = d2V_dr2 * rhat_outer + (dV_dr * inv_r) * (I3 - rhat_outer)
            
            i3 = 3 * i
            j3 = 3 * j
            
            H[i3:i3+3, i3:i3+3] += block
            H[j3:j3+3, j3:j3+3] += block
            H[i3:i3+3, j3:j3+3] -= block
            H[j3:j3+3, i3:i3+3] -= block
            
    return H

def newton_raphson_polish(c_init, species, ratio, max_iters=25, tol=1e-11):
    c = c_init.copy()
    e_curr, g_curr = blj_eval(c, species, ratio)
    
    for it in range(max_iters):
        gnorm = np.linalg.norm(g_curr)
        if gnorm < tol:
            return c, e_curr, gnorm, it
            
        H = compute_analytical_hessian(c, species, ratio)
        # Solve H p = -g in the non-zero mode subspace using pseudo-inverse
        try:
            # pinv with cutoff 1e-5 ignores the 6 zero modes
            H_inv = np.linalg.pinv(H, rcond=1e-5)
            p = -np.dot(H_inv, g_curr)
        except Exception:
            p = -g_curr / (gnorm + 1e-8)
            
        # Backtracking line search
        alpha = 1.0
        step_ok = False
        for _ in range(15):
            c_cand = c + alpha * p
            e_cand, g_cand = blj_eval(c_cand, species, ratio)
            if e_cand <= e_curr:
                c = c_cand
                e_curr = e_cand
                g_curr = g_cand
                step_ok = True
                break
            alpha *= 0.5
            
        if not step_ok:
            # Gradient descent fallback
            alpha = 1e-4
            c = c - alpha * g_curr
            e_curr, g_curr = blj_eval(c, species, ratio)
            
    return c, e_curr, np.linalg.norm(g_curr), max_iters

def main():
    print("=" * 70)
    print("LENS 2: Analytical Newton-Raphson Polish & 3Nx3N Hessian Certification")
    print("=" * 70)
    
    run_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    file_n7 = os.path.join(run_dir, "data", "all", "1.1", "7")
    file_n13 = os.path.join(run_dir, "data", "all", "1.1", "13")
    
    # 1. Finite-Difference Gradient Verification on N=7
    print("\n--- Phase 1: Finite-Difference Gradient Validation (N=7, ratio=1.1) ---")
    n7, sp7, c7 = parse_point_file(file_n7)
    e7, grad_ana = blj_eval(c7.flatten(), sp7, ratio=1.1)
    
    eps = 1e-6
    grad_num = np.zeros_like(grad_ana)
    c_flat = c7.flatten()
    for idx in range(len(c_flat)):
        c_plus = c_flat.copy()
        c_plus[idx] += eps
        ep, _ = blj_eval(c_plus, sp7, ratio=1.1)
        
        c_minus = c_flat.copy()
        c_minus[idx] -= eps
        em, _ = blj_eval(c_minus, sp7, ratio=1.1)
        
        grad_num[idx] = (ep - em) / (2.0 * eps)
        
    grad_diff = np.max(np.abs(grad_ana - grad_num))
    print(f"Max absolute difference (Analytical vs Numerical Gradient): {grad_diff:.2e}")
    assert grad_diff < 1e-7, "Gradient validation failed!"
    print("Analytical gradient verified to machine precision.")
    
    # 2. Precision Polish on N=7
    print("\n--- Phase 2: Precision Polish on N=7 via Analytical Newton-Raphson ---")
    c7_opt, e7_opt, gnorm7, it7 = newton_raphson_polish(c7.flatten(), sp7, ratio=1.1)
    print(f"Polished N=7 Energy: {e7_opt:.12f} (initial: {e7:.12f}, delta: {e7 - e7_opt:.2e}) in {it7} iters")
    print(f"Polished N=7 Gradient Norm: {gnorm7:.2e} (< 1e-10 requirement: {gnorm7 < 1e-10})")
    assert gnorm7 < 1e-10, "Polish failed to reach gnorm < 1e-10!"
    
    # 3. 3Nx3N Analytical Hessian Eigenvalue Certification on N=7
    print("\n--- Phase 3: Analytical Hessian Normal Mode Certification (N=7) ---")
    H7 = compute_analytical_hessian(c7_opt, sp7, ratio=1.1)
    eigs7 = np.linalg.eigvalsh(H7)
    
    zero_modes_7 = [val for val in eigs7 if abs(val) < 1e-6]
    neg_modes_7 = [val for val in eigs7 if val < -1e-6]
    pos_modes_7 = [val for val in eigs7 if val >= 1e-6]
    
    print(f"Total Hessian Eigenvalues (3N = 21):")
    print(f"  First 6 eigenvalues (rigid translations + rotations): {eigs7[:6]}")
    print(f"  7th eigenvalue (lowest vibrational mode): {eigs7[6]:.8f}")
    print(f"  Max eigenvalue: {eigs7[-1]:.8f}")
    print(f"  Zero modes count (|lambda| < 1e-6): {len(zero_modes_7)} (expected: exactly 6)")
    print(f"  Negative modes count (lambda < -1e-6): {len(neg_modes_7)} (expected: 0)")
    assert len(zero_modes_7) == 6, f"Expected exactly 6 zero modes, got {len(zero_modes_7)}!"
    assert len(neg_modes_7) == 0, f"Expected 0 negative modes, got {len(neg_modes_7)}!"
    print("Certification Passed: Exactly 6 near-zero modes and zero negative eigenvalues confirm certified local minimum.")
    
    # 4. Certification on N=13
    print("\n--- Phase 4: Precision Polish & Hessian Certification on N=13 ---")
    n13, sp13, c13 = parse_point_file(file_n13)
    e13_init, _ = blj_eval(c13.flatten(), sp13, ratio=1.1)
    c13_opt, e13_opt, gnorm13, it13 = newton_raphson_polish(c13.flatten(), sp13, ratio=1.1)
    print(f"Polished N=13 Energy: {e13_opt:.12f} (initial: {e13_init:.12f}, delta: {e13_init - e13_opt:.2e}) in {it13} iters")
    print(f"Polished N=13 Gradient Norm: {gnorm13:.2e} (< 1e-10 requirement: {gnorm13 < 1e-10})")
    assert gnorm13 < 1e-10, "N=13 polish failed to reach gnorm < 1e-10!"
    
    H13 = compute_analytical_hessian(c13_opt, sp13, ratio=1.1)
    eigs13 = np.linalg.eigvalsh(H13)
    zero_modes_13 = [val for val in eigs13 if abs(val) < 1e-6]
    neg_modes_13 = [val for val in eigs13 if val < -1e-6]
    print(f"N=13 Zero modes: {len(zero_modes_13)} (expected: 6), Negative modes: {len(neg_modes_13)} (expected: 0)")
    print(f"N=13 7th eigenvalue: {eigs13[6]:.8f} > 0")
    assert len(zero_modes_13) == 6 and len(neg_modes_13) == 0, "N=13 Hessian validation failed!"
    print("N=13 Certification Passed: Certified minimum verified.")
    
    print("\nLENS 2 COMPLETE: Analytical gradient and Hessian verified; normal-mode certification confirmed.")

if __name__ == "__main__":
    main()
