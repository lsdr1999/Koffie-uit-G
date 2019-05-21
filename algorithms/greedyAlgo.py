import random
from algorithms import randomAlgo
from classes import station
from classes import railroad
from classes import trajectory as tj
from classes import trainlining
from helpers import visual

def runGreedy(railroad, trainlining, runs, rerun, algorithm, image):
    """
    Runs the greedyTrajectory function on a randomly chosen trajectory of \
    a randomly generated trainlining. Then checks which of the versions of the\
    trainlining is best, and continues with the winning solution.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        runs (int): amount of iterations chosen for the algorithm to run.
        rerun (string): defines whether the user wants to rerun the algorithm 100 times.
        algorithm (string): chosen algorithm (can be all or hillclimber).
        image (string): defines what image is generated after the algorithm.

    Returns (only when algorithm == "all"):
        list (list): list of the countList and scoreList
    Returns (only when rerun == "y"):
        scoreList(list): list of the values of the solutions
    """
    highestScore = 0
    countList = []
    scoreList = []
    averageList = []

    for i in range(int(runs)):
        trainlining.trajectories = []
        for trajectory in range(trainlining.maxTrajectories):
            trajectory = greedyTrajectory(railroad, trainlining)
            trainlining.trajectories.append(trajectory)
        score = trainlining.calculateScore()
        countList.append(i)
        scoreList.append(highestScore)
        averageList.append(score)
        if score > highestScore:
            bestTrainLining = trainlining
            highestScore = score
        if ((i-1) % 100) == 0 and rerun == "n":
            print(f"counter: {(i-1)} score: {highestScore}")

    sum = 0
    for score in averageList:
        sum += score
    average = sum / int(runs)
    if rerun == "n":
        print(average)
    elif rerun == "y":
        return scoreList

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "visual":
        visual.makeCard(railroad, bestTrainLining)
    elif image == "graph":
        visual.makeGraph(countList, scoreList)

def greedyTrajectory(railroad, trainlining):
    """
    Creates a trajectory based on several constraints (i.e. shortest time, already\
    visited, if it's critical or not) and then checks whether the solution increases.\
    Keeps the best solution.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
    Returns:
        trajectory (Class): generated trajectory by the algorithm, filled with the\
        stations that it has visited.
    """
    keylist = []
    for key, value in railroad.stationDict.items():
        keylist.append(key)

    startStation = random.choice(keylist)
    trajectory = tj.Trajectory(trainlining.maxLength)
    trajectory.addVisitedStations(startStation)
    trajectory.calculateLength()

    while (trajectory.length < trainlining.maxLength):
        iets = sorted(railroad.stationDict[startStation].connections, key = lambda connection:(1- connection[2], connection[1]))

        counter = 0
        for connection in iets:
            nextStation = connection
            if nextStation[0] not in trajectory.visitedStations:
                break

            counter += 1
            if counter == len(iets):
                return trajectory


        if nextStation:
            nextStationName = nextStation[0]
            trajectory.addVisitedStations(nextStationName)
            time = nextStation[1]
            critical = nextStation[2]
            id = nextStation[3]
            trajectory.addConnection(startStation, nextStationName, time, critical, id)
            trajectory.calculateLength()
            startStation = nextStationName
        else:
            break

    return trajectory
