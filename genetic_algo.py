import random
import math
from random_algo import make_random_route
from dienstregeling import Dienstregeling
from hillclimber_algo import hillclimber

def genetic(dienstregeling,railroad):
    dienstregeling = dienstregeling
    railroad = railroad
    populationSize = 50
    generations = 1000
    population = makePopulation(dienstregeling, populationSize, railroad)
    highestScore = 0
    bestDienstregeling = []
    counter = 0


    for i in range(generations):
        counter += 1
        scores = scorePopulation(dienstregeling, population)
        standardizedScores = standardize(scores)
        probabilityScores = calculateProbabilities(standardizedScores, population)
        mutatedChildren = []
        for j in range(populationSize):
            parents = chooseParents(population, probabilityScores)
            crossoverChild = crossover(parents)
            mutatedChild = mutate(crossoverChild, railroad, dienstregeling)
            dienstregeling.trajectories = mutatedChild
            mutatedChildScore = dienstregeling.calculateScore()

            if mutatedChildScore > highestScore:
                highestScore = mutatedChildScore
                bestDienstregeling = mutatedChild

            mutatedChildren.append(mutatedChild)

        if (counter % 10) == 0:
            print(f"counter: {counter} score: {highestScore}")
            print(len(mutatedChild))

        population = mutatedChildren


def makePopulation(dienstregeling, populationSize, railroad):
    populationList = []
    for i in range(populationSize):
        individual = []
        for i in range(dienstregeling.maxTrajectories):
            trajectory = make_random_route(railroad, dienstregeling.maxLength)
            individual.append(trajectory)
        populationList.append(individual)

    return populationList

def scorePopulation(dienstregeling, population):
    scoreList = []
    for individual in population:
        dienstregeling.trajectories = individual
        score = dienstregeling.calculateScore()
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


def chooseParents(population, probabilityScores):
    mergedList = list(zip(population, probabilityScores))

    r = random.random()
    ParentsTrajectories = []
    for i in range(2):
        for (possibleParent, probability) in mergedList:
            if r < probability:
                ParentsTrajectories.append(possibleParent)
                break
            else:
                r -= probability

    return ParentsTrajectories


def crossover(parents):
    r = random.randint(0,1)
    r2 = random.randint(4,6)
    child = []
    child += addCrossoverChild(int(len(parents[r]) - r2), parents[r])

    if r == 1:
        child += addCrossoverChild(r2, parents[0])
    else:
        child += addCrossoverChild(r2, parents[1])

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

def mutate(crossoverChild, railroad, dienstregeling):
    dienstregeling.trajectories = crossoverChild
    hillclimber(dienstregeling, railroad)
    mutatedChild = dienstregeling.trajectories

    return mutatedChild
