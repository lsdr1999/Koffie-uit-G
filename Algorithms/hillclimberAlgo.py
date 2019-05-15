import random
from algorithms import randomAlgo as ra

def hillclimber(trainlining, railroad):

    # Calculate the old score
    oldScore = trainlining.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    extraScore = 0
    extraTrajectory = []
    if len(trainlining.trajectories) < trainlining.maxTrajectories:
        extraTrajectory = ra.make_random_route(railroad, trainlining.maxLength)
        trainlining.trajectories.append(extraTrajectory)
        extraScore = trainlining.calculateScore()
        trainlining.trajectories.remove(extraTrajectory)


    # Remove a random trajectory and calculate score
    changeTrajectory = random.choice(trainlining.trajectories)
    trainlining.trajectories.remove(changeTrajectory)
    intermediateScore = trainlining.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    newTrajectory = ra.make_random_route(railroad, trainlining.maxLength)
    trainlining.trajectories.append(newTrajectory)
    newScore = trainlining.calculateScore()

    # if the new score is the highest, return
    if newScore > oldScore and newScore > intermediateScore and newScore > extraScore:
        return

    # If the intermediate score was the highest, change back
    if intermediateScore > oldScore and intermediateScore > newScore and intermediateScore > extraScore:
        trainlining.trajectories.remove(newTrajectory)

    # If the orginal score was the highest, change back
    if oldScore > newScore and oldScore > intermediateScore and oldScore > extraScore:
        trainlining.trajectories.remove(newTrajectory)
        trainlining.trajectories.append(changeTrajectory)

    # Else if the extra trajectory was highest, change back
    if extraScore > newScore and extraScore > intermediateScore and extraScore > oldScore:
        trainlining.trajectories.remove(newTrajectory)
        trainlining.trajectories.append(changeTrajectory)
        trainlining.trajectories.append(extraTrajectory)
