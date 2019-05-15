
class Station(object):
    """
    Defines a station object, a station has a name, coordinates, and has
    connections with other stations that take a certain time to reach
    """

    def __init__(self, name, xCoordinate, yCoordinate, critical):
        """
        Initializes a station object
        """
        self.name = name
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.connections = []
        self.critical = critical

    def addConnection(self, name, time, critical, id):
        self.connections.append([name, time, critical, id])
