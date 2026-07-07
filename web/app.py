"""Streamlit app for semantic movie recommendations."""

from __future__ import annotations

from pathlib import Path
import os
import sys

import numpy as np
import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
os.chdir(PROJECT_ROOT)
SRC_ROOT = PROJECT_ROOT / "src"
CONFIG_ROOT = PROJECT_ROOT / "config"
for path in (str(PROJECT_ROOT), str(SRC_ROOT), str(CONFIG_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from vector_recommender.logger import get_logger
from vector_recommender.ml.semantic_recommender import SemanticMovieRecommender

from config.settings import DEFAULT_TOP_K, get_dataset_path, get_embeddings_path

logger = get_logger(__name__)


@st.cache_resource
def build_recommender() -> SemanticMovieRecommender:
    """Create and cache the recommender instance."""
    dataset_path = get_dataset_path()
    embeddings_path = get_embeddings_path()
    dataframe = pd.read_csv(dataset_path)
    embeddings = np.load(embeddings_path)
    return SemanticMovieRecommender(dataframe=dataframe, embeddings=embeddings)


st.set_page_config(page_title="Vector Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Vector Recommender")
st.write("Describe the kind of movie you want to watch and I will suggest five similar titles.")

query = st.text_input(
    "What would you like to watch?",
    placeholder="A thrilling sci-fi adventure with emotional depth",
    key="movie_prompt",
)

submit = st.button("Find movies", type="primary")
if submit or st.session_state.get("movie_prompt") and st.session_state.get("movie_prompt") != "":
    if not query.strip():
        st.warning("Please write a movie description first.")
    else:
        logger.info("Generating recommendations for query: %s", query)
        recommender = build_recommender()
        recommendations = recommender.recommend(query, top_k=DEFAULT_TOP_K)

        if not recommendations:
            st.info("No movies matched your request right now.")
        else:
            cols = st.columns(5)
            for col, movie in zip(cols, recommendations):
                with col:
                    st.markdown(f"### {movie['title']}")
                    st.write(movie.get("overview") or "No overview available.")
                    raw_genres = movie.get("genres") or []
                    genre_names = []
                    if isinstance(raw_genres, str):
                        try:
                            import ast

                            parsed_genres = ast.literal_eval(raw_genres)
                            if isinstance(parsed_genres, list):
                                for genre in parsed_genres:
                                    if isinstance(genre, dict):
                                        name = genre.get("name") or genre.get("genre")
                                        if name:
                                            genre_names.append(str(name))
                            elif isinstance(parsed_genres, dict):
                                name = parsed_genres.get("name") or parsed_genres.get("genre")
                                if name:
                                    genre_names.append(str(name))
                        except Exception:
                            genre_names = []
                    elif isinstance(raw_genres, list):
                        for genre in raw_genres:
                            if isinstance(genre, dict):
                                name = genre.get("name") or genre.get("genre")
                                if name:
                                    genre_names.append(str(name))
                            elif genre is not None:
                                genre_names.append(str(genre))

                    genre_text = ", ".join(genre_names) if genre_names else "Unknown"
                    st.caption(f"Genres: {genre_text}")
                    release_date = movie.get("release_date") or "Unknown"
                    vote_average = movie.get("vote_average")
                    vote_text = f"⭐ {vote_average:.1f}" if vote_average is not None else "⭐ N/A"
                    st.caption(f"Release: {release_date} · {vote_text}")
                    st.progress(min(1.0, max(0.0, movie.get("similarity", 0.0))))
                    st.caption(f"Similarity: {movie.get('similarity', 0.0):.2f}")
