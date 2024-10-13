import matplotlib.pyplot as plt


def regional_percentage_of_global_sales(df):
    """
    Vypočítá procentuální podíl prodejů podle regionu a vytvoří koláčové grafy pro top 3 hry podle globálních prodejů.
    """
    # Výpočet procentuálních podílů
    df = df.assign(
        NA_percent=lambda x: (x['NA_Sales'] / x['Global_Sales'].replace(0, 1)) * 100,
        EU_percent=lambda x: (x['EU_Sales'] / x['Global_Sales'].replace(0, 1)) * 100,
        JP_percent=lambda x: (x['JP_Sales'] / x['Global_Sales'].replace(0, 1)) * 100,
        Other_percent=lambda x: (x['Other_Sales'] / x['Global_Sales'].replace(0, 1)) * 100,
    )

    top_3 = df[['Name', 'Global_Sales', 'NA_percent', 'EU_percent', 'JP_percent', 'Other_percent']].sort_values(by='Global_Sales', ascending=False).head(3)

    for _, row in top_3.iterrows():
        plot_pie_chart(row)


def plot_pie_chart(row):
        labels = ['NA', 'EU', 'JP', 'Other']
        sizes = [row['NA_percent'], row['EU_percent'], row['JP_percent'], row['Other_percent']]
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title(f'Procentuální podíl prodejů pro {row["Name"]}')
        plt.savefig(f'results/task_5_{row["Name"].replace(" ", "_")}.png')
        plt.close()
