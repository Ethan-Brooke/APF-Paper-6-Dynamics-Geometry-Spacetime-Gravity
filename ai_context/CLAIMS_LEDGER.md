# Claims Ledger — Paper 6

| # | Claim | Status | Proof location | Code check | Failure mode |
|---|---|---|---|---|---|
| 1 | PLEC path form + Euler-Lagrange | nontrivial | Supp §1 | `check_L_PLEC_path` | non-least-cost admissible path |
| 2 | Regime R five-type exhaustiveness | nontrivial | Supp §2 | `check_Regime_R` | sixth exit type exhibited |
| 3 | $T_{7B}$ Lorentzian signature forced | nontrivial | Supp §3 | `check_T_7B` | Euclidean / split signature admissible |
| 4 | $T_8$ spacetime $d = 4$ | nontrivial | Supp §4 | `check_T_8` | alternative dimension admissible |
| 5 | $A9$ unified closure + Einstein | nontrivial | Supp §5 | `check_A9_closure` | alternative gravitational action |
| 6 | $T_{\rm graviton}$ via Weinberg-Witten | imported + structural | Supp §6 | `check_T_graviton` | massive graviton admissible |
| 7 | $T_{11}$: $\Omega_\Lambda = 42/61$ with $C_{\rm vacuum} = 42$ | nontrivial (load-bearing) | Supp §T11 | `check_T11` | $27 + 3 + 12$ decomposition disputed |
| 8 | $L_{\rm self\_exclusion}$: $d_{\rm eff} = 102$ | nontrivial (load-bearing) | Supp §L_self_exclusion | `check_L_self_exclusion` | self-correlation count disputed |
| 9 | $T_{12} / T_{12E}$ dark matter | nontrivial (open bridge) | Supp §T12 | `check_T12`, `check_T12E` | no particle-ID mechanism |
| 10 | $T_{\rm interface\_sector\_bridge}$ | nontrivial (primary bridge receiver) | Supp §Bridge_compressed | `check_T_interface_sector_bridge` | $V_{\rm global} \ne V_\Lambda$ |
| 11 | $T_{\rm I1\_bridge\_at\_joint\_K42}$ | nontrivial (Phase 14f.4) | Supp (2026-04-23) | `check_T_I1_bridge_at_joint_K42` | joint point at $K \ne 42$ |
| 12 | $H_0 = 67.76$ km/s/Mpc prediction | arithmetic + structural | Main §11.4 | `check_L_H0_prediction` | — |
| 13 | $H_0$ falsifier (7.09σ tension) | empirical | Main §11.4 falsifier | — | Route V admissible with ~2× coupling |
| 14 | Three-entropies unification ($S_{\rm vN} = S_{\rm Bek} = S_{\rm dS}$) | nontrivial | Supp §horizon | `check_T_horizon_reciprocity` | three-way inequality at some interface |

## Attack surface priority

Claims 7, 8, 10, 11. Claims 7+8 are the independent routes to $C_{\rm vacuum} = 42$ and $d_{\rm eff} = 102$ — if they fail, Paper 8's Theorem 1.1 loses its upstream.

---

*21 bank-registered checks verify this paper in this repo.*
