# 11. Promedio de valoración del tomatómetro y la audiencia o publico
# print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
# print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")
# 12. Para cada película, calcular la diferencia entre audiencia y críticos
# 13. Histograma de las diferencias de valoración

import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

rat_tomatometer = df_movies['tomatometer_rating'].mean()
print("promedio de tomatometer es: " +str(rat_tomatometer))
print("-------------------------------------------")

rat_audience = df_movies['audience_rating'].mean()
print("promedio de audience es: " +str(rat_audience))

df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

plt.figure(figsize = (12,8))
plt.hist(df_movies['rating_diff'], bins = 30, edgecolor = 'black', color = 'seagreen')
plt.title("Distribucion, diferencia entre audiencia y criticos")
plt.axvline(x=0, color='red', linestyle='--', linewidth=2)
plt.xlabel("Diferencia (Audiencia - Criticos)")
plt.ylabel("Numero de peliculas")
plt.show()