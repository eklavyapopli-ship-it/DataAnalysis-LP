import pandas as pd

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

df.to_csv('data.csv', index=False)
print(df)
