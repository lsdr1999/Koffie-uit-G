from railroad import Railroad
from traject import Trajectory

class Dienstregeling():

	def __init__(self, maxTrajectories):
		self.trajectories = [] # List if lists of the visited stations of trajectories
		self.maxTrajectories = maxTrajectories # maximum of trajectories
		self.qualityK = 0.0 # max quality K
		self.totalCritical = Railroad.totalCritical() # sum of critical connections
		self.visitedCriticalConnections = set()
		self.totalTime = 0 # total length in minutes of trajectories combined


	def calculateScore(self):
		"""
		Calculates the quality of the lining
		"""
		p = len(self.visitedCriticalConnection) / self.totalCritical
		self.qualityK = p * 10000 - (len(self.trajectories) * 20 + self.totalTime / 10)
		return self.qualityK


	def addVisitedCriticalConnections(criticalConnectionSet):
		for connection in criticalConnectionSet:
			self.visitedCriticalConnections.add(connection)


	def addTrajectory(trajectory):
		self.trajectories.append(trajectory)


	def addTrajectoryTime(time):
		"""
		Adds the total time of a trajectory
		"""
		self.totalTime += time
