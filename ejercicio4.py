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
    print(f"Promedio de edades según el género:\n{mean_age_by_gender}")
    df[column] = df.apply(lambda row: mean_age_by_gender[row[group_by]] if pd.isnull(row[column]) else row[column],
                          axis=1)
    return df


def histogram(df):
    # Histograma de las edades por clase
    axes = df.hist(column='age', by='p_class', bins=20, edgecolor='black', figsize=(15, 10))

    # Ajustar el título de cada subgráfico y las etiquetas de los ejes
    for ax in axes.flatten():
        ax.set_title(f'Clase {ax.get_title()}')  # Título individual para cada clase
        ax.set_xlabel('Edad')
        ax.set_ylabel('Frecuencia')

    # Título principal para el conjunto de los histogramas
    plt.suptitle('Histograma de las Edades por Clase', y=1.02)

    plt.tight_layout()
    plt.show()


def boxplots(df):
    df.boxplot(column='age', by='survived', grid=False, vert=False, figsize=(10, 5))
    plt.title('Diagrama de Cajas para las Edades de los Supervivientes y No Supervivientes')
    plt.suptitle('')
    plt.xlabel('Edad')
    plt.ylabel('Supervivencia (0=No, 1=Sí)')
    plt.show()


def calculate_ttest_ind(class_1_survival, class_2_survival):
    t_stat, p_value = stats.ttest_ind(class_1_survival, class_2_survival, alternative='two-sided')
    return t_stat, p_value


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
    print(f"Tasa de supervivencia por género:\n{survival_rate_by_gender}\n")

    # Histograma de las edades por clase
    histogram(df)

    # Diagrama de cajas para las edades de los supervivientes y no supervivientes
    boxplots(df)

    # Intervalo de confianza para la edad promedio
    confidence_level = 0.95
    degrees_freedom = len(df['age']) - 1
    sample_mean = np.mean(df['age'])
    sample_standard_error = stats.sem(df['age'])

    confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)
    print(f"Intervalo de confianza para la edad promedio: {confidence_interval}\n")

    # Promedio de edad por género
    women_age = df[df['gender'] == 'female']['age']
    t_stat, p_value = stats.ttest_1samp(women_age, 56, alternative='greater')
    print(f"Prueba t para la edad promedio de las mujeres: t={t_stat}, p={p_value}\n")

    men_age = df[df['gender'] == 'male']['age']
    t_stat, p_value = stats.ttest_1samp(men_age, 56, alternative='greater')
    print(f"Prueba t para la edad promedio de los hombres: t={t_stat}, p={p_value}\n")

    # Prueba t para la tasa de supervivencia entre hombres y mujeres
    men_survival = df[df['gender'] == 'male']['survived']
    women_survival = df[df['gender'] == 'female']['survived']
    t_stat, p_value = stats.ttest_ind(men_survival, women_survival, alternative='two-sided')
    print(f"Diferencia en la tasa de supervivencia entre hombres y mujeres: t={t_stat}, p={p_value}\n")

    # Prueba t para la tasa de supervivencia entre las clases
    class_1_survival = df[df['p_class'] == 1]['survived']
    class_2_survival = df[df['p_class'] == 2]['survived']
    class_3_survival = df[df['p_class'] == 3]['survived']

    t_stat_12, p_value_12 = calculate_ttest_ind(class_1_survival, class_2_survival)
    t_stat_13, p_value_13 = calculate_ttest_ind(class_1_survival, class_3_survival)
    t_stat_23, p_value_23 = calculate_ttest_ind(class_2_survival, class_3_survival)

    print(f"Diferencia en la tasa de supervivencia entre clase 1 y clase 2: t={t_stat_12}, p={p_value_12}\n")
    print(f"Diferencia en la tasa de supervivencia entre clase 1 y clase 3: t={t_stat_13}, p={p_value_13}\n")
    print(f"Diferencia en la tasa de supervivencia entre clase 2 y clase 3: t={t_stat_23}, p={p_value_23}\n")

    ttest_ages, p_value_ages = stats.ttest_ind(women_age, men_age, alternative='two-sided')
    print(f"Diferencia en la edad promedio entre hombres y mujeres: t={ttest_ages}, p={p_value_ages}\n")


main()
