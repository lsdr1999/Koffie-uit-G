from sys import argv
from Classes import railroad as rail
from Algorithms import random_algo
from Classes import dienstregeling as dr
from Algorithms import advanced_hillclimber as ah
from Algorithms import hillclimber_algo as ha
from Algorithms import genetic_algo as ge
# from Algorithms import greedy_algo as gr
from Algorithms import new_hillclimber_algo as nha
from visual import makeCard, makeGraph


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
    makeGraph(count_list, score_list)

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
    makeGraph(count_list, score_list)

    for trajectory in dienstregeling.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "genetic":
    ge.genetic(dienstregeling, railroad)

if algorithm == "newhillclimber":
    dienstregeling.addTrajectories(railroad)
    counter = 0
    for i in range(1000):
        counter += 1
        nha.newHillclimber(dienstregeling, railroad, maxLength)
        score = dienstregeling.calculateScore()
        count_list.append(counter)
        score_list.append(score)
        if (counter % 1000) == 0:
            print(f"counter: {counter} score: {score}")
    makeGraph(count_list, score_list)

if algorithm == "advancedhillclimber":
    dienstregeling.addTrajectories(railroad)
    counter = 0
    number = 3
    for i in range(100):
        counter += 1
        ah.advancedHillclimber(dienstregeling, railroad, maxLength, number)
        print("main")
        print(len(dienstregeling.trajectories))
        score = dienstregeling.calculateScore()

if algorithm == "greedy":
    gr.greedy_traject(dienstregeling, railroad, maxLength)
makeCard(railroad, dienstregeling)
