import random
from algorithms import randomAlgo as ra

def hillclimber(dienstregeling, railroad):

    # Save incoming arguments
    dienstregeling = dienstregeling
    railroad = railroad

    # Calculate the old score
    oldScore = dienstregeling.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    extraScore = 0
    extraTrajectory = []
    if len(dienstregeling.trajectories) < dienstregeling.maxTrajectories:
        extraTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
        dienstregeling.trajectories.append(extraTrajectory)
        extraScore = dienstregeling.calculateScore()
        dienstregeling.trajectories.remove(extraTrajectory)


    # Remove a random trajectory and calculate score
    changeTrajectory = random.choice(dienstregeling.trajectories)
    dienstregeling.trajectories.remove(changeTrajectory)
    intermediateScore = dienstregeling.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    newTrajectory = ra.make_random_route(railroad, dienstregeling.maxLength)
    dienstregeling.trajectories.append(newTrajectory)
    newScore = dienstregeling.calculateScore()

    # if the new score is the highest, return
    if newScore > oldScore and newScore > intermediateScore and newScore > extraScore:
        return

    # If the intermediate score was the highest, change back
    if intermediateScore > oldScore and intermediateScore > newScore and intermediateScore > extraScore:
        dienstregeling.trajectories.remove(newTrajectory)

    # If the orginal score was the highest, change back
    if oldScore > newScore and oldScore > intermediateScore and oldScore > extraScore:
        dienstregeling.trajectories.remove(newTrajectory)
        dienstregeling.trajectories.append(changeTrajectory)

    # Else if the extra trajectory was highest, change back
    if extraScore > newScore and extraScore > intermediateScore and extraScore > oldScore:
        dienstregeling.trajectories.remove(newTrajectory)
        dienstregeling.trajectories.append(changeTrajectory)
        dienstregeling.trajectories.append(extraTrajectory)
