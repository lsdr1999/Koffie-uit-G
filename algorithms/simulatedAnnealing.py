from algorithms import hillclimberAlgo as ha
from algorithms import advancedHillclimber as ah
from helpers import visual
import numpy as np
import random

def simAnnealing(railroad, trainlining, runs, algorithm, hill, image):
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
        T = calculateT(T)
        score = trainlining.calculateScore()

        if score > highestScore:
            highestScore = score
            bestTrainLining = trainlining
        scoreList.append(highestScore)

        if ((i - 1) % 1000) == 0:
            print(f"counter: {(i-1)} score: {score} T = {T}")
            print(f"highest score: {highestScore} length {trainlining.trackLength}")

    for trajectory in bestTrainLining.trajectories:
        print(trajectory.visitedStations)

    if algorithm == "all":
        list = [countList, scoreList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoreList)
    elif image == "visual":
        visual.makeCard(railroad, trainlining)


def getScores(railroad, trainlining, basic):
    if basic:
        info = ha.hillclimber(railroad, trainlining, True)
    else:
        info = ah.advancedHillclimber(railroad, trainlining, True)

    return info

def calculateT(T):
    T = T * 0.9999
    return T

def calculateSoftmax(scores, T):
    newScores = []
    for score in scores:
        score = score / (1000 * T)
        newScores.append(score)

    scores = np.array(newScores)
    return np.exp(scores - (max(scores)-(max(scores) * T)))/ np.sum(np.exp(scores-(max(scores)- (max(scores) * T))))

def chooseTrajectoryChange(probabilityScores, scoreNames):
    mergedList = list(zip(probabilityScores, scoreNames))
    r = random.random()
    for probabilityScore, scoreName in mergedList:
        if r < probabilityScore:
            return scoreName
        else:
            r -= probabilityScore

def changeTrainLining(winner, trajectories, basic):
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
