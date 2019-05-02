import random
from random_algo import make_random_route
from dienstregeling import Dienstregeling
from hillclimber_algo import hillclimber

def genetic(dienstregeling,railroad):
    dienstregeling = dienstregeling
    railroad = railroad
    populationSize = 10
    generations = 100000
    population = makePopulation(dienstregeling, populationSize, railroad)
    highestScore = 0
    bestDienstregeling = 0
    counter = 0

    for i in range(generations):
        counter += 1
        scores = scorePopulation(dienstregeling, population)
        pizza = 0
        for score in scores:
            pizza = pizza+ score
        pizza = pizza/10
        print(pizza)

        probabilityScores = calculateProbabilities(scores, population)
        parents = chooseParents(population, probabilityScores)
        mutatedChildren = []
        for j in range(populationSize):
            crossoverChild = crossover(parents, dienstregeling.maxTrajectories)
            mutatedChild = mutate(crossoverChild, railroad, dienstregeling)
            dienstregeling.trajectories = mutatedChild
            mutatedChildScore = dienstregeling.calculateScore()
            mutatedChildren.append(mutatedChild)

            if mutatedChildScore > highestScore:
                highestScore = mutatedChildScore
                bestDienstregeling = mutatedChild

        if (counter % 100) == 0:
            print(f"counter: {counter} score: {highestScore}")

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

def calculateProbabilities(scores, population):
    scoreSum = 0
    for score in scores:
        score -= 5000
        scoreSum += score

    probabilities = []
    for score in scores:
        score -= 5000
        probability = score/scoreSum
        probabilities.append(probability)

    return probabilities

def chooseParents(population, probabilityScores):
    mergedList = list(zip(population, probabilityScores))

    r = random.random()
    combinedParentsTrajectories = []
    for i in range(2):
        for (possibleParent, probability) in mergedList:
            if r < probability:
                combinedParentsTrajectories = combinedParentsTrajectories + possibleParent
                break
            else:
                r -= probability

    return combinedParentsTrajectories

def crossover(parents, maxTrajectories):
    child = []
    for i in range(maxTrajectories):
        trajectory = random.choice(parents)
        while trajectory in child:
            trajectory = random.choice(parents)
        child.append(trajectory)

    return child

def mutate(crossoverChild, railroad, dienstregeling):
    changeTrajectory = random.choice(crossoverChild)
    crossoverChild.remove(changeTrajectory)

    newTrajectory = make_random_route(railroad, dienstregeling.maxLength)
    crossoverChild.append(newTrajectory)

    return crossoverChild
