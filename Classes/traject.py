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

    def calculateVisitedCritical(self, railroad):
        for connection in self.connections:
            if railroad.station_dict[connection[0]][3] or railroad.station_dict[connection[1]][3]:
                self.visitedCritical.update(connection)

    def calculateLength(self):
        length = 0
        for connection in self.connections:
            length += connection[2]
        self.length = length
