""" Utilities for processing TMDB datasets """

import numpy as np
import pandas as pd

from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def replace_zero_with_nan(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """Replace zero values with NaN in the specified columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    columns : list[str]
        Columns where zeros should be interpreted as missing values.

    Returns
    -------
    pd.DataFrame
        DataFrame with the specified columns processed.
    """
    df = df.copy()

    for column in columns:
        if column not in df.columns:
            logger.warning("Column '%s' not found. Skipping.", column)
            continue

        replaced = (df[column] == 0).sum()

        if replaced:
            logger.info(
                "Replacing %d zero values with NaN in '%s'.",
                replaced,
                column,
            )

        df[column] = df[column].replace(0, np.nan)

    return df

def convert_to_datetime(
    df: pd.DataFrame,
    column: str,
) -> pd.DataFrame:
    """Convert a DataFrame column to datetime.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    column : str
        Name of the column to convert.

    Returns
    -------
    pd.DataFrame
        DataFrame with the converted column.

    Raises
    ------
    ValueError
        If the column does not exist.
    """
    if column not in df.columns:
        logger.error("Column '%s' not found.", column)
        raise ValueError(f"Column '{column}' not found.")

    logger.info("Converting '%s' to datetime.", column)

    df = df.copy()
    df[column] = pd.to_datetime(df[column], errors="coerce")

    return df