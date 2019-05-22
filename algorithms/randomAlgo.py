import random
from classes import station
from classes import railroad
from classes import trajectory as tj
from helpers import visual

def runRandom(railroad, trainlining, runs, rerun, algorithm, image):
    """
    Executes the makeRandomRoute function for the amount of runs and keeps track\
    of the solutions and other values.

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
        highestScore (float): final solution of algorithm
    """

    highestScore = 0
    countList = []
    scoreList = []
    averageList = []

    for i in range(int(runs)):
        trainlining.trajectories = []
        countList.append(i)
        trainlining.addTrajectories(railroad)
        score = trainlining.calculateScore()
        averageList.append(score)
        if score > highestScore:
            bestTrainLining = trainlining
            highestScore = score
        scoreList.append(highestScore)
        if ((i-1) % 100) == 0 and rerun == "n":
            print(f"counter: {(i-1)} score: {highestScore}")


    sum = 0
    for score in averageList:
        sum += score
    average = sum / int(runs)
    if rerun == "n":
        print(average)

    if rerun == "y":
        return highestScore
    elif rerun == "n":
        for trajectory in bestTrainLining.trajectories:
            print(trajectory.visitedStations)
            print("\n")

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoreList)
    else:
        visual.makeCard(railroad, bestTrainLining)




def makeRandomRoute(railroad, trainlining):
    """
    This algorithm uses a randomly generated trainlining, and compares\
    to it with the same trainlining with a randomly adjusted trajectory. \
    The best solution is saved and this procedure continues.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.

    Returns:
        trajectory (Class): part of the trainlining that passes several stations.
    """
    trajectory = tj.Trajectory(trainlining.maxLength)

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
