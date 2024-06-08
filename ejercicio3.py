import numpy as np
from scipy.stats import binom, mode, geom, poisson
import matplotlib.pyplot as plt

# Distribución 1 - binomial

def binomial_distribution(n, p, sizes):
    samples = [binom.rvs(n, p, size=size) for size in sizes]
    return samples, sizes

def first_distribution(n, p, sizes):
    samples, sizes = binomial_distribution(n, p, sizes)
    create_boxplots(samples, sizes)
    create_histograms(samples, sizes)
    calc_median(samples, sizes)
    calc_mode(samples, sizes)
    calc_mean(samples, sizes)
    calc_variance(samples, sizes)
    theoretical_mean = n * p
    theoretical_variance = n * p * (1 - p)
    print(f"Esperanza teórica de la distribución binomial: {theoretical_mean}")
    print(f"Varianza teórica de la distribución binomial: {theoretical_variance}")

# Distribución 2 - geométrica

def geometrical_distribution(p, sizes):
    samples = [geom.rvs(p, size=size) for size in sizes]
    return samples, sizes

def second_distribution(p, sizes):
    samples, sizes = geometrical_distribution(p, sizes)
    create_boxplots(samples, sizes)
    create_histograms(samples, sizes)
    calc_median(samples, sizes)
    calc_mode(samples, sizes)
    calc_mean(samples, sizes)
    calc_variance(samples, sizes)
    theoretical_mean = 1 / p
    theoretical_variance = (1 - p) / (p ** 2)
    print(f"Esperanza teórica de la distribución geométrica: {theoretical_mean}")
    print(f"Varianza teórica de la distribución geométrica: {theoretical_variance}")

# Distribución 3 - Poisson

def poisson_distribution(l, sizes):
    samples = [poisson.rvs(l, size=size) for size in sizes]
    return samples, sizes

def third_distribution(l, sizes):
    samples, sizes = poisson_distribution(l, sizes)
    create_boxplots(samples, sizes)
    create_histograms(samples, sizes)
    calc_median(samples, sizes)
    calc_mode(samples, sizes)
    calc_mean(samples, sizes)
    calc_variance(samples, sizes)
    theoretical_mean = l
    theoretical_variance = l
    print(f"Esperanza teórica de la distribución de Poisson: {theoretical_mean}")
    print(f"Varianza teórica de la distribución de Poisson: {theoretical_variance}")
    
# Funciones auxiliares

def calc_mode(samples, sizes):
    for i, sample in enumerate(samples):
        mode_val = mode(sample)[0]
        print(f"Muestra de tamaño {sizes[i]}: Moda = {mode_val}")

def calc_median(samples, sizes):
    for i, sample in enumerate(samples):
        median = np.median(sample)
        print(f"Muestra de tamaño {sizes[i]}: Mediana = {median}")

def calc_mean(samples, sizes):
    for i, sample in enumerate(samples):
        mean = np.mean(sample)
        print(f"Muestra de tamaño {sizes[i]}: Media empírica = {mean}")

def calc_variance(samples, sizes):
    for i, sample in enumerate(samples):
        variance = np.var(sample, ddof=1)  # ddof=1 para obtener la varianza muestral
        print(f"Muestra de tamaño {sizes[i]}: Varianza empírica = {variance}")

def create_boxplots(samples, sizes):
    plt.figure(figsize=(8, 4))
    for i, sample in enumerate(samples):
        plt.subplot(2, 2, i + 1)
        plt.boxplot(sample, vert=False, patch_artist=True)
        plt.title(f"Diagrama de Cajas para n={sizes[i]}")
        plt.xlabel('Valores de la muestra')
        plt.ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()

def create_histograms(samples, sizes):
    plt.figure(figsize=(8, 4))
    for i, sample in enumerate(samples):
        plt.subplot(2, 2, i + 1)
        plt.hist(sample, bins=20, edgecolor='black')
        plt.title(f"Histograma para n={sizes[i]}")
        plt.xlabel('Valores de la muestra')
        plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

# Función principal

def main():
    sizes = [10**2, 10**3, 10**4, 10**5]
    print("Distribución binomial")
    first_distribution(100, 0.35, sizes)
    print("Distribución geométrica")
    second_distribution(0.3, sizes)
    print("Distribución de Poisson")
    third_distribution(30, sizes)

main()
