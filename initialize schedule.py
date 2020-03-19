import json
jsonFile = open('schedule.json', 'r')
data = json.load(jsonFile)
jsonFile.close()
for day, activity in data.items():
    for activity, time in activity.items():
        print("How much is your " + activity + " time for " + day + "?")
        data[day][activity] = int(input())
        jsonFile = open('schedule.json', 'w')
        json.dump(data, jsonFile)
        jsonFile.close()