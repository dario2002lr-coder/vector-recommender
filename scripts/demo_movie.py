import argparse
import os
import sys
from pathlib import Path

# Ensure src is on the import path when running from project root.
ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from dotenv import load_dotenv
from vector_recommender.ingestion.tmdb.client import TMDBClient
from vector_recommender.ingestion.tmdb.service import TMDBService
from vector_recommender.logger import get_logger

logger = get_logger("demo_movie")


def load_env() -> None:
    load_dotenv(ROOT / ".env")


def get_access_token() -> str:
    token = os.getenv("TMDB_ACCESS_TOKEN")
    if not token or token == "your_tmdb_access_token_here":
        raise RuntimeError(
            "TMDB_ACCESS_TOKEN is not configured. Please set it in .env."
        )
    return token


def run_demo(query: str = "The Matrix") -> None:
    logger.info("Starting TMDB demo")
    token = get_access_token()

    client = TMDBClient(access_token=token)
    service = TMDBService(client=client)

    logger.info("Searching for movie: %s", query)
    search_results = client.search_movie(query)
    if not search_results.get("results"):
        logger.warning("No results found for query: %s", query)
        return

    first_movie = search_results["results"][0]
    movie_id = first_movie["id"]
    logger.info("Found movie id=%s title=%s", movie_id, first_movie.get("title"))

    logger.info("Fetching full details for movie id=%s", movie_id)
    movie = service.get_movie(movie_id)

    print("\n=== Movie object ===")
    print(movie.model_dump_json(indent=2))
    print("\n=== Movie attributes ===")
    print(f"ID: {movie.id}")
    print(f"Title: {movie.title}")
    print(f"Overview: {movie.overview}")
    print(f"Release date: {movie.release_date}")
    print(f"Genres: {movie.genres}")
    print(f"Genre IDs: {movie.genre_ids}")
    print(f"Poster path: {movie.poster_path}")
    print(f"Backdrop path: {movie.backdrop_path}")
    print(f"Adult: {movie.adult}")
    print(f"Original title: {movie.original_title}")
    print(f"Original language: {movie.original_language}")
    print(f"Popularity: {movie.popularity}")
    print(f"Video: {movie.video}")
    print(f"Vote average: {movie.vote_average}")
    print(f"Vote count: {movie.vote_count}")

    logger.info("Demo completed successfully")


def parse_args() -> str:
    parser = argparse.ArgumentParser(
        description="Run a TMDB movie demo and print the mapped Movie object."
    )
    parser.add_argument(
        "title",
        nargs="?",
        default="The Matrix",
        help="Movie title to search for (default: 'The Matrix')",
    )
    args = parser.parse_args()
    return args.title


if __name__ == "__main__":
    load_env()
    query = parse_args()
    run_demo(query=query)

