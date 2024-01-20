#These three will still be needed if we drop OR-Tools
import pandas as pd #pip install pandas
import numpy as np
import os
import datetime
from datetime import timedelta
import random
import string
import xlsxwriter


import locationClass
import truckClass

def getFilePath(filename):
    return os.path.realpath(__file__)+f'\\..\\{filename}' # Gets the current directory

#This method serves no purpose other than placing the variables potentially modified by them at the top/in an easily accessible location
def importData():
    days = ["Monday", "Friday"]
    numDriversPerDay = [3,3]

    dataList = []
    for i in range(len(days)):
        #matrix containing the time in minutes between locations
        matrix = pd.read_excel(getFilePath('timeMatrixMaker\\dailyTimeMatrices.xlsx'), sheet_name=days[i].title())
        #Matrix containing the time windows for locations
        dayData = pd.read_excel(getFilePath(f'{days[i].lower()}_data.xlsx'))

        maxCapacity = 10000

        daytaList = [matrix, dayData, numDriversPerDay[i], maxCapacity, days[i]] #haha, it's a pun
        dataList.append(daytaList)
    return dataList


def createLocations(matrix, dayData, numDrivers):

    #converts excel sheet to a list and casts the list to tuples
    timeWindows = dayData[['Time Start','Time End', 'Unavailable Start', 'Unavailable End']].to_numpy().tolist()
    tupleWindows = [tuple(elt) for elt in timeWindows]

    #Converts the time windows from time variables (hour:minute:seconds) to minutes since the start of the shift
    minuteWindows = []
    date = datetime.date(1, 1, 1)
    shiftStartTime = datetime.time(7, 0, 0)
    shiftStart = datetime.datetime.combine(date, shiftStartTime)
    for index, timeTuple in enumerate(tupleWindows):
        startTime = timeTuple[0]
        endTime = timeTuple[1]
        unavailableStart = timeTuple[2]
        unavailableEnd = timeTuple[3]

        date = datetime.date(1, 1, 1)
        start = datetime.datetime.combine(date, startTime) #the value need to be converted from a datetime.time type to a datetime.datetime type before they can be subtracted 
        end = datetime.datetime.combine(date, endTime)
        start_in_minutes = (start - shiftStart).total_seconds() / 60 #finds time difference between the time window and the shift start time (7:00 AM), converts it to seconds, and then into mintues
        end_in_minutes = (end - shiftStart).total_seconds() / 60

        unavailStart = datetime.datetime.combine(date, unavailableStart) 
        unavailEnd = datetime.datetime.combine(date, unavailableEnd)
        unavailStart_in_minutes = (unavailStart - shiftStart).total_seconds() / 60 
        unavailEnd_in_minutes = (unavailEnd - shiftStart).total_seconds() / 60

        minuteWindows.append((int(start_in_minutes), int(end_in_minutes), int(unavailStart_in_minutes), int(unavailEnd_in_minutes)))
        
    
    locations = []
    locationIDs = dayData[['Location ID']].to_numpy().ravel() # .ravel() removes the brackets around all the values
    locationName = dayData[['Location Name']].to_numpy().ravel()
    locationAddress = dayData[['Location Address']].to_numpy().ravel()
    hasTimeWindow = dayData[['Has Time Window']].to_numpy().ravel()
    serviceTime = dayData[['Service Time']].to_numpy().ravel()
    locationType = dayData[['Location Type']].to_numpy().ravel()
    pounds = dayData[['Pounds']].to_numpy().ravel()
    #matrix.drop('Location ID', axis=1, inplace=True)
    timeMatrix = matrix.values

    #In this order: locationIndex, locationID, locationName, locationAddress, hasTimeWindow, startTime, endTime, unavailableStart, unavailableEnd, serviceTime, locationType, pounds, distances, arrivalTime
    locations = []
    for i in range(len(locationIDs)):
        newLocation = locationClass.Location(i, locationIDs[i], locationName[i], locationAddress[i], hasTimeWindow[i], minuteWindows[i][0], minuteWindows[i][1], 
        minuteWindows[i][2], minuteWindows[i][3], serviceTime[i], locationType[i], pounds[i], timeMatrix[i], 0)

        #Extends the time window for unconstrainted locations by 60 minutes if the number of drivers is less than 3
        if(numDrivers < 3):
            if(newLocation.getHasTimeWindow() == False and numDrivers < 3):
                newLocation.extendEndTime(60)
        locations.append(newLocation)
    
    return locations


def createTrucks(numDrivers, maxCapacity, warehouse):
    #In this order: driverNum, route, maxCapacity, currentCapacity
    activeTrucks = []
    for i in range(numDrivers):
        newRoute = [warehouse]
        newTruck = truckClass.Truck("Driver " + str(i+1), newRoute, 15, maxCapacity, 0)
        activeTrucks.append(newTruck)

    return activeTrucks


def createRoutes(locations, trucks): #numSimulations represents the number of simulations (1 == 1 route per truck)

    def calculateTravelTime(currentStop, nextStop):
        return currentStop.getDistances()[nextStop.getIndex()]
    

    warehouse = locations.pop(0) #removes the warehouse from list of places to be visited
    random.shuffle(locations)

    currentTruck = 0
    leastTime = 0
    while locations: 
        stop = locations.pop(getBestLocationIndex(trucks[currentTruck], locations, trucks[currentTruck].getRoute()[-1].getArrivalTime()))
        # getBestLocationIndex(trucks[currentTruck], locations, trucks[currentTruck].getRoute()[-1].getArrivalTime())
        travelTime = calculateTravelTime(trucks[currentTruck].getRoute()[-1], stop)

        # # Checks if the next is an agency. If we have enough, go to the agency, otherwise readd agency to end and continue to next iter
        # if stop.getLocationType() == 0 and trucks[currentTruck].getCurrentCapacity()+stop.getPounds() < 0:
        #     # Check if any donors are left...            
        #     donors_remain = False
        #     for l in locations:
        #         if l.getLocationType() == 1:
        #             donors_remain = True
        #             break
        #     if donors_remain:
        #         locations.append(stop)
        #         continue
        #     else:
        #         return [None, 0]
        # # Same thing but with donor
        # elif stop.getLocationType() == 1 and trucks[currentTruck].getCurrentCapacity()+stop.getPounds() > trucks[currentTruck].maxCapacity:
        #     # Check if any agencies are left...
        #     agencies_remain = False
        #     for l in locations:
        #         if l.getLocationType() == 0:
        #             agencies_remain = True
        #             break
        #     if agencies_remain:
        #         locations.append(stop)
        #         continue
        #     else:
        #         return [None, 0]

        trucks[currentTruck].addStop(stop, travelTime)


        #Truck with the lowest current route time given next stop
        for truck in range(len(trucks)):
            if(trucks[truck].getRouteTime() <= trucks[currentTruck].getRouteTime()):
                currentTruck = truck
    
    numValid = 0
    fullRoute = []
    for truck in trucks:
        isValid = truck.validateRoute()
        if(isValid):
            numValid += 1
        fullRoute.append(truck)
    
    return [fullRoute, numValid]

def validate(truck, location, currentTime):
    # Check capacity
    if truck.getCurrentCapacity()+location.getPounds() > truck.maxCapacity or truck.getCurrentCapacity()+location.getPounds() < 0:
        return False
    # Check time
    if(currentTime < location.getStartTime()-30 or currentTime > location.getEndTime()+30):
        return False

def getBestLocationIndex(truck, locations, currentTime):
    # Gets the index of the next available location with the tightest timeframe (i.e. most tightly constrainted locations have priority)
    best = (0,10000) # index, amount of time
    for i in range(len(locations)):
        location = locations[i]
        if validate(truck, location, currentTime):
            timeframe = location.getEndTime() - location.getStartTime()
            if timeframe < best[1]: # If a tighter timeframe..
                best = (i,timeframe)
    return best[0]
    
def createPriorityList(dayData):
    
    priorityList = []
    
    timeWindows = dayData[['Location ID','Time Start','Time End']].to_numpy().tolist()
    print(timeWindows)
    
    
    for i in timeWindows:
        print(f"{i[0]} {i[1]} {i[2]}")
        locID = i[0]
        t1 = str(i[1])
        t2 = str(i[2])
        
        format = '%H:%M:%S'
        tdelta = datetime.strptime(t2, format) - datetime.strptime(t1, format)
        onehour = timedelta(minutes=60)
        print(tdelta)
        if tdelta < onehour:
            print('ADD TO LIST')
            priorityList.append(str(locID))
            print(priorityList)       


def export_schedule(weekRoutes):
    ids = []
    colnames = []
    df = pd.DataFrame()

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'schedule.xlsx')

    workbook = xlsxwriter.Workbook(filename)

    for day in weekRoutes:
        for truck in day[1]:
            df[truck.getDriverNum()] = pd.Series(truck.getRoute())
            colnames.append(truck.getDriverNum())
    
        
        worksheet = workbook.add_worksheet(day[0])
        worksheet.write_row(1,0,colnames)

        row = 2
        col = 0
        for truck in day[1]:
            for stop in truck.getRoute():
                worksheet.write(row, col, stop.getLocationDetails())
                row += 1
            col += 1
            row = 2
        
        worksheet.write(0, 0, day[0], workbook.add_format({'bold': True, 'color': '#E26B0A', 'size': 20}))

        # Create a format to use in the merged range.
        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#4d87e3',
            'font_size': 14})
        worksheet.merge_range("A1:C1", day[0] + " - Schedule", header_format)

        route_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'valign': 'vcenter'
        })
        route_format.set_text_wrap()
        for row in range(20):
            worksheet.set_row(row,60)
        worksheet.set_column(0,2,40, route_format)



    

    workbook.close()



def main():

    numSimulations = 10000
    validFullRoutes = []
    validRoutesCount = 0

    dataList = importData()
    weekRoutes = []
    for data in dataList:
        for i in range(numSimulations):
            locations = createLocations(data[0], data[1], data[2])
            activeTrucks = createTrucks(data[2],data[3], locations[0])
            dayOfWeek = data[4]

            results = createRoutes(locations, activeTrucks)
            validRoutesCount += results[1]
            if(results[1] == len(activeTrucks)):
                validFullRoutes.append(results[0])
        
        print("num trucks: " + str(len(activeTrucks)))
        print(str(numSimulations) + " simulations were ran. " + str(len(validFullRoutes)) + " were valid (all three trucks had valid routes)")
        #displays the number of individual trucks that had a valid route. This is for testing purposes
        print("a total of " + str(validRoutesCount) + " valid routes for a single truck were found")


        #Finds and prints the fastest rout
        fastestRouteTime = 0
        fastestRoute = []
        for fullRoute in validFullRoutes:

            totalRouteTime = 0
            for truck in fullRoute:
                totalRouteTime += truck.getRouteTime()
            
            if fastestRouteTime == 0: #used to set the fastest route during the first iteration
                fastestRouteTime = totalRouteTime
                fastestRoute = fullRoute

            elif fastestRouteTime > totalRouteTime: 
                fastestRouteTime = totalRouteTime
                fastestRoute = fullRoute


        print("[FASTEST GENERATED ROUTE]" +"\nTotal Route Time: " + str(fastestRouteTime) + "\nRoute Taken:")
        weekRoutes.append([dayOfWeek, fastestRoute])
        for truck in fastestRoute:
            for i in range(len(truck.getRoute())):
                stop = truck.getRoute()[i]
                print("Location: " + str(stop.getLocationID()) + " - " + str(stop.getLocationName()) +  " visited at: " + str(stop.getArrivalTime()))
            print("")

    export_schedule(weekRoutes)



    



if __name__ == '__main__':
    main()
