import json
jsonFile = open('schedule.json', 'r')
data = json.load(jsonFile)
jsonFile.close()
weekBusyTime = 0
for day, activity in data.items():
    dayBusyTime = 0
    for activity, time in activity.items():
        dayBusyTime += time
    weekBusyTime += dayBusyTime
    print("You have " + str(dayBusyTime) + " hours of busy time on " + day + "s")
print("You have " + str(weekBusyTime) + " of busy time in a week")
