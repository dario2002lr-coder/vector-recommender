"""Utilities for saving processed datasets."""

import pandas as pd

from config.config import TMDB_5000_PROCESSED_PATH
from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def save_processed_tmdb_5000(
    df: pd.DataFrame,
) -> None:
    """Save the processed TMDB 5000 dataset."""

    TMDB_5000_PROCESSED_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info(
        "Saving processed dataset to '%s'.",
        TMDB_5000_PROCESSED_PATH,
    )

    df.to_csv(
        TMDB_5000_PROCESSED_PATH,
        index=False,
    )

    logger.info("Processed dataset saved successfully.")