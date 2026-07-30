"""Utilities for loading embedding models."""

from sentence_transformers import SentenceTransformer

from vector_recommender.logger import get_logger

logger = get_logger(__name__)

def load_embedding_model(
    model_name: str,
) -> SentenceTransformer:
    """Load a SentenceTransformer model.

    Parameters
    ----------
    model_name : str
        Name of the model to load.

    Returns
    -------
    SentenceTransformer
        Loaded embedding model.
    """
    logger.info(
        "Loading embedding model '%s'.",
        model_name,
    )

    model = SentenceTransformer(model_name)

    logger.info("Embedding model loaded successfully.")

    return model