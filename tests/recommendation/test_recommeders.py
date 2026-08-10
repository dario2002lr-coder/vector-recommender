"""Integration tests for movie recommendations."""

from config.config import (
    TMDB_5000_EMBEDDINGS_PATH,
    TMDB_5000_SEMANTIC_PATH,
    EMBEDDING_MODEL_NAME
)
from vector_recommender.io.loaders import (
    load_csv,
    load_numpy_array,
)
from vector_recommender.ml.embeddings.loaders import (
    load_embedding_model,
)
from vector_recommender.recommendation.recommenders import (
    recommend_movies,
)


def test_recommend_movies():
    """Test movie recommendations using the TMDB 5000 dataset."""

    movies_df = load_csv(
        TMDB_5000_SEMANTIC_PATH,
    )

    embeddings = load_numpy_array(
        TMDB_5000_EMBEDDINGS_PATH,
    )

    model = load_embedding_model(EMBEDDING_MODEL_NAME)

    results = recommend_movies(
        query="I want a sci-fi movie with time travel",
        movies_df=movies_df,
        embeddings=embeddings,
        model=model,
        top_k=10,
    )

    print("\nRecommended movies:")
    print(results.to_string(index=False))

    assert len(results) == 10
    assert "title" in results.columns
    assert "similarity" in results.columns