from spoor import Spoor
from traject import Trajectory

class Dienstregeling():

	def __init__(self, spoor):
		self.trajectories = 0 # how many trajectories are used
		self.maxTrajectories = 7 # maximum of trajectories
		self.qualityK = 0.0 # max quality K
		self.totalCritical = 20 # sum of critical connections
		self.visitedCriticalConnectionCount = 0 #count of connections visited
		self.visitedConnections = [] #empty list of all of the visited connections
		self.totalTime = 0 # total length in minutes of trajectories combined

	def calculateScore(self):
		"""
		Calculates the quality of the lining
		"""
		p = float(self.visitedCriticalConnectionCount / self.totalCritical)
		self.qualityK = p * 10000 - (self.trajectories * 20 + self.totalTime / 10)
		return self.qualityK

	def addVisited(connection):
		"""
		Adds a visited station to the list of visited station and adds it to
		the visitedConnectionCount if it is a critical connection
		"""
		if (station[critical] and not in self.visitedConnections): #DEZE FUNCTIE KLOPT NOG NIET
			self.visitedConnections.append(station)
			self.visitedCriticalConnectionCount += 1
		self.totalTime += int(station[time]) #even checken hoeveelste variable dit is van connection

	def startTrajectory(self):
		if (self.trajectories <= self.maxTrajectories):
			#start traject ???
			self.trajectories += 1
		else:
			return self.calculateScore
