"""Speech-to-Text utilities using Vosk (stub)."""

from __future__ import annotations

from typing import Optional

from logger import LOGGER


def transcribe(audio_path: str) -> Optional[str]:
    """Transcribe an audio file and return the recognised text.

    This is a lightweight stub that always returns ``None`` because the
    heavy Vosk model is not bundled. The function logs the access and can
    be expanded on a real Raspberry Pi installation.
    """
    LOGGER.info("Transcription requested for %s", audio_path)
    return None

