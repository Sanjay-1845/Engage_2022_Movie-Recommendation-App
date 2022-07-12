# Engage_2022_Movie-Recommendation-App
Link of my web application : https://movie-recommendation-app201.herokuapp.com/
It is a content based movie recommendation app which ,on entering a movie name recommendeds ten most similar movie, present in the dataset used by me(movies dataset from tmdb website), these recommended movies consits of their title ,poster as well as homepage link of the movie.
This web application make use of cosine similarity and sorting algorithms over the movies data that we have.
tmdb_5000_movies and tmdb_5000_credits.csv are the two files used from tmdb website that consist of data of around 5000 movies. 
movie-recommendation-app.ipynb files consists of the python code that process that data and provide us with the useful data (similarity.pkl and movies_dict.pkl) by making use of different libraries like numpy,pandas,nltk etc.
movies_dict.pkl consists of required data of movies in useful form and similarity.pkl consists of similarity matrix data that we obtained by applying the cosine similarity algorithm over vector(which is formed by vectorising the tags associated with movies) .
These two data files are used in main streamlit app file i.e. app.py that make use of similarity values and sorting algorithm to recommend the movies.
