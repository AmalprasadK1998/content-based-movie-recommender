import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=54f258c18e953ee77c068ea278670840&language=en-US".format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


def recommend(movie):

    movie_index = movies[movies['title']==movie].index[0]

    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]]['title'])

        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster

st.title('Movie Reccomender System')

movies = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies)

movies_drop = movies['title'].values

selected_movie = st.selectbox(
    'Choose a movie!',
    (movies_drop))

similarity = pickle.load(open('similarity.pkl','rb'))

if st.button('Reccomend'):
    names,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])





