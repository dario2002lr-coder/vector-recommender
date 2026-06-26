"""Tests to validate TMDB API client connection and functionality"""
import pytest
from vector_recommender.ingestion.tmdb.client import TMDBClient


class TestTMDBClient:
    """TMDB client tests"""

    def test_client_initialization(self, tmdb_access_token):
        """Verify that the client initializes correctly"""
        client = TMDBClient(access_token=tmdb_access_token)
        assert client.access_token == tmdb_access_token

    def test_search_movie(self, tmdb_access_token):
        """Test movie search - Verify API connectivity"""
        client = TMDBClient(access_token=tmdb_access_token)
        
        # Search for a well-known movie
        result = client.search_movie("The Matrix")
        
        assert "results" in result
        assert len(result["results"]) > 0
        assert any("Matrix" in movie.get("title", "") for movie in result["results"])

    def test_get_movie(self, tmdb_access_token):
        """Test getting details of a specific movie"""
        client = TMDBClient(access_token=tmdb_access_token)
        
        # The Matrix - ID: 603
        movie_id = 603
        result = client.get_movie(movie_id)
        
        assert result["id"] == movie_id
        assert "title" in result
        assert "overview" in result
