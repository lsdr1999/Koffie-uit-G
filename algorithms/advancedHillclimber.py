import copy
import random
from algorithms import randomAlgo as ra
from helpers import visual
import random

def runAdvancedHillclimber(railroad, trainlining, runs, algorithm, image):
    """
    Runs the advancedHillclimber algorithm for (runs) times. At the end it\
    generates a visual representation of the results.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        runs (int): amount of iterations chosen for the algorithm to run.
        algorithm (string): chosen algorithm (can be all or hillclimber).
        image (string): defines what image is generated after the algorithm.

    Returns (only when algorithm == "all"):
        list (list): list of the countList and scoreList
    """
    trainlining.addTrajectories(railroad)
    countList = []
    scoreList = []

    for i in range(int(runs)):
        trainlining = advancedHillclimber(railroad, trainlining, False)
        score = trainlining.calculateScore()
        if (i % 10) == 0:
            print(f"counter: {i} score: {score}")
        countList.append(i)
        scoreList.append(score)

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoreList)
    elif image == "visual":
        visual.makeCard(railroad, trainlining)


def advancedHillclimber(railroad, trainlining, sim):
    """
    Makes several adjustments to the initial trainlining. Then compares them to\
    one another, and keeps the best solution.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        sim (bool):

    Returns:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
    """

    number = random.randint(1,10)
    old = trainlining.calculateScore()
    startTrajectory = random.choice(trainlining.trajectories)
    trainlining.trajectories.remove(startTrajectory)
    start = startScore(trainlining)

    intermediateInfo = intermediateScore(trainlining, startTrajectory, number)
    intermediate = intermediateInfo[0]
    iTrajectory = intermediateInfo[1]
    iTrain = intermediateInfo[2]

    newInfo= newScore(trainlining, iTrajectory, number, railroad)
    new = newInfo[0]
    nTraject = newInfo[1]
    nTrain = newInfo[2]


    extraInfo = extraScore(trainlining, startTrajectory, railroad)
    extra = extraInfo[0]
    eTrain = extraInfo[1]

    if sim:
        return [start, old, intermediate, new, extra], [trainlining, startTrajectory, iTrain, nTrain, eTrain]

    trainlining.trajectories.append(startTrajectory)

    if extra > old and extra > start and extra > intermediate and extra > new and len(trainlining.trajectories) < trainlining.maxTrajectories:
        trainlining = eTrain

    elif start >= old and start >= intermediate and start >= extra and start >= new:
        trainlining.trajectories.remove(startTrajectory)

    elif intermediate > old and intermediate > start and intermediate > new and intermediate > extra:
        trainlining = iTrain

    elif new >= old and new > start and new >= intermediate and new > extra:
        trainlining = nTrain


    trainlining.calculateScore()
    return trainlining


def startScore(trainlining):
    """
    Calculates the startScore: the initial trainlining without the randomly selected\
    trajectory(startTrajectory).

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.

    Returns:
        startScore (float): calculated solution of the initial trainlining without\
        the randomly selected trajectory (startTrajectory).
    """
    startScore = trainlining.calculateScore()
    return startScore

def intermediateScore(trainlining, startTrajectory, number):
    """
    Makes small adjustments to the startTrajectory by popping stations. Then\
    calculates the solution of the trainlining while using that trajectory.

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        startTrajectory (Class): randomly selected trajectory from the trainlining.
        number (int): randomly selected integer between 1 and 10.

    Returns:
        intermediateScore (float): solution of the trainlining using the \
        imtermediateTrajectory.
        intermediateTrajectory (Class): adjusted startTrajectory
        intermediateTrainlining (Class): adjusted trainlining
    """
    intermediateTrajectory = copy.deepcopy(startTrajectory)
    intermediateTrainlining = copy.deepcopy(trainlining)

    for i in range(number):
        if len(intermediateTrajectory.connections) > 0:
            intermediateTrajectory.visitedStations.pop()
            intermediateTrajectory.connections.pop()

    intermediateTrainlining.trajectories.append(intermediateTrajectory)
    intermediateScore = intermediateTrainlining.calculateScore()
    return intermediateScore, intermediateTrajectory, intermediateTrainlining


def newScore(trainlining, iTrajectory, number, railroad):
    """
    Adjusts the iTrajectory (intermediateTrajectory) by adding new visited stations\
    at the start of the trajectory. Then calculates the solution of the trainlining \
    after adding this trajectory.

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        iTrajectory (Class): adjusted startTrajectory with popped stations.
        number (int): randomly selected integer between 1 and 10.
        railroad (Class): lays out the connections of the Netherlands or Holland.

    Returns:
        newScore (float): newly calculated solution of the adjusted tarinlining.
        newTrajectory (Class): the adjusted intermediateTrajectory.
        newTrainlining (Class): adjusted trainlining with the newTrajectory.

    """
    newTrajectory = copy.deepcopy(iTrajectory)
    newtrainlining = copy.deepcopy(trainlining)

    trajectoryLen = len(newTrajectory.visitedStations)
    startStation = newTrajectory.visitedStations[0]

    for i in range(number):
        nextStation = random.choice(railroad.stationDict[startStation].connections)
        nextStationName = nextStation[0]
        time = nextStation[1]
        critical = nextStation[2]
        id = nextStation[3]
        # check whether new connection does not exceed the maximal time of trajectory
        if newTrajectory.length + time < int(newTrajectory.maxLength):
            newTrajectory.visitedStations.insert(0, nextStationName)
            newTrajectory.connections.insert(0, [startStation, nextStationName, time, critical, id])
            newTrajectory.calculateLength()
            startStation = nextStationName
        else:
            break

    newtrainlining.trajectories.append(newTrajectory)
    newScore = newtrainlining.calculateScore()
    return newScore, newTrajectory, newtrainlining


def extraScore(trainlining, startTrajectory, railroad):
    """
    extraScore adds the startTrajectory to the trainlining and then newly generates\
    a random trajectory and also adds this to the trainlining. Then it calculates\
    the new solution.

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        startTrajectory (Class): randomly selected trajectory from trainlining.
        railroad (Class): lays out the connections of the Netherlands or Holland.

    Returns:
        extraScore (float): newly calculated solution of the adjusted trainlining.
        extraTrainlining (Class): adjusted trainlining with the startTrajectory\
        and extraTrajectory.

    """
    extraTrainlining = copy.deepcopy(trainlining)
    extraTrajectory = ra.makeRandomRoute(railroad, trainlining)
    extraTrainlining.trajectories.append(startTrajectory)
    extraTrainlining.trajectories.append(extraTrajectory)
    extraScore = extraTrainlining.calculateScore()
    return extraScore, extraTrainlining
