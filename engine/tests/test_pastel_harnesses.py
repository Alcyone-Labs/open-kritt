"""Pastel multi-harness registration smoke tests (BLG-601)."""

from open_kritt_engine.harnesses import PASTEL_CLI_HARNESSES, PastelCliHarness, harness_for


def test_pastel_harnesses_register():
    for name in sorted(PASTEL_CLI_HARNESSES):
        h = harness_for(name, timeout_seconds=30, model_provider="ollama")
        assert isinstance(h, PastelCliHarness)
        assert h.name == name


def test_unknown_harness_still_rejected():
    try:
        harness_for("not-a-real-harness", timeout_seconds=1)
        assert False, "expected HarnessError"
    except Exception as exc:
        assert "unsupported harness" in str(exc).lower() or "harness" in str(exc).lower()
