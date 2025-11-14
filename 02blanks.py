import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
df.dropna(inplace=True)
df.to_csv('data.csv', index=False)
print(df)
