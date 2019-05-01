import random
from random_algo import make_random_route

def genetic(dienstregeling,railroad):
    dienstregeling = dienstregeling
    railroad = railroad
    populationsize = 10

    population = makePopulation()
    calculateScore


def makePopulation():
    populationList = []
    for i in range(populationsize):
        individual = []
        for i in range(dienstregeling.maxTrajectories):
            trajectory = make_random_route(railroad, dienstregeling.maxLength)
            individual.append(trajectory)
        populationList.append(individual)

    return populationList
