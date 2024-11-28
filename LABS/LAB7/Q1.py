import numpy as np
import pandas as pd

df = pd.read_csv("heart.csv")
df.columns
df.info()
print(df.describe())
