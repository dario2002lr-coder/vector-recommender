"""TMDB API client for movie data retrieval"""
import requests

from vector_recommender.logger import get_logger


logger = get_logger(__name__)


class TMDBClient:
    """Client for interacting with The Movie Database (TMDB) API v3"""
    
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, access_token: str):
        """Initialize the TMDB client with an access token.
        
        Args:
            access_token: TMDB API v4 access token (Bearer token format)
        """
        self.access_token = access_token
        logger.info("TMDBClient initialized")

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        """Make a GET request to the TMDB API.
        
        Args:
            endpoint: API endpoint path (e.g., '/movie/603')
            params: Optional query parameters
            
        Returns:
            dict: JSON response from the API
            
        Raises:
            requests.HTTPError: If the API request fails
        """
        if params is None:
            params = {}

        headers = {"Authorization": f"Bearer {self.access_token}"}

        url = f"{self.BASE_URL}{endpoint}"
        logger.debug("Sending request to TMDB: %s %s", url, params)

        response = requests.get(url, params=params, headers=headers)

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            logger.error("TMDB request failed: %s %s", response.status_code, response.text)
            raise

        logger.info("TMDB request succeeded: %s", endpoint)
        return response.json()

    def get_movie(self, movie_id: int) -> dict:
        """Get detailed information about a specific movie.
        
        Args:
            movie_id: The TMDB movie ID
            
        Returns:
            dict: Movie details from TMDB
        """
        return self._get(f"/movie/{movie_id}")

    def search_movie(self, query: str) -> dict:
        """Search for movies by title.
        
        Args:
            query: Movie title to search for
            
        Returns:
            dict: Search results containing a list of movies
        """
        return self._get("/search/movie", {"query": query})