"""Shared configuration for tests"""
import os
import pytest
from dotenv import load_dotenv

# Load environment variables for tests
load_dotenv(".env")


@pytest.fixture
def tmdb_access_token():
    """Fixture to get TMDB access token"""
    token = os.getenv("TMDB_ACCESS_TOKEN")
    if not token or token == "your_tmdb_access_token_here":
        pytest.skip("TMDB_ACCESS_TOKEN not configured in .env")
    return token
