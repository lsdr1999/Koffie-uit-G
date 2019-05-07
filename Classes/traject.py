from Classes import station

class Trajectory(object):
    """
    ljkdsjklfdjkafj
    """
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.length = 0
        self.visitedCritical = set()
        self.visitedStations = []
        self.connections = []

    def addVisitedStations(self, nextStation):
        self.visitedStations.append(nextStation)

    def addConnection(self, start_station, next_station, time):
        self.connections.append([start_station, next_station, time])

    def addVisitedCritical(self, id):
        """
        Adds a visited station to the list of visited station and adds it to
        the visitedConnectionCount if it is a critical connection
        """
        self.visitedCritical.add(id)

    def calculateLength(self):
        length = 0
        for connection in self.connections:
            length += connection[2]
        self.length = length
