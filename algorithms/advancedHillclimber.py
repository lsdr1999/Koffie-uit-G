import copy
import random
from algorithms import randomAlgo as ra
from helpers import visual
import random

def runAdvancedHillclimber(railroad, trainlining):
    trainlining.addTrajectories(railroad)

    for i in range(10000):
        trainlining = advancedHillclimber(railroad, trainlining, False)
        if (i - 1 % 1) == 0:
            score = trainlining.calculateScore()
            print(f"counter: {i-1} score: {score}")
    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
    visual.makeCard(railroad, trainlining)

def advancedHillclimber(railroad, trainlining, sim):
    number = random.randint(1,10)
    old = trainlining.calculateScore()
    startTrajectory = random.choice(trainlining.trajectories)
    trainlining.trajectories.remove(startTrajectory)
    start = startScore(trainlining, startTrajectory)

    intermediateInfo = intermediateScore(trainlining, startTrajectory, number)
    intermediate = intermediateInfo[0]
    iTraject = intermediateInfo[1]
    iTrain = intermediateInfo[2]

    newInfo= newScore(trainlining, iTraject, number, railroad)
    new = newInfo[0]
    nTraject = newInfo[1]
    nTrain = newInfo[2]


    extraInfo = extraScore(trainlining, startTrajectory, railroad)
    extra = extraInfo[0]
    eTrain = extraInfo[1]

    if sim:
        return [start, old, intermediate, new, extra], [trainlining, startTrajectory, iTrain, nTrain, eTrain]

    trainlining.trajectories.append(startTrajectory)

    if extra > old and extra > start and extra > intermediate and extra > new and len(trainlining.trajectories) < trainlining.maxTrajectories:
        trainlining = eTrain

    elif start >= old and start >= intermediate and start >= extra and start >= new:
        trainlining.trajectories.remove(startTrajectory)

    elif intermediate > old and intermediate > start and intermediate > new and intermediate > extra:
        trainlining = iTrain

    elif new >= old and new > start and new >= intermediate and new > extra:
        trainlining = nTrain


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

    intermediatetrainlining.trajectories.append(intermediateTrajectory)
    intermediateScore = intermediatetrainlining.calculateScore()
    return intermediateScore, intermediateTrajectory, intermediatetrainlining

def newScore(trainlining, iTraject, number, railroad):
    newTrajectory = copy.deepcopy(iTraject)
    newtrainlining = copy.deepcopy(trainlining)

    trajectoryLen = len(newTrajectory.visitedStations)
    startStation = newTrajectory.visitedStations[0]

    for i in range(number):
        nextStation = random.choice(railroad.stationDict[startStation].connections)
        nextStationName = nextStation[0]
        time = nextStation[1]
        critical = nextStation[2]
        id = nextStation[3]
        # check whether new connection does not exceed the maximal time of trajectory
        if newTrajectory.length + time < int(newTrajectory.maxLength):
            newTrajectory.visitedStations.insert(0, nextStationName)
            newTrajectory.connections.insert(0, [startStation, nextStationName, time, critical, id])
            newTrajectory.calculateLength()
            startStation = nextStationName
        else:
            break

    newtrainlining.trajectories.append(newTrajectory)
    newScore = newtrainlining.calculateScore()
    return newScore, newTrajectory, newtrainlining

def extraScore(trainlining, startTrajectory, railroad):
    extratrainlining = copy.deepcopy(trainlining)
    extraTrajectory = ra.makeRandomRoute(railroad, trainlining)
    extratrainlining.trajectories.append(startTrajectory)
    extratrainlining.trajectories.append(extraTrajectory)
    extraScore = extratrainlining.calculateScore()
    return extraScore, extratrainlining
