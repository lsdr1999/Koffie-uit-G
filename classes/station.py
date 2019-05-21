
class Station(object):
    """
    Defines a station object, a station has a name, coordinates, and has
    connections with other stations that take a certain time to reach
    """

    def __init__(self, name, xCoordinate, yCoordinate, critical):
        """
        Initializes a station object

        Args:
            name (string): station name
            xCoordinate (float): xCoordinate of the station
            yCoordinate (float): yCoordinate of the station
            critical (bool): critical station
        """
        self.name = name
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.connections = []
        self.critical = critical


    def addConnection(self, name, time, critical, id):
        """
        Adds all possible connections between stations to a list

        Args:
            name (string): station name
            time (int): the time between two stations
            critical (bool): critical station/connection
            id (int): id of each station
        """
        self.connections.append([name, time, critical, id])
