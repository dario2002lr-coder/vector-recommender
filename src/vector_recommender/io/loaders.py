""" Utilities for loading TMBD datasets """

from pathlib import Path

import pandas as pd

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