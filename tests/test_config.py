import importlib.util
from pathlib import Path

import pytest


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.py"
REQUIRED_VALUES = {
    "API_ID": "12345",
    "API_HASH": "test-api-hash",
    "BOT_TOKEN": "123:token",
    "OWNER_ID": "123",
    "CHANNEL_ID": "-100123",
    "CHANNEL_ID2": "-100456",
    "MONGO_URL": "mongodb://localhost/test",
    "PREMIUM_LOGS": "-100789",
}


def load_config():
    spec = importlib.util.spec_from_file_location("config_under_test", CONFIG_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def set_valid_environment(monkeypatch):
    for name, value in REQUIRED_VALUES.items():
        monkeypatch.setenv(name, value)


def test_config_loads_with_valid_environment(monkeypatch):
    set_valid_environment(monkeypatch)
    config = load_config()

    assert config.API_ID == 12345
    assert config.OWNER_ID == 123
    assert config.CHANNEL_ID == -100123
    assert config.PREMIUM_LOGS == -100789


def test_missing_required_value_has_clear_error(monkeypatch):
    set_valid_environment(monkeypatch)
    monkeypatch.delenv("BOT_TOKEN")

    with pytest.raises(RuntimeError, match="BOT_TOKEN"):
        load_config()


def test_invalid_integer_has_clear_error(monkeypatch):
    set_valid_environment(monkeypatch)
    monkeypatch.setenv("API_ID", "not-an-integer")

    with pytest.raises(RuntimeError, match="API_ID.*integer"):
        load_config()
