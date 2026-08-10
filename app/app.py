import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pages.home import render_home

st.set_page_config(
    page_title="Vector Recommender",
    page_icon="🎬",
    layout="wide",
)

render_home()