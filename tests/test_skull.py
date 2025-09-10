import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from motors import Servo
from main import self_test


def test_self_test_skips_camera(monkeypatch):
    monkeypatch.setattr("main.capture_frame", lambda: None)
    monkeypatch.setattr("main.synthesize", lambda text: 1.0)
    cfg = {"servos": {}}
    assert self_test(cfg) is True


def test_self_test_skips_tts(monkeypatch):
    monkeypatch.setattr("main.capture_frame", lambda: (640, 480))
    monkeypatch.setattr("main.synthesize", lambda text: None)
    cfg = {"servos": {}}
    assert self_test(cfg) is True


def test_servo_respects_soft_limits():
    servo = Servo(channel=0, min_angle=100, max_angle=500, idle=300)

    assert servo.set_position(300) == 300
    assert servo.set_position(50) == 100
    assert servo.set_position(600) == 500

