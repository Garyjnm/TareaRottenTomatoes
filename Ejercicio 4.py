#df_genres_exploded = df_movies_copy.assign(
# genre=df_movies_copy['genre'].str.split(',')
# ).explode('genre')

import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

df_movies_copy = df_movies.copy()

df_genres_exploded = df_movies_copy.assign(
genre=df_movies_copy['genre'].str.split(',')
).explode('genre')