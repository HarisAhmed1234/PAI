import pandas as pd

data = {'name': ['Ali', 'Haris', 'Sara', 'Faizan', 'Ayesha'],
        'age': [25, 22, 28, 24, 26]}

df = pd.DataFrame(data)

df.index = range(101, 101 + len(df))

print(df)
