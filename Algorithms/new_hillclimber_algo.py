import copy
import random
from Algorithms import random_algo as ra

def newHillclimber(dienstregeling, railroad, maxLength):

    # Save incoming arguments
    number = 3
    # Calculate the old score
    oldScore = dienstregeling.calculateScore()
    # print(f"This is the old score {oldScore}")

    aTrajectory = random.choice(dienstregeling.trajectories)
    for i in range(len(dienstregeling.trajectories)):
        if len(aTrajectory.connections) == 0:
            aTrajectory = random.choice(dienstregeling.trajectories)

    dienstregeling.trajectories.remove(aTrajectory)
    randomTrajectory = copy.copy(aTrajectory)
    startScore = dienstregeling.calculateScore()
    # print(f"This is the start score {startScore}")

    # Remove (number) connections from a randomTrajectory
    for i in range(number):
        if len(randomTrajectory.connections) > 0:
            removeConnection(randomTrajectory)
        else:
            break

    dienstregeling.trajectories.append(randomTrajectory)

    intermediateScore = dienstregeling.calculateScore()
    # print(f"This is the intermediate score {intermediateScore}")
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
                randomTrajectory.calculateLength()
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
    if startScore > intermediateScore and startScore > newScore and startScore > oldScore:
        extraTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
        dienstregeling.trajectories.append(extraTrajectory)
        extraScore = dienstregeling.calculateScore()
        # print(f"This is the extraScore {extraScore}")
        dienstregeling.trajectories.remove(extraTrajectory)
        # print("extrascore")
    # print(f"This is the final score {finalScore}")
    checkBest(number, dienstregeling, randomTrajectory, aTrajectory, extraTrajectory, oldScore, startScore, intermediateScore, newScore, extraScore)

def removeConnection(randomTrajectory):
    randomTrajectory.visitedStations.pop()
    randomTrajectory.connections.pop()


def addNewConnection(randomTrajectory, start_station, next_station_name, time, critical, id):
    randomTrajectory.addVisitedStations(next_station_name)
    randomTrajectory.addConnection(start_station, next_station_name, time, critical, id)

def checkBest(number, dienstregeling, randomTrajectory, aTrajectory, extraTrajectory, oldScore, startScore, intermediateScore, newScore, extraScore):
    # startScore is better
    if startScore >= newScore and startScore >= oldScore and startScore >= intermediateScore and startScore >= extraScore:
        return

    # newScore is better
    elif newScore >= oldScore and newScore >= startScore and newScore >= intermediateScore and newScore >= extraScore:
        dienstregeling.trajectories.append(randomTrajectory)
        finalScore = newScore

    # intermediateScore is better
    elif intermediateScore >= oldScore and intermediateScore >= startScore and intermediateScore >= newScore and intermediateScore >= extraScore:
        for i in range(number):
            removeConnection(randomTrajectory)

        dienstregeling.trajectories.append(randomTrajectory)
        finalScore = intermediateScore

    # oldScore is better
    elif oldScore >= startScore and oldScore >= newScore and oldScore >= intermediateScore and oldScore >= extraScore:
        dienstregeling.trajectories.append(aTrajectory)
        finalScore = oldScore

    # extraScore is better
    elif extraScore >= newScore and extraScore >= startScore and extraScore >= intermediateScore and extraScore >= newScore:
        dienstregeling.trajectories.append(extraTrajectory)
        finalScore = extraScore
