"""Feature engineering utilities for TMDB datasets."""

import pandas as pd
from config.config import WEIGHTED_RATING_VOTE_COUNT_PERCENTILE
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

def create_profit_feature(
        df: pd.DataFrame,
) -> pd.DataFrame:
    """Create a profit feature from revenue and budget."""

    if "revenue" not in df.columns or "budget" not in df.columns:
        logger.error("Columns 'revenue' and/or 'budget' not found.")
        raise ValueError("Columns 'revenue' and/or 'budget' not found.")

    logger.info("Creating profit feature.")

    df = df.copy()

    df["profit"] = df["revenue"] - df["budget"]

    logger.info("Created feature: 'profit'.")
    logger.debug(df[["revenue", "budget", "profit"]].head())

def compute_weighted_rating(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Compute the IMDb weighted rating.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    pd.DataFrame
        DataFrame with the new ``weighted_rating`` column.
    """
    required_columns = {
        "vote_average",
        "vote_count",
    }

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        logger.error(
            "Missing required columns: %s",
            ", ".join(sorted(missing_columns)),
        )
        raise ValueError(
            f"Missing required columns: {', '.join(sorted(missing_columns))}"
        )

    logger.info("Computing weighted rating.")

    df = df.copy()

    c = df["vote_average"].mean()
    m = df["vote_count"].quantile(
        WEIGHTED_RATING_VOTE_COUNT_PERCENTILE
    )

    logger.info(
        "Minimum vote threshold (percentile %.2f): %.0f",
        WEIGHTED_RATING_VOTE_COUNT_PERCENTILE,
        m,
    )