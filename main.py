import pandas as pd
import matplotlib.pyplot as plt
import math
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
if df.duplicated().any():
    df.drop_duplicates(inplace=False, keep='first', subset=None )
else:
    print("no duplicate found")
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df['Calories'] = df['Calories'].astype(int)
df.to_csv('data.csv', index=True)

# Insights
# avergaes and top categories
listCalories = []
listDuration = []
listPulse = []
listMaxPulse = []
fullList = [listCalories, listDuration, listPulse, listMaxPulse]


for c in df['Calories']:
    fullList[0].append(c)
ListCaloriesSum = sum(listCalories)
averageCalories = ListCaloriesSum/len(listCalories)
print(f"the average calories burned is {averageCalories}")

# ----*------* #

for w in df['Duration']:
    fullList[1].append(w)
listDurationSum = sum(listDuration)
averageDuration = listDurationSum/len(listDuration)
print(f"the average workout duration is {averageDuration}")

# ----*------* #


for p in df['Pulse']:
    fullList[2].append(p)
listPulseSum = sum(listPulse)
averagePulse = listPulseSum/len(listPulse)
print(f"the average pulse rate is {averagePulse}")
# ----*------* #


for m in df['Maxpulse']:
    fullList[3].append(m)
listMaxPulseSum = sum(listMaxPulse)
averageMaxPulse = listMaxPulseSum/len(listMaxPulse)
print(f"the average pulse rate is {averageMaxPulse}")

# ----*------* #
MaxCaloriesBurned = max(listCalories)
indexCalories = listCalories.index(MaxCaloriesBurned)
print(f"the workout with max calories burned is {df.iloc[indexCalories]}")


# ----*------* #
MinCaloriesBurned = min(listCalories)
indexCalories = listCalories.index(MinCaloriesBurned)
print(f"the workout with min calories burned is {df.iloc[indexCalories]}")


# ----*------* #
MaxWorkoutDuration = max(listDuration)
indexCalories = listDuration.index(MaxWorkoutDuration)
print(f"the workout with max workout duration is {df.iloc[indexCalories]}")


# ----*------* #
MinWorkoutDuration = min(listDuration)
indexCalories = listDuration.index(MinWorkoutDuration)
print(f"the workout with min workout duration is {df.iloc[indexCalories]}")

# Pearson's Correlation
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


# Calories and Duration Relationship
duration = []
calories = []
Efficiency = []
for j in df['Calories']:
    calories.append(j)
for i in df['Duration']:
    duration.append(i)


numerator = sum(calories)
denominator = sum(duration)
for k in range(len(duration)):
    Efficiency.append(numerator/denominator)
maxEfficiency = max(Efficiency)
leastEfficiency = min(Efficiency)
averageEfficiency = sum(Efficiency)/len(Efficiency)
indexMaxEfficiency = Efficiency.index(maxEfficiency)
indexMinEfficiency = Efficiency.index(leastEfficiency)
print(f"the max efficiency is {maxEfficiency} and the data is {df.iloc[indexMaxEfficiency]}")
print(f"the min efficiency is {leastEfficiency} and the data is {df.iloc[indexMinEfficiency]}")
print(f"the average efficiency is {averageEfficiency}")


# Ploting Graph of the above relationship
plt.plot(duration, Efficiency)
plt.xlabel("Workout Session Number")
plt.ylabel("Efficiency (Total Calories / Total Duration)")
plt.title("Workout Efficiency Trend")
plt.show()






    



