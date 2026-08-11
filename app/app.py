import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


st.set_page_config(
    page_title="Vector Recommender",
    page_icon="🎬",
    layout="wide",
)


st.title("🎬 Vector Recommender")

st.write(
    """
    Welcome to Vector Recommender.

    Discover movies using semantic search powered by
    sentence embeddings.
    """
)

st.divider()

st.subheader("What can you do?")

st.write(
    """
    Describe the kind of movie you would like to watch,
    and the recommender will find the movies that are
    semantically closest to your description.
    """
)

st.page_link(
    "pages/recommender.py",
    label="Go to Movie Recommender",
    icon="🎥",
)