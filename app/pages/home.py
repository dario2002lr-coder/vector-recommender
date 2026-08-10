import streamlit as st

from app.utils.cache import (
    load_embeddings,
    load_model,
    load_movies,
)

from vector_recommender.recommendation.recommenders import (
    recommend_movies,
)


def render_home():

    st.title("🎬 Vector Movie Recommender")

    st.write(
        "Describe the kind of movie you would like to watch."
    )

    query = st.text_input(
        "Movie description"
    )

    model = load_model()

    movies = load_movies()

    embeddings = load_embeddings()

    if st.button("Recommend"):

        results = recommend_movies(
            query=query,
            movies_df=movies,
            embeddings=embeddings,
            model=model,
        )

        st.dataframe(
            results,
            use_container_width=True,
        )