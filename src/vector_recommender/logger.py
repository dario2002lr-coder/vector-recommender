"""Logging utilities for vector_recommender."""

import logging
import sys

LEVEL_COLORS = {
    "DEBUG": "\033[37m",
    "INFO": "\033[36m",
    "WARNING": "\033[33m",
    "ERROR": "\033[31m",
    "CRITICAL": "\033[41m",
}
RESET_COLOR = "\033[0m"


class ColorFormatter(logging.Formatter):
    """Formatter that applies ANSI color codes to log levels."""

    def __init__(self, fmt: str, datefmt: str | None = None, use_color: bool = True):
        super().__init__(fmt=fmt, datefmt=datefmt)
        self.use_color = use_color and sys.stderr.isatty()

    def format(self, record: logging.LogRecord) -> str:
        if self.use_color and record.levelname in LEVEL_COLORS:
            original_levelname = record.levelname
            record.levelname = f"{LEVEL_COLORS[original_levelname]}{original_levelname}{RESET_COLOR}"
            formatted = super().format(record)
            record.levelname = original_levelname
            return formatted
        return super().format(record)


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Create or retrieve a configured logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = ColorFormatter(
            fmt="%(asctime)s %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
