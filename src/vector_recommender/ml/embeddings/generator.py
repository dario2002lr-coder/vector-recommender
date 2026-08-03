"""Utilities for generating sentence embeddings."""

import numpy as np
from sentence_transformers import SentenceTransformer

from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def generate_embeddings(
    texts: list[str],
    model: SentenceTransformer,
    *,
    show_progress_bar: bool = False,
) -> np.ndarray:
    """Generate normalized embeddings from a list of texts.

    Parameters
    ----------
    texts : list[str]
        List of input texts.
    model : SentenceTransformer
        Loaded SentenceTransformer model.
    show_progress_bar : bool, default=False
        Whether to display the encoding progress bar.

    Returns
    -------
    np.ndarray
        Array containing one embedding per input text.
    """
    if not texts:
        logger.error("No texts were provided.")
        raise ValueError("No texts were provided.")

    logger.info(
        "Generating embeddings for %d texts.",
        len(texts),
    )

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=show_progress_bar,
    )

    logger.info(
        "Generated embeddings with shape %s.",
        embeddings.shape,
    )

    return embeddings