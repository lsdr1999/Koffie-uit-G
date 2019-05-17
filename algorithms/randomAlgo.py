import random
from classes import station
from classes import railroad
from classes import trajectory as tj
from helpers import visual

def runRandom(railroad, trainlining, runs):
    highestScore = 0
    countList = []
    scoreList = []
    averageList = []
    for i in range(runs):
        trainlining.trajectories = []
        countList.append(i)
        trainlining.addTrajectories(railroad)
        score = trainlining.calculateScore()
        averageList.append(score)
        if score > highestScore:
            bestTrainLining = trainlining
            highestScore = score
        scoreList.append(highestScore)
        if ((i-1) % 100) == 0:
            print(f"counter: {(i-1)} score: {highestScore}")

    sum = 0
    for score in averageList:
        sum += score
    average = sum/runs
    print(average)
    visual.makeGraph(railroad, bestTrainLining)
    for trajectory in bestTrainLining.trajectories:
        print(trajectory.visitedStations)
        print("\n")



def makeRandomRoute(railroad, trainlining):
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
