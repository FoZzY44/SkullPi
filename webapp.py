"""Minimal Flask web interface."""

from __future__ import annotations

from flask import Flask, jsonify, request

from logger import LOGGER
from motors import MotorController, Servo

app = Flask(__name__)
controller = MotorController()


@app.route("/move", methods=["POST"])
def move() -> tuple[str, int]:
    """Move a servo via HTTP POST.

    Expected JSON body::

        {"name": "jaw", "pulse": 300}
    """
    data = request.get_json(force=True)
    name = data.get("name")
    pulse = int(data.get("pulse", 0))
    result = controller.move(name, pulse)
    if result is None:
        return jsonify({"error": "unknown servo"}), 400
    return jsonify({"pulse": result}), 200


def run(host: str = "0.0.0.0", port: int = 5000) -> None:
    """Run the Flask development server."""
    LOGGER.info("Starting web application on %s:%s", host, port)
    app.run(host=host, port=port)


if __name__ == "__main__":  # pragma: no cover
    run()

