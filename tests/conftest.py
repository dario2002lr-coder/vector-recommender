"""Configuración compartida para tests"""
import os
import pytest
from dotenv import load_dotenv

# Cargar variables de entorno para tests
load_dotenv(".env")


@pytest.fixture
def tmdb_access_token():
    """Fixture para obtener el token de acceso de TMDB"""
    token = os.getenv("TMDB_ACCESS_TOKEN")
    if not token or token == "your_tmdb_access_token_here":
        pytest.skip("TMDB_ACCESS_TOKEN no configurado en .env")
    return token
