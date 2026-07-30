""" Utilities for loading processed TMDB dataset """

from pathlib import Path

import pandas as pd

from vector_recommender.io.loaders import _load_csv
from config.config import TMDB_5000_PROCESSED_PATH
from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def load_processed_tmdb_5000() -> pd.DataFrame:
    """Load the processed TMDB 5000 dataset."""
    return _load_csv(TMDB_5000_PROCESSED_PATH)