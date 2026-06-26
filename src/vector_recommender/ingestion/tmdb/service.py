"""Service layer for TMDB movie data ingestion"""
from .mapper import tmdb_to_movie
from vector_recommender.logger import get_logger


logger = get_logger(__name__)


class TMDBService:
    """High-level service for managing TMDB API interactions"""
    
    def __init__(self, client):
        """Initialize the TMDB service.
        
        Args:
            client: TMDBClient instance
        """
        self.client = client
        logger.info("TMDBService initialized")

    def get_movie(self, movie_id: int):
        """Retrieve and map a single movie by ID.
        
        Args:
            movie_id: The TMDB movie ID
            
        Returns:
            Movie: Domain model with movie details
        """
        logger.debug("Fetching movie with id=%s", movie_id)
        data = self.client.get_movie(movie_id)
        movie = tmdb_to_movie(data)
        logger.info("Fetched movie %s", movie.title)
        return movie

    def search_movie(self, query: str):
        """Search for movies and return raw results.
        
        Args:
            query: Movie title to search for
            
        Returns:
            list: Search results
        """
        logger.debug("Searching TMDB for query=%s", query)
        data = self.client.search_movie(query)
        results = data["results"]
        logger.info("Search returned %s results for query=%s", len(results), query)
        return results