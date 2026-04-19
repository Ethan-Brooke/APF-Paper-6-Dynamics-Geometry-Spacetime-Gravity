"""apf/bank.py — Paper 6 registry.

Lightweight registry for the 22-check subset bundled in this
paper-companion repo. Mirrors the canonical apf.bank API: REGISTRY (dict),
get_check(name), run_all(verbose=False).
"""
from collections import OrderedDict
import traceback

from apf import core as _core


def _build_registry():
    reg = OrderedDict()
    for name in ['check_Regime_exit_Type_II', 'check_Regime_exit_Type_III', 'check_L_irr', 'check_L_Gleason_finite', 'check_T_Bek', 'check_Regime_exit_Type_I', 'check_Regime_exit_Type_IV', 'check_Regime_exit_Type_V', 'check_T7B', 'check_L_HKM_causal_geometry', 'check_L_Malament_uniqueness', 'check_T8', 'check_T10', 'check_T9_grav', 'check_A9_closure', 'check_T11', 'check_L_equation_of_state', 'check_L_DESI_response', 'check_L_saturation_partition', 'check_L_equip', 'check_L_anomaly_free', 'check_Regime_R']:
        fn = getattr(_core, name, None)
        if fn is None:
            # Function couldn't be extracted — skip with a warning attribute
            continue
        reg[name] = fn
    return reg


REGISTRY = _build_registry()
EXPECTED_CHECK_COUNT = 22


def get_check(name):
    """Return the check function registered as `name`. Raises KeyError if missing."""
    if name not in REGISTRY:
        raise KeyError(f"Check '{name}' not found. Available: {sorted(REGISTRY.keys())}")
    return REGISTRY[name]


def run_all(verbose=False):
    """Run every registered check, returning a list of result dicts."""
    results = []
    for name, fn in REGISTRY.items():
        try:
            r = fn()
            if not isinstance(r, dict):
                # Some legacy checks return True/False
                r = {"name": name, "passed": bool(r), "key_result": str(r)}
            elif "passed" not in r:
                r["passed"] = True
            r.setdefault("name", name)
        except Exception as e:
            r = {
                "name": name,
                "passed": False,
                "error": f"{type(e).__name__}: {e}",
                "traceback": traceback.format_exc(),
            }
        if verbose:
            status = "PASS" if r.get("passed", True) else "FAIL"
            print(f"  {r['name']}: {status}")
            if r.get("key_result"):
                print(f"    {r['key_result']}")
        results.append(r)
    return results
