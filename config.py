"""Configuration file management for SkullPi."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from logger import LOGGER

CONFIG_FILE = Path("config.json")
STATE_FILE = Path("state.json")
TEMPLATE_DIR = Path("templates")


def load_config() -> Dict[str, Any]:
    """Load configuration from :data:`CONFIG_FILE`.

    Returns
    -------
    dict
        Configuration data.
    """
    if not CONFIG_FILE.exists():
        LOGGER.error("Configuration file missing: %s", CONFIG_FILE)
        return {}
    with CONFIG_FILE.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_state() -> Dict[str, Any]:
    """Load persistent state.

    Returns
    -------
    dict
        State data.
    """
    if not STATE_FILE.exists():
        LOGGER.warning("State file missing: %s", STATE_FILE)
        return {}
    with STATE_FILE.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state: Dict[str, Any]) -> None:
    """Persist state to :data:`STATE_FILE`.

    Parameters
    ----------
    state:
        State dictionary to save.
    """
    with STATE_FILE.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)
        LOGGER.info("State saved: %s", state)


