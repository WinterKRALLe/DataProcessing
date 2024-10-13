import pandas as pd

from task_1.genre_frequencies import plot_genre_frequencies
from task_2.correlation import calculate_correlation
from task_3.correlation_per_year import calculate_correlation_per_year, plot_correlation_over_years
from task_4.sports_sales import analyze_sports_sales
from task_5.regional_percentage_of_global_sales import regional_percentage_of_global_sales
from task_6.total_sales_by_year import total_sales_by_year
from task_7.top_5_games_by_region import top_5_games_by_region


def filter_data_by_year(data, start_year, end_year):
    return data[(data['Year'] >= start_year) & (data['Year'] < end_year)]


def main():
    data = pd.read_csv('data/vgsales.csv')

    if data is None:
        return

    # 1
    filtered_data = filter_data_by_year(data, 1990, 2000)
    plot_genre_frequencies(filtered_data)
    # 2
    correlation = calculate_correlation(data, 'NA_Sales','EU_Sales')
    print(f"Korelační koeficient mezi NA_Sales a EU_Sales: {correlation}")
    # 3 
    correlation_values = calculate_correlation_per_year(data, 1985,2010, 'NA_Sales', 'EU_Sales')
    plot_correlation_over_years(correlation_values, 1985, 2010)
    # 4
    analyze_sports_sales(data)
    # 5
    regional_percentage_of_global_sales(data)
    # 6
    total_sales_by_year(filtered_data)
    # 7
    top_5_games_by_region(data)


if __name__ == "__main__":
    main()
