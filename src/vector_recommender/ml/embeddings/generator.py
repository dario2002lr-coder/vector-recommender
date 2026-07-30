"""Utilities for generating sentence embeddings."""

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

from config.config import EMBEDDING_MODEL_NAME
from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def generate_embeddings(
    df: pd.DataFrame,
) -> np.ndarray:
    """Generate embeddings from semantic documents."""

    if "semantic_document" not in df.columns:
        logger.error("Column 'semantic_document' not found.")
        raise ValueError("Column 'semantic_document' not found.")

    logger.info(
        "Loading embedding model '%s'.",
        EMBEDDING_MODEL_NAME,
    )

    model = SentenceTransformer(
        EMBEDDING_MODEL_NAME,
    )

    logger.info("Generating embeddings.")

    embeddings = model.encode(
        df["semantic_document"].tolist(),
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    logger.info(
        "Generated embeddings with shape %s.",
        embeddings.shape,
    )

    return embeddings