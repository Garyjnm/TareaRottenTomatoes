#df_genres_exploded = df_movies_copy.assign(
# genre=df_movies_copy['genre'].str.split(',')
# ).explode('genre')

import pandas as pd
import matplotlib.pyplot as plt

