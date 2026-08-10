import streamlit as st

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


@st.cache_resource
def load_model():
    return load_embedding_model(EMBEDDING_MODEL_NAME)


@st.cache_data
def load_movies():
    return load_csv(
        TMDB_5000_SEMANTIC_PATH
    )


@st.cache_data
def load_embeddings():
    return load_numpy_array(
        TMDB_5000_EMBEDDINGS_PATH
    )