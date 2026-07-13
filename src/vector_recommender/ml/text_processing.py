"""Text preprocessing helpers for semantic movie representations."""

from __future__ import annotations

from typing import Any

import pandas as pd


def build_semantic_document(row: pd.Series) -> str:
    """Create a semantic textual document for a movie row."""
    title = _clean_text(row.get("title"))
    genres = _clean_text(row.get("genres"))
    overview = _clean_text(row.get("overview"))
    keywords = _clean_text(row.get("keywords"))
    tagline = _clean_text(row.get("tagline"))

    parts = [part for part in [title, genres, overview, keywords, tagline] if part]
    return ". ".join(parts)


def _clean_text(value: Any) -> str:
    """Normalize a value into a readable text fragment."""
    if pd.isna(value):
        return ""

    if isinstance(value, list):
        return ", ".join(str(item) for item in value)

    if isinstance(value, str):
        text = value.strip()
        return text if text else ""

    return str(value)
