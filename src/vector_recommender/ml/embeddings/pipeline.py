"""Pipeline for generating movie embeddings."""

from config.config import (
    TMDB_5000_EMBEDDINGS_PATH,
    TMDB_5000_SEMANTIC_PATH,
)

from vector_recommender.ml.embeddings.generator import (
    generate_embeddings,
)
from vector_recommender.io.loaders import _load_csv
from vector_recommender.io.savers import save_numpy_array
from vector_recommender.logger import get_logger

logger = get_logger(__name__)


def generate_tmdb_5000_embeddings():
    """Generate embeddings for the TMDB 5000 dataset."""

    logger.info("Starting embedding generation pipeline.")

    movies_df = _load_csv(
        TMDB_5000_SEMANTIC_PATH,
    )

    embeddings = generate_embeddings(
        movies_df,
    )

    save_numpy_array(
        embeddings,
        TMDB_5000_EMBEDDINGS_PATH,
    )

    logger.info(
        "Embedding generation pipeline completed successfully."
    )

    return embeddings


if __name__ == "__main__":
    generate_tmdb_5000_embeddings()