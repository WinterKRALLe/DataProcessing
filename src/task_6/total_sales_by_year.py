import matplotlib.pyplot as plt


def total_sales_by_year(data):
    """
    Vykreslí celkové globální prodeje her mezi lety 1990 (včetně) a 2000 (vyjma).
    """
    yearly_sales = data.groupby('Year')['Global_Sales'].sum().reset_index()
    
    yearly_sales = yearly_sales[yearly_sales['Global_Sales'] > 0]

    if yearly_sales.empty:
        print("Žádná data k vykreslení.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(yearly_sales['Year'], yearly_sales['Global_Sales'], marker='o', linestyle='-', color='green')
    plt.title('Vývoj globálních prodejů her podle roku')
    plt.xlabel('Rok')
    plt.ylabel('Celkové globální prodeje (v milionech)')
    plt.grid(True)

    plt.savefig('results/task_6_total_sales_by_year.png')
    plt.close()
