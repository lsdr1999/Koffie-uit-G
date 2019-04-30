import random
from random_algo import make_random_route
from score import calculateScore

def hillclimber(railroad, trajectories, maxLength, totalCritical):

    railroad = railroad
    trajectories = trajectories
    maxLength = maxLength
    totalCritical

    oldScore = calculateScore(railroad,trajectories, totalCritical)
    changeTrajectory = random.choice(trajectories)
    trajectories.remove(changeTrajectory)
    intermediateScore = calculateScore(railroad, trajectories, totalCritical)
    newTrajectory = make_random_route(railroad, maxLength)
    trajectories.append(newTrajectory)
    newScore = calculateScore(railroad,trajectories, totalCritical)
    # print("the trajectory that is to be changed:")
    # print(changeTrajectory)
    # print("the trajectory that will replace it")
    # print(newTrajectory)

    if newScore > oldScore and newScore > intermediateScore:
        # for trajectory in trajectories:
        #     print(trajectory)
        # print(int(oldScore))
        # print(int(newScore))
        return trajectories

    elif intermediateScore > oldScore and intermediateScore > newScore:
        trajectories.remove(newTrajectory)
        return trajectories
    else:
        trajectories.remove(newTrajectory)
        trajectories.append(changeTrajectory)
        # for trajectory in trajectories:
        #     print(trajectory)
        # print(int(oldScore))
        # print(int(newScore))
        return trajectories
