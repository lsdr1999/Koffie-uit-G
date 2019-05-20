import random
import math
from algorithms import randomAlgo as ra
from classes import trainlining
from classes import trajectory
from algorithms import hillclimberAlgo as ha
from algorithms import advancedHillclimber as ahc
from helpers import visual

def genetic(trainlining, railroad, runs, algorithm, populationSize, recombinationCoefficient, mutationRate, image):
    generations = int(runs) / populationSize
    population = makePopulation(trainlining, populationSize, railroad)
    highestScore = 0
    bestTrainlining = []
    countList = []
    scoresList = []

    for i in range(int(generations)):
        scores = scorePopulation(trainlining, population)
        standardizedScores = standardize(scores)
        probabilityScores = calculateProbabilities(standardizedScores, population)
        mutatedChildren = []
        mutatedChildrenScore = 0
        countList.append(i)
        for j in range(populationSize):
            number = 2
            parents = chooseParents(population, probabilityScores, number)
            crossoverChild = crossover(parents, recombinationCoefficient)
            mutatedChild = mutate(crossoverChild, railroad, trainlining, mutationRate)
            trainlining.trajectories = mutatedChild
            mutatedChildScore = trainlining.calculateScore()
            mutatedChildrenScore += mutatedChildScore

            if mutatedChildScore > highestScore:
                highestScore = mutatedChildScore
                bestTrainlining = mutatedChild
            mutatedChildren.append(mutatedChild)

        newPopulation = tournament(trainlining, population, mutatedChildren)

        if (i % 10) == 0:
            print(f"counter: {i} score: {highestScore}")
            trainlining.trajectories = bestTrainlining
            trainlining.calculateScore()
            print(len(trainlining.visitedCriticalConnections))

            sum = 0
            for individual in newPopulation:
                trainlining.trajectories = individual
                score = trainlining.calculateScore()
                sum += score
            print(sum/len(newPopulation))

        population = newPopulation
        scoresList.append(highestScore)
    trainlining.trajectories = bestTrainlining
    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        
    if algorithm == "all":
        list = [countList, scoresList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoresList)
    elif image == "visual":
        visual.makeCard(railroad, trainlining)




def makePopulation(trainlining, populationSize, railroad):
    populationList = []
    for i in range(populationSize):
        individual = []
        for i in range(trainlining.maxTrajectories):
            trajectory = ra.makeRandomRoute(railroad, trainlining)
            individual.append(trajectory)
        populationList.append(individual)

    return populationList

def scorePopulation(trainlining, population):
    scoreList = []
    for individual in population:
        trainlining.trajectories = individual
        score = trainlining.calculateScore()
        scoreList.append(score)
    return(scoreList)

def standardize(scores):
    lowScore = 10000
    for score in scores:
        if score < lowScore:
            lowScore = score

    standardizedScores = []
    for score in scores:
        standardizedScore = score - lowScore
        standardizedScores.append(standardizedScore)

    return standardizedScores

def calculateProbabilities(standardizedScores, population):
    scoreSum = 0
    for score in standardizedScores:
        scoreSum += score

    probabilities = []
    for score in standardizedScores:
        probability = score/scoreSum
        probabilities.append(probability)

    return probabilities


def chooseParents(population, probabilityScores, number):
    mergedList = list(zip(population, probabilityScores))
    r = random.random()
    parentsTrajectories = []
    for i in range(int(number)):
        for (possibleParent, probability) in mergedList:
            if r < probability:
                parentsTrajectories.append(possibleParent)
                break
            else:
                r -= probability

    return parentsTrajectories

def tournament(trainlining, parentPopulation, mutatedChildren):
    participants = []
    participants += parentPopulation
    participants += mutatedChildren
    newPopulation = []
    while len(participants) > 0:
        participant1 = random.choice(participants)
        trainlining.trajectories = participant1
        score1 = trainlining.calculateScore()
        participants.remove(participant1)
        participant2 = random.choice(participants)
        participants.remove(participant2)
        trainlining.trajectories = participant2
        score2 = trainlining.calculateScore()

        if score1 > score2:
            newPopulation.append(participant1)
        else:
            newPopulation.append(participant2)

    return newPopulation

def crossover(parents, recombinationCoefficient):
    r = random.randint(0,1)
    length = int(len(parents[r])-(len(parents[r]) * recombinationCoefficient))

    child = []
    child += addCrossoverChild(int(len(parents[r]) - length), parents[r])

    if r == 1:
        child += addCrossoverChild(length, parents[0])
    else:
        child += addCrossoverChild(length, parents[1])

    return child

def addCrossoverChild(length, parent):
    child = []
    for i in range(length):
        trajectory = random.choice(parent)
        while trajectory in child:
            trajectory = random.choice(parent)
            break
        child.append(trajectory)

    return child

def mutate(crossoverChild, railroad, trainlining, mutationRate):
    trainlining.trajectories = crossoverChild
    for i in range(mutationRate):
        ha.hillclimber(railroad, trainlining, False)
    mutatedChild = trainlining.trajectories

    return mutatedChild
