import random
from random_algo import make_random_route
from score import calculateScore

def hillclimber(railroad, trajectories, maxLength, totalCritical):

    railroad = railroad
    trajectories = trajectories
    maxLength = maxLength
    totalCritical

    oldScore = calculateScore(railroad,trajectories, totalCritical)
    print(int(oldScore))

    changeTrajectory = random.choice(trajectories)

    newTrajectory = make_random_route(railroad, maxLength)
