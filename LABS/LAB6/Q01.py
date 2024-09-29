import pandas as pd

df = pd.read_csv('your_dataset.csv')

print(df.head())

filtered_movies = df[(df['revenue'] > 2000000) & (df['budget'] < 1000000)]

print(filtered_movies)

filtered_movies.to_csv('filtered_movies.csv', index=False)
