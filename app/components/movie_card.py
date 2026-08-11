"""Movie card UI component."""

import pandas as pd
import streamlit as st
import ast

def _format_genres(value):
    """Format TMDB genre data as a readable string."""
    if value is None or pd.isna(value):
        return None

    value = str(value).strip()

    if not value:
        return None

    try:
        genres = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return None

    if not isinstance(genres, list):
        return None

    names = [
        genre["name"]
        for genre in genres
        if isinstance(genre, dict) and "name" in genre
    ]

    if not names:
        return None

    return " · ".join(names)

def _format_value(value, fallback="N/A"):
    """Return a display-friendly value."""
    if value is None or pd.isna(value) or str(value).strip() == "":
        return fallback

    return str(value).strip()


def _truncate_text(text, max_length=300):
    """Truncate text while preserving whole words."""
    text = _format_value(text, "")

    if not text:
        return "No overview available."

    if len(text) <= max_length:
        return text

    truncated = text[:max_length].rsplit(" ", 1)[0]

    return f"{truncated}..."


def render_movie_card(movie: pd.Series) -> None:
    """Render a movie recommendation as a visual card."""

    title = _format_value(
        movie.get("title"),
        "Unknown title",
    )

    overview = _truncate_text(
        movie.get("overview"),
    )

    release_year = _format_value(
        movie.get("release_year"),
    )

    genres = _format_genres(
        movie.get("genres"),
    )

    vote_average = movie.get("vote_average")
    similarity = movie.get("similarity")

    with st.container(border=True):
        st.subheader(title)

        metadata = []

        if release_year != "N/A":
            metadata.append(f"📅 {release_year}")

        if genres != "N/A":
            metadata.append(f"🎭 {genres}")

        if metadata:
            st.caption(" • ".join(metadata))

        st.write(overview)

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:
            if pd.notna(vote_average):
                st.metric(
                    "⭐ Rating",
                    f"{float(vote_average):.1f}/10",
                )
            else:
                st.metric(
                    "⭐ Rating",
                    "N/A",
                )

        with metric_col2:
            if pd.notna(similarity):
                st.metric(
                    "🧠 Similarity",
                    f"{float(similarity) * 100:.1f}%",
                )
            else:
                st.metric(
                    "🧠 Similarity",
                    "N/A",
                )
