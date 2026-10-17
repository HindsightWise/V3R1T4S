// ============================================================================
// AB_Protein_Hunter.cc — v3 with Tri-Class Rigid-Core Polymer Moves:
//   - Class I:   N-Terminal Tail Re-Docking (k = 1..8, leaves core 100% rigid)
//   - Class II:  C-Terminal Tail Re-Docking (k = 1..8, leaves core 100% rigid)
//   - Class III: Exact Sum-Preserving Internal Loop Bridges (3-bond S^2 x S^1
//                bridge, 4-bond quad bridge, crankshafts, bond swaps, reversals,
//                and reptation — leaves both prefix and suffix 100% rigid)
//   + Soft-Core L-BFGS & Damped Newton-Raphson Polisher (||grad||_2 < 1e-13)
// ============================================================================
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <random>
#include <algorithm>
#include <iomanip>
#include <thread>
#include <mutex>
#include <atomic>
#include <chrono>
#include "json.hpp"

using json = nlohmann::json;

struct Instance {
    std::string label;
    int L;
    int declared_L;
    int D;
    std::string seq;
    double table10_negE;
    std::vector<double> init_deg;
    std::vector<double> c_mat;
};

inline void angles_to_u(int L, const double* x, double* ux, double* uy, double* uz) {
    const int n_th = L - 2;
    const double* th = x;
    const double* be = x + n_th;
    ux[0] = std::cos(th[0]);
    uy[0] = std::sin(th[0]);
    uz[0] = 0.0;
    for (int m = 1; m < n_th; ++m) {
        double cb = std::cos(be[m - 1]);
        ux[m] = std::cos(th[m]) * cb;
        uy[m] = std::sin(th[m]) * cb;
        uz[m] = std::sin(be[m - 1]);
    }
}

inline void u_to_angles(int L, const double* ux, const double* uy, const double* uz, double* x) {
    const int n_th = L - 2;
    double* th = x;
    double* be = x + n_th;
    th[0] = std::atan2(uy[0], ux[0]);
    for (int m = 1; m < n_th; ++m) {
        double z = std::clamp(uz[m], -1.0, 1.0);
        be[m - 1] = std::asin(z);
        th[m] = std::atan2(uy[m], ux[m]);
    }
}

inline double eval_energy_and_grad(
    const Instance& inst,
    const double* __restrict x,
    double* __restrict grad,
    double* __restrict px,
    double* __restrict py,
    double* __restrict pz,
    double* __restrict ct,
    double* __restrict st,
    double* __restrict cb,
    double* __restrict sb,
    double* __restrict gx,
    double* __restrict gy,
    double* __restrict gz,
    double r2_floor = 1e-12
) {
    const int L = inst.L;
    const int n_th = L - 2;
    const int n_be = L - 3;
    const double* th = x;
    const double* be = x + n_th;

    for (int m = 0; m < n_th; ++m) {
        ct[m] = std::cos(th[m]);
        st[m] = std::sin(th[m]);
    }
    for (int m = 0; m < n_be; ++m) {
        cb[m] = std::cos(be[m]);
        sb[m] = std::sin(be[m]);
    }

    px[0] = 0.0; py[0] = 0.0; pz[0] = 0.0;
    px[1] = 0.0; py[1] = 1.0; pz[1] = 0.0;
    px[2] = ct[0]; py[2] = 1.0 + st[0]; pz[2] = 0.0;
    for (int m = 1; m < n_th; ++m) {
        px[m + 2] = px[m + 1] + ct[m] * cb[m - 1];
        py[m + 2] = py[m + 1] + st[m] * cb[m - 1];
        pz[m + 2] = pz[m + 1] + sb[m - 1];
    }

    double E_bb = 0.0;
    for (int m = 0; m < n_th; ++m) {
        E_bb += (1.0 - ct[m]);
    }
    E_bb *= 0.25;

    for (int i = 0; i < L; ++i) {
        gx[i] = 0.0; gy[i] = 0.0; gz[i] = 0.0;
    }

    double E_lj = 0.0;
    const double* c_mat = inst.c_mat.data();
    for (int i = 0; i < L - 2; ++i) {
        const double pxi = px[i], pyi = py[i], pzi = pz[i];
        double gxi = 0.0, gyi = 0.0, gzi = 0.0;
        const double* c_row = c_mat + i * L;
        for (int j = i + 2; j < L; ++j) {
            const double dx = pxi - px[j];
            const double dy = pyi - py[j];
            const double dz = pzi - pz[j];
            const double raw_r2 = dx * dx + dy * dy + dz * dz;
            const double r2 = (raw_r2 < r2_floor) ? r2_floor : raw_r2;
            const double inv_r2 = 1.0 / r2;
            const double inv_r6 = inv_r2 * inv_r2 * inv_r2;
            const double inv_r12 = inv_r6 * inv_r6;
            const double cij = c_row[j];
            E_lj += 4.0 * (inv_r12 - cij * inv_r6);
            const double coef = 48.0 * inv_r2 * inv_r6 * (0.5 * cij - inv_r6);
            const double fx = coef * dx;
            const double fy = coef * dy;
            const double fz = coef * dz;
            gxi += fx; gyi += fy; gzi += fz;
            gx[j] -= fx; gy[j] -= fy; gz[j] -= fz;
        }
        gx[i] += gxi; gy[i] += gyi; gz[i] += gzi;
    }

    double sx = 0.0, sy = 0.0, sz = 0.0;
    for (int m = n_th - 1; m >= 1; --m) {
        sx += gx[m + 2];
        sy += gy[m + 2];
        sz += gz[m + 2];
        grad[m] = 0.25 * st[m] + sx * (-st[m] * cb[m - 1]) + sy * (ct[m] * cb[m - 1]);
        grad[n_th + m - 1] = sx * (-ct[m] * sb[m - 1]) + sy * (-st[m] * sb[m - 1]) + sz * cb[m - 1];
    }
    sx += gx[2];
    sy += gy[2];
    grad[0] = 0.25 * st[0] + sx * (-st[0]) + sy * ct[0];

    return E_bb + E_lj;
}

bool solve_linear(int D, std::vector<double>& A, const std::vector<double>& b, std::vector<double>& x) {
    x = b;
    for (int i = 0; i < D; ++i) x[i] = -x[i];
    for (int k = 0; k < D; ++k) {
        int piv = k;
        double max_v = std::abs(A[k * D + k]);
        for (int i = k + 1; i < D; ++i) {
            double v = std::abs(A[i * D + k]);
            if (v > max_v) { max_v = v; piv = i; }
        }
        if (max_v < 1e-15) return false;
        if (piv != k) {
            for (int j = k; j < D; ++j) std::swap(A[k * D + j], A[piv * D + j]);
            std::swap(x[k], x[piv]);
        }
        double diag = A[k * D + k];
        for (int i = k + 1; i < D; ++i) {
            double factor = A[i * D + k] / diag;
            A[i * D + k] = 0.0;
            for (int j = k + 1; j < D; ++j) {
                A[i * D + j] -= factor * A[k * D + j];
            }
            x[i] -= factor * x[k];
        }
    }
    for (int i = D - 1; i >= 0; --i) {
        double sum = x[i];
        for (int j = i + 1; j < D; ++j) sum -= A[i * D + j] * x[j];
        x[i] = sum / A[i * D + i];
    }
    return true;
}

struct Workspace {
    int M = 16;
    int L, D;
    std::vector<double> px, py, pz, ct, st, cb, sb, gx, gy, gz;
    std::vector<double> g, g_prev, x_new, g_new, d, q, alpha;
    std::vector<std::vector<double>> s_hist, y_hist;
    std::vector<double> rho_hist;
    std::vector<double> ux, uy, uz;

    Workspace(int L_, int D_) : L(L_), D(D_),
        px(L_), py(L_), pz(L_), ct(L_), st(L_), cb(L_), sb(L_), gx(L_), gy(L_), gz(L_),
        g(D_), g_prev(D_), x_new(D_), g_new(D_), d(D_), q(D_), alpha(M),
        s_hist(M, std::vector<double>(D_)), y_hist(M, std::vector<double>(D_)), rho_hist(M),
        ux(L_ - 2), uy(L_ - 2), uz(L_ - 2) {}

    double eval(const Instance& inst, const double* x, double* grad_out, double r2_floor = 1e-12) {
        return eval_energy_and_grad(inst, x, grad_out,
            px.data(), py.data(), pz.data(),
            ct.data(), st.data(), cb.data(), sb.data(),
            gx.data(), gy.data(), gz.data(), r2_floor);
    }

    double lbfgs(const Instance& inst, std::vector<double>& x, int max_iter = 500, double gtol = 1e-11, double r2_floor = 1e-12) {
        double f = eval(inst, x.data(), g.data(), r2_floor);
        int hist_len = 0;
        int hist_head = 0;

        for (int iter = 0; iter < max_iter; ++iter) {
            double gnorm = 0.0;
            for (int i = 0; i < D; ++i) gnorm = std::max(gnorm, std::abs(g[i]));
            if (gnorm < gtol) break;

            for (int i = 0; i < D; ++i) q[i] = g[i];
            for (int k = hist_len - 1; k >= 0; --k) {
                int idx = (hist_head - 1 - (hist_len - 1 - k) + M * 100) % M;
                double dot = 0.0;
                for (int i = 0; i < D; ++i) dot += s_hist[idx][i] * q[i];
                alpha[k] = rho_hist[idx] * dot;
                for (int i = 0; i < D; ++i) q[i] -= alpha[k] * y_hist[idx][i];
            }
            double gamma = 1.0;
            if (hist_len > 0) {
                int last = (hist_head - 1 + M) % M;
                double sy = 0.0, yy = 0.0;
                for (int i = 0; i < D; ++i) {
                    sy += s_hist[last][i] * y_hist[last][i];
                    yy += y_hist[last][i] * y_hist[last][i];
                }
                if (yy > 1e-24 && sy > 0.0) gamma = sy / yy;
            }
            for (int i = 0; i < D; ++i) d[i] = gamma * q[i];
            for (int k = 0; k < hist_len; ++k) {
                int idx = (hist_head - hist_len + k + M * 100) % M;
                double dot = 0.0;
                for (int i = 0; i < D; ++i) dot += y_hist[idx][i] * d[i];
                double beta = rho_hist[idx] * dot;
                for (int i = 0; i < D; ++i) d[i] += s_hist[idx][i] * (alpha[k] - beta);
            }
            for (int i = 0; i < D; ++i) d[i] = -d[i];

            double dg = 0.0, dnorm = 0.0;
            for (int i = 0; i < D; ++i) {
                dg += d[i] * g[i];
                dnorm = std::max(dnorm, std::abs(d[i]));
            }
            if (dg >= 0.0 || !std::isfinite(dg)) {
                for (int i = 0; i < D; ++i) d[i] = -g[i];
                dg = 0.0; dnorm = 0.0;
                for (int i = 0; i < D; ++i) {
                    dg += d[i] * g[i];
                    dnorm = std::max(dnorm, std::abs(d[i]));
                }
                hist_len = 0; hist_head = 0;
            }

            double step = (dnorm > 0.25) ? (0.25 / dnorm) : 1.0;
            bool accepted = false;
            double f_new = f;
            for (int ls = 0; ls < 35; ++ls) {
                for (int i = 0; i < D; ++i) x_new[i] = x[i] + step * d[i];
                f_new = eval(inst, x_new.data(), g_new.data(), r2_floor);
                if (std::isfinite(f_new) && f_new <= f + 1e-4 * step * dg) {
                    accepted = true;
                    break;
                }
                step *= 0.5;
            }
            if (!accepted) {
                if (hist_len > 0) {
                    hist_len = 0; hist_head = 0;
                    continue;
                } else {
                    break;
                }
            }

            double sy = 0.0;
            for (int i = 0; i < D; ++i) {
                double si = x_new[i] - x[i];
                double yi = g_new[i] - g[i];
                s_hist[hist_head][i] = si;
                y_hist[hist_head][i] = yi;
                sy += si * yi;
            }
            x = x_new;
            g = g_new;
            f = f_new;
            if (sy > 1e-22) {
                rho_hist[hist_head] = 1.0 / sy;
                hist_head = (hist_head + 1) % M;
                if (hist_len < M) hist_len++;
            }
        }
        return f;
    }

    double newton_polish(const Instance& inst, std::vector<double>& x) {
        double f = lbfgs(inst, x, 2000, 1e-12, 1e-12);
        std::vector<double> H(D * D), H_work(D * D), gp(D), gm(D), dx(D), xt(D);
        double lambda = 1e-9;

        for (int n_step = 0; n_step < 10; ++n_step) {
            f = eval(inst, x.data(), g.data());
            double gmax = 0.0;
            for (int i = 0; i < D; ++i) gmax = std::max(gmax, std::abs(g[i]));
            if (gmax < 1e-13) break;

            const double eps = 1e-7;
            xt = x;
            for (int j = 0; j < D; ++j) {
                double orig = xt[j];
                xt[j] = orig + eps;
                eval(inst, xt.data(), gp.data());
                xt[j] = orig - eps;
                eval(inst, xt.data(), gm.data());
                xt[j] = orig;
                double inv2e = 0.5 / eps;
                for (int i = 0; i < D; ++i) {
                    H[i * D + j] = (gp[i] - gm[i]) * inv2e;
                }
            }
            for (int i = 0; i < D; ++i) {
                for (int j = i + 1; j < D; ++j) {
                    double avg = 0.5 * (H[i * D + j] + H[j * D + i]);
                    H[i * D + j] = avg;
                    H[j * D + i] = avg;
                }
            }

            bool step_ok = false;
            for (int damp_try = 0; damp_try < 12; ++damp_try) {
                H_work = H;
                for (int i = 0; i < D; ++i) H_work[i * D + i] += lambda;
                if (solve_linear(D, H_work, g, dx)) {
                    double step = 1.0;
                    for (int ls = 0; ls < 15; ++ls) {
                        for (int i = 0; i < D; ++i) x_new[i] = x[i] + step * dx[i];
                        double fn = eval(inst, x_new.data(), g_new.data());
                        double gn_max = 0.0;
                        for (int i = 0; i < D; ++i) gn_max = std::max(gn_max, std::abs(g_new[i]));
                        if (fn <= f + 1e-12 && (gn_max < gmax || fn < f)) {
                            x = x_new;
                            g = g_new;
                            f = fn;
                            lambda = std::max(1e-12, lambda * 0.2);
                            step_ok = true;
                            break;
                        }
                        step *= 0.5;
                    }
                }
                if (step_ok) break;
                lambda *= 10.0;
            }
            if (!step_ok) break;
        }
        return eval(inst, x.data(), g.data());
    }

    static inline void rotate_pair_crankshaft(
        double& ux1, double& uy1, double& uz1,
        double& ux2, double& uy2, double& uz2,
        double phi
    ) {
        double wx = ux1 + ux2, wy = uy1 + uy2, wz = uz1 + uz2;
        double wnorm = std::sqrt(wx * wx + wy * wy + wz * wz);
        if (wnorm < 1e-6) return;
        wx /= wnorm; wy /= wnorm; wz /= wnorm;
        double c = std::cos(phi), s = std::sin(phi);
        auto rot = [&](double& vx, double& vy, double& vz) {
            double dot = wx * vx + wy * vy + wz * vz;
            double cx = wy * vz - wz * vy;
            double cy = wz * vx - wx * vz;
            double cz = wx * vy - wy * vx;
            vx = vx * c + cx * s + wx * dot * (1.0 - c);
            vy = vy * c + cy * s + wy * dot * (1.0 - c);
            vz = vz * c + cz * s + wz * dot * (1.0 - c);
        };
        rot(ux1, uy1, uz1);
        rot(ux2, uy2, uz2);
    }

    static inline bool solve_two_unit_vectors_for_sum(
        double rx, double ry, double rz, double psi,
        double& u2x, double& u2y, double& u2z,
        double& u3x, double& u3y, double& u3z
    ) {
        double rnorm = std::sqrt(rx * rx + ry * ry + rz * rz);
        if (rnorm <= 1e-5 || rnorm >= 1.9999) return false;
        double h = 0.5 * rnorm;
        double s = std::sqrt(std::max(0.0, 1.0 - h * h));
        double rhat_x = rx / rnorm, rhat_y = ry / rnorm, rhat_z = rz / rnorm;
        double ax = (std::abs(rhat_x) < 0.8) ? 1.0 : 0.0;
        double ay = (std::abs(rhat_x) < 0.8) ? 0.0 : 1.0;
        double az = 0.0;
        double e1x = rhat_y * az - rhat_z * ay;
        double e1y = rhat_z * ax - rhat_x * az;
        double e1z = rhat_x * ay - rhat_y * ax;
        double e1n = std::sqrt(e1x * e1x + e1y * e1y + e1z * e1z);
        e1x /= e1n; e1y /= e1n; e1z /= e1n;
        double e2x = rhat_y * e1z - rhat_z * e1y;
        double e2y = rhat_z * e1x - rhat_x * e1z;
        double e2z = rhat_x * e1y - rhat_y * e1x;
        double cp = std::cos(psi), sp = std::sin(psi);
        double px_perp = s * (cp * e1x + sp * e2x);
        double py_perp = s * (cp * e1y + sp * e2y);
        double pz_perp = s * (cp * e1z + sp * e2z);
        u2x = h * rhat_x + px_perp; u2y = h * rhat_y + py_perp; u2z = h * rhat_z + pz_perp;
        u3x = h * rhat_x - px_perp; u3y = h * rhat_y - py_perp; u3z = h * rhat_z - pz_perp;
        return true;
    }

    void propose_move(const Instance& inst, const std::vector<double>& x_cur, std::vector<double>& x_cand, std::mt19937_64& rng) {
        x_cand = x_cur;
        angles_to_u(L, x_cand.data(), ux.data(), uy.data(), uz.data());
        int n_u = L - 2;
        std::uniform_real_distribution<double> U01(0.0, 1.0);
        std::normal_distribution<double> N01(0.0, 1.0);
        double r = U01(rng);

        if (r < 0.22) {
            // CLASS I: Pure N-Terminal Tail Re-Docking (m = 0..k-1, k = 1..9)
            // Leaves p[k+1..L-1] 100% mutually rigid!
            int k = 1 + (rng() % std::min(9, n_u));
            int mode = rng() % 4;
            if (mode == 0) {
                // Focused angular kick on N-terminal tail (theta[0..k-1], beta[0..k-2])
                double sigma = (U01(rng) < 0.5) ? 0.45 : 1.35;
                for (int m = 0; m < k; ++m) {
                    if (U01(rng) < 0.75) x_cand[m] += N01(rng) * sigma;
                    if (m >= 1 && U01(rng) < 0.75) x_cand[n_u + m - 1] += N01(rng) * sigma;
                }
            } else if (mode == 1) {
                // N-terminal 3-bond bridge starting right at m=0 (with u[0] in xy-plane!)
                for (int attempt = 0; attempt < 15; ++attempt) {
                    int m2 = 1 + (rng() % std::min(4, n_u - 2));
                    int m3 = m2 + 1 + (rng() % std::min(4, n_u - 1 - m2));
                    double sx = ux[0] + ux[m2] + ux[m3];
                    double sy = uy[0] + uy[m2] + uy[m3];
                    double sz = uz[0] + uz[m2] + uz[m3];
                    double th0_new = x_cand[0] + N01(rng) * 0.9;
                    double vx = std::cos(th0_new), vy = std::sin(th0_new), vz = 0.0;
                    double psi = (U01(rng) * 2.0 - 1.0) * M_PI;
                    if (solve_two_unit_vectors_for_sum(sx - vx, sy - vy, sz - vz, psi,
                        ux[m2], uy[m2], uz[m2], ux[m3], uy[m3], uz[m3])) {
                        ux[0] = vx; uy[0] = vy; uz[0] = 0.0;
                        u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
                        break;
                    }
                }
            } else if (mode == 2) {
                // N-terminal crankshaft + tail twist
                if (k >= 3) {
                    int m1 = 1 + (rng() % (k - 1));
                    int m2 = m1 + 1 + (rng() % std::min(3, n_u - 1 - m1));
                    rotate_pair_crankshaft(ux[m1], uy[m1], uz[m1], ux[m2], uy[m2], uz[m2], N01(rng) * 1.1);
                }
                double th0 = x_cand[0] + N01(rng) * 0.8;
                ux[0] = std::cos(th0); uy[0] = std::sin(th0); uz[0] = 0.0;
                u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
            } else {
                // N-terminal reflection/inversion of u[0..k-1]
                for (int m = 0; m < k; ++m) {
                    if (m >= 1 && U01(rng) < 0.6) uz[m] = -uz[m];
                    if (U01(rng) < 0.6) uy[m] = -uy[m];
                }
                u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
            }
        } else if (r < 0.44) {
            // CLASS II: Pure C-Terminal Tail Re-Docking (m = n_u-k .. n_u-1, k = 1..9)
            // Leaves p[0..L-1-k] 100% mutually rigid!
            int k = 1 + (rng() % std::min(9, n_u));
            int start_m = n_u - k;
            int mode = rng() % 3;
            if (mode == 0) {
                double sigma = (U01(rng) < 0.5) ? 0.45 : 1.35;
                for (int m = start_m; m < n_u; ++m) {
                    if (U01(rng) < 0.75) x_cand[m] += N01(rng) * sigma;
                    if (m >= 1 && U01(rng) < 0.75) x_cand[n_u + m - 1] += N01(rng) * sigma;
                }
            } else if (mode == 1 && k >= 2) {
                std::reverse(ux.begin() + start_m, ux.end());
                std::reverse(uy.begin() + start_m, uy.end());
                std::reverse(uz.begin() + start_m, uz.end());
                for (int m = start_m; m < n_u; ++m) {
                    ux[m] += N01(rng) * 0.25;
                    uy[m] += N01(rng) * 0.25;
                    uz[m] += N01(rng) * 0.25;
                    double n = std::sqrt(ux[m]*ux[m] + uy[m]*uy[m] + uz[m]*uz[m]);
                    if (n > 1e-8) { ux[m] /= n; uy[m] /= n; uz[m] /= n; }
                }
                u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
            } else {
                for (int m = start_m; m < n_u; ++m) {
                    if (m >= 1 && U01(rng) < 0.6) uz[m] = -uz[m];
                    if (U01(rng) < 0.6) uy[m] = -uy[m];
                }
                u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
            }
        } else if (r < 0.68) {
            // CLASS III-A: Exact 3-Bond & 4-Bond Spherical Loop Bridge (S^2 x S^1)
            // Strictly preserves u[m1]+u[m2]+u[m3] (or 4 bonds), leaving BOTH prefix & suffix 100% rigid!
            int n_bridges = (U01(rng) < 0.7) ? 1 : 2;
            for (int b = 0; b < n_bridges; ++b) {
                for (int attempt = 0; attempt < 15; ++attempt) {
                    int span1 = 1 + (rng() % 4);
                    int span2 = 1 + (rng() % 4);
                    if (1 + span1 + span2 >= n_u) continue;
                    int m1 = 1 + (rng() % (n_u - 1 - span1 - span2));
                    int m2 = m1 + span1;
                    int m3 = m2 + span2;
                    double sx = ux[m1] + ux[m2] + ux[m3];
                    double sy = uy[m1] + uy[m2] + uy[m3];
                    double sz = uz[m1] + uz[m2] + uz[m3];
                    double scale = (U01(rng) < 0.5) ? 0.5 : 1.4;
                    double vx = ux[m1] + N01(rng) * scale;
                    double vy = uy[m1] + N01(rng) * scale;
                    double vz = uz[m1] + N01(rng) * scale;
                    double vn = std::sqrt(vx * vx + vy * vy + vz * vz);
                    if (vn < 1e-8) continue;
                    vx /= vn; vy /= vn; vz /= vn;
                    double psi = (U01(rng) * 2.0 - 1.0) * M_PI;
                    if (solve_two_unit_vectors_for_sum(sx - vx, sy - vy, sz - vz, psi,
                        ux[m2], uy[m2], uz[m2], ux[m3], uy[m3], uz[m3])) {
                        ux[m1] = vx; uy[m1] = vy; uz[m1] = vz;
                        break;
                    }
                }
            }
            u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
        } else if (r < 0.86) {
            // CLASS III-B: Multi-Pair Invariant-Sum Crankshaft Rotations (1 to 3 pairs)
            int n_pairs = 1 + (rng() % 3);
            for (int p = 0; p < n_pairs; ++p) {
                int span = 1 + (rng() % std::min(8, n_u - 2));
                int m1 = 1 + (rng() % (n_u - 1 - span));
                int m2 = m1 + span;
                double phi = (U01(rng) < 0.5) ? (N01(rng) * 0.6) : ((U01(rng) * 2.0 - 1.0) * M_PI);
                rotate_pair_crankshaft(ux[m1], uy[m1], uz[m1], ux[m2], uy[m2], uz[m2], phi);
            }
            u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
        } else {
            // CLASS III-C: Exact Sum-Preserving Permutations (Swap / Reversal / Reptation)
            int span = 1 + (rng() % std::min(7, n_u - 2));
            int m1 = 1 + (rng() % (n_u - 1 - span));
            int m2 = m1 + span;
            double sub_r = U01(rng);
            if (sub_r < 0.4) {
                std::swap(ux[m1], ux[m2]);
                std::swap(uy[m1], uy[m2]);
                std::swap(uz[m1], uz[m2]);
            } else if (sub_r < 0.7) {
                std::reverse(ux.begin() + m1, ux.begin() + m2 + 1);
                std::reverse(uy.begin() + m1, uy.begin() + m2 + 1);
                std::reverse(uz.begin() + m1, uz.begin() + m2 + 1);
            } else {
                double tx = ux[m1], ty = uy[m1], tz = uz[m1];
                for (int m = m1; m < m2; ++m) {
                    ux[m] = ux[m + 1]; uy[m] = uy[m + 1]; uz[m] = uz[m + 1];
                }
                ux[m2] = tx; uy[m2] = ty; uz[m2] = tz;
            }
            u_to_angles(L, ux.data(), uy.data(), uz.data(), x_cand.data());
        }
    }
};

std::mutex io_mtx;

void save_solution(const Instance& inst, const std::vector<double>& x_rad, Workspace& ws) {
    const double rad2deg = 180.0 / M_PI;
    double f = ws.eval(inst, x_rad.data(), ws.g.data());
    double negE = -f;
    double gmax = 0.0, g2 = 0.0;
    for (double v : ws.g) {
        gmax = std::max(gmax, std::abs(v));
        g2 += v * v;
    }
    g2 = std::sqrt(g2);
    double gain = negE - inst.table10_negE;
    json j_out;
    j_out["label"] = inst.label;
    j_out["L"] = inst.L;
    j_out["D"] = inst.D;
    j_out["seq"] = inst.seq;
    j_out["table10_negE"] = inst.table10_negE;
    j_out["negE"] = negE;
    j_out["gain_over_table10"] = gain;
    j_out["grad_inf"] = gmax;
    j_out["grad_l2"] = g2;
    std::vector<double> deg(inst.D), rad(inst.D);
    for (int i = 0; i < inst.D; ++i) {
        rad[i] = x_rad[i];
        deg[i] = x_rad[i] * rad2deg;
    }
    j_out["angles_rad"] = rad;
    j_out["angles_deg"] = deg;
    std::ofstream ofs("best_" + inst.label + ".json");
    ofs << j_out.dump(2) << "\n";
}

void hunt_instance(const Instance& inst, double seconds_budget, int num_threads) {
    const double deg2rad = M_PI / 180.0;
    std::vector<double> global_best_x(inst.D);

    std::string saved_path = "best_" + inst.label + ".json";
    std::ifstream ifs(saved_path);
    if (ifs.good()) {
        json js = json::parse(ifs);
        for (int i = 0; i < inst.D; ++i) global_best_x[i] = js["angles_rad"][i];
    } else {
        for (int i = 0; i < inst.D; ++i) global_best_x[i] = inst.init_deg[i] * deg2rad;
    }

    Workspace init_ws(inst.L, inst.D);
    double init_E = init_ws.newton_polish(inst, global_best_x);
    double global_best_negE = -init_E;
    if (global_best_negE > inst.table10_negE + 1e-3) {
        save_solution(inst, global_best_x, init_ws);
    }

    auto t_start = std::chrono::steady_clock::now();
    std::atomic<long long> total_hops{0};

    auto worker = [&](int tid) {
        std::mt19937_64 rng(987654321ULL + tid * 104729ULL + inst.L * 997ULL + std::chrono::steady_clock::now().time_since_epoch().count());
        Workspace ws(inst.L, inst.D);
        std::vector<double> cur_x, cand_x;
        double cur_negE;
        {
            std::lock_guard<std::mutex> lk(io_mtx);
            cur_x = global_best_x;
            cur_negE = global_best_negE;
        }
        int stag = 0;
        while (true) {
            double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t_start).count();
            if (el >= seconds_budget) break;

            ws.propose_move(inst, cur_x, cand_x, rng);
            ws.lbfgs(inst, cand_x, 55, 1e-5, 0.55);
            double f_cand = ws.lbfgs(inst, cand_x, 350, 1e-9, 1e-12);
            double cand_negE = -f_cand;
            total_hops++;

            if (cand_negE > cur_negE + 1e-5) {
                f_cand = ws.newton_polish(inst, cand_x);
                cand_negE = -f_cand;
                cur_x = cand_x;
                cur_negE = cand_negE;
                stag = 0;

                std::lock_guard<std::mutex> lk(io_mtx);
                if (cand_negE > global_best_negE + 1e-6) {
                    global_best_negE = cand_negE;
                    global_best_x = cand_x;
                    double g2 = 0.0;
                    ws.eval(inst, cand_x.data(), ws.g.data());
                    for (double v : ws.g) g2 += v * v;
                    g2 = std::sqrt(g2);
                    double gain = global_best_negE - inst.table10_negE;
                    std::cout << "  *** [WIN " << inst.label << " L=" << inst.L << "] t=" << std::fixed << std::setprecision(1) << el
                              << "s hops=" << total_hops.load()
                              << " | -E* = " << std::setprecision(6) << global_best_negE
                              << " (Tab10=" << std::setprecision(4) << inst.table10_negE
                              << ", gain=" << std::showpos << std::setprecision(6) << gain << std::noshowpos
                              << ", ||g||_2=" << std::scientific << std::setprecision(2) << g2 << ") ***\n" << std::flush;
                    save_solution(inst, global_best_x, ws);
                }
            } else {
                std::uniform_real_distribution<double> U01(0.0, 1.0);
                double diff = cand_negE - cur_negE;
                if (diff > -1.5 && U01(rng) < std::exp(diff / 0.30)) {
                    cur_x = cand_x;
                    cur_negE = cand_negE;
                }
                stag++;
                if (stag > 50) {
                    std::lock_guard<std::mutex> lk(io_mtx);
                    cur_x = global_best_x;
                    cur_negE = global_best_negE;
                    stag = 0;
                }
            }
        }
    };

    std::vector<std::thread> threads;
    for (int t = 0; t < num_threads; ++t) threads.emplace_back(worker, t);
    for (auto& th : threads) th.join();

    double g2 = 0.0;
    init_ws.eval(inst, global_best_x.data(), init_ws.g.data());
    for (double v : init_ws.g) g2 += v * v;
    g2 = std::sqrt(g2);
    double gain = global_best_negE - inst.table10_negE;
    std::cout << "[" << std::setw(5) << inst.label << " L=" << std::setw(2) << inst.L << " D=" << std::setw(3) << inst.D << "] Done ("
              << total_hops.load() << " hops) | Tab10=" << std::fixed << std::setprecision(4) << inst.table10_negE
              << " -> Best -E* = " << std::setprecision(6) << global_best_negE
              << " (gain=" << std::showpos << std::setprecision(6) << gain << std::noshowpos
              << ", ||g||_2=" << std::scientific << std::setprecision(2) << g2 << ")\n" << std::flush;
}

int main(int argc, char** argv) {
    double secs_per_inst = (argc > 1) ? std::stod(argv[1]) : 3.5;
    std::string filter = (argc > 2) ? argv[2] : "ALL";

    std::ifstream f("benchmarks.json");
    json j = json::parse(f);
    std::vector<Instance> insts;
    for (auto& item : j) {
        Instance inst;
        inst.label = item["label"];
        inst.L = item["L"];
        inst.declared_L = item["declared_L"];
        inst.D = item["D"];
        inst.seq = item["seq"];
        inst.table10_negE = item["table10_negE"];
        for (double v : item["angles_deg"]) inst.init_deg.push_back(v);
        inst.c_mat.resize(inst.L * inst.L, 0.0);
        for (int a = 0; a < inst.L; ++a) {
            for (int b = 0; b < inst.L; ++b) {
                char sa = inst.seq[a], sb = inst.seq[b];
                inst.c_mat[a * inst.L + b] = (sa == 'A' && sb == 'A') ? 1.0 : ((sa == 'B' && sb == 'B') ? 0.5 : -0.5);
            }
        }
        insts.push_back(inst);
    }

    std::sort(insts.begin(), insts.end(), [](const Instance& a, const Instance& b) {
        return a.L > b.L;
    });

    for (auto& inst : insts) {
        if (filter != "ALL" && inst.label != filter) continue;
        if (inst.L < 29 && filter == "ALL") continue;
        hunt_instance(inst, secs_per_inst, 6);
    }
    return 0;
}
