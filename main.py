from sys import argv
from classes import railroad as rail
from algorithms import randomAlgo
from classes import trainlining as tl
from algorithms import advancedHillclimber as ah
from algorithms import hillclimberAlgo as ha
from algorithms import geneticAlgo as ge
from algorithms import greedyAlgo as gr
from algorithms import randomAlgo as ra
from helpers import visual
from helpers import userInterface as UI
from algorithms import simulatedAnnealing as sa


if (len(argv) != 4):
    print("main.py, max number trajectories, max length in minutes of trajectory, type of algorithm")
    quit(1)

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

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "hillclimber":
    ha.runHillclimber(railroad, trainlining, runs)

if algorithm == "genetic":
    ge.genetic(trainlining, railroad)


if algorithm == "advancedhillclimber":
    ah.runAdvancedHillclimber(railroad, trainlining)


if algorithm == "simulatedannealing":
    sa.simAnnealing(railroad, trainlining)

# visual.makeCard(railroad, trainlining)
