from classes import railroad
from classes import trajectory
from algorithms import randomAlgo as ra
from algorithms import hillclimberAlgo

class Trainlining():

    def __init__(self, maxTrajectories, maxLength, totalCritical):
        self.trajectories = [] # List of lists of the visited stations of trajectories
        self.maxTrajectories = int(maxTrajectories) # maximum of trajectories
        self.maxLength = int(maxLength)
        self.totalCritical = totalCritical # sum of critical connections
        self.visitedCriticalConnections = set()
        self.trackLength = 0

    def calculateScore(self):
        self.setTrackLength()
        self.setVisitedCriticalConnections()
        p = self.calculateP()

        score = p * 10000 - (len(self.trajectories) * 20 + self.trackLength / 10)
        return score

    def calculateP(self):
        p = float(len(self.visitedCriticalConnections)) / float(self.totalCritical)
        return p

    def setTrackLength(self):
        self.trackLength = 0
        for trajectory in self.trajectories:
            trajectory.calculateLength()
            self.trackLength += trajectory.length

    def setVisitedCriticalConnections(self):
        self.visitedCriticalConnections.clear()
        for trajectory in self.trajectories:
            trajectory.calculateVisitedCritical()
            self.visitedCriticalConnections.update(trajectory.visitedCritical)

    def addTrajectories(self, railroad):
        for trajectory in range(self.maxTrajectories):
            trajectory = ra.make_random_route(railroad, self.maxLength)
            self.trajectories.append(trajectory)
