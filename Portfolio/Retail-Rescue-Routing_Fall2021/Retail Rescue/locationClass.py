class Location:
    def __init__(self, index, locationID, locationName, locationAddress, hasTimeWindow, startTime, endTime, unavailableStart, unavailableEnd, serviceTime, locationType, pounds, distances, arrivalTime):
        self.index = index
        self.locationID = locationID
        self.locationName = locationName
        self.locationAddress = locationAddress
        self.hasTimeWindow = hasTimeWindow
        self.startTime = startTime
        self.endTime = endTime
        self.unavailableStart = unavailableStart
        self.unavailableEnd = unavailableEnd
        self.serviceTime = serviceTime
        self.locationType = locationType
        self.pounds = pounds
        self.distances = distances
        self.arrivalTime = arrivalTime

        if self.locationType == 0:
            self.pounds = self.pounds * -1


    def getLocation(self):
        return str(self.locationID) + ", " + str(self.startTime) + ", " + str(self.endTime) + ", " + str(self.serviceTime) + ", " + str(self.locationType) + ", " + str(self.pounds) + ", " + str(self.distances)

    def getLocationDetails(self):
        type = ""
        if self.locationType == 1:
            type = "Donor# "
        elif self.locationType == 0:
            type = "Agency# "
        time = self.convertMinutes()
        return str(self.locationName) + "\n" + str(self.locationAddress) + '\n' + type + str(self.locationID) + "\n" + str(time)


    def getIndex(self):
        return self.index
    def setIndex(self, index):
        self.index = index

    def getLocationID(self):
        return self.locationID
    def setLocationID(self, id):
        self.locationID = id

    def getLocationName(self):
        return self.locationName
    def setLocationName(self, name):
        self.locationName = name

    def getLocationAddress(self):
        return self.locationAddress
    def setLocationAddress(self, name):
        self.locationAddress = name

    def getHasTimeWindow(self):
        return self.hasTimeWindow
    def setHasTimeWindow(self, hasTimeWindow):
        self.hasTimeWindow = hasTimeWindow

    def getStartTime(self):
        return self.startTime
    def setStartTime(self, start):
        self.startTime = start

    def getEndTime(self):
        return self.endTime
    def setEndTime(self, end):
        self.endTime = end
    def extendEndTime(self, extension):
        self.endTime += extension

    def getUnavailableStart(self):
        return self.unavailableStart
    def setUnavailableStart(self, start):
        self.unavailableStart = start

    def getUnavailableEnd(self):
        return self.unavailableEnd
    def setUnavailableEnd(self, end):
        self.unavailableEnd = end

    def getServiceTime(self):
        return self.serviceTime
    def setServiceTime(self, service):
        self.serviceTime = service

    def getLocationType(self):
        return self.locationType
    def setLocationType(self, type):
        self.locationType = type

    def getPounds(self):
        return self.pounds
    def setPounds(self, lbs):
        self.pounds = lbs

    def getDistances(self):
        return self.distances
    def setDistances(self, minutes):
        self.distances = minutes

    def getArrivalTime(self):
        return self.arrivalTime
    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime

    def convertMinutes(self):
        hour = self.arrivalTime // 60 + 7
        minutes = self.arrivalTime % 60 + 30

        if minutes >= 60:
            hour += 1
            minutes -= 60


        return "%d:%02d" % (hour, minutes)
      


    