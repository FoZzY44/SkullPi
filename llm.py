"""Interface to language models (OpenAI API)."""

from __future__ import annotations

import os
from typing import Optional

from logger import LOGGER

try:  # pragma: no cover - optional dependency
    import openai
except Exception:  # pragma: no cover
    openai = None  # type: ignore


def ask(prompt: str, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo") -> str:
    """Send a prompt to OpenAI and return the response text.

    If the API key or the library is not available, a canned response is
    returned to keep the application running in offline mode.
    """
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not openai or not key:
        LOGGER.warning("LLM not available, returning canned response")
        return "Je ne peux pas répondre pour le moment."

    openai.api_key = key
    try:
        resp = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}])
        return resp.choices[0].message["content"].strip()
    except Exception as exc:  # pragma: no cover
        LOGGER.error("LLM request failed: %s", exc)
        return "Erreur de génération."  # noqa: D401

