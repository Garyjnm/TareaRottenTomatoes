# 8. ¿Cuántas películas hay en total? Mostrar en consola
# 10. ¿Cuántas películas fueron calificadas como "Certified Fresh", "Fresh" y "Rotten"? usa value counts sobre la columna tomatometer_status

import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

num_peliculas = len(df_movies)

print("El numero de peliculas totales es")
print(num_peliculas)

Distribucion_Calificaciones = df_movies['tomatometer_status'].value_counts()
print(Distribucion_Calificaciones)

plt.figure(figsize=(6, 6))
Distribucion_Calificaciones.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=["yellow", "red", "green"])
plt.title("Distribución de calificaciones")
plt.ylabel("")
plt.show()

