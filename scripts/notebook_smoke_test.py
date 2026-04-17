#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

import matplotlib
import nbformat


matplotlib.use("Agg")


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def load_code_cells(notebook_path: Path) -> list[str]:
    notebook = nbformat.read(notebook_path, as_version=4)
    return [cell.source for cell in notebook.cells if cell.cell_type == "code"]


def exec_code_cells(notebook_path: Path, code_cell_numbers: list[int], namespace: dict | None = None) -> dict:
    namespace = {} if namespace is None else namespace
    namespace.setdefault("__name__", "__main__")
    code_cells = load_code_cells(notebook_path)
    for number in code_cell_numbers:
        exec(code_cells[number - 1], namespace)
    return namespace


def assert_counts(counts: dict, min_total: int = 1) -> None:
    assert isinstance(counts, dict), f"Expected dict counts, got {type(counts)!r}"
    assert counts, "Counts dictionary is empty"
    assert all(isinstance(key, str) for key in counts), f"Unexpected key types: {counts}"
    assert all(isinstance(value, int) for value in counts.values()), f"Unexpected value types: {counts}"
    assert sum(counts.values()) >= min_total, f"Unexpected total shots: {counts}"


def smoke_unit_1() -> None:
    ns = exec_code_cells(NOTEBOOKS / "01-logistics.ipynb", [1, 2, 3, 4])
    assert_counts(ns["results"], min_total=128)


def smoke_unit_2() -> None:
    ns = exec_code_cells(NOTEBOOKS / "02-cryptography.ipynb", [1, 2, 3, 4, 5])
    assert_counts(ns["results"], min_total=1000)
    assert ns["best_outcome"] == ns["expected_peak"], (
        f"Unexpected dominant crypto phase peak: {ns['best_outcome']} != {ns['expected_peak']}"
    )
    assert ns["peak_probability"] >= 0.6, f"Crypto peak too diffuse: {ns['peak_probability']:.3f}"
    assert ns["r"] == 4, f"Unexpected recovered period: {ns['r']}"


def smoke_unit_3() -> None:
    ns = exec_code_cells(NOTEBOOKS / "03-drug-discovery.ipynb", [1, 2, 3, 4])
    energy = ns["compute_energy"](0.5, ns["coeffs"], shots=128)
    assert isinstance(energy, float), f"Unexpected energy type: {type(energy)!r}"


def smoke_unit_4() -> None:
    ns = exec_code_cells(NOTEBOOKS / "04-machine-learning.ipynb", [1, 2, 3])
    circuit = ns["kernel_circuit"](ns["X_train"][0], ns["X_train"][1])
    counts = ns["run_qasm"](circuit, shots=128)
    assert_counts(counts, min_total=128)
    probability_00 = counts.get("00", 0) / sum(counts.values())
    assert 0.0 <= probability_00 <= 1.0, f"Invalid probability: {probability_00}"


def smoke_unit_5() -> None:
    ns = exec_code_cells(NOTEBOOKS / "05-finance.ipynb", [1, 2, 5, 6])
    assert_counts(ns["results"], min_total=1000)
    assert ns["best_outcome"] == ns["expected_peak"], (
        f"Unexpected dominant finance phase peak: {ns['best_outcome']} != {ns['expected_peak']}"
    )
    assert ns["peak_probability"] >= 0.6, f"Finance peak too diffuse: {ns['peak_probability']:.3f}"
    assert abs(ns["exercise_prob_qae_toy"] - ns["exercise_fraction"]) <= 0.05, (
        "Finance toy amplitude estimate drifted away from the discretised exercise fraction"
    )


def smoke_unit_6() -> None:
    ns = exec_code_cells(NOTEBOOKS / "06-supply-chains.ipynb", [1, 2, 3])
    assert_counts(ns["results"], min_total=1000)


def smoke_unit_7() -> None:
    ns = exec_code_cells(NOTEBOOKS / "07-materials-science.ipynb", [1, 2, 3])
    assert_counts(ns["results"], min_total=1000)
    assert ns["best_outcome"] == ns["expected_peak"], (
        f"Unexpected dominant phase peak: {ns['best_outcome']} != {ns['expected_peak']}"
    )
    assert ns["peak_probability"] >= 0.6, f"Peak too diffuse: {ns['peak_probability']:.3f}"
    assert ns["grid_error"] <= 0.25, f"Grid approximation too large: {ns['grid_error']:.4f}"


def smoke_unit_8() -> None:
    ns = exec_code_cells(NOTEBOOKS / "08-climate-energy.ipynb", [1, 2, 3])
    assert isinstance(ns["E_vqe"], float), f"Unexpected VQE energy type: {type(ns['E_vqe'])!r}"


SMOKE_TESTS = {
    "01-logistics.ipynb": smoke_unit_1,
    "02-cryptography.ipynb": smoke_unit_2,
    "03-drug-discovery.ipynb": smoke_unit_3,
    "04-machine-learning.ipynb": smoke_unit_4,
    "05-finance.ipynb": smoke_unit_5,
    "06-supply-chains.ipynb": smoke_unit_6,
    "07-materials-science.ipynb": smoke_unit_7,
    "08-climate-energy.ipynb": smoke_unit_8,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run notebook smoke tests against the current Quokka API.")
    parser.add_argument(
        "--notebook",
        action="append",
        choices=sorted(SMOKE_TESTS),
        help="Limit execution to one or more notebooks.",
    )
    args = parser.parse_args()

    selected = args.notebook or sorted(SMOKE_TESTS)
    failures: list[tuple[str, str]] = []

    for notebook_name in selected:
        print(f"[smoke] {notebook_name}")
        try:
            SMOKE_TESTS[notebook_name]()
        except Exception as exc:  # noqa: BLE001
            failures.append((notebook_name, f"{type(exc).__name__}: {exc}"))
            print(f"  FAIL: {type(exc).__name__}: {exc}")
        else:
            print("  PASS")

    if failures:
        print("\nSmoke test failures:")
        for notebook_name, message in failures:
            print(f"- {notebook_name}: {message}")
        return 1

    print("\nAll selected notebook smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())