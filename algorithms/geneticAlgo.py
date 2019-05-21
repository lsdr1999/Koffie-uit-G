import random
import math
from algorithms import randomAlgo as ra
from classes import trainlining
from classes import trajectory
from algorithms import hillclimberAlgo as ha
from algorithms import advancedHillclimber as ahc
from helpers import visual

def genetic(trainlining, railroad, runs, rerun, algorithm, populationSize, recombinationCoefficient, mutationRate, image):
    """
    Generates a random population of x raillinings of which the scores are
    calculated. Based on these scores, probabilities for each raillining are
    generated. The higher the probability the higher the chance that a
    raillining is chosen. For x times, children are generated out of two
    raillinings. Out of these parents and children, two are are randomly chosen
    to 'battle' against each other. The one with the highest score survives.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        runs (int): amount of iterations chosen for the algorithm to run.
        rerun (string): defines whether the user wants to rerun the algorithm 100 times.
        algorithm (string): chosen algorithm (can be all or hillclimber).
        populationSize (int): the total population size
        recombinationCoefficient (int): the coefficient of recombination that takes place
        mutationRate (int): the rate in which mutation takes place
        image (string): defines what image is generated after the algorithm.

    Returns (only when algorithm == "all"):
        list (list): list of the countList and scoreList
    Returns (only when rerun == "y"):
        scoreList(list): list of the values of the solutions
    """
    generations = int(runs) / int(populationSize)
    population = makePopulation(trainlining, int(populationSize), railroad)
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
        for j in range(int(populationSize)):
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

        if (i % 10) == 0 and rerun == "n":
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
    if rerun == "n":
        for trajectory in trainlining.trajectories:
            print(trajectory.visitedStations)
    elif rerun == "y":
        return [scoresList, highestScore]

    if algorithm == "all":
        list = [countList, scoresList]
        return list
    elif image == "graph":
        visual.makeGraph(countList, scoresList)
    else:
        visual.makeCard(railroad, trainlining)


def makePopulation(trainlining, populationSize, railroad):
    """
    Creates a population and returns a list

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        int(populationSize (int): the total population size
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.

    Returns:
        a populationList which consists of the total population
    """
    populationList = []
    for i in range(int(populationSize)):
        individual = []
        for i in range(trainlining.maxTrajectories):
            trajectory = ra.makeRandomRoute(railroad, trainlining)
            individual.append(trajectory)
        populationList.append(individual)

    return populationList


def scorePopulation(trainlining, population):
    """
    Creates a list of scores

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        population (list): a population based on trainlining, populationSize and railroad

    Returns:
        a scoreList which consists of the scores of the total population
    """
    scoreList = []
    for individual in population:
        trainlining.trajectories = individual
        score = trainlining.calculateScore()
        scoreList.append(score)
    return(scoreList)


def standardize(scores):
    """
    Stadardizes the lowest score to create a bigger difference

    Args:
        scores (list): a list with all scores

    Returns:
        a list of standardizedScores
    """
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
    """
    Calculates the probabilities via standardizedScores and the population

    Args:
        standardizedScores (list): list of new scores
        population (list): a population based on trainlining, populationSize and railroad

    Returns:
        a list of probabilities
    """
    scoreSum = 0
    for score in standardizedScores:
        scoreSum += score

    probabilities = []
    for score in standardizedScores:
        probability = score/scoreSum
        probabilities.append(probability)

    return probabilities


def chooseParents(population, probabilityScores, number):
    """
    Chooses parents via population and probabilityScores

    Args:
        population (list): a population based on trainlining, populationSize and railroad
        probabilityScores (list): a list of all probability scores
        number (int): randomly generated int between 0 en 1

    Returns:
        a list of parentsTrajectories
    """

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
    """
    The tournament based on trainlining, the parent population and mutated children

    Args:
        trainlining (Class): generated solution of an algorithm of a trainlining\
        parentPopulation (list): list in which all parents are present
        mutatedChildren (list): list in which all children are present

    Returns:
        a list of the newPopulation
    """
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
    """
    Crossover recombination with parents to get children

    Args:
        parents (list): a list of all parents
        recombinationCoefficient (int): the coefficient of recombination that takes place

    Returns:
        a list of children
    """
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
    """
    Adds child to the Child list

    Args:
        length (int): the lenght of a trajectory
        parent (string): random parent from list

    Returns:
        a list of children
    """
    child = []
    for i in range(length):
        trajectory = random.choice(parent)
        while trajectory in child:
            trajectory = random.choice(parent)
            break
        child.append(trajectory)

    return child


def mutate(crossoverChild, railroad, trainlining, mutationRate):
    """
    Mutates the trainlining, creates trajectories via the mutationRate

    Args:
        crossoverChild (list): list of children
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
        mutationRate (int): the rate in which mutation takes place

    Returns:
        the mutatedChild, the new trajectory
    """
    trainlining.trajectories = crossoverChild
    for i in range(mutationRate):
        ha.hillclimber(railroad, trainlining, False)
    mutatedChild = trainlining.trajectories

    return mutatedChild
