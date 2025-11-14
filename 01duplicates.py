import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
if df.duplicated().any():
    print(True)
    df.drop_duplicates(inplace=False, keep='first', subset=None )
    df.to_csv('data.csv', index=True)
else:
    print(False)


