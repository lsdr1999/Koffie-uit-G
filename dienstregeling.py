from railroad import Railroad
from traject import Trajectory
from random_algo import make_random_route

class Dienstregeling():

    def __init__(self, maxTrajectories):
        self.trajectories = [] # List of lists of the visited stations of trajectories
        self.maxTrajectories = int(maxTrajectories) # maximum of trajectories
        self.qualityK = 0.0 # max quality K
        self.totalCritical = 0 # sum of critical connections
        self.visitedCriticalConnections = set()
        self.totalTime = 0 # total length in minutes of trajectories combined

    def make_dienstregeling(self):
        railroad = Railroad()
        railroad.loadStations()
        self.totalCritical = railroad.addTotalCritical()
        for trajectory in range(self.maxTrajectories):
            self.addTrajectory(railroad)

        for trajectory in self.trajectories:
            print(trajectory)
            print("\n")
        self.calculateScore()

    def calculateScore(self):
        """
        Calculates the quality of the lining
        """
        p = float(len(self.visitedCriticalConnections)) / float(self.totalCritical)
        print("number of visted critical connections:")
        print(len(self.visitedCriticalConnections))
        print("\n")
        print("fraction of ciritical connections visited:")
        print(p)
        print("\n")
        print("total minutes of track:")
        print(self.totalTime)
        self.qualityK = p * 10000 - (len(self.trajectories) * 20 + self.totalTime / 10)
        print("total K score:")
        print(int(self.qualityK))
        return self.qualityK


    def addVisitedCriticalConnections(criticalConnectionSet):
        for connection in criticalConnectionSet:
            self.visitedCriticalConnections.add(connection)


    def addTrajectory(self, railroad):
        trajectory = make_random_route(railroad)
        self.trajectories.append(trajectory[0])
        self.totalTime += int(trajectory[1])
        self.visitedCriticalConnections.update(trajectory[2])
