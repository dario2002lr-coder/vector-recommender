"""Utilities for saving processed datasets."""

import pandas as pd

from config.config import TMDB_5000_PROCESSED_PATH
from vector_recommender.logger import get_logger
from vector_recommender.io.savers import save_dataframe

logger = get_logger(__name__)


def save_processed_tmdb_5000(
    df: pd.DataFrame,
) -> None:
    """Save the processed TMDB 5000 dataset."""
    save_dataframe(
        df,
        TMDB_5000_PROCESSED_PATH,
        index=False,
    )