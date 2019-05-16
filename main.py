from sys import argv
from classes import railroad as rail
from algorithms import randomAlgo
from classes import trainlining as tl
from algorithms import advancedHillclimber as ah
from algorithms import hillclimberAlgo as ha
from algorithms import geneticAlgo as ge
from algorithms import greedyAlgo as gr
from helpers import visual
from helpers import userInterface as UI


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

countList = []
scoreList = []

trainlining = tl.Trainlining(maxTrajectories, maxLength, totalCritical)
if algorithm == "random":
    counter = 0
    highestScore = 0
    for i in range(1):
        trainlining.trajectories = []
        counter += 1
        countList.append(counter)
        trainlining.addTrajectories(railroad)
        score = trainlining.calculateScore()
        if score > highestScore:
            highestScore = score
        scoreList.append(highestScore)
        if (counter % 100) == 0:
            print(f"counter: {counter} score: {highestScore}")
    visual.makeGraph(countList, scoreList)

if algorithm == "greedy":
    trainlining.addTrajectories(railroad)
    counter = 0
    for i in range(1):
        counter += 1
        gr.greedy_traject(trainlining, railroad, maxLength)
        score = trainlining.calculateScore()
        countList.append(counter)
        scoreList.append(score)
        if (counter % 1) == 0:
            print(f"counter: {counter} score: {score}")
    # visual.makeGraph(countList, scoreList)

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "hillclimber":
    trainlining.addTrajectories(railroad)
    counter = 0
    for i in range(10000):
        counter += 1
        ha.hillclimber(trainlining, railroad)
        score = trainlining.calculateScore()
        countList.append(counter)
        scoreList.append(score)
        if (counter % 1000) == 0:
            print(f"counter: {counter} score: {score}")
    # visual.makeGraph(countList, scoreList)

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "genetic":
    ge.genetic(trainlining, railroad)


if algorithm == "advancedhillclimber":
    trainlining.addTrajectories(railroad)
    counter = 0
    number = 1
    for i in range(10000):
        counter += 1
        trainlining = ah.advancedHillclimber(trainlining, railroad, maxLength, number)
        if (counter % 100) == 0:
            print(len(trainlining.trajectories))
            score = trainlining.calculateScore()
            print(f"counter: {counter} score: {score}")


visual.makeCard(railroad, trainlining)
