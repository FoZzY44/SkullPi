"""Safety related utilities."""

from __future__ import annotations

from typing import Callable, Optional

from logger import LOGGER

try:  # pragma: no cover
    import RPi.GPIO as GPIO
except Exception:  # pragma: no cover
    GPIO = None  # type: ignore


class EmergencyButton:
    """Handle a physical emergency stop button."""

    def __init__(self, pin: int, callback: Optional[Callable[[], None]] = None) -> None:
        self.pin = pin
        self.callback = callback
        if GPIO:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, self._pressed, bouncetime=300)
            LOGGER.info("Emergency button configured on GPIO %s", pin)
        else:  # pragma: no cover
            LOGGER.warning("RPi.GPIO not available; emergency button disabled")

    def _pressed(self, channel: int) -> None:  # pragma: no cover - hardware interaction
        LOGGER.warning("Emergency button pressed on channel %s", channel)
        if self.callback:
            self.callback()

