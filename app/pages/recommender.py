import streamlit as st

from utils.cache import (
    load_embeddings,
    load_model,
    load_movies,
)

from config.config import (
    TOP_K_RECOMMENDATIONS,
)

from vector_recommender.recommendation.recommenders import (
    recommend_movies,
)

from components.movie_card import render_movie_card

st.title("🎥 Movie Recommender")

st.write(
    "Describe the kind of movie you would like to watch."
)

query = st.text_input(
    "Movie description",
    placeholder="A sci-fi movie about time travel...",
)

if st.button("Recommend", type="primary"):

    if not query.strip():
        st.warning("Please enter a movie description.")
    else:
        with st.spinner("Finding movies..."):
            model = load_model()
            movies = load_movies()
            embeddings = load_embeddings()

            results = recommend_movies(
                query=query,
                movies_df=movies,
                embeddings=embeddings,
                model=model,
                top_k=TOP_K_RECOMMENDATIONS,
            )

        st.subheader("Recommendations")

        for _, movie in results.iterrows():
            render_movie_card(movie)