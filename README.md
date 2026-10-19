# 🎬 Movie Recommender System

A content-based movie discovery app built with Python, Pandas, scikit-learn, and Streamlit. It recommends films similar to a selected title and displays movie posters and metadata from The Movie Database (TMDB).

## Features

- Browse trending movies from TMDB.
- Choose a film and get up to five similar recommendations.
- View posters, ratings, release dates, genres, and short summaries.
- Use a content-based approach based on text features and cosine similarity.

## How It Works

1. The companion notebook prepares and combines movie metadata.
2. Text features are vectorized using `CountVectorizer`.
3. Cosine similarity scores are calculated between movies.
4. The Streamlit app loads the serialized movie data and similarity matrix, then retrieves movie details from TMDB.

## Repository Contents

- `app.py` — Streamlit application.
- `Movie_Recommender_System.ipynb` — notebook for exploring and preparing the recommender.
- `movie_dict.pkl` — serialized movie metadata used by the app.
- `requirements.txt` — Python dependencies.
- `similarity.pkl` — also required by `app.py`; generate it from the notebook if it is not present in your local checkout.

## Prerequisites

- Python 3.10 or newer recommended
- A TMDB API key for posters, ratings, trending titles, and other movie details

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/Ishant-Mishra/Movie-Recommender-System.git
cd Movie-Recommender-System
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and configure the API key:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and replace the placeholder with your own TMDB API key. Keep `.env` private; never commit real keys.

Start the app:

```bash
streamlit run app.py
```

If Streamlit reports that `similarity.pkl` is missing, open and run the notebook’s model-preparation cells to regenerate the similarity matrix in the repository root before starting the app.

## Dataset

The project uses TMDB movie metadata. The dataset is not bundled separately as a raw download; see the [TMDB Movie Metadata dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). Check the dataset’s terms and attribution requirements before redistributing it.

## Limitations

This is an educational content-based recommender, not a personalized or collaborative-filtering system. Recommendations depend on the available metadata and preprocessing. TMDB API access and network availability are required for live movie details.

## Future Improvements

- Add API timeouts and user-friendly handling for unavailable TMDB responses.
- Improve the model build workflow so all required artifacts can be reproduced consistently.
- Add tests for preprocessing and recommendation ranking.
- Explore hybrid or collaborative filtering.

## Acknowledgements

- [The Movie Database (TMDB)](https://www.themoviedb.org/)
- [TMDB Movie Metadata dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
