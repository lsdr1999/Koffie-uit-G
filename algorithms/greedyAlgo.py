import random
from algorithms import randomAlgo

from classes import station
from classes import railroad
from classes import trajectory as tj
from classes import trainlining
from helpers import visual

def runGreedy(railroad, trainlining, runs):
    highestScore = 0
    countList = []
    scoreList = []
    averageList = []

    for i in range(runs):
        trainlining.trajectories = []
        for trajectory in range(trainlining.maxTrajectories):
            trajectory = greedy_traject(railroad, trainlining)
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
    average = sum/runs
    print(average)
    visual.makeCard(railroad, bestTrainLining)

def greedy_traject(railroad, trainlining):

    # Find random start station
    keylist = []
    for key, value in railroad.stationDict.items():
        keylist.append(key)
    startStation = random.choice(keylist)
    trajectory = tj.Trajectory(trainlining.maxLength)
    trajectory.addVisitedStations(startStation)

    # sorteer connection in railroad.station_dict[startStation].connections op de volgende manier:
        # niet bezocht en kritiek?
        # kortste tijd?
        # niet bezocht?
    # maken van traject op basis van iteratie over sorted list
            # niet bezocht en kritiek gevonden -> kies deze boven andere opties (onafhankelijk van tijd)
            # korste tijd gevonden en niet kritiek in connections -> kies deze boven andere opties
            # niet bezocht gevonden en niet kritiek of korte tijd -> kies dan deze , maar vervang wanneer mogelijk

    trajectory.calculateLength()
    while (trajectory.length < trainlining.maxLength):
        iets = sorted(railroad.stationDict[startStation].connections, key = lambda connection:(1- connection[2], connection[1]))
        # print(iets)

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
