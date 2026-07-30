"""Utilities for safely merging TMDB datasets."""

import pandas as pd

from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def merge_movies_and_credits(
    movies_df: pd.DataFrame,
    credits_df: pd.DataFrame,
) -> pd.DataFrame:
    """Safely merge the TMDB movies and credits datasets.

    Parameters
    ----------
    movies_df : pd.DataFrame
        Movies dataset.
    credits_df : pd.DataFrame
        Credits dataset.

    Returns
    -------
    pd.DataFrame
        Merged dataset.

    Raises
    ------
    ValueError
        If the titles associated with the same movie id differ between
        the two datasets.
    """

    logger.info("Preparing credits dataset for merge...")

    credits_df = credits_df.rename(columns={"movie_id": "id"}).copy()

    logger.info("Validating title consistency between datasets...")

    title_check = movies_df.merge(
        credits_df[["id", "title"]],
        on="id",
        how="inner",
        suffixes=("_movies", "_credits"),
    )

    inconsistent_titles = title_check[
        title_check["title_movies"] != title_check["title_credits"]
    ]

    if not inconsistent_titles.empty:
        logger.error(
            "%d title mismatches detected between movies and credits datasets.",
            len(inconsistent_titles),
        )

        logger.error(
            "First mismatched ids: %s",
            inconsistent_titles["id"].head().tolist(),
        )

        raise ValueError(
            "Movies and credits datasets contain inconsistent titles."
        )

    logger.info("Title consistency validation passed.")

    logger.info("Merging datasets...")

    merged_df = movies_df.merge(
        credits_df[["id", "cast", "crew"]],
        on="id",
        how="inner",
    )

    logger.info(
        "Merge completed successfully (%d rows, %d columns).",
        len(merged_df),
        len(merged_df.columns),
    )

    return merged_df