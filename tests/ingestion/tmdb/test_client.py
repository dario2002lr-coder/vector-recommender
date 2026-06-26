"""Tests to validate TMDB API client connection and functionality"""
import pytest
from vector_recommender.ingestion.tmdb.client import TMDBClient


class TestTMDBClient:
    """TMDB client tests"""

    def test_client_initialization(self, tmdb_access_token, logger):
        """Verify that the client initializes correctly"""
        logger.info("Starting test_client_initialization")
        client = TMDBClient(access_token=tmdb_access_token)
        assert client.access_token == tmdb_access_token

    def test_search_movie(self, tmdb_access_token, logger):
        """Test movie search - Verify API connectivity"""
        logger.info("Starting test_search_movie")
        client = TMDBClient(access_token=tmdb_access_token)
        
        # Search for a well-known movie
        result = client.search_movie("The Matrix")
        
        assert "results" in result
        assert len(result["results"]) > 0
        assert any("Matrix" in movie.get("title", "") for movie in result["results"])

    def test_get_movie(self, tmdb_access_token, logger):
        """Test getting details of a specific movie"""
        logger.info("Starting test_get_movie")
        client = TMDBClient(access_token=tmdb_access_token)
        
        # The Matrix - ID: 603
        movie_id = 603
        result = client.get_movie(movie_id)
        
        assert result["id"] == movie_id
        assert "title" in result
        assert "overview" in result
