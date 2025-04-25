# 1. Importar las librerías necesarias
# 2. Leer el archivo CSV
# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
# 4. Verificar los nombres de las columnas
# 5. Convertir la columna 'in_theaters_date' al tipo datetime
# 6. Verificar que la conversión fue exitosa (dtypes)
# 7. Mostrar si hubo valores no convertidos (NaT) missing_dates = df_movies['in_theaters_date'].isna().sum() print(f"\nPelículas con fechas no reconocidas: {missing_dates}")

import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

print("------------------Primeras 5 filas del dataframe--------------------------")
print(df_movies.head(5))

print("------------------Tipo de datos antes de la conversion--------------------------")
print(df_movies.dtypes)

print("------------------Tipo de datos despues de la conversion--------------------------")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

print(df_movies.dtypes)