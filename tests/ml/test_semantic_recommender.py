import numpy as np
import pandas as pd
import vector_recommender.ml.semantic_recommender as semantic_recommender
from config import settings as config_settings

from vector_recommender.ml.semantic_recommender import SemanticMovieRecommender
from vector_recommender.ml.text_processing import build_semantic_document


class DummyEncoder:
    def encode(self, texts, normalize_embeddings=True):
        vectors = []
        for text in texts:
            lowered = text.lower()
            if "space" in lowered:
                vectors.append([1.0, 0.0])
            elif "romance" in lowered:
                vectors.append([0.8, 0.6])
            else:
                vectors.append([0.2, 0.99])

        array = np.array(vectors, dtype=float)
        if normalize_embeddings:
            norms = np.linalg.norm(array, axis=1, keepdims=True)
            array = array / norms
        return array


def test_build_semantic_document_uses_available_fields():
    row = pd.Series(
        {
            "title": "The Matrix",
            "genres": "Action, Science Fiction",
            "overview": "A hacker learns about reality.",
            "keywords": "future, rebellion",
            "tagline": "The fight for the future.",
        }
    )

    document = build_semantic_document(row)

    assert "The Matrix" in document
    assert "Action" in document
    assert "Science Fiction" in document
    assert "A hacker learns about reality." in document


def test_load_dataset_uses_project_root_when_module_lives_under_src(tmp_path, monkeypatch):
    project_root = tmp_path / "project"
    dataset_dir = project_root / "data" / "processed" / "tmdb_5000_movie_dataset"
    dataset_dir.mkdir(parents=True)
    dataset_path = dataset_dir / "tmdb_5000_semantic.csv"
    dataset_path.write_text("title,overview\nTest Movie,Example overview\n", encoding="utf-8")

    monkeypatch.setattr(config_settings, "get_project_root", lambda: project_root)

    recommender = SemanticMovieRecommender(dataframe=None, embeddings=np.zeros((1, 1)))

    assert recommender.dataframe is not None
    assert recommender.dataframe.iloc[0]["title"] == "Test Movie"


def test_recommend_returns_most_similar_movies():
    dataframe = pd.DataFrame(
        [
            {
                "title": "The Matrix",
                "genres": "Action, Science Fiction",
                "overview": "A hacker discovers reality.",
                "keywords": "future",
                "tagline": "The fight for the future.",
                "vote_average": 8.7,
                "popularity": 120.0,
            },
            {
                "title": "Interstellar",
                "genres": "Sci-Fi, Adventure",
                "overview": "A space mission crosses the cosmos.",
                "keywords": "space",
                "tagline": "Mankind was born on Earth. It was never meant to die here.",
                "vote_average": 8.6,
                "popularity": 100.0,
            },
            {
                "title": "A Beautiful Mind",
                "genres": "Drama, Romance",
                "overview": "A brilliant mathematician struggles with life.",
                "keywords": "romance",
                "tagline": "A story of love and genius.",
                "vote_average": 8.2,
                "popularity": 90.0,
            },
        ]
    )

    embeddings = np.array([[1.0, 0.0], [0.8, 0.6], [0.2, 0.99]], dtype=float)
    recommender = SemanticMovieRecommender(
        dataframe=dataframe,
        embeddings=embeddings,
        encoder=DummyEncoder(),
    )

    results = recommender.recommend("space adventure", top_k=2)

    assert [movie["title"] for movie in results] == ["The Matrix", "Interstellar"]
    assert results[0]["similarity"] >= results[1]["similarity"]
