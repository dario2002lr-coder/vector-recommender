"""Mapper to convert TMDB API data to domain models"""
from vector_recommender.domain.movie import Movie


def tmdb_to_movie(data: dict) -> Movie:
    """Convert TMDB API movie response to Movie domain model.

    Args:
        data: Raw movie data from TMDB API

    Returns:
        Movie: Domain model instance with mapped data
    """
    genre_ids = data.get("genre_ids")
    if genre_ids is None:
        genre_ids = [genre["id"] for genre in data.get("genres", []) if "id" in genre]

    return Movie(
        id=data["id"],
        title=data["title"],
        overview=data.get("overview"),
        release_date=data.get("release_date"),
        genres=[g["name"] for g in data.get("genres", [])],
        genre_ids=genre_ids,
        poster_path=data.get("poster_path"),
        backdrop_path=data.get("backdrop_path"),
        adult=data.get("adult"),
        original_title=data.get("original_title"),
        original_language=data.get("original_language"),
        popularity=data.get("popularity"),
        video=data.get("video"),
        vote_average=data.get("vote_average"),
        vote_count=data.get("vote_count"),
    )