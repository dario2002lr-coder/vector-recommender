""" Utilities for loading TMBD datasets """

from pathlib import Path

import pandas as pd

from config.config import TMDB_5000_CREDITS_PATH, TMDB_5000_MOVIES_PATH
from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def _load_csv(path: Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.
    """
    if not path.exists():
        logger.error("File not found: %s", path)
        raise FileNotFoundError(f"File not found: {path}")

    logger.info("Loading dataset: %s", path.name)

    df = pd.read_csv(path)

    logger.info(
        "Loaded %s (%d rows, %d columns).",
        path.name,
        len(df),
        len(df.columns),
    )

    return df

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