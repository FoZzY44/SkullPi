"""Supervisor module implementing a basic state machine."""

from __future__ import annotations

import enum
from typing import Callable, Dict

from logger import LOGGER


class Mode(enum.Enum):
    """Operational modes for SkullPi."""

    IDLE = "idle"
    ACCUEIL = "accueil"
    MUSIQUE = "musique"
    IA = "ia"
    CALIBRATION = "calibration"
    SLEEP = "sleep"


class Supervisor:
    """Simple event driven state machine."""

    def __init__(self) -> None:
        self.mode = Mode.IDLE
        self.handlers: Dict[Mode, Callable[[], None]] = {
            Mode.IDLE: self._handle_idle,
            Mode.ACCUEIL: self._handle_accueil,
            Mode.MUSIQUE: self._handle_musique,
            Mode.IA: self._handle_ia,
            Mode.CALIBRATION: self._handle_calibration,
            Mode.SLEEP: self._handle_sleep,
        }

    def set_mode(self, mode: Mode) -> None:
        LOGGER.info("Switching mode %s -> %s", self.mode, mode)
        self.mode = mode

    def step(self) -> None:
        """Run one iteration of the state machine."""
        handler = self.handlers.get(self.mode)
        if handler:
            handler()

    def _handle_idle(self) -> None:
        LOGGER.debug("Idle mode running")

    def _handle_accueil(self) -> None:
        LOGGER.debug("Accueil mode running")
        self.set_mode(Mode.IDLE)

    def _handle_musique(self) -> None:
        LOGGER.debug("Musique mode running")
        self.set_mode(Mode.IDLE)

    def _handle_ia(self) -> None:
        LOGGER.debug("IA mode running")
        self.set_mode(Mode.IDLE)

    def _handle_calibration(self) -> None:
        LOGGER.debug("Calibration mode running")
        self.set_mode(Mode.IDLE)

    def _handle_sleep(self) -> None:
        LOGGER.debug("Sleep mode running")

