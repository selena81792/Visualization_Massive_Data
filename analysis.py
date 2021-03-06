import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('data.csv', sep = ';')
df = df.drop(0)  # remove useless type data line

my_columns = df.columns.to_list()[1:45]
for i in my_columns:
   df[i] = df[i].astype('float')   # float type for all except country name
# df.info()

area = df["Area(sq km)"].dropna()
print("\n===============\nCountry Area\n===============\n")
print("Maximum:", area.max() )
print("Minimum:", area.min() )
def my_mean(x):
    return np.average(x, weights=np.ones_like(x) / x.size)

print("Mean:", area.mean() )
print("Std:", area.std() )

gdp_per_capita = df["GDP - per capita"].dropna()
print("\n===============\nGDP - per capita\n===============\n")
print("Maximum:", gdp_per_capita.max() )
print("Minimum:", gdp_per_capita.min() )
def my_mean(x):
    return np.average(x, weights=np.ones_like(x) / x.size)

print("Mean:", gdp_per_capita.mean() )
print("Std:", gdp_per_capita.std() )
