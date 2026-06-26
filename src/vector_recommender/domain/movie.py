"""Movie domain model"""
from pydantic import BaseModel


class Movie(BaseModel):
    """Domain model representing a movie with its metadata"""
    
    id: int
    title: str
    overview: str | None = None
    release_date: str | None = None
    genres: list[str] = []
    vote_average: float | None = None
    vote_count: int | None = None