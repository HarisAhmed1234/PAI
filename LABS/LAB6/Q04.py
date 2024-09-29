import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'attempts': [1, 2, 1, 2]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df.index = range(100, 100 + len(df))

print("\nDataFrame with custom index starting at 100:")
print(df)
