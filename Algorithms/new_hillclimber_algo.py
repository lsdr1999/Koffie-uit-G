import copy
import random
from Algorithms import random_algo as ra

def newHillclimber(dienstregeling, railroad, maxLength):
    # Save incoming arguments
    number = 3
    connectioncount = 0
    # print(f"This is the old score {oldScore}")
    # check whether there are unnecessary (empty) trajectories
    for trajectory in dienstregeling.trajectories:
        if len(trajectory.connections) == 0:
            print("one trajectory with 0 connections")
            print(trajectory.connections)
            print(trajectory.visitedStations)
            dienstregeling.trajectories.remove(trajectory)
        else:
            connectioncount += len(trajectory.connections)
    print(connectioncount)

    # Calculate the old score (nothing changed)
    oldScore = dienstregeling.calculateScore()

    # pick a random trajectory and make a copy
    aTrajectory = random.choice(dienstregeling.trajectories)
    randomTrajectory = copy.deepcopy(aTrajectory)

    # remove the trajectory from dienstregeling
    dienstregeling.trajectories.remove(aTrajectory)

    # calculate the startscore (dienstregeling without trajectory)
    startScore = dienstregeling.calculateScore()
    # print(f"This is the start score {startScore}")

    # Remove (number) connections from randomTrajectory
    for i in range(number):
        if len(randomTrajectory.connections) > 0:
            removeConnection(randomTrajectory)
        else:
            dienstregeling.trajectories.append(aTrajectory)
            print("empty trajectory")
            return

    # add the adjusted trajectory to dienstregeling and calculxate score
    dienstregeling.trajectories.append(randomTrajectory)
    check = 0
    for trajectory in dienstregeling.trajectories:
        check += len(trajectory.connections)
    print(f"connectioncount after popping {check}")
    intermediateScore = dienstregeling.calculateScore()

    # print(f"This is the intermediate score {intermediateScore}")
    # remove the trajectory again
    dienstregeling.trajectories.remove(randomTrajectory)

    # save the length of the visitedStations to select the startstation
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

            # check whether new connection does not exceed the maximal time of trajectory
            if randomTrajectory.length + time < int(maxLength):
                addNewConnection(randomTrajectory, start_station, next_station_name, time, critical, id)
                randomTrajectory.calculateLength()
                start_station = next_station_name
        else:
            break
    # add the new trajectory to dienstregeling and calculate the score
    dienstregeling.trajectories.append(randomTrajectory)
    newScore = dienstregeling.calculateScore()

    # remove the trajectory again
    dienstregeling.trajectories.remove(randomTrajectory)
    # print(f"This is the newScore {newScore}")

    # Insert a new randomly made trajectory and calculate score
    extraTrajectory = []
    extraTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
    # print(extraTrajectory.visitedStations)
    dienstregeling.trajectories.append(extraTrajectory)
    extraScore = dienstregeling.calculateScore()
    # print(f"This is the extraScore {extraScore}")

    #remove the extraTrajectory
    dienstregeling.trajectories.remove(extraTrajectory)

    # Calculate which version of the dienstregeling is best
    checkBest(number, dienstregeling, randomTrajectory, aTrajectory, extraTrajectory, oldScore, startScore, intermediateScore, newScore, extraScore)
    connect = 0
    for trajectory in dienstregeling.trajectories:
        connect += len(trajectory.connections)
    dienstregeling.calculateScore()
    p = dienstregeling.calculateP()
    print(p)
    print(len(dienstregeling.visitedCriticalConnections))

def removeConnection(randomTrajectory):
    randomTrajectory.visitedStations.pop()
    randomTrajectory.connections.pop()


def addNewConnection(randomTrajectory, start_station, next_station_name, time, critical, id):
    randomTrajectory.addVisitedStations(next_station_name)
    randomTrajectory.addConnection(start_station, next_station_name, time, critical, id)

def checkBest(number, dienstregeling, randomTrajectory, aTrajectory, extraTrajectory, oldScore, startScore, intermediateScore, newScore, extraScore):
    # startScore is better
    if startScore > newScore and startScore > oldScore and startScore > intermediateScore and startScore > extraScore:
        finalScore = startScore
        print("startscore, less")
        return

    # newScore is better
    elif newScore > oldScore and newScore > startScore and newScore > intermediateScore and newScore > extraScore:
        dienstregeling.trajectories.append(randomTrajectory)
        print("newscore, same")
        finalScore = newScore

    # intermediateScore is better
    elif intermediateScore >= oldScore and intermediateScore >= startScore and intermediateScore >= newScore and intermediateScore >= extraScore:

        for i in range(number):
            removeConnection(aTrajectory)

        dienstregeling.trajectories.append(aTrajectory)
        print("intermediate, -3")
        count = 0
        for trajectory in dienstregeling.trajectories:
            count += len(trajectory.connections)
        finalScore = intermediateScore

    # oldScore is better
    elif oldScore > startScore and oldScore > newScore and oldScore > intermediateScore and oldScore > extraScore:
        print("check!")
        print(len(dienstregeling.trajectories))
        dienstregeling.trajectories.append(aTrajectory)
        print(len(dienstregeling.trajectories))
        print("oldScore, should stay same")
        finalScore = oldScore

    # extraScore is better
    elif extraScore >= newScore and extraScore >= startScore and extraScore >= intermediateScore and extraScore >= newScore:
        dienstregeling.trajectories.append(aTrajectory)
        dienstregeling.trajectories.append(extraTrajectory)
        finalScore = extraScore
        print("extra, same or more")

    # if oldScore and newScore are the same
    elif oldScore == newScore:
        dienstregeling.trajectories.append(randomTrajectory)
        finalScore = oldScore
        print("oldscore = newscore, same")
