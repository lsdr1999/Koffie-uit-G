from algorithms import hillclimberAlgo as ha
from helpers import visual
import numpy as np
import random

def simAnnealing(railroad, trainlining):
    runs = 100000
    T = 1
    highestScore = 0
    countList = []
    scoreList = []
    scoreNames = ["newScore", "oldScore", "intermediateScore", "extraScore" ]
    trainlining.addTrajectories(railroad)
    for i in range(runs):
        info = getScores(railroad, trainlining)
        probabilityScores = calculateSoftmax(info[0], T)
        winner = chooseTrajectoryChange(probabilityScores, scoreNames)
        trainlining = changeTrainLining(winner, info[1])
        T = calculateT(T)
        score = trainlining.calculateScore()

        if score > highestScore:
            highestScore = score
            bestTrainLining = trainlining

        if ((i - 1) % 1000) == 0:
            print(f"counter: {(i-1)} score: {score} T = {T}")
            print(f"highest score: {highestScore}")

    visual.makeCard(railroad, bestTrainLining)


def getScores(railroad, trainlining):
    info = ha.hillclimber(railroad, trainlining, True)

    return info

def calculateT(T):
    T = T * 0.9999
    return T

def calculateSoftmax(scores, T):
    newScores = []
    for score in scores:
        score = score/(1000 * T)
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

def changeTrainLining(winner, trajectories):
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

    return trainlining
