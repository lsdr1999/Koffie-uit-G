from station import Station

class Trajectory(object):
    """"""

    def __init__(self):
        super(, self).__init__()
        self.maxLength = 120
        self.length = 0
        self.visitedStations = []

    def addConnections (connection):
        self.visitedStations.append(connection)

    def addTime (time):
        if (self.length < self.maxLength):
            self.length += time
            return True
        else:
            return False
