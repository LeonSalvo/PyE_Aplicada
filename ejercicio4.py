import pandas as pd
from scipy import stats
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def mean_calculator(df, group_by, column):
    return df.groupby(group_by)[column].mean()

def fill_na_column(df, group_by, column):
    mean_age_by_gender = mean_calculator(df, group_by, column)
    print("Promedio de edades según el género: ")
    print(mean_age_by_gender)
    df[column] = df.apply(lambda row: mean_age_by_gender[row[group_by]] if pd.isnull(row[column]) else row[column], axis=1)
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
    print("La media de las edades es: ", mean_age)

    # Calculo de la mediana
    median_age = df['age'].median()
    print("La mediana de las edades es: ", median_age)

    # Calculo de la moda
    mode_age = df['age'].mode()[0]
    print("La moda de las edades es: ", mode_age)

    # Calculo del rango
    range_age = df['age'].max() - df['age'].min()
    print("El rango de las edades es: ", range_age)

    # Calculo de la varianza
    variance_age = df['age'].var()
    print("La varianza de las edades es: ", variance_age)

    # Calculo de la desviación estándar
    std_dev_age = df['age'].std()
    print("La desviación estándar de las edades es: ", std_dev_age)

    # Calculo de la tasa de supervivencia general
    survival_rate = df['survived'].mean()
    print("La tasa de supervivencia general es: ", survival_rate)

    # Calculo de la tasa de supervivencia por género

main()