"""Movie domain model"""
from pydantic import BaseModel


class Movie(BaseModel):
    """Domain model representing a movie with its metadata."""

    id: int
    title: str
    overview: str | None = None
    release_date: str | None = None
    genres: list[str] = []
    genre_ids: list[int] | None = None
    poster_path: str | None = None
    backdrop_path: str | None = None
    adult: bool | None = None
    original_title: str | None = None
    original_language: str | None = None
    popularity: float | None = None
    video: bool | None = None
    vote_average: float | None = None
    vote_count: int | None = None