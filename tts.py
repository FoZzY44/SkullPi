"""Simple Text-to-Speech wrapper using ``espeak-ng``."""

from __future__ import annotations

import audioop
import subprocess
import wave
from contextlib import closing
from pathlib import Path
from typing import Optional

from logger import LOGGER

TMP_WAV = Path("tts_output.wav")


def synthesize(text: str, voice: str = "fr+m3") -> Optional[float]:
    """Synthesize *text* into a WAV file and return its RMS value.

    The RMS can be used to drive the jaw servo for basic lip-sync.

    Parameters
    ----------
    text: str
        Sentence to speak.
    voice: str, default ``"fr+m3"``
        Voice to use with ``espeak-ng``.

    Returns
    -------
    Optional[float]
        Root mean square of the generated audio or ``None`` on failure.
    """
    cmd = ["espeak-ng", "-v", voice, "-w", str(TMP_WAV), text]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as exc:  # pragma: no cover - fails if espeak absent
        LOGGER.error("TTS synthesis failed: %s", exc)
        return None

    try:
        with closing(wave.open(str(TMP_WAV), "rb")) as wf:
            frames = wf.readframes(wf.getnframes())
            rms = audioop.rms(frames, wf.getsampwidth())
            LOGGER.info("Synthesised %s with RMS=%s", text, rms)
            return float(rms)
    except Exception as exc:  # pragma: no cover
        LOGGER.error("Failed to analyse wav: %s", exc)
        return None

