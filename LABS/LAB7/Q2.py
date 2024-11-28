import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("heart.csv")
print(data.head())  # First few rows

# Rename column
data = data.rename(columns={'sex': "gender"})

# Replace values in 'gender'
data['gender'] = data['gender'].replace({1: "M", 0: "F"})
print(data['gender'].unique())  # Check unique values

# Calculate mean
print("\nMean:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].mean())

# Calculate median
print("\nMedian:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].median())

# Calculate mode
print("\nMode:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].mode())
