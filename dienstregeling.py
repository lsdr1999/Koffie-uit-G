from railroad import Railroad
from traject import Trajectory
from random_algo import make_random_route
from hillclimber_algo import hillclimber

class Dienstregeling():

    def __init__(self, maxTrajectories, maxLength, totalCritical):
        self.trajectories = [] # List of lists of the visited stations of trajectories
        self.maxTrajectories = int(maxTrajectories) # maximum of trajectories
        self.maxLength = int(maxLength)
        self.totalCritical = totalCritical # sum of critical connections
        self.visitedCriticalConnections = set()
        self.TrackLength = 0

    def calculateScore(self):
        self.setTrackLength()
        self.setVisitedCriticalConnections()
        p = self.calculateP()

        score = p * 10000 - (len(self.trajectories) * 20 + self.TrackLength / 10)

        return score

    def calculateP(self):
        p = float(len(self.visitedCriticalConnections)) / float(self.totalCritical)
        return p

    def setTrackLength(self):
        self.TrackLength = 0
        for trajectory in self.trajectories:
            self.TrackLength += int(trajectory[1])

    def setVisitedCriticalConnections(self):
        self.visitedCriticalConnections.clear()
        for trajectory in self.trajectories:
            self.visitedCriticalConnections.update(trajectory[2])

    def addTrajectories(self, railroad):
        for trajectory in range(self.maxTrajectories):
            trajectory = make_random_route(railroad, self.maxLength)
            self.trajectories.append(trajectory)
