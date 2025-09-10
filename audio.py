"""Audio playback utilities (stub)."""

from __future__ import annotations

import audioop
import wave
from contextlib import closing
from pathlib import Path
from typing import Optional

from logger import LOGGER


def rms_from_wav(path: str) -> Optional[float]:
    """Return RMS level of a WAV file for lip-sync."""
    try:
        with closing(wave.open(path, "rb")) as wf:
            frames = wf.readframes(wf.getnframes())
            return float(audioop.rms(frames, wf.getsampwidth()))
    except Exception as exc:  # pragma: no cover
        LOGGER.error("Failed to compute RMS: %s", exc)
        return None


def play_mp3(path: str) -> None:
    """Stub MP3 playback function.

    On the real device this would stream audio via an external player.
    Here we only log the event to keep tests light-weight.
    """
    LOGGER.info("Playing MP3: %s", path)

