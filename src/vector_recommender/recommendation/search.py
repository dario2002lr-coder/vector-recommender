"""Utilities for semantic search."""

import numpy as np

from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def search_similar_embeddings(
    query_embedding: np.ndarray,
    embeddings: np.ndarray,
    top_k: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Search the most similar embeddings.

    Parameters
    ----------
    query_embedding : np.ndarray
        Query embedding.
    embeddings : np.ndarray
        Embedding matrix.
    top_k : int, default=10
        Number of results to return.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Indices of the most similar embeddings and their similarities.
    """
    if top_k <= 0:
        logger.error("top_k must be greater than zero.")
        raise ValueError("top_k must be greater than zero.")

    if embeddings.shape[0] == 0:
        logger.error("Embedding matrix is empty.")
        raise ValueError("Embedding matrix is empty.")

    logger.info(
        "Searching top %d similar embeddings.",
        top_k,
    )

    # Cosine similarity because all embeddings are normalized
    similarities = (
        embeddings @ query_embedding.ravel()
    )

    top_indices = np.argsort(
        similarities
    )[::-1][:top_k]

    logger.info("Semantic search completed.")

    return top_indices, similarities[top_indices]