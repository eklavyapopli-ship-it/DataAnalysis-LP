import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
#  we will be calculating Efficiency and then max , mean and min efficiency
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


# ploting the graph
plt.plot(duration, Efficiency)
plt.xlabel("Workout Session Number")
plt.ylabel("Efficiency (Total Calories / Total Duration)")
plt.title("Workout Efficiency Trend")
plt.show()