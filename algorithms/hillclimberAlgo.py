import random
from algorithms import randomAlgo as ra
from helpers import visual

def runHillclimber(railroad, trainlining, runs, algorithm, image):
    countList = []
    scoreList = []
    sim = False
    trainlining.addTrajectories(railroad)
    for i in range(int(runs)):
        countList.append(i)
        hillclimber(railroad, trainlining, sim)
        score = trainlining.calculateScore()
        scoreList.append(score)
        if ((i - 1) % 100) == 0:
            print(f"counter: {(i-1)} score: {score}")

    if algorithm == "all":
        list = [countList, scoreList]
    elif image == "visual":
        visual.makeCard(railroad, trainlining)
    elif image == "graph":
        visual.makeGraph(countList, scoreList)
    return score

    return score

def hillclimber(railroad, trainlining, sim):
    oldScore = trainlining.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    extraScore = 0
    extraTrajectory = []
    if len(trainlining.trajectories) < trainlining.maxTrajectories:
        extraTrajectory = ra.makeRandomRoute(railroad, trainlining)
        trainlining.trajectories.append(extraTrajectory)
        extraScore = trainlining.calculateScore()
        trainlining.trajectories.remove(extraTrajectory)


    # Remove a random trajectory and calculate score
    changeTrajectory = random.choice(trainlining.trajectories)
    trainlining.trajectories.remove(changeTrajectory)
    intermediateScore = trainlining.calculateScore()

    # Insert a new randomly made trajectory and calculate score
    newTrajectory = ra.makeRandomRoute(railroad, trainlining)
    trainlining.trajectories.append(newTrajectory)
    newScore = trainlining.calculateScore()

    if sim:
        return [newScore, oldScore, intermediateScore, extraScore], [trainlining, newTrajectory, changeTrajectory, extraTrajectory]

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

    return trainlining
