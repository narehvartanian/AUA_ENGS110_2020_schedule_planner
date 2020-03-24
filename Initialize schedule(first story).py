import json
with open("schedule1.json") as jsonFile:
    data = json.load(jsonFile)
jsonFile.close()
for day, activity in data.items():
    weekCheck = False
    while (weekCheck == False):
        total = 0
        for activity, time in activity.items():
            dayCheck = False
            while (dayCheck != True):
                print("How much is your " + activity + " time for " + day + "?")
                userInput = int(input())
                if(userInput < 24 and userInput >= 0):
                    data[day][activity] = userInput
                    total += userInput
                    dayCheck = True
                else:
                    print("Your inserted hour is invalid, please insert a number less than 24.")
        if (total < 24):
            weekCheck = True
            jsonFile = open("schedule1.json", "w")
            json.dump(data, jsonFile, indent=2)
            jsonFile.close()
        else:
            print("Error! Your activity time for today is more than 24 hours!")
            print("Please reschedule your " + day + " activites")
            activity = data[day]
