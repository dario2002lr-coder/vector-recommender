"""Mapper to convert TMDB API data to domain models"""
from vector_recommender.domain.movie import Movie


def tmdb_to_movie(data: dict) -> Movie:
    """Convert TMDB API movie response to Movie domain model.
    
    Args:
        data: Raw movie data from TMDB API
        
    Returns:
        Movie: Domain model instance with mapped data
    """
    return Movie(
        id=data["id"],
        title=data["title"],
        overview=data.get("overview"),
        release_date=data.get("release_date"),
        genres=[g["name"] for g in data.get("genres", [])],
        vote_average=data.get("vote_average"),
        vote_count=data.get("vote_count"),
    )