import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).resolve().parents[1] / "Extractor" / "modules" / "__init__.py"


def load_module():
    spec = importlib.util.spec_from_file_location("module_discovery_under_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("enabled", ["", "0", "false", "no", "off"])
def test_eval_module_is_disabled_by_default_or_false_values(monkeypatch, enabled):
    monkeypatch.setenv("ENABLE_EVAL_MODULE", enabled)
    module = load_module()
    monkeypatch.setattr(
        module.glob,
        "glob",
        lambda _pattern: ["/tmp/eval.py", "/tmp/classplus.py", "/tmp/__init__.py"],
    )
    monkeypatch.setattr(module, "isfile", lambda _path: True)

    assert "eval" not in module.__list_all_modules()
    assert "classplus" in module.__list_all_modules()


@pytest.mark.parametrize("enabled", ["1", "true", "yes", "on", " TRUE "])
def test_eval_module_can_be_enabled_explicitly(monkeypatch, enabled):
    monkeypatch.setenv("ENABLE_EVAL_MODULE", enabled)
    module = load_module()
    monkeypatch.setattr(
        module.glob,
        "glob",
        lambda _pattern: ["/tmp/eval.py", "/tmp/classplus.py", "/tmp/__init__.py"],
    )
    monkeypatch.setattr(module, "isfile", lambda _path: True)

    assert "eval" in module.__list_all_modules()
