"""Service layer for TMDB movie data ingestion"""
from .mapper import tmdb_to_movie


class TMDBService:
    """High-level service for managing TMDB API interactions"""
    
    def __init__(self, client):
        """Initialize the TMDB service.
        
        Args:
            client: TMDBClient instance
        """
        self.client = client

    def get_movie(self, movie_id: int):
        """Retrieve and map a single movie by ID.
        
        Args:
            movie_id: The TMDB movie ID
            
        Returns:
            Movie: Domain model with movie details
        """
        data = self.client.get_movie(movie_id)
        return tmdb_to_movie(data)

    def search_movie(self, query: str):
        """Search for movies and return raw results.
        
        Args:
            query: Movie title to search for
            
        Returns:
            list: Search results
        """
        data = self.client.search_movie(query)
        return data["results"]