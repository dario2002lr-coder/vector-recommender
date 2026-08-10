import streamlit as st

from pages.home import render_home

st.set_page_config(
    page_title="Vector Recommender",
    page_icon="🎬",
    layout="wide",
)

render_home()