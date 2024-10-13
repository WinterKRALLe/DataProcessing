import matplotlib.pyplot as plt
import numpy as np


def calculate_correlation_per_year(data, start_year, end_year, col1, col2):
    """
    Vypočítá korelační koeficient mezi dvěma sloupci pro každý rok v daném rozsahu.
    """
    correlation_values = {}

    for year in range(start_year, end_year + 1):
        year_data = data[data['Year'] == year]
        correlation = year_data[col1].corr(year_data[col2])
        correlation_values[year] = correlation
    return correlation_values


def plot_correlation_over_years(correlation_values, start_year, end_year):
    """
    Vykreslí korelační koeficienty pro jednotlivé roky.
    """
    plt.figure(figsize=(10, 6))
    years = list(correlation_values.keys())
    correlations = list(correlation_values.values())

    valid_correlations = [c for c in correlations if c is not None]

    min_corr = np.floor(min(valid_correlations) * 10) / 10
    max_corr = np.ceil(max(valid_correlations) * 10) / 10
    plt.plot(years, correlations, marker='o', linestyle='-',color='skyblue')
    plt.title(f'Korelace mezi NA_Sales a EU_Sales v letech{start_year} až {end_year}')
    plt.xlabel('Rok')
    plt.ylabel('Korelační koeficient')
    plt.ylim(min_corr, max_corr)
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('results/task_3_correlation_per_year.png')
    plt.close() 
