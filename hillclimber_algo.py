import random
from random_algo import make_random_route

def hillclimber(dienstregeling, railroad):

    # Save incoming arguments
    dienstregeling = dienstregeling
    railroad = railroad

    # Calculate the old score
    oldScore = dienstregeling.calculateScore()

    # Remove a random trajectory and calculate score
    changeTrajectory = random.choice(dienstregeling.trajectories)
    dienstregeling.trajectories.remove(changeTrajectory)
    intermediateScore = dienstregeling.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    newTrajectory = make_random_route(railroad, dienstregeling.maxLength)
    dienstregeling.trajectories.append(newTrajectory)
    newScore = dienstregeling.calculateScore()

    # If the intermediate score was the highest, change back
    if intermediateScore > oldScore and intermediateScore > newScore:
        dienstregeling.trajectories.remove(newTrajectory)

    # If the orginal score was the highest, change back
    elif oldScore > newScore and oldScore > intermediateScore:
        dienstregeling.trajectories.remove(newTrajectory)
        dienstregeling.trajectories.append(changeTrajectory)
