import json

class JsonFile:

    def openScheduleFile(self):
        with open("schedule.json") as jsonFile:
            data = json.load(jsonFile)
        jsonFile.close()
        return data

    def openFreeTimeFile(self):
        with open("freeTime.json") as jsonFile:
            freeTimeData = json.load(jsonFile)
        jsonFile.close()
        return freeTimeData

jsonfile = JsonFile()


class Schedule:
    def __init__(self, data, freeTimeData):
        self.data = data
        self.freeTimeData = freeTimeData
    def initializeSchedule(self, data):
        self.data = data
        for day, activity in self.data.items():
            weekCheck = False
            while weekCheck == False:
                total = 0
                for activity, time in activity.items():
                    dayCheck = False
                    while dayCheck != True:
                        print("How much is your " + activity + " time for " + day + "?")
                        userInput = int(input())
                        if userInput <= 24 and userInput >= 0:
                            self.data[day][activity] = userInput
                            total += userInput
                            dayCheck = True
                        else:
                            print("Invalid Time")
                if total < 24:
                    weekCheck = True
                    jsonFile = open('schedule.json', 'w')
                    json.dump(self.data, jsonFile, indent=2)
                    jsonFile.close()
                else:
                    print("Error! Your today activity time is more than 24 hours!")
                    print("Please reschedule your " + day + " activities")
                    activity = self.data[day]

    def calculateBusyTime(self, data):
        self.data = data
        weekBusyTime = 0
        for day, activity in self.data.items():
            dayBusyTime = 0
            for activity, time in activity.items():
                dayBusyTime += time
            weekBusyTime += dayBusyTime
            print("You have " + str(dayBusyTime) + " hours of busy time on " + day + "s")
        print("You have " + str(weekBusyTime) + " of busy time in a week")

    def calculateFreeTime(self, data, freeTime):
        self.data = data
        self.freeTime = freeTime
        weekFreeTime = 0
        for day, activity in self.data.items():
            dayTotalBusyTime = 0
            for activity, time in activity.items():
                dayTotalBusyTime += time
            dayFreeTime = 24 - dayTotalBusyTime
            weekFreeTime += dayFreeTime
            self.freeTime[day] = dayFreeTime
            jsonFile = open('freeTime.json', 'w')
            json.dump(self.freeTime, jsonFile, indent=2)
            jsonFile.close()
            print("You have " + str(dayFreeTime) + " hours of free time on " + day + "s")
        print("You have " + str(weekFreeTime) + " of free time in a week")

    def addActivity(self, data, freeTimeData):
        self.data= data
        self.freeTimeData = freeTimeData
        userTerminate = 'n'
        while userTerminate != 'y':
            dayCheck = False
            while dayCheck != True:
                userInputDay = input("Enter the day you want to add activity: ").capitalize()
                for key in self.data.keys():
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
                elif userTime > self.freeTimeData[userInputDay]:
                    print("You don't have that much free time on " + userInputDay + "s")
                else:
                    self.data[userInputDay][userActivity] = userTime
                    jsonFile = open("schedule.json", "w")
                    json.dump(self.data, jsonFile, indent=2)
                    jsonFile.close()

                    self.freeTimeData[userInputDay] -= userTime
                    jsonFile = open("freeTime.json", "w")
                    json.dump(self.freeTimeData, jsonFile, indent=2)
                    jsonFile.close()
                    print("Done!")
                    break
            userTerminate = input('Do you want to exit? (y/n): ')

    def ShowSchedule(self, data):
        self.data = data
        for day, activity in self.data.items():
            print("---------------------- " + day.upper() + " ----------------------")
            for item, time in activity.items():
                print(item + ": " + str(time), "hours", end="  ")
            print("\n")

def main():
    userSchedule = Schedule(jsonfile.openScheduleFile(), jsonfile.openFreeTimeFile())
    userSchedule.initializeSchedule(jsonfile.openScheduleFile())
    userSchedule.calculateBusyTime(jsonfile.openScheduleFile())
    print()
    userSchedule.calculateFreeTime(jsonfile.openScheduleFile(), jsonfile.openFreeTimeFile())
    userSchedule.addActivity(jsonfile.openScheduleFile(), jsonfile.openFreeTimeFile())
    userSchedule.ShowSchedule(jsonfile.openScheduleFile())

main()
