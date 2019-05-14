from sys import argv
from classes import railroad as rail
from algorithms import randomAlgo
from classes import dienstregeling as dr
from algorithms import advancedHillclimber as ah
from algorithms import hillclimberAlgo as ha
from algorithms import geneticAlgo as ge
# from algorithms import greedy_algo as gr
from helpers import visual


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

count_list = []
score_list = []

dienstregeling = dr.Dienstregeling(maxTrajectories, maxLength, totalCritical)
if algorithm == "random":
    counter = 0
    highestScore = 0
    for i in range(1):
        dienstregeling.trajectories = []
        counter += 1
        count_list.append(counter)
        dienstregeling.addTrajectories(railroad)
        score = dienstregeling.calculateScore()
        if score > highestScore:
            highestScore = score
        score_list.append(highestScore)
        if (counter % 100) == 0:
            print(f"counter: {counter} score: {highestScore}")
    visual.makeGraph(count_list, score_list)

if algorithm == "hillclimber":
    dienstregeling.addTrajectories(railroad)
    counter = 0
    for i in range(100000):
        counter += 1
        ha.hillclimber(dienstregeling, railroad)
        score = dienstregeling.calculateScore()
        count_list.append(counter)
        score_list.append(score)
        if (counter % 1000) == 0:
            print(f"counter: {counter} score: {score}")
    visual.makeGraph(count_list, score_list)

    for trajectory in dienstregeling.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "genetic":
    ge.genetic(dienstregeling, railroad)


if algorithm == "advancedhillclimber":
    dienstregeling.addTrajectories(railroad)
    counter = 0
    number = 1
    for i in range(10000):
        counter += 1
        dienstregeling = ah.advancedHillclimber(dienstregeling, railroad, maxLength, number)
        if (counter % 100) == 0:
            print(len(dienstregeling.trajectories))
            score = dienstregeling.calculateScore()
            print(f"counter: {counter} score: {score}")


visual.makeCard(railroad, dienstregeling)
