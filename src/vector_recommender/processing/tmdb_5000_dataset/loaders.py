""" Utilities for loading TMBD datasets """

from pathlib import Path

import pandas as pd

from vector_recommender.io.loaders import _load_csv
from config.config import TMDB_5000_CREDITS_PATH, TMDB_5000_MOVIES_PATH
from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def load_tmdb_5000_movies() -> pd.DataFrame:
    """Load the TMDB 5000 movies dataset."""
    return _load_csv(TMDB_5000_MOVIES_PATH)


def load_tmdb_5000_credits() -> pd.DataFrame:
    """Load the TMDB 5000 credits dataset."""
    return _load_csv(TMDB_5000_CREDITS_PATH)


def load_tmdb_5000() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the complete TMDB 5000 dataset.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame]
        Movies and credits DataFrames.
    """
    logger.info("Loading TMDB 5000 dataset...")

    movies_df = load_tmdb_5000_movies()
    credits_df = load_tmdb_5000_credits()

    logger.info("TMDB 5000 dataset loaded successfully.")

    return movies_df, credits_df