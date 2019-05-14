import copy
import random
from algorithms import randomAlgo as ra

def advancedHillclimber(dienstregeling, railroad, maxLength, number):
    old = dienstregeling.calculateScore()
    startTrajectory = random.choice(dienstregeling.trajectories)
    dienstregeling.trajectories.remove(startTrajectory)
    start = startScore(dienstregeling, startTrajectory)

    intermediateInfo = intermediateScore(dienstregeling, startTrajectory, number)
    intermediate = intermediateInfo[0]
    iTraject = intermediateInfo[1]
    iDienst = intermediateInfo[2]

    if len(iTraject.visitedStations) != 0:
        newInfo= newScore(dienstregeling, iTraject, number, maxLength, railroad)
        new = newInfo[0]
        Trajectory = newInfo[1]
        nDienst = newInfo[2]

    else:
        new = 0

    extraInfo = extraScore(dienstregeling, startTrajectory, railroad)
    extra = extraInfo[0]
    eDienst = extraInfo[1]

    # print(old)
    # print(start)
    # print(intermediate)
    # print(new)
    # print(extra)
    # print("\n")

    if old >= start and old >= intermediate and old >= new and old >= extra:
        dienstregeling.trajectories.append(startTrajectory)

    elif intermediate > old and intermediate > start and intermediate > new and intermediate > extra:
        dienstregeling = iDienst

    elif new > old and new > start and new > intermediate and new > extra:
        dienstregeling = nDienst
    elif extra > old and extra > start and extra > intermediate and extra > new:
        dienstregeling = eDienst
        if len(dienstregeling.trajectories) < int(maxLength) and \
            start > intermediate and start > new:
            dienstregeling.trajectories.append(startTrajectory)

    dienstregeling.calculateScore()
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

    if len(intermediateTrajectory.connections) > 0:
        intermediateTrajectory.calculateLength()
        intermediateDienstregeling.trajectories.append(intermediateTrajectory)
    else:
        intermediateTrajectory.visitedStations = []

    intermediateScore = intermediateDienstregeling.calculateScore()
    return intermediateScore, intermediateTrajectory, intermediateDienstregeling

def newScore(dienstregeling, iTraject, number, maxLength, railroad):
    newTrajectory = copy.deepcopy(iTraject)
    newDienstregeling = copy.deepcopy(dienstregeling)

    trajectoryLen = len(newTrajectory.visitedStations)
    start_station = newTrajectory.visitedStations[0]
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
    extraDienstregeling.trajectories.append(startTrajectory)
    extraDienstregeling.trajectories.append(extraTrajectory)
    extraScore = extraDienstregeling.calculateScore()
    return extraScore, extraDienstregeling
