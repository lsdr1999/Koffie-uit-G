from station import Station

class Trajectory(object):
    """"""

    def __init__(self, maxLength):
        super(, self).__init__()
        self.maxLength = maxLength
        self.length = 0
        self.visitedCritical = set()
        self.visitedStations = []

    def addVisitedStations (nextStation):
        self.visitedStations.append(nextStation)

    def addVisitedCritical(begin_station, end_station):
		"""
		Adds a visited station to the list of visited station and adds it to
		the visitedConnectionCount if it is a critical connection
		"""
		self.visitedCritical.add([begin_station, end_station])

    def add__len__(time):
        self.length += time


        
