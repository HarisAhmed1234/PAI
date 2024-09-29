import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

filtered_data = df[(df['Year'] == 1987) | (df['Year'] == 1989)]

print(filtered_data)
