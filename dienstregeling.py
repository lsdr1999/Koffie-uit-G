from railroad import Railroad
from traject import Trajectory
from random_algo import make_random_route
from hillclimber_algo import hillclimber
from score import calculateScore

class Dienstregeling():

    def __init__(self, maxTrajectories, maxLength, algorithm,):
        self.trajectories = [] # List of lists of the visited stations of trajectories
        self.maxTrajectories = int(maxTrajectories) # maximum of trajectories
        self.maxLength = int(maxLength)
        self.totalCritical = 0 # sum of critical connections
        self.algorithm = str(algorithm)

    def make_dienstregeling(self):
        railroad = Railroad()
        railroad.loadStations()
        self.totalCritical = railroad.addTotalCritical()
        for trajectory in range(self.maxTrajectories):
            self.addTrajectory(railroad)

        # for trajectory in self.trajectories:
        #     print(trajectory[0])
        #     print("\n")
        score = calculateScore(railroad, self.trajectories, self.totalCritical)

        if self.algorithm == "hillclimber":
            for i in range(50000):
                trajectories = hillclimber(railroad, self.trajectories, self.maxLength, self.totalCritical)
                self.trajectories = trajectories
                score = calculateScore(railroad, self.trajectories, self.totalCritical)
                print(score)

            print(self.trajectories)

    def addVisitedCriticalConnections(criticalConnectionSet):
        for connection in criticalConnectionSet:
            self.visitedCriticalConnections.add(connection)


    def addTrajectory(self, railroad):
        trajectory = make_random_route(railroad, self.maxLength)
        self.trajectories.append(trajectory)
