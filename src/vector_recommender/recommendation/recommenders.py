"""Movie recommendation utilities."""

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

from vector_recommender.logger import get_logger
from vector_recommender.ml.embeddings.generator import (
    generate_embeddings,
)
from vector_recommender.recommendation.search import (
    search_similar_embeddings,
)

logger = get_logger(__name__)


def recommend_movies(
    query: str,
    movies_df: pd.DataFrame,
    embeddings: np.ndarray,
    model: SentenceTransformer,
    top_k: int,
) -> pd.DataFrame:
    """Recommend movies based on a natural language query.

    Parameters
    ----------
    query : str
        User query.
    movies_df : pd.DataFrame
        Movie metadata.
    embeddings : np.ndarray
        Movie embeddings.
    model : SentenceTransformer
        Loaded embedding model.
    top_k : int, default=10
        Number of recommendations.

    Returns
    -------
    pd.DataFrame
        Recommended movies ordered by semantic similarity.
    """
    if len(movies_df) != embeddings.shape[0]:
        logger.error(
            "Movies dataframe and embedding matrix have different sizes."
        )
        raise ValueError(
            "Movies dataframe and embedding matrix have different sizes."
        )

    logger.info(
        "Generating recommendations for query: '%s'.",
        query,
    )

    query_embedding = generate_embeddings(
        texts=[query],
        model=model,
    )

    top_indices, similarities = search_similar_embeddings(
        query_embedding=query_embedding,
        embeddings=embeddings,
        top_k=top_k,
    )

    results = movies_df.iloc[top_indices][
        [
            "title",
            "release_year",
            "genres",
            "vote_average",
            "weighted_rating",
        ]
    ].copy()

    results["similarity"] = similarities

    logger.info(
        "Generated %d recommendations.",
        len(results),
    )

    return results