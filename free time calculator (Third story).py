import json
jsonFile = open('schedule.json', 'r')
data = json.load(jsonFile)
jsonFile.close()
weekFreeTime = 0
for day, activity in data.items():
    dayTotalBusyTime = 0
    for activity, time in activity.items():
        dayTotalBusyTime += time
    dayFreeTime = 24 - dayTotalBusyTime
    weekFreeTime += dayFreeTime
    print("You have " + str(dayFreeTime) + " hours of free time on " + day + "s")
print("You have " + str(weekFreeTime) + " of free time in a week")

