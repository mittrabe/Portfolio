class Truck:
    def __init__(self, driverNum, route, routeTime, maxCapacity, currentCapacity):
        self.driverNum = driverNum
        self.route = route
        self.routeTime = routeTime
        self.maxCapacity = maxCapacity
        self.currentCapacity = currentCapacity
        self.routeValid = True


    #===================
    #   CONSTRAINTS
    #===================

    #check that the length of the route is less than the max shift length
    #def checkRouteTime(self):


    #checks that the trucks capacity stays between the 0 and the max capacity
    def checkCapacity(self):
        if(self.currentCapacity > self.maxCapacity or self.currentCapacity < 0):
            self.routeValid = False

    #checks if truck arrives at stop within the allowed time window
    def checkArrivalTime(self, stop, arrivalTime):
        #the -15 and +15 are meant to give some slack to locations with very narrow time windows
        if(arrivalTime < stop.getStartTime()-30 or arrivalTime > stop.getEndTime()+30):
            self.routeValid = False
        
        #makes route invalid if a stop occurs or is still occuring during a specific time window locations are unavailable 
        if(arrivalTime >= stop.getUnavailableStart()-stop.getServiceTime() and arrivalTime <= stop.getUnavailableEnd()):
            self.routeValid = False

    def addStop(self, newStop, travelTime):
        arrivalTime = self.getRouteTime() + travelTime
        newStop.setArrivalTime(arrivalTime)
        self.route.append(newStop)
        self.checkArrivalTime(newStop, arrivalTime)
        self.setRouteTime(travelTime + newStop.getServiceTime())
        self.setCurrentCapacity(newStop.getPounds())
        self.checkCapacity()

    def validateRoute(self):
        return self.routeValid
    
    #===================
    #  GETTERS/SETTERS
    #===================
    def getDriverNum(self):
        return self.driverNum
    
    def setDriverNum(self, driverNum):
        self.route = driverNum

    def getRoute(self):
        return self.route
    
    def setRoute(self, newRoute):
        self.route = newRoute

    def getRouteTime(self):
        return self.routeTime
    
    def setRouteTime(self, timeTaken):
        self.routeTime += timeTaken 

    def getCurrentCapacity(self):
        return self.currentCapacity
    
    def setCurrentCapacity(self, pounds):
        self.currentCapacity = self.currentCapacity + pounds
    