import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns

# Distribucion 1 - binomial

def binomial_distribution():
    n = 100
    p = 0.35
    sizes = [10**2, 10**3, 10**4, 10**5]
    samples = [binom.rvs(n, p, size=size) for size in sizes]
    return samples, sizes

def create_boxplots(samples, sizes):
    plt.figure(figsize=(8, 4))
    for i, sample in enumerate(samples):
        plt.subplot(2, 2, i + 1)
        sns.boxplot(sample)
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
    
def main():
    samples, sizes = binomial_distribution()
    # create_boxplots(samples, sizes)
    create_histograms(samples, sizes)

main()


