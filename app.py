import streamlit as st
import pickle
import pandas as pd
import requests  # to fetch poster from tmdb using API



# Function to fetch posters
def fetch_posters(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3f250cb970e4591da5ebe4d5198db951'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



# Function to fetch homepage link
def fetch_homepage(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3f250cb970e4591da5ebe4d5198db951'.format(movie_id))
    data = response.json()
    return data['homepage']


# This function will sort movies as per similarity with the given movie
def provideClosestMovies(index):
    recommend_mov=sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    return recommend_mov





# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    recommend_mov = provideClosestMovies(index)
    recommended_movies=[]
    movie_overview=[]
    recommended_movie_poster=[]
    overview=[]
    homepage=[]
    for i in recommend_mov[1:11]:
        st.header(movies.iloc[i[0]].title)
        first, sec = st.columns(2)
        first.image(fetch_posters(movies.iloc[i[0]].movie_id))
        sec.subheader('Overview:')
        sec.write(movies.iloc[i[0]].overview)
        link = '' + (fetch_homepage(movies.iloc[i[0]].movie_id))
        if len(link):
            sec.write('Homepage Link:')
            sec.markdown(link, unsafe_allow_html=True)
    return




# Importing files using pickel
similarity=pickle.load(open('similarity.pkl','rb'))
movies_in_dict=pickle.load(open('movies_dict.pkl','rb'))

# Our data frame
movies = pd.DataFrame(movies_in_dict)


st.title('Movie Recommendation App')

# Select Box
selected_movie = st.selectbox(
     'Select your faviorite movie',
     movies['title'].values)

# Button
if st.button('Recommend'):
     recommend(selected_movie)








