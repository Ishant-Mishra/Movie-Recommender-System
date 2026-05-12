import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #E50914;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #AAAAAA;
    margin-bottom: 40px;
}

.movie-title {
    text-align: center;
    color: white;
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}

.rating {
    color: gold;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
}

.overview {
    font-size: 14px;
    color: #CCCCCC;
    text-align: center;
}

.poster-container {
    overflow: hidden;
    border-radius: 18px;
}

.poster-container img {
    border-radius: 18px;
    transition: all 0.4s ease;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.6);
}

.poster-container img:hover {
    transform: scale(1.08);
    box-shadow: 0px 10px 30px rgba(229,9,20,0.8);
}

.genre-chip {
    display: inline-block;
    background-color: #E50914;
    color: white;
    padding: 5px 12px;
    margin: 3px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
}

.section-title {
    font-size: 35px;
    font-weight: bold;
    color: white;
    margin-top: 40px;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    color: #888888;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# LOAD DATA
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


API_KEY = "f278e1b63cbaa73ad83a0f7bc74f8225"

def fetch_movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    response = requests.get(url)

    data = response.json()

    poster_path = data.get('poster_path')

    full_path = (
        "https://image.tmdb.org/t/p/w500/" + poster_path
        if poster_path
        else "https://via.placeholder.com/500x750?text=No+Image"
    )

    genres = [genre['name'] for genre in data.get('genres', [])]

    return {
        "poster": full_path,
        "rating": data.get('vote_average', 'N/A'),
        "overview": data.get('overview', 'No overview available'),
        "release_date": data.get('release_date', 'N/A'),
        "genres": genres,
        "link": f"https://www.themoviedb.org/movie/{movie_id}"
    }


# FETCH TRENDING MOVIES
def fetch_trending_movies():

    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"

    response = requests.get(url)

    data = response.json()

    trending_movies = []

    for movie in data['results'][:5]:

        poster = "https://image.tmdb.org/t/p/w500/" + movie['poster_path']

        trending_movies.append({
            "title": movie['title'],
            "poster": poster,
            "rating": movie['vote_average'],
            "link": f"https://www.themoviedb.org/movie/{movie['id']}"
        })

    return trending_movies


# Recommender Function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        details = fetch_movie_details(movie_id)

        recommended_movies.append({
            "title": movies.iloc[i[0]].title,
            "poster": details['poster'],
            "rating": details['rating'],
            "overview": details['overview'],
            "release_date": details['release_date'],
            "genres": details['genres'],
            "link": details['link']
        })

    return recommended_movies

# Title
st.markdown(
    '<div class="title">🎬 Movie Recommender System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover Movies Similar To Your Favourite Ones</div>',
    unsafe_allow_html=True
)


# Trending Sections
st.markdown(
    '<div class="section-title">🔥 Trending Movies</div>',
    unsafe_allow_html=True
)

trending_movies = fetch_trending_movies()

trend_cols = st.columns(5)

for idx, movie in enumerate(trending_movies):

    with trend_cols[idx]:

        st.markdown(
            f"""
            <div class="poster-container">
                <a href="{movie['link']}" target="_blank">
                    <img src="{movie['poster']}" width="100%">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="movie-title">
                {movie['title']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rating">
                ⭐ {movie['rating']}
            </div>
            """,
            unsafe_allow_html=True
        )


# Movie Selection Box
st.markdown(
    '<div class="section-title">🎥 Get Recommendations</div>',
    unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    "Search or Select a Movie",
    movies['title'].values
)


# Buttons
if st.button('Recommend Movies'):

    recommendations = recommend(selected_movie_name)

    cols = st.columns(5)

    for idx, movie in enumerate(recommendations):

        with cols[idx]:

            # CLICKABLE POSTER
            st.markdown(
                f"""
                <div class="poster-container">
                    <a href="{movie['link']}" target="_blank">
                        <img src="{movie['poster']}" width="100%">
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

            # TITLE
            st.markdown(
                f"""
                <div class="movie-title">
                    {movie['title']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # RATING
            st.markdown(
                f"""
                <div class="rating">
                    ⭐ {movie['rating']}
                </div>
                """,
                unsafe_allow_html=True
            )

            # GENRE CHIPS
            genres_html = ""

            for genre in movie['genres']:
                genres_html += f'<span class="genre-chip">{genre}</span>'

            st.markdown(genres_html, unsafe_allow_html=True)

            # RELEASE DATE
            st.caption(f"📅 {movie['release_date']}")

            # OVERVIEW
            st.markdown(
                f"""
                <div class="overview">
                    {movie['overview'][:120]}...
                </div>
                """,
                unsafe_allow_html=True
            )


# FOOTER
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Ishant Mishra
    </div>
    """,
    unsafe_allow_html=True
)