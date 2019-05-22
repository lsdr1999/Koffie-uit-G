from algorithms import hillclimberAlgo as ha
from algorithms import advancedHillclimber as ah
from helpers import visual
import numpy as np
import random

def simAnnealing(railroad, trainlining, runs, rerun, algorithm, hill, image):
    """
    In this algorithm all changes are given a probability of
    acceptance based on a softmax of their respective scores. As the algorithm
    runs the probability that lower scores are accepted decreases, and the
    probabilities that higher scores are accepted increases.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        runs (int): amount of iterations chosen for the algorithm to run.
        rerun (string): defines whether the user wants to rerun the algorithm 100 times.
        algorithm (string): chosen algorithm (can be all or hillclimber).
        image (string): defines what image is generated after the algorithm.

    Returns(only when algorithm == "all"):
        list (list): list of the countList and scoreList
    Returns (only when rerun == "y"):
        highestScore (float): final solution of the algorithm.

    """
    if hill == "a":
        basic = False
    else:
        basic = True

    T = 1
    highestScore = 0
    countList = []
    scoreList = []

    if basic:
        scoreNames = ["newScore", "oldScore", "intermediateScore", "extraScore"]
    else:
        scoreNames = ["startScore", "oldScore", "intermediateScore", "newScore", "extraScore"]

    trainlining.addTrajectories(railroad)
    for i in range(int(runs)):
        countList.append(i)
        info = getScores(railroad, trainlining, basic)
        probabilityScores = calculateSoftmax(info[0], T)
        winner = chooseTrajectoryChange(probabilityScores, scoreNames)
        trainlining = changeTrainLining(winner, info[1], basic)
        T = calculateT(T, runs)
        score = trainlining.calculateScore()

        if score > highestScore:
            highestScore = score
            bestTrainLining = trainlining
        scoreList.append(highestScore)

        if ((i - 1) % 1000) == 0 and rerun == "n":
            print(f"counter: {(i-1)} score: {score} T = {T}")
            print(f"highest score: {highestScore} length {trainlining.trackLength}")
            print(len(trainlining.trajectories))
    if rerun == "n":
        for trajectory in bestTrainLining.trajectories:
            print(trajectory.visitedStations)
    elif rerun == "y":
        return highestScore

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoreList)
    else:
        visual.makeCard(railroad, trainlining)


def getScores(railroad, trainlining, basic):
    """
    Gets score information from the hillclimber algorithm

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        basic (string): choice for basic or advanced Hillclimber

    Returns:
        info (list): which includes information on the railroad and trainlining
    """
    if basic:
        info = ha.hillclimber(railroad, trainlining, True)
    else:
        info = ah.advancedHillclimber(railroad, trainlining, True)

    return info


def calculateT(T, runs):

    """
    Calculates the temperature

    Args:
        T (float): the temperature which is needed for the coolingscheme
        Runs (int): the amount of iterations
    Returns:
        T (float): the temperature which is needed for the coolingscheme
    """
    logarithmicMultiplier = 1-(10/ int(runs))
    T = T * logarithmicMultiplier

    return T


def calculateSoftmax(scores, T):
    """
    Calculates the softmax

    Args:
        scores (float): the solutions from the hillclimber
        T (float): the temperature

    Returns:
        The new solution
    """
    newScores = []
    for score in scores:
        score = score / (1000 * T)
        newScores.append(score)

    scores = np.array(newScores)
    return np.exp(scores - (max(scores)-(max(scores) * T)))/ np.sum(np.exp(scores-(max(scores)- (max(scores) * T))))


def chooseTrajectoryChange(probabilityScores, scoreNames):
    """
    Chooses the trajectory change

    Args:
        probabilityScores (int): the probability solutions
        scoreNames (string): the names of the solutions

    Returns:
        scoreName (string): name of the chosen solution
    """
    mergedList = list(zip(probabilityScores, scoreNames))
    r = random.random()
    for probabilityScore, scoreName in mergedList:
        if r < probabilityScore:
            return scoreName
        else:
            r -= probabilityScore


def changeTrainLining(winner, trajectories, basic):
    """
    Changes the trainlining to the winner and returns it

    Args:
        winner (string): the 'best' trainling
        trajectories (list): list of all trajectories
        basic (string): choice for basic or advanced Hillclimber

    Returns:
        The new trainlining
    """
    if basic:
        trainlining = trajectories[0]
        newTrajectory = trajectories[1]
        changeTrajectory = trajectories[2]
        extraTrajectory = trajectories[3]


        if winner == "intermediateScore":
            trainlining.trajectories.remove(newTrajectory)

        if winner == "oldScore":
            trainlining.trajectories.remove(newTrajectory)
            trainlining.trajectories.append(changeTrajectory)

        if winner == "extraScore":
            trainlining.trajectories.remove(newTrajectory)
            trainlining.trajectories.append(changeTrajectory)
            if extraTrajectory != []:
                trainlining.trajectories.append(extraTrajectory)
    else:
        trainlining = trajectories[0]
        startTrajectory = trajectories[1]
        iTrain = trajectories[2]
        nTrain = trajectories[3]
        eTrain = trajectories[4]

        if winner == "oldScore":
            trainlining.trajectories.append(startTrajectory)

        if winner == "intermediateScore":
            trainlining = iTrain

        if winner == "newScore":
            trainlining = nTrain

        if winner == "extraScore":
            trainlining.trajectories.append(startTrajectory)
            if len(trainlining.trajectories) < trainlining.maxTrajectories:
                trainlining = eTrain

    return trainlining
