import random
import math
from random_algo import make_random_route
from dienstregeling import Dienstregeling
from hillclimber_algo import hillclimber

def genetic(dienstregeling,railroad):
    dienstregeling = dienstregeling
    railroad = railroad
    populationSize = 20
    generations = 100000
    recombinationCoefficient = 0.5
    mutationRate = 1
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
        mutatedchildrenscore = 0
        for j in range(populationSize):
            parents = chooseParents(population, probabilityScores)
            crossoverChild = crossover(parents, recombinationCoefficient)
            mutatedChild = mutate(crossoverChild, railroad, dienstregeling, mutationRate)
            dienstregeling.trajectories = mutatedChild
            mutatedChildScore = dienstregeling.calculateScore()
            mutatedchildrenscore += mutatedChildScore

            if mutatedChildScore > highestScore:
                highestScore = mutatedChildScore
                bestDienstregeling = mutatedChild

            mutatedChildren.append(mutatedChild)

        if (counter % 100) == 0:
            print(f"counter: {counter} score: {highestScore}")
            print(mutatedchildrenscore/ len(mutatedChildren))
            sum = 0
            for child in mutatedChildren:
                sum += int(len(child))
            print(sum/len(mutatedChildren))

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

def mutate(crossoverChild, railroad, dienstregeling, mutationRate):
    dienstregeling.trajectories = crossoverChild
    for i in range(mutationRate):
        hillclimber(dienstregeling, railroad)
    mutatedChild = dienstregeling.trajectories

    return mutatedChild

def mutate2(crossoverChild,railroad, dienstregeling, mutationRate):
    r = random.randint(1,3)
    if r == 1:
        crossoverChild.remove(random.choice(crossoverChild))

    elif r == 2 and len(crossoverChild) < 20:
        crossoverChild.append(make_random_route(railroad, dienstregeling.maxLength))

    else:
        crossoverChild.remove(random.choice(crossoverChild))
        crossoverChild.append(make_random_route(railroad, dienstregeling.maxLength))

    return crossoverChild
