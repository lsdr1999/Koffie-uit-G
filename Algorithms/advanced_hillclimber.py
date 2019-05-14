import copy
import random
from Algorithms import random_algo as ra

def advancedHillclimber(dienstregeling, railroad, maxLength, number):
    old = dienstregeling.calculateScore()
    print("start")
    print(len(dienstregeling.trajectories))
    startTrajectory = random.choice(dienstregeling.trajectories)
    dienstregeling.trajectories.remove(startTrajectory)
    start = startScore(dienstregeling, startTrajectory)
    intermediate, iTraject, iDienst = intermediateScore(dienstregeling, startTrajectory, number)
    print("\n")

    new, nTrajectory, nDienst = newScore(dienstregeling, iTraject, number, maxLength, railroad)
    extra, eDienst = extraScore(dienstregeling, startTrajectory, railroad)

    if old > start and old > intermediate and old > new and old > extra:
        dienstregeling.trajectories.append(startTrajectory)
        print("!1")
        print(len(dienstregeling.trajectories))
    elif start > old and start > intermediate and start > new and start > extra:
        print("!2")
        print(len(dienstregeling.trajectories))
    elif intermediate > old and intermediate > start and intermediate > new and intermediate > extra:
        print(len(dienstregeling.trajectories))
        dienstregeling = iDienst
        print(len(dienstregeling.trajectories))
        print("!3")

    elif new > old and new > start and new > intermediate and new > extra:
        dienstregeling = nDienst
        print("!4")
        print(len(dienstregeling.trajectories))
    elif extra > old and extra > start and extra > intermediate and extra > new:
        dienstregeling = eDienst
        print("!5")
        print(len(dienstregeling.trajectories))
        if len(dienstregeling.trajectories) < int(maxLength) and \
            start > intermediate and start > new:
            dienstregeling.trajectories.append(startTrajectory)
        print(len(dienstregeling.trajectories))
    print(len(dienstregeling.trajectories))
    return dienstregeling

def startScore(dienstregeling, startTrajectory):
    startScore = dienstregeling.calculateScore()
    return startScore

def intermediateScore(dienstregeling, startTrajectory, number):
    intermediateTrajectory = copy.deepcopy(startTrajectory)
    intermediateDienstregeling = copy.deepcopy(dienstregeling)

    for i in range(number):
        if len(intermediateTrajectory.connections) > 0:
            intermediateTrajectory.visitedStations.pop()
            intermediateTrajectory.connections.pop()
        else:
            intermediateScore = 0
            return intermediateScore

    intermediateTrajectory.calculateLength()
    intermediateDienstregeling.trajectories.append(intermediateTrajectory)

    intermediateScore = intermediateDienstregeling.calculateScore()
    return intermediateScore, intermediateTrajectory, intermediateDienstregeling

def newScore(dienstregeling, iTraject, number, maxLength, railroad):
    newTrajectory = copy.deepcopy(iTraject)
    newDienstregeling = copy.deepcopy(dienstregeling)

    trajectoryLen = len(newTrajectory.visitedStations)
    start_station = newTrajectory.visitedStations[trajectoryLen - 1]
    for i in range(number):
        if newTrajectory.length < int(maxLength):
            next_station = random.choice(railroad.station_dict[start_station].connections)
            next_station_name = next_station[0]
            time = next_station[1]
            critical = next_station[2]
            id = next_station[3]

            # check whether new connection does not exceed the maximal time of trajectory
            if newTrajectory.length + time < int(maxLength):
                newTrajectory.addVisitedStations(next_station_name)
                newTrajectory.addConnection(start_station, next_station_name, time, critical, id)
                newTrajectory.calculateLength()
                start_station = next_station_name
        else:
            break
    newDienstregeling.trajectories.append(newTrajectory)

    newScore = newDienstregeling.calculateScore()
    return newScore, newTrajectory, newDienstregeling

def extraScore(dienstregeling, startTrajectory, railroad):
    extraDienstregeling = copy.deepcopy(dienstregeling)
    extraTrajectory = []
    extraTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
    extraDienstregeling.trajectories.append(extraTrajectory)
    extraScore = extraDienstregeling.calculateScore()
    return extraScore, extraDienstregeling
