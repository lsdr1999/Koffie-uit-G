from classes import station

class Trajectory(object):
    """
    Class that creates a trajectory out of stations and connections.
    It adds visited Stations and connections and calculates both the total visitedCritical
    as the total Length of the trajectory.
    """

    def __init__(self, maxLength):
        """
        Initializes a trajectory object

        Args:
            maxLength (int): information from user via UI (amount of time per trajectory)
        """
        self.maxLength = maxLength
        self.length = 0
        self.visitedCritical = set()
        self.visitedStations = []
        self.connections = []


    def addVisitedStations(self, nextStation):
        """
        Adds visited stations to a list

        Args:
            nextStation (string): the go to station from the start/last station
        """
        self.visitedStations.append(nextStation)


    def addConnection(self, startStation, nextStation, time, critical, id):
        """
        Fills a connections list with information about stations, time and 'critical'

        Args:
            startStation (string): the start/last station
            nextStation (string): the go to station
            time (int): the time between two stations
            critcal (bool): critical connection
            id (int): id of connection
        """
        self.connections.append([startStation, nextStation, time, critical, id])


    def calculateVisitedCritical(self):
        """
        Adds all visited critical connections to a set
        """
        self.visitedCritical.clear()
        for connection in self.connections:
            if connection[3]:
                id = connection[4]
                self.visitedCritical.add(id)


    def calculateLength(self):
        """
        Calculates the total length of a single trajectory
        """
        length = 0
        for connection in self.connections:
            length += connection[2]
        self.length = length
