from station import Station
from railroad import Railroad

class Trajectory(object):
    """"""

    def __init__(self):
        super(, self).__init__()
        self.maxLength = 120
        self.length = 0
        self.connections = []

    def addConnection(start_station, next_station, time):
        self.connections.append([])

    def addTime (time):
        self.length += int(time)
