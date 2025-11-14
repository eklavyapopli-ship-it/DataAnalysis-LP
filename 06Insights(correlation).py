import pandas as pd
import math
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
duration = []
calories = []
a = []
b = []
n = []
denom1 = []
denom2 = []
for x in df['Duration']:
    duration.append(x)
xm = sum(duration)/len(duration)
for y in df['Calories']:
    calories.append(y)
ym = sum(calories)/len(calories)
for xi in duration:
    a.append(xi-xm)

for yi in calories:
    b.append(yi-ym)

# calculating correlation
for i in range(len(a)):
    n.append(a[i] * b[i])
    p = a[i]**2
    denom1.append(p)
    q = b[i]**2
    denom2.append(q)
numerator = sum(n)
s = sum(denom1)
t = sum(denom2)
denominator = math.sqrt(s*t)
v = numerator/denominator
print(f"the correlation between DURATION AND CALORIES IS : {v}")



