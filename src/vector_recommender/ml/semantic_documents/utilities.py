"""Utilities for semantic movie documents."""

from __future__ import annotations
import pandas as pd
import ast
from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def extract_field(
    items: list[dict],
    field: str,
) -> list[str]:
    """Extract a field from a list of dictionaries."""

    return [
        item[field]
        for item in items
        if field in item
    ]

def parse_tmdb_json_list(value: object) -> list[dict]:
    """Parse a TMDB JSON-like string into a list of dictionaries."""

    if pd.isna(value):
        return []

    value = str(value).strip()

    if not value or value == "[]":
        return []

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError, TypeError):
        logger.warning("Failed to parse TMDB JSON list.")
        return []