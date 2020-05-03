import json
def openScheduleFile():
    with open('schedule.json') as jsonFile:
        data = json.load(jsonFile)
    jsonFile.close()
    return data

def openFreeTimeFile():
    with open('freeTime.json') as jsonFile:
        freeTimeData = json.load(jsonFile)
    jsonFile.close()
    return freeTimeData

def initializeSchedule(data):
    for day, activity in data.items():
        weekCheck = False
        while weekCheck == False:
            total = 0
            for activity, time in activity.items():
                dayCheck = False
                while dayCheck != True:
                    print("How much is your " + activity + " time for " + day + "?")
                    userInput = int(input())
                    if userInput <= 24 and userInput >= 0:
                        data[day][activity] = userInput
                        total += userInput
                        dayCheck = True
                    else:
                        print("Invalid Time")
            if total < 24:
                weekCheck = True
                jsonFile = open('schedule.json', 'w')
                json.dump(data, jsonFile, indent=2)
                jsonFile.close()
            else:
                print("Error! Your today activity time is more than 24 hours!")
                print("Please reschedule your " + day + " activites")
                activity = data[day]

def calculateBusyTime(data):
    weekBusyTime = 0
    for day, activity in data.items():
        dayBusyTime = 0
        for activity, time in activity.items():
            dayBusyTime += time
        weekBusyTime += dayBusyTime
        print("You have " + str(dayBusyTime) + " hours of busy time on " + day + "s")
    print("You have " + str(weekBusyTime) + " of busy time in a week")

def calculateFreeTime(data,freeTime):
    weekFreeTime = 0
    for day, activity in data.items():
        dayTotalBusyTime = 0
        for activity, time in activity.items():
            dayTotalBusyTime += time
        dayFreeTime = 24 - dayTotalBusyTime
        weekFreeTime += dayFreeTime
        freeTime[day] = dayFreeTime
        jsonFile = open('freeTime.json', 'w')
        json.dump(freeTime, jsonFile, indent=2)
        jsonFile.close()
        print("You have " + str(dayFreeTime) + " hours of free time on " + day + "s")
    print("You have " + str(weekFreeTime) + " of free time in a week")



def addActivity(data,freeTimeData):
    userTerminate = 'n'
    while userTerminate != 'y':
        dayCheck = False
        while dayCheck != True:
            userInputDay = input("Enter the day you want to add activity: ").capitalize()
            for key in data.keys():
                if key == userInputDay:
                    dayCheck = True
                    break
            if dayCheck == False:
                print("Enter a valid week day!")
        userActivity = input("What activity do you want to add to " + userInputDay + ": ").capitalize()
        dayTimeCheck = False
        while dayTimeCheck != True:
            userTime = int(input("How many hours do you do " + userActivity + " on " + userInputDay + "s: "))
            if userTime >= 24 or userTime <= 0:
                print("Invalid Time!")
            elif userTime > freeTimeData[userInputDay]:
                print("You don't have that much free time on " + userInputDay + "s")
            else:
                data[userInputDay][userActivity] = userTime
                jsonFile = open("schedule.json", "w")
                json.dump(data, jsonFile, indent=2)
                jsonFile.close()

                freeTimeData[userInputDay] -= userTime
                jsonFile = open("freeTime.json", "w")
                json.dump(freeTimeData, jsonFile, indent=2)
                jsonFile.close()
                print("Done!")
                break
        userTerminate = input('Do you want to exit? (y/n): ')

def ShowSchedule(data):
    for day, activity in data.items():
        print("---------------------- " + day.upper() + " ----------------------")
        for item, time in activity.items():
            print(item + ": " + str(time), "hours", end="  ")
        print("\n")


def main():
    data = openScheduleFile()
    freeTimeData = openFreeTimeFile()
    initializeSchedule(data)
    print("\nYour Free Times: ")
    calculateFreeTime(data,freeTimeData)
    print("\nYour Busy Times: ")
    calculateBusyTime(data)
    print("\nAdd any activity you would like, to your schedule!")
    addActivity(data,freeTimeData)
    ShowSchedule(data)
main()