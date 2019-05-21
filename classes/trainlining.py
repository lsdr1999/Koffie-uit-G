from classes import railroad
from classes import trajectory
from algorithms import randomAlgo as ra

class Trainlining():
    """
    Class that creates the trajectories, calculates the length of
    trajectories and calculates the score (the quality of the trainlining)
    """

    def __init__(self, maxTrajectories, maxLength, totalCritical):
        """
        Initializes a trainlining object

        Args:
            maxTrajectories (int): information from user via UI (amount of trajectories)
            maxLength (int): information from user via UI (amount of time per trajectory)
            totalCritical (list): list of all critical stations
        """
        self.trajectories = []
        self.maxTrajectories = int(maxTrajectories)
        self.maxLength = int(maxLength)
        self.totalCritical = totalCritical
        self.visitedCriticalConnections = set()
        self.trackLength = 0


    def calculateScore(self):
        """
        Calculates the quality of the trainling via the score formula

        Returns:
            The calculated score
        """
        self.setTrackLength()
        self.setVisitedCriticalConnections()
        p = self.calculateP()

        score = p * 10000 - (len(self.trajectories) * 20 + self.trackLength / 10)
        return score


    def calculateP(self):
        """
        Calculates 'p', a fraction which is used in the calculateScore function

        Returns:
            The 'p' value
        """
        p = float(len(self.visitedCriticalConnections)) / float(self.totalCritical)
        return p


    def setTrackLength(self):
        """
        Sets the total length of the trainling, out of a combination of all trajectory lengths
        """
        self.trackLength = 0
        for trajectory in self.trajectories:
            trajectory.calculateLength()
            self.trackLength += trajectory.length


    def setVisitedCriticalConnections(self):
        """
        Updates visitedCriticalConnections, a set which collects all visited critical stations
        """
        self.visitedCriticalConnections.clear()
        for trajectory in self.trajectories:
            trajectory.calculateVisitedCritical()
            self.visitedCriticalConnections.update(trajectory.visitedCritical)


    def addTrajectories(self, railroad):
        """
        Adds a trajectory to the trajectories list until maxTrajectories is reached

        Args:
            Railroad (Class): lays out the connections of the Netherlands or North- and South-Holland
        """
        for trajectory in range(self.maxTrajectories):
            trajectory = ra.makeRandomRoute(railroad, self)
            self.trajectories.append(trajectory)
