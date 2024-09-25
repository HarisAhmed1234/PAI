import pandas as pd

df = pd.read_csv('movies.csv')

print("Original DataFrame:")
print(df)

sorted_movies = df.sort_values(by='runtime', ascending=False)

print("\nSorted DataFrame by Runtime (Descending):")
print(sorted_movies)

sorted_movies.to_csv('sorted_movies.csv', index=False)
