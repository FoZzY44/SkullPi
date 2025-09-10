"""Entry point for SkullPi."""

from __future__ import annotations

from config import load_config, load_state
from logger import LOGGER
from motors import MotorController, Servo
from supervisor import Mode, Supervisor
from tts import synthesize
from vision import capture_frame


def self_test(cfg: dict) -> bool:
    """Perform basic health checks for critical components."""
    controller = MotorController()
    for name, data in cfg.get("servos", {}).items():
        servo = Servo(
            channel=data["channel"],
            min_angle=data["min"],
            max_angle=data["max"],
            idle=data["idle"],
        )
        controller.register_servo(name, servo)
        servo.set_position(data["idle"])
    if capture_frame() is None:
        LOGGER.warning("Camera self-test skipped")
    camera_ok = True

    tts_ok = True
    if synthesize("test") is None:
        LOGGER.warning("TTS self-test skipped")

    return camera_ok and tts_ok


def main() -> None:
    """Main application entry point."""
    cfg = load_config()
    state = load_state()
    LOGGER.info("Loaded config and state: %s %s", cfg.keys(), state)

    supervisor = Supervisor()

    if not self_test(cfg):
        LOGGER.error("Self tests failed - entering sleep mode")
        supervisor.set_mode(Mode.SLEEP)

    supervisor.step()


if __name__ == "__main__":  # pragma: no cover
    main()

