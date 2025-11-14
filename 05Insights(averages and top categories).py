import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

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






    