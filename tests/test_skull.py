import pytest
from motors import Servo


def test_servo_respects_soft_limits():
    servo = Servo(channel=0, min_angle=100, max_angle=500, idle=300)

    assert servo.set_position(300) == 300
    assert servo.set_position(50) == 100
    assert servo.set_position(600) == 500

