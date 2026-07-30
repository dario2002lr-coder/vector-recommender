"""Utilities for building semantic movie documents."""

import pandas as pd

from vector_recommender.logger import get_logger
from vector_recommender.ml.semantic_documents.text_utils import (
    clean_text,
    format_list,
)
from vector_recommender.ml.semantic_documents.utilities import (
    extract_field,
    parse_tmdb_json_list,
)

logger = get_logger(__name__)

def build_semantic_document(
    row: pd.Series,
) -> str:
    """Build a semantic document describing a movie."""

    title = clean_text(row["title"])
    overview = clean_text(row["overview"])
    tagline = clean_text(row["tagline"])

    genres = extract_field(
        parse_tmdb_json_list(row["genres"]),
        "name",
    )

    keywords = extract_field(
        parse_tmdb_json_list(row["keywords"]),
        "name",
    )

    parts = []

    if title:
        if genres:
            parts.append(
                f"{title} is a {format_list(genres)} movie."
            )
        else:
            parts.append(title)

    if overview:
        parts.append(
            f"Overview:\n{overview}"
        )

    if keywords:
        parts.append(
            f"The movie explores themes such as {format_list(keywords)}."
        )

    if tagline:
        parts.append(
            f'Tagline:\n"{tagline}"'
        )

    return "\n\n".join(parts)

def build_semantic_documents(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Generate semantic documents for all movies."""

    logger.info("Generating semantic documents.")

    df = df.copy()

    df["semantic_document"] = df.apply(
        build_semantic_document,
        axis=1,
    )

    logger.info(
        "Generated semantic documents for %d movies.",
        len(df),
    )

    return df