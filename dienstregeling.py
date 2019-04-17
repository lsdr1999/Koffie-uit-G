from railroad import Railroad
from traject import Trajectory
from loadstations import

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
		# if (len(self.trajectories) == self.maxTrajectories):
		# 	return len(self.trajectories)

	def addTrajectoryTime(time):
		"""
		Adds the total time of a trajectory
		"""
<<<<<<< HEAD
		self.totalTime += time
=======
		if (railroad[3] is True and): #and connection is not in a dictionary (which one????)
		 	self.visitedCriticalConnectionCount += 1

		if (): #check if connection from A to B is in railroad as A to B
			self.visitedConnections[self.trajectories] = (f"{railroad[0]} to {railroad[1]}")
		elif (): # check if connection from A to B is in railroad as B to A
			self.visitedConnections[self.trajectories] = (f"{railroad[1]} to {railroad[0]}")

		self.totalTime += int(railroad[2]) #even checken hoeveelste variable dit is van connection

	def startTrajectory(self):
		# if not all critical stations are visited and there are still trajectories left
		if (self.trajectories <= self.maxTrajectories and self.visitedConnectionCount < self.totalCritical):
			#start traject ???
			self.trajectories += 1
		#we ran out of trajectories or all critical connections have been visited.
		else:
			return self.calculateScore
>>>>>>> 09c2ba56cf1545eff9d57dbbb1a27bf50261d971
