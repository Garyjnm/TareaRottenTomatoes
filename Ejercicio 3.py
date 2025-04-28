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