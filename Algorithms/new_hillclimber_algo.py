import copy
import random
from Algorithms import random_algo as ra

def newHillclimber(dienstregeling, railroad, maxLength):

    # Save incoming arguments
    number = 3

    # Calculate the old score
    oldScore = dienstregeling.calculateScore()
    print(f"This is the old score {oldScore}")

    aTrajectory = random.choice(dienstregeling.trajectories)
    dienstregeling.trajectories.remove(aTrajectory)
    randomTrajectory = copy.copy(aTrajectory)
    startScore = dienstregeling.calculateScore()
    print(f"This is the start score {startScore}")

    # Remove (number) connections from a randomTrajectory
    for i in range(number):
        if len(randomTrajectory.connections) > 0:
            removeConnection(randomTrajectory)
        else:
            print(randomTrajectory.visitedStations)
            break

    calculateNewScores(randomTrajectory)
    dienstregeling.trajectories.append(randomTrajectory)

    intermediateScore = dienstregeling.calculateScore()
    print(f"This is the intermediate score {intermediateScore}")
    dienstregeling.trajectories.remove(randomTrajectory)

    trajectoryLen = len(randomTrajectory.visitedStations)
    start_station = randomTrajectory.visitedStations[trajectoryLen - 1]
    # Add new cities to trajectory

    for i in range(number):
        if randomTrajectory.length < int(maxLength):
            next_station = random.choice(railroad.station_dict[start_station].connections)
            next_station_name = next_station[0]
            time = next_station[1]
            critical = next_station[2]
            id = next_station[3]

            if randomTrajectory.length + time < int(maxLength):
                addNewConnection(randomTrajectory, start_station, next_station_name, time, critical, id)
                calculateNewScores(randomTrajectory)
                start_station = next_station_name
        else:
            break
    dienstregeling.trajectories.append(randomTrajectory)
    newScore = dienstregeling.calculateScore()
    dienstregeling.trajectories.remove(randomTrajectory)
    # print(f"This is the newScore {newScore}")

    # Insert a new randomly made trajectory and calculate score
    extraScore = 0
    extraTrajectory = []
    if startScore > intermediateScore and startScore > newScore:
        extraTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
        dienstregeling.trajectories.append(extraTrajectory)
        extraScore = dienstregeling.calculateScore()
        print(f"This is the extraScore {extraScore}")
        dienstregeling.trajectories.remove(extraTrajectory)

    if newScore > oldScore and newScore > intermediateScore and newScore > extraScore:
        dienstregeling.trajectories.append(randomTrajectory)
        finalScore = newScore
    elif intermediateScore > oldScore and intermediateScore > newScore and intermediateScore > extraScore:
        for i in range(number):
            removeConnection(randomTrajectory)
        dienstregeling.trajectories.append(randomTrajectory)
        finalScore = intermediateScore
    elif oldScore > newScore and oldScore > intermediateScore and oldScore > extraScore:
        dienstregeling.trajectories.append(aTrajectory)
        finalScore = oldScore
    elif extraScore > newScore and extraScore > intermediateScore and extraScore > newScore:
        dienstregeling.trajectories.append(extraTrajectory)
        finalScore = extraScore
    print(f"This is the final score {finalScore}")

def removeConnection(randomTrajectory):
    randomTrajectory.visitedStations.pop()
    randomTrajectory.connections.pop()


def calculateNewScores(randomTrajectory):
    randomTrajectory.calculateLength()
    randomTrajectory.calculateVisitedCritical()

def addNewConnection(randomTrajectory, start_station, next_station_name, time, critical, id):
    randomTrajectory.addVisitedStations(next_station_name)
    randomTrajectory.addConnection(start_station, next_station_name, time, critical, id)
