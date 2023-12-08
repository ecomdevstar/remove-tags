import pandas as pd

df = pd.read_excel('Export_2023-12-08_043047.xlsx')

df['Tags'] = df['Tags'].str.replace('New, ', '')
df['Tags'] = df['Tags'].str.replace('New,', '')
df['Tags'] = df['Tags'].str.replace(', New', '')
df['Tags'] = df['Tags'].str.replace(',New', '')
df['Tags'] = df['Tags'].str.replace('New', '')

df.to_csv('output.csv')