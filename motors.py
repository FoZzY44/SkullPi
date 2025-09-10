"""Servo motor control utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from logger import LOGGER


@dataclass
class Servo:
    """Representation of a single PWM controlled servo.

    Parameters
    ----------
    channel: int
        PWM channel on PCA9685 controller.
    min_angle: int
        Minimum pulse width allowed.
    max_angle: int
        Maximum pulse width allowed.
    idle: int
        Idle position pulse width.
    """

    channel: int
    min_angle: int
    max_angle: int
    idle: int
    position: int = 0

    def __post_init__(self) -> None:
        self.position = self.idle
        LOGGER.debug(
            "Servo initialised on channel %s with min=%s max=%s idle=%s",
            self.channel,
            self.min_angle,
            self.max_angle,
            self.idle,
        )

    def set_position(self, pulse: int) -> int:
        """Set servo to a given pulse width respecting soft limits.

        Parameters
        ----------
        pulse: int
            Desired pulse width.

        Returns
        -------
        int
            Actual pulse width sent to the servo after clamping.
        """
        clamped = max(self.min_angle, min(self.max_angle, pulse))
        self.position = clamped
        LOGGER.debug("Servo %s set to %s", self.channel, clamped)
        return clamped


class MotorController:
    """High level motor controller for multiple servos.

    This is a minimal stub compatible with the PCA9685 board. Hardware
    communication is intentionally left out so that the module can be
    executed on systems without the hardware attached.
    """

    def __init__(self) -> None:
        self.servos: dict[str, Servo] = {}
        LOGGER.info("Motor controller initialised (stub mode)")

    def register_servo(self, name: str, servo: Servo) -> None:
        """Register a servo under a human readable name."""
        self.servos[name] = servo
        LOGGER.debug("Registered servo %s -> %s", name, servo)

    def move(self, name: str, pulse: int) -> Optional[int]:
        """Move a registered servo.

        Parameters
        ----------
        name: str
            Servo identifier.
        pulse: int
            Desired pulse width.

        Returns
        -------
        Optional[int]
            The clamped pulse width if servo exists else ``None``.
        """
        servo = self.servos.get(name)
        if not servo:
            LOGGER.error("Unknown servo %s", name)
            return None
        return servo.set_position(pulse)

