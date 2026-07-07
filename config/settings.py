"""Application configuration values."""

from __future__ import annotations

from pathlib import Path

DEFAULT_TOP_K = 5
MODEL_NAME = "BAAI/bge-small-en-v1.5"


def get_project_root() -> Path:
    """Return the project root by searching upward from the current working directory first."""
    candidate = Path.cwd().resolve()
    for parent in (candidate, *candidate.parents):
        if (parent / "pyproject.toml").exists() or (parent / ".git").exists():
            return parent

    candidate = Path(__file__).resolve()
    for parent in (candidate, *candidate.parents):
        if (parent / "pyproject.toml").exists() or (parent / ".git").exists():
            return parent

    return Path(__file__).resolve().parents[1]


def get_dataset_path() -> Path:
    """Return the processed dataset path."""
    return get_project_root() / "data" / "processed" / "tmdb_5000_movie_dataset" / "tmdb_5000_semantic.csv"


def get_embeddings_path() -> Path:
    """Return the embeddings file path."""
    return get_project_root() / "data" / "processed" / "tmdb_5000_movie_dataset" / "movie_embeddings.npy"
