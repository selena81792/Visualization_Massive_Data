import matplotlib.pyplot as plt
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
# print(df.head())


def plot_bar(my_data_choice, my_parameter_choice):
    df.sort_values(by=[my_data_choice], inplace=True, ascending=False)
    df2 = df[:my_parameter_choice].copy()
    df2.dropna(subset=[my_data_choice])
    
    # df2 = pd.concat([df2, new_row])
    plt.title(my_data_choice + ' of top ' + str(my_parameter_choice) + ' countries')
    plt.bar(df2['Country'], df2[my_data_choice], width=0.8, bottom=None, align='center')
    plt.show()
    plt.close()

my_data_choice_number = 1
my_parameter_choice = 10
my_parameter_choice_min = 2
my_parameter_choice_max = 30
def my_data_choice_words(x):
    return {
        1: 'Area(sq km)',
        2: 'GDP',
        3: 'Population',
        4: 'Internet users',
    }[x]

print('Please enter type of data to visualize: (enter a number 1-4)')
print('1) country size (sq km) (default)')
print('2) GDP')
print('3) Population')
print('4) Internet users')
user_input = -1
user_input_raw = input()
try:
    user_input = int(user_input_raw)
    if (user_input < 1 or user_input > 4):
        user_input = 1
except ValueError:
    user_input = 1
my_data_choice_number = user_input

print('Please enter how many countries to show: (enter a number, default 10)')
user_input = -1
user_input_raw = input()
try:
    user_input = int(user_input_raw)
    if (user_input < 2 or user_input > 30):
        user_input = 10
except ValueError:
    user_input = 10
my_parameter_choice = user_input

print(my_data_choice_words(my_data_choice_number))

plot_bar(my_data_choice_words(my_data_choice_number), my_parameter_choice)