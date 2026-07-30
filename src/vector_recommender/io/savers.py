"""Utilities for saving data."""

from pathlib import Path

import numpy as np
import pandas as pd

from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def save_dataframe(
    df: pd.DataFrame,
    path: Path,
    *,
    index: bool = False,
) -> None:
    """Save a DataFrame as a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save.
    path : Path
        Destination path.
    index : bool, default=False
        Whether to save the DataFrame index.
    """
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info(
        "Saving DataFrame to '%s'.",
        path,
    )

    df.to_csv(
        path,
        index=index,
    )

    logger.info("DataFrame saved successfully.")

def save_numpy_array(
    array: np.ndarray,
    path: Path,
) -> None:
    """Save a NumPy array."""

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info(
        "Saving NumPy array to '%s'.",
        path,
    )

    np.save(
        path,
        array,
    )

    logger.info("NumPy array saved successfully.")