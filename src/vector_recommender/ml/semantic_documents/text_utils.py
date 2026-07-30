"""Text utilities for semantic document generation."""

import pandas as pd


def clean_text(value: object) -> str | None:
    """Return a cleaned string or ``None`` if the value is missing."""

    if pd.isna(value):
        return None

    value = str(value).strip()

    return value or None


def format_list(items: list[str]) -> str | None:
    """Format a list into a natural language string."""

    if not items:
        return None

    if len(items) == 1:
        return items[0]

    if len(items) == 2:
        return f"{items[0]} and {items[1]}"

    return f"{', '.join(items[:-1])} and {items[-1]}"