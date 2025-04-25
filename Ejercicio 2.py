# 8. ¿Cuántas películas hay en total? Mostrar en consola
# 10. ¿Cuántas películas fueron calificadas como "Certified Fresh", "Fresh" y "Rotten"? usa value counts sobre la columna tomatometer_status

import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

num_peliculas = len(df_movies)

print("El numero de peliculas totales es")
print(num_peliculas)

