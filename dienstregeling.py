from railroad import Railroad
from traject import Trajectory
from loadstations import 

class Dienstregeling():

	def __init__(self):
		self.trajectories = 0 # how many trajectories are used
		self.maxTrajectories = 7 # maximum of trajectories
		self.qualityK = 0.0 # max quality K
		self.totalCritical = 20 # sum of critical connections
		self.visitedCriticalConnectionCount = 0 #count of connections visited
		self.visitedConnections = {} #dict with visited connections with number of trajectory as key
		self.totalTime = 0 # total length in minutes of trajectories combined

	def calculateScore(self):
		"""
		Calculates the quality of the lining
		"""
		p = float(self.visitedCriticalConnectionCount / self.totalCritical)
		self.qualityK = p * 10000 - (self.trajectories * 20 + self.totalTime / 10)
		return self.qualityK

	def addVisited(railroad):
		"""
		Adds a visited station to the list of visited station and adds it to
		the visitedConnectionCount if it is a critical connection
		"""
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
