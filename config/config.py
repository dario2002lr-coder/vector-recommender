from pathlib import Path

# --------------------------------- PATHS --------------------------------- #
PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT/"data"
RAW_DATA_DIR = DATA_DIR/"raw"
PROCESSED_DATA_DIR = DATA_DIR/"processed"

TMDB_5000_DATASET_DIR = RAW_DATA_DIR/"tmdb_5000_movie_dataset"
TMDB_5000_PROCESSED_DIR = PROCESSED_DATA_DIR/"tmdb_5000_movie_dataset"

TMDB_5000_CREDITS_PATH = TMDB_5000_DATASET_DIR/"tmdb_5000_credits.csv"
TMDB_5000_MOVIES_PATH = TMDB_5000_DATASET_DIR/"tmdb_5000_movies.csv"
TMDB_5000_PROCESSED_PATH = TMDB_5000_PROCESSED_DIR/"tmdb_5000_processed.csv"
TMDB_5000_SEMANTIC_PATH = TMDB_5000_PROCESSED_DIR/"tmdb_5000_semantic.csv"
TMDB_5000_EMBEDDINGS_PATH = TMDB_5000_PROCESSED_DIR/"movie_embeddings.npy"

# --------------------------------- FEATURE ENGINEERING --------------------------------- #
WEIGHTED_RATING_VOTE_COUNT_PERCENTILE = 0.10

#-------------------------------- EMBEDDING MODEL --------------------------------- #
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"