from sys import argv
from helpers import run


if __name__ == "__main__":
    if len(argv) != 2:
        print("main.py, short/long")

<<<<<<< HEAD
if (argv[1].isalpha() or argv[2].isalpha()):
    print("number of trajectories and max length should be integers")
    quit(1)

maxTrajectories = argv[1]
maxLength = argv[2]
algorithm = argv[3]

railroad = rail.Railroad()
railroad.loadStations()
totalCritical = railroad.addTotalCritical()
trainlining = tl.Trainlining(maxTrajectories, maxLength, totalCritical)

countList = []
scoreList = []

runs = 10000



if algorithm == "random":
    ra.runRandom(railroad, trainlining, runs)

if algorithm == "greedy":
    gr.runGreedy(railroad, trainlining, runs)

if algorithm == "hillclimber":
    ha.runHillclimber(railroad, trainlining, runs)

if algorithm == "genetic":
    ge.genetic(trainlining, railroad)


if algorithm == "advancedhillclimber":
    ah.runAdvancedHillclimber(railroad, trainlining)


if algorithm == "simulatedannealing":
    sa.simAnnealing(railroad, trainlining)

# visual.makeCard(railroad, trainlining)
=======
    userChoice = argv[1]
    run.runAll(userChoice)
>>>>>>> 781142ae1605fa17e5f49aa5c1ae8776c165d787
