import copy
import random
from algorithms import randomAlgo as ra

def advancedHillclimber(trainlining, railroad, maxLength, number):
    old = trainlining.calculateScore()
    startTrajectory = random.choice(trainlining.trajectories)
    trainlining.trajectories.remove(startTrajectory)
    start = startScore(trainlining, startTrajectory)

    intermediateInfo = intermediateScore(trainlining, startTrajectory, number)
    intermediate = intermediateInfo[0]
    iTraject = intermediateInfo[1]
    iDienst = intermediateInfo[2]

    if len(iTraject.visitedStations) != 0:
        newInfo= newScore(trainlining, iTraject, number, maxLength, railroad)
        new = newInfo[0]
        Trajectory = newInfo[1]
        nDienst = newInfo[2]

    else:
        new = 0

    extraInfo = extraScore(trainlining, startTrajectory, railroad)
    extra = extraInfo[0]
    eDienst = extraInfo[1]

    # print(old)
    # print(start)
    # print(intermediate)
    # print(new)
    # print(extra)
    # print("\n")

    if old >= start and old >= intermediate and old >= new and old >= extra:
        trainlining.trajectories.append(startTrajectory)

    elif intermediate > old and intermediate > start and intermediate > new and intermediate > extra:
        trainlining = iDienst

    elif new > old and new > start and new > intermediate and new > extra:
        trainlining = nDienst
    elif extra > old and extra > start and extra > intermediate and extra > new:
        trainlining = eDienst
        if len(trainlining.trajectories) < int(maxLength) and \
            start > intermediate and start > new:
            trainlining.trajectories.append(startTrajectory)

    trainlining.calculateScore()
    return trainlining

def startScore(trainlining, startTrajectory):
    startScore = trainlining.calculateScore()
    return startScore

def intermediateScore(trainlining, startTrajectory, number):
    intermediateTrajectory = copy.deepcopy(startTrajectory)
    intermediatetrainlining = copy.deepcopy(trainlining)

    for i in range(number):
        if len(intermediateTrajectory.connections) > 0:
            intermediateTrajectory.visitedStations.pop()
            intermediateTrajectory.connections.pop()

    if len(intermediateTrajectory.connections) > 0:
        intermediateTrajectory.calculateLength()
        intermediatetrainlining.trajectories.append(intermediateTrajectory)
    else:
        intermediateTrajectory.visitedStations = []

    intermediateScore = intermediatetrainlining.calculateScore()
    return intermediateScore, intermediateTrajectory, intermediatetrainlining

def newScore(trainlining, iTraject, number, maxLength, railroad):
    newTrajectory = copy.deepcopy(iTraject)
    newtrainlining = copy.deepcopy(trainlining)

    trajectoryLen = len(newTrajectory.visitedStations)
    startStation = newTrajectory.visitedStations[0]
    for i in range(number):
        if newTrajectory.length < int(maxLength):
            nextStation = random.choice(railroad.station_dict[startStation].connections)
            nextStationName = nextStation[0]
            time = nextStation[1]
            critical = nextStation[2]
            id = nextStation[3]

            # check whether new connection does not exceed the maximal time of trajectory
            if newTrajectory.length + time < int(maxLength):
                newTrajectory.addVisitedStations(nextStationName)
                newTrajectory.addConnection(startStation, nextStationName, time, critical, id)
                newTrajectory.calculateLength()
                startStation = nextStationName
        else:
            break

    newtrainlining.trajectories.append(newTrajectory)
    newScore = newtrainlining.calculateScore()
    return newScore, newTrajectory, newtrainlining

def extraScore(trainlining, startTrajectory, railroad):
    extratrainlining = copy.deepcopy(trainlining)
    extraTrajectory = []
    extraTrajectory = ra.makeRandomRoute(railroad, trainlining.maxLength)
    extratrainlining.trajectories.append(startTrajectory)
    extratrainlining.trajectories.append(extraTrajectory)
    extraScore = extratrainlining.calculateScore()
    return extraScore, extratrainlining
