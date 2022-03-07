import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv', sep = ';')
df = df.drop(0)  # remove useless type data line

my_columns = df.columns.to_list()[1:45]
for i in my_columns:
   df[i] = df[i].astype('float')   # float type for all except country name

# df.info()
# print(df.head())


df = df.dropna(subset=['GDP - per capita']).dropna(subset=['Internet users'])
estimator = LinearRegression()

X = df['GDP - per capita'].values.reshape(-1, 1)
y = df['Internet users'].values.reshape(-1, 1)
# Fit inputs to outputs
estimator.fit(X, y)

print(f"estimator score: {estimator.score(X, y)}")
print(f"etimator coefficient: {estimator.coef_}")
print(f"estimator b: {estimator.intercept_}")
