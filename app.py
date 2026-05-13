

import pandas as pd
import streamlit as st
import pickle
import numpy as np

def recommend(movie):
    movie_index = movies[movies['title_x'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title_x)

    return recommended_movies


st.title('Movie review system')
st.header('Movie review system')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl', 'rb'))
import lzma

with lzma.open("similarity.pkl.xz", "rb") as f:
    similarity = pickle.load(f)
option = st.selectbox(
    "Select a movie",
    movies['title_x'].values
)

if st.button("Recommend"):
    recommendations = recommend(option)

    for movie in recommendations:
        st.write(movie)
