import importlib

import Extractor.modules as modules


def test_eval_module_is_disabled_by_default(monkeypatch):
    monkeypatch.delenv("ENABLE_EVAL_MODULE", raising=False)
    monkeypatch.setattr(
        modules.glob,
        "glob",
        lambda _pattern: ["/tmp/eval.py", "/tmp/classplus.py", "/tmp/__init__.py"],
    )
    monkeypatch.setattr(modules, "isfile", lambda _path: True)

    importlib.reload(modules)

    assert "eval" not in modules.ALL_MODULES
    assert "classplus" in modules.ALL_MODULES


def test_eval_module_can_be_enabled_explicitly(monkeypatch):
    monkeypatch.setenv("ENABLE_EVAL_MODULE", "true")
    monkeypatch.setattr(
        modules.glob,
        "glob",
        lambda _pattern: ["/tmp/eval.py", "/tmp/classplus.py", "/tmp/__init__.py"],
    )
    monkeypatch.setattr(modules, "isfile", lambda _path: True)

    importlib.reload(modules)

    assert "eval" in modules.ALL_MODULES
