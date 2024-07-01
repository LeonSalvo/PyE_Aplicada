import pandas as pd
from scipy import stats

# Cargar el archivo CSV
file_path = 'titanik.csv'
df = pd.read_csv(file_path)

# Mostrar las primeras filas del dataframe
df.head(), df.info()

# Calcular la media de las edades según el género
mean_age_by_gender = df.groupby('gender')['age'].mean()

print(mean_age_by_gender)

# Llenar los valores faltantes en la columna 'age' con la media de la edad según el género
df['age'] = df.apply(lambda row: mean_age_by_gender[row['gender']] if pd.isnull(row['age']) else row['age'], axis=1)

# Verificar si hay valores nulos restantes en la columna 'age'
df['age'].isnull().sum()

# Calcular la media
mean_age = df['age'].mean()

# Calcular la mediana
median_age = df['age'].median()

# Calcular la moda
mode_age = df['age'].mode()[0]

# Calcular el rango
range_age = df['age'].max() - df['age'].min()

# Calcular la varianza
variance_age = df['age'].var()

# Calcular la desviación estándar
std_dev_age = df['age'].std()

mean_age, median_age, mode_age, range_age, variance_age, std_dev_age
