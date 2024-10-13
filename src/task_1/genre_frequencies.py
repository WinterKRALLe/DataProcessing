import matplotlib.pyplot as plt


def plot_genre_frequencies(filtered_data):
    """
    Vykreslí četnost žánrů her mezi lety 1990 a 2000.
    """
    genre_counts = filtered_data['Genre'].value_counts()

    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='bar', color='skyblue')
    
    plt.title('Četnost žánrů her mezi lety 1990 a 2000')
    plt.xlabel('Žánr')
    plt.ylabel('Počet her')
    plt.xticks(rotation=45)
    
    for i, count in enumerate(genre_counts):
        plt.text(i, count + 0.5, str(count), ha='center')

    plt.tight_layout()
    plt.savefig('results/task_1_genre_frequencies.png')
    plt.close()
