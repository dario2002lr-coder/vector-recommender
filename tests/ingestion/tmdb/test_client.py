"""Test para validar la conexión y funcionamiento del cliente de TMDB"""
import pytest
from vector_recommender.ingestion.tmdb.client import TMDBClient


class TestTMDBClient:
    """Tests del cliente TMDB"""

    def test_client_initialization(self, tmdb_access_token):
        """Verifica que el cliente se inicialice correctamente"""
        client = TMDBClient(access_token=tmdb_access_token)
        assert client.access_token == tmdb_access_token

    def test_search_movie(self, tmdb_access_token):
        """Prueba búsqueda de película - Verifica conectividad con API"""
        client = TMDBClient(access_token=tmdb_access_token)
        
        # Buscamos una película muy conocida
        result = client.search_movie("The Matrix")
        
        assert "results" in result
        assert len(result["results"]) > 0
        assert any("Matrix" in movie.get("title", "") for movie in result["results"])

    def test_get_movie(self, tmdb_access_token):
        """Prueba obtener detalles de una película específica"""
        client = TMDBClient(access_token=tmdb_access_token)
        
        # The Matrix - ID: 603
        movie_id = 603
        result = client.get_movie(movie_id)
        
        assert result["id"] == movie_id
        assert "title" in result
        assert "overview" in result
