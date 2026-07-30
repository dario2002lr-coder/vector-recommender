"""Pipeline for processing the TMDB 5000 dataset."""

from vector_recommender.logger import get_logger
from vector_recommender.processing.tmdb_5000_dataset.features import (
    compute_weighted_rating,
    create_profit_feature,
    extract_release_features,
)
from vector_recommender.processing.tmdb_5000_dataset.loaders import load_tmdb_5000
from vector_recommender.processing.tmdb_5000_dataset.merge import (
    merge_movies_and_credits,
)
from vector_recommender.processing.tmdb_5000_dataset.savers import save_processed_tmdb_5000
from vector_recommender.processing.tmdb_5000_dataset.utilities import (
    convert_to_datetime,
    replace_zero_with_nan,
)

def process_tmdb_5000() -> None:
    """Process the TMDB 5000 dataset."""
    logger = get_logger(__name__)

    logger.info("Loading TMDB 5000 datasets...")
    movies_df, credits_df = load_tmdb_5000()

    logger.info("Merging datasets...")
    merged_df = merge_movies_and_credits(movies_df, credits_df)

    logger.info("Replacing zero values with NaN...")
    merged_df = replace_zero_with_nan(
        merged_df,
        columns=["budget", "revenue", "vote_average", "vote_count"],
    )

    logger.info("Converting 'release_date' to datetime...")
    merged_df = convert_to_datetime(merged_df, column="release_date")

    logger.info("Extracting release features...")
    merged_df = extract_release_features(merged_df)

    logger.info("Creating profit feature...")
    merged_df = create_profit_feature(merged_df)

    logger.info("Computing weighted rating...")
    merged_df = compute_weighted_rating(merged_df)

    logger.info("Saving processed dataset...")
    save_processed_tmdb_5000(merged_df)

    logger.info("TMDB 5000 dataset processing complete.")
    logger.debug("Processed dataset preview:\n%s", merged_df.head())
    logger.debug("Processed dataset info:\n%s", merged_df.info())

if __name__ == "__main__":
    process_tmdb_5000()