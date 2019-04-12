class Station(object):
    """
    Defines a station object, a station has a name, coordinates, and has
    connections with other stations that take a certain time to reach
    """

    def __init__(self, name, xcoordinate, ycoordinate, critical):
        """
        Initializes a station object
        """
        self.name = name
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.connections = []
        self.critical = critical

    def addConnection(self, name, time, critical):
        self.connections.append([name, time, critical])

    def __str__(self):
        return (f"{self.name}, {self.xcoordinate}, \
{self.ycoordinate}, {self.critical}\n")
