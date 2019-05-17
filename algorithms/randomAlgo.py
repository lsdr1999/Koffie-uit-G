import random
from classes import station
from classes import railroad
from classes import trajectory as tj

def makeRandomRoute(railroad, maxLength):
    railroad = railroad
    maxLength = maxLength
    trajectory = tj.Trajectory(maxLength)

    keylist = []
    for key, value in railroad.stationDict.items():
        keylist.append(key)
    startStation = random.choice(keylist)
    trajectory.addVisitedStations(startStation)

    while True:
        nextStation = random.choice(railroad.stationDict[startStation].connections)
        nextStationName = nextStation[0]
        time = nextStation[1]
        critical = nextStation[2]
        id = nextStation[3]

        if trajectory.length + time < trajectory.maxLength:
            trajectory.addVisitedStations(nextStationName)
            trajectory.addConnection(startStation, nextStationName, time, critical, id)
            trajectory.calculateLength()
            startStation = nextStationName
        else:
            break

    return trajectory
