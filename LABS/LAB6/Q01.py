import pandas as pd

data = {'movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
        'revenue': [3000000, 2500000, 500000, 1000000, 4500000],
        'budget': [800000, 500000, 1200000, 900000, 700000]}

df = pd.DataFrame(data)

filtered_movies = df[(df['revenue'] > 2000000) & (df['budget'] < 1000000)]

print(filtered_movies)
