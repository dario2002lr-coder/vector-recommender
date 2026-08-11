# Vector Recommender

AI-powered recommendation project built with Python, Streamlit, and semantic embeddings.

## Overview

This project is a movie recommendation prototype based on semantic search over natural language descriptions. It uses the TMDB 5000 dataset to load movie metadata, process additional features, build semantic documents, and generate embeddings that allow the system to find movies that are closest in meaning to a user query.

## Achievements So Far

- Data processing and cleaning for the TMDB 5000 dataset.
- Feature engineering, including release year/month, profit, and weighted rating.
- Building semantic documents for each movie.
- Generating embeddings using a pretrained `sentence-transformers` model.
- Performing fast vector search with cosine similarity.
- Building a simple Streamlit web interface with text input and recommendation cards.
- Designing a modular architecture with separated data loading, processing, embedding generation, and recommendation logic.

## Project Structure

- `app/`
  - `app.py`: main Streamlit landing page.
  - `pages/recommender.py`: movie recommendation app page.
  - `components/movie_card.py`: UI component for rendering movie cards.
  - `utils/cache.py`: cached loading of model, dataset, and embeddings.

- `src/vector_recommender/`
  - `recommendation/recommenders.py`: recommendation logic based on user queries.
  - `recommendation/search.py`: similarity search over embeddings.
  - `ml/embeddings/generator.py`: normalized embedding generation.
  - `ml/embeddings/loaders.py`: embedding model loader.
  - `ml/embeddings/pipeline.py`: embedding generation pipeline for TMDB 5000.
  - `processing/tmdb_5000_dataset/`: TMDB 5000 dataset preprocessing.
  - `io/`: file loading and saving utilities.
  - `ingestion/tmdb/`: TMDB API client and service layer.
  - `logger.py`: configurable logger with console formatting.

- `config/config.py`: data paths, model settings, and global constants.
- `data/`: raw and processed dataset files.
- `scripts/demo_movie.py`: TMDB API demo script using the project client and service.

## Dependencies

The main dependencies are defined in `pyproject.toml` and include:

- `streamlit`
- `pandas`
- `sentence-transformers`
- `numpy`
- `requests`
- `pydantic`
- `matplotlib`
- `seaborn`
- `umap-learn`
- `python-dotenv` (development)
- `pytest`, `pytest-mock` (testing)

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   or using the `pyproject.toml` with a modern Python environment:

   ```bash
   pip install .
   pip install -e .
   pip install -r requirements-dev.txt
   ```

2. Run the Streamlit app from the project root:

   ```bash
   streamlit run app/app.py
   ```

3. Open the browser at the URL shown by Streamlit.

## Data and Embeddings

The project uses paths defined in `config/config.py`:

- `data/raw/tmdb_5000_movie_dataset/tmdb_5000_movies.csv`
- `data/raw/tmdb_5000_movie_dataset/tmdb_5000_credits.csv`
- `data/processed/tmdb_5000_movie_dataset/tmdb_5000_processed.csv`
- `data/processed/tmdb_5000_movie_dataset/tmdb_5000_semantic.csv`
- `data/processed/tmdb_5000_movie_dataset/movie_embeddings.npy`

### Current Data Flow

1. Load raw TMDB 5000 CSVs.
2. Merge movies and credits datasets.
3. Replace invalid zero values with `NaN`.
4. Convert `release_date` to datetime.
5. Extract release date and profit features.
6. Compute `weighted_rating`.
7. Generate semantic documents and embeddings.
8. Load processed data and embeddings into Streamlit.

## Current Usage

- `app/pages/recommender.py` accepts a natural language movie description.
- `recommend_movies()` generates a query embedding and searches for the most similar movies.
- `components/movie_card.py` formats the results and displays key metrics.

## Implemented Features

- Movie recommendations via semantic search.
- Handling structured TMDB metadata.
- Streamlit-based recommendation UI.
- Cached resource loading for improved app performance.

## Project Status

- Phase one completed: data processing, embedding generation, and UI prototype.
- Future improvement ideas:
  - add more datasets (TV shows, games, other media).
  - extend hybrid recommendations with collaborative or content-based features.
  - integrate LLM explanations for recommendations.
  - add integration tests for the Streamlit app.
  - automate embedding generation and ETL scripts.

## Additional Notes

- A `.env` file can be used to configure `TMDB_ACCESS_TOKEN` when running `scripts/demo_movie.py`.
- The configured embedding model is `BAAI/bge-small-en-v1.5`.
- Data paths and constants are centralized in `config/config.py`.
