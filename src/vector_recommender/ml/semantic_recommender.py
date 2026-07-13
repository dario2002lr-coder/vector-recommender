"""Semantic movie recommendation utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from vector_recommender.logger import get_logger
from vector_recommender.ml.text_processing import build_semantic_document

from config import settings

logger = get_logger(__name__)

class SemanticMovieRecommender:
    """Recommend movies by semantic similarity using precomputed embeddings."""

    def __init__(
        self,
        dataframe: pd.DataFrame | None,
        embeddings: np.ndarray | None = None,
        encoder: SentenceTransformer | Any | None = None,
        model_name: str | None = None,
    ) -> None:
        self.dataframe: pd.DataFrame | None = None
        self.embeddings = embeddings
        self.encoder = encoder
        self.model_name = model_name or settings.MODEL_NAME
        self.logger = logger

        if dataframe is None:
            self.load_dataset()
        else:
            self.dataframe = dataframe.copy()

        if self.embeddings is None:
            self._load_embeddings()

    def _load_embeddings(self) -> None:
        embeddings_path = settings.get_embeddings_path()
        if not embeddings_path.exists():
            raise FileNotFoundError(
                f"Embeddings file not found: {embeddings_path}. "
                f"Project root resolved to: {settings.get_project_root()}"
            )

        self.embeddings = np.load(embeddings_path)
        self.logger.info("Loaded movie embeddings from %s", embeddings_path)

    def _ensure_encoder(self) -> Any:
        if self.encoder is None:
            self.encoder = SentenceTransformer(self.model_name)
            self.logger.info("Loaded sentence transformer model %s", self.model_name)
        return self.encoder

    def _encode_query(self, query: str) -> np.ndarray:
        encoder = self._ensure_encoder()
        query_embedding = encoder.encode([query], normalize_embeddings=True)
        return query_embedding.astype(float)

    def recommend(self, query: str, top_k: int | None = None) -> list[dict[str, Any]]:
        """Return the top-k movies most similar to a natural language query."""
        if not query or not query.strip():
            raise ValueError("Query must not be empty")

        if self.dataframe is None:
            raise ValueError("Movie dataset is not available")

        if self.embeddings is None or len(self.embeddings) == 0:
            raise ValueError("Embeddings are not available")

        selected_top_k = top_k or settings.DEFAULT_TOP_K

        query_embedding = self._encode_query(query)
        similarity_scores = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = np.argsort(similarity_scores)[::-1][:selected_top_k]

        results: list[dict[str, Any]] = []
        for index in top_indices:
            row = self.dataframe.iloc[index]
            results.append(
                {
                    "id": int(row.get("id", index)),
                    "title": row.get("title", "Unknown"),
                    "overview": row.get("overview", ""),
                    "genres": row.get("genres", []),
                    "release_date": row.get("release_date", ""),
                    "vote_average": float(row.get("vote_average", 0.0)) if pd.notna(row.get("vote_average")) else None,
                    "popularity": float(row.get("popularity", 0.0)) if pd.notna(row.get("popularity")) else None,
                    "similarity": float(similarity_scores[index]),
                }
            )

        self.logger.info("Recommended %s movies for query: %s", len(results), query)
        return results

    def load_dataset(self, data_path: str | Path | None = None) -> pd.DataFrame:
        """Load the processed movie dataset from disk."""
        if data_path is None:
            data_path = settings.get_dataset_path()
        data_path = Path(data_path)
        if not data_path.exists():
            raise FileNotFoundError(
                f"Movie dataset file not found: {data_path}. "
                f"Project root resolved to: {settings.get_project_root()}"
            )
        dataframe = pd.read_csv(data_path)
        self.dataframe = dataframe
        self.logger.info("Loaded movie dataset from %s", data_path)
        return self.dataframe
