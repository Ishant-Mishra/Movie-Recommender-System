
# Movie Recommender System

A content-based Movie Recommender System built using Python, Machine Learning, and Streamlit.

This project recommends movies similar to the one selected by the user using cosine similarity and text vectorization techniques.

---

# Features

* Movie recommendation based on similarity
* Interactive Streamlit web interface
* Content-based filtering approach
* Fast recommendation generation
* TMDB API integration for movie posters
* Clean and simple UI

---

# Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle
* TMDB API


# How It Works

1. Movie datasets are preprocessed and cleaned.
2. Important features such as genres, keywords, cast, crew, and overview are combined.
3. Text vectorization is performed using CountVectorizer.
4. Cosine similarity is calculated between movie vectors.
5. The system recommends movies with the highest similarity scores.

## Dataset

The dataset is not included in this repository due to size limitations.

You can download it from:
[[Dataset Link]](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


# Future Improvements

* Add collaborative filtering
* Add user authentication
* Improve recommendation accuracy
* Deploy full application online
* Add search history and favorites
* Add hybrid recommendation system

# License

This project is for educational and learning purposes.
