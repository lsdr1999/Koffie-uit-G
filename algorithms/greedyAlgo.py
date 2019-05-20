import random
from algorithms import randomAlgo
from classes import station
from classes import railroad
from classes import trajectory as tj
from classes import trainlining
from helpers import visual

def runGreedy(railroad, trainlining, runs, algorithm, image):
    highestScore = 0
    countList = []
    scoreList = []
    averageList = []

    for i in range(int(runs)):
        trainlining.trajectories = []
        for trajectory in range(trainlining.maxTrajectories):
            trajectory = greedy_trajectory(railroad, trainlining)
            trainlining.trajectories.append(trajectory)
        score = trainlining.calculateScore()
        countList.append(i)
        scoreList.append(highestScore)
        averageList.append(score)
        if score > highestScore:
            bestTrainLining = trainlining
            highestScore = score
        if ((i-1) % 100) == 0:
            print(f"counter: {(i-1)} score: {highestScore}")

    sum = 0
    for score in averageList:
        sum += score
    average = sum / int(runs)
    print(average)

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "visual":
        visual.makeCard(railroad, bestTrainLining)
    elif image == "graph":
        visual.makeGraph(countList, scoreList)

def greedy_trajectory(railroad, trainlining):

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
