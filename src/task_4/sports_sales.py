def analyze_sports_sales(data):
    """
    Analyzuje prodeje sportovních her v datech a vypisuje statistiky.
    """
    print('Task 4:')
    
    sports_data = data[data['Genre'] == 'Sports'].copy()
    
    sports_data['Sales_Difference'] = sports_data['NA_Sales'] - sports_data['EU_Sales']
    
    stats = sports_data['Sales_Difference'].agg(['min', 'max', 'mean', 'std'])
    
    min_game = sports_data.loc[sports_data['Sales_Difference'].idxmin(), 'Name']
    max_game = sports_data.loc[sports_data['Sales_Difference'].idxmax(), 'Name']
    
    print(f"Minimální rozdíl: {stats['min']} (Hra: {min_game})")
    print(f"Maximální rozdíl: {stats['max']} (Hra: {max_game})")
    print(f"Průměr: {stats['mean']}")
    print(f"Směrodatná odchylka: {stats['std']}")
