from Classes import railroad
from Classes import traject
from Algorithms import random_algo as ra
from Algorithms import hillclimber_algo

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
            trajectory.calculateLength
            self.TrackLength += trajectory.length

    def setVisitedCriticalConnections(self):
        self.visitedCriticalConnections.clear()
        for trajectory in self.trajectories:
            trajectory.calculateVisitedCritical()
            self.visitedCriticalConnections.update(trajectory.visitedCritical)

    def addTrajectories(self, railroad):
        for trajectory in range(self.maxTrajectories):
            trajectory = ra.make_random_route(railroad, self.maxLength)
            self.trajectories.append(trajectory)
