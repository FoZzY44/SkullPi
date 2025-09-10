"""Vision and face tracking utilities (stub)."""

from __future__ import annotations

from typing import Optional, Tuple

from logger import LOGGER

try:  # pragma: no cover
    import cv2
except Exception:  # pragma: no cover
    cv2 = None  # type: ignore


def capture_frame() -> Optional[Tuple[int, int]]:
    """Capture a single frame and return its dimensions.

    This function serves as a lightweight self-test that the camera can be
    accessed. It returns the width and height if successful.
    """
    if not cv2:
        LOGGER.warning("OpenCV not available")
        return None
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        LOGGER.error("Unable to open camera")
        return None
    ret, frame = cap.read()
    cap.release()
    if not ret:
        LOGGER.error("Failed to capture frame")
        return None
    height, width = frame.shape[:2]
    LOGGER.info("Captured frame %sx%s", width, height)
    return width, height

