import numpy as np
from scipy.stats import binom, mode
import matplotlib.pyplot as plt

# Distribucion 1 - binomial

def binomial_distribution():
    n = 100
    p = 0.35
    sizes = [10**2, 10**3, 10**4, 10**5]
    samples = [binom.rvs(n, p, size=size) for size in sizes]
    return samples, sizes

def calc_mode_mean(samples, sizes):
    for i, sample in enumerate(samples):
        median = np.median(sample)
        mode_val = mode(sample)[0]
        print(f"Muestra de tamaño {sizes[i]}: Mediana = {median}, Moda = {mode_val}")

def create_boxplots(samples, sizes):
    plt.figure(figsize=(8, 4))  # Tamaño de la figura
    # Crear un diagrama de cajas para cada muestra
    for i, sample in enumerate(samples):
        plt.subplot(2, 2, i + 1)  # Crea los diagramas en una cuadricula de 2x2
        plt.boxplot(sample, vert=False, patch_artist=True)  # Crea el boxplot (diagrama) horizontal (patch_artist es para que tenga colorg)
        plt.title(f"Diagrama de Cajas para n={sizes[i]}")  # Título
        plt.xlabel('Valores de la muestra')  # titulo eje x
        plt.ylabel('Frecuencia')  # titulo del eje y

    plt.tight_layout()  # para que no se superponga
    plt.show()  # ventana emergente con los graficos
    
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
    
def main():
    samples, sizes = binomial_distribution()
    create_boxplots(samples, sizes)
    create_histograms(samples, sizes)
    calc_mode_mean(samples, sizes)

main()


