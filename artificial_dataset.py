import numpy as np
import pandas as pd

n = 300
data = {
        'Age': np.random.normal(25, 5, n).astype(int),
        'Salary': np.random.normal(4000, 1000, n).astype(int),
        'Love': np.random.normal(0.8, 0.5, n).astype(int),
        'Pets': np.random.normal(2.5, 1, n).astype(int),
        'Health': np.random.normal(24, 3, n),
       }

health = (10000 - (data['Salary']) - (10 * np.random.randn(n) + 50)) / 100    #health negative correlate with salary
happiness = (data['Love'] + data['Pets']) * (10 * np.random.randn(n) + 50)    #happiness correlate with Love and Pets

data['Health'] = health
data['Happiness'] = happiness

df = pd.DataFrame(data=data)
df

df.to_csv('artificial_data.csv')  
