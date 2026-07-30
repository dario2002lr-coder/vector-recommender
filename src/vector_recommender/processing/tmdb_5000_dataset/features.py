"""Feature engineering utilities for TMDB datasets."""

import pandas as pd

from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def extract_release_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Extract release year and month from the release date."""

    if "release_date" not in df.columns:
        logger.error("Column 'release_date' not found.")
        raise ValueError("Column 'release_date' not found.")

    logger.info("Extracting release date features.")

    df = df.copy()

    df["release_year"] = df["release_date"].dt.year
    df["release_month"] = df["release_date"].dt.month

    logger.info(
        "Created features: 'release_year' and 'release_month'."
    )

    return df