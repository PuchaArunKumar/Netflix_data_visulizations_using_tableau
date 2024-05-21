import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df['cast'] = df['cast'].fillna('Anonymous')
df['country'] = df['country'].fillna('Anonymous')
df=df.dropna()
print(df)
print(df.info())
print(df.isna().sum())
df.to_csv('Netflix_titles(1).csv')