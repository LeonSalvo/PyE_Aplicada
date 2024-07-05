import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def mean_calculator(df, group_by, column):
    return df.groupby(group_by)[column].mean()


def fill_na_column(df, group_by, column):
    mean_age_by_gender = mean_calculator(df, group_by, column)
    print(f"Promedio de edades según el género: {mean_age_by_gender}")
    df[column] = df.apply(lambda row: mean_age_by_gender[row[group_by]] if pd.isnull(row[column]) else row[column],
                          axis=1)
    return df


def main():
    # Cargar el archivo CSV
    file_path = 'titanik.csv'
    df = load_csv(file_path)
    # Columna a llenar debido a valores faltantes
    column = 'age'
    # Columna por la cual se agrupará para calcular la media
    group_by = 'gender'

    fill_na_column(df, group_by, column)

    # Calculo de la media
    mean_age = df['age'].mean()
    print(f"La media de las edades es: {mean_age}\n")

    # Calculo de la mediana
    median_age = df['age'].median()
    print(f"La mediana de las edades es: {median_age}\n")

    # Calculo de la moda
    mode_age = df['age'].mode()[0]
    print(f"La moda de las edades es: {mode_age}\n")

    # Calculo del rango
    range_age = df['age'].max() - df['age'].min()
    print(f"El rango de las edades es: {range_age}\n")

    # Calculo de la varianza
    variance_age = df['age'].var()
    print(f"La varianza de las edades es: {variance_age}\n")

    # Calculo de la desviación estándar
    std_dev_age = df['age'].std()
    print(f"La desviación estándar de las edades es: {std_dev_age}\n")

    # Calculo de la tasa de supervivencia general
    survival_rate = df['survived'].mean()
    print(f"La tasa de supervivencia general es: {survival_rate}\n")

    # Calculo de la tasa de supervivencia por género
    survival_rate_by_gender = df.groupby('gender')['survived'].mean()
    print(f"Taza de supervivencia por género: {survival_rate_by_gender}\n")

    # Histograma de las edades por clase
    df.hist(column='age', by='p_class', bins=20, edgecolor='black', figsize=(15, 10))
    plt.suptitle('Histograma de las Edades por Clase', y=1.02)
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()

    # Diagrama de cajas para las edades de los supervivientes y no supervivientes
    df.boxplot(column='age', by='survived', grid=False, vert=False, figsize=(10, 5))
    plt.title('Diagrama de Cajas para las Edades de los Supervivientes y No Supervivientes')
    plt.suptitle('')
    plt.xlabel('Edad')
    plt.ylabel('Supervivencia (0=No, 1=Sí)')
    plt.show()

    # Intervalo de confianza para la edad promedio
    confidence_level = 0.95
    degrees_freedom = len(df['age']) - 1
    sample_mean = np.mean(df['age'])
    sample_standard_error = stats.sem(df['age'])

    confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)
    print(f"Intervalo de confianza para la edad promedio: {confidence_interval}\n")


main()
