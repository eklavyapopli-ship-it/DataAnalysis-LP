import pandas as pd

df = pd.read_csv('data.csv')
df['Calories'] = df['Calories'].astype(int)
df.to_csv('data.csv', index=False)
print(df)
