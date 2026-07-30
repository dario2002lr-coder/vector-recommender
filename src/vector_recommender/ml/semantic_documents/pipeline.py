"""Pipeline for generating semantic documents from the TMDB 5000 dataset."""

from config.config import (
    TMDB_5000_PROCESSED_PATH,
    TMDB_5000_SEMANTIC_PATH,
)

from vector_recommender.io.loaders import _load_csv
from vector_recommender.io.savers import save_dataframe
from vector_recommender.logger import get_logger
from vector_recommender.ml.semantic_documents.builders import (
    build_semantic_documents,
)

logger = get_logger(__name__)


def generate_tmdb_5000_semantic_documents():
    """Generate semantic documents for the TMDB 5000 dataset."""

    logger.info("Starting semantic document generation pipeline.")

    # -----------------------------------------------------------------
    # Load processed dataset
    # -----------------------------------------------------------------

    movies_df = _load_csv(
        TMDB_5000_PROCESSED_PATH,
    )

    # -----------------------------------------------------------------
    # Generate semantic documents
    # -----------------------------------------------------------------

    movies_df = build_semantic_documents(
        movies_df,
    )

    # -----------------------------------------------------------------
    # Save dataset
    # -----------------------------------------------------------------

    save_dataframe(
        movies_df,
        TMDB_5000_SEMANTIC_PATH,
    )

    logger.info(
        "Semantic document generation pipeline completed successfully."
    )

    return movies_df


if __name__ == "__main__":
    generate_tmdb_5000_semantic_documents()