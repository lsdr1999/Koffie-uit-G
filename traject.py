from station import Station

class Trajectory(object):
    """
    ljkdsjklfdjkafj
    """
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.length = 0
        self.visitedCritical = set()
        self.visitedStations = []

    def addVisitedStations(self, nextStation):
        self.visitedStations.append(nextStation)

    def addVisitedCritical(self, begin_station, end_station):
        """
        Adds a visited station to the list of visited station and adds it to
        the visitedConnectionCount if it is a critical connection
        """

        self.visitedCritical.add([begin_station, end_station])

    def addLength(self, time):
        self.length += time
