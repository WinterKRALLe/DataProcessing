import matplotlib.pyplot as plt


def top_5_games_by_region(df):
    """
    Vykreslí 5 nejlepších her podle prodejů v Severní Americe, Evropě a Japonsku.
    """
    regiony = ['NA_Sales', 'EU_Sales', 'JP_Sales']
    
    for region in regiony:
        top_5 = df[['Name', region, 'Global_Sales']].sort_values(by=region, ascending=False).head(5)

        ax = top_5.plot(kind='bar', x='Name', y=[region, 'Global_Sales'], title=f'5 Nejlepších her v {region[:-6]}', figsize=(10, 6))
        
        plt.ylabel('Prodeje (v milionech)')
        
        for i in range(len(top_5)):
            ax.text(i, top_5[region].iloc[i] + 0.5, str(round(top_5[region].iloc[i], 2)), ha='center')

        plt.tight_layout()
        
        plt.savefig(f'results/task_7_top_5_games_by_region_{region[:-6]}.png')
        plt.close()
