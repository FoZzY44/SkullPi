# SkullPi

Prototype modular code base for the interactive SkullPi robot. The project
runs on a Raspberry Pi and is split into multiple small modules so that each
hardware component can be developed and tested independently.

## Requirements

- Python 3.9+
- ``espeak-ng`` for Text-to-Speech
- Optional: OpenCV, Vosk, RPi.GPIO, OpenAI Python package

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install flask
```

Additional libraries like ``opencv-python`` or ``openai`` can be installed
when running on the Raspberry Pi.

## Running

To start the demo application:

```bash
python main.py
```

A small web interface is available at ``http://<pi>:5000`` and exposes a
``/move`` endpoint for servo control.

## Tests

Unit tests are located in ``tests`` and can be run with ``pytest``:

```bash
pytest
```

## Configuration

Runtime configuration is stored in ``config.json``. Templates with predefined
phrases and idle motions are located in ``templates/``.

