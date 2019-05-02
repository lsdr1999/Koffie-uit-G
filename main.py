# from dienstregeling import Dienstregeling
from railroad import Railroad
from sys import argv
from random_algo import make_random_route
from dienstregeling import Dienstregeling
from hillclimber_algo import hillclimber
from genetic_algo import genetic
# from traject import Trajectory

if (len(argv) != 4):
    print("main.py, max number trajectories, max length in minutes of trajectory, type of algorithm")
    quit(1)

if (argv[1].isalpha() or argv[2].isalpha()):
    print("number of trajectories and max length should be integers")
    quit(1)

maxTrajectories = argv[1]
maxLength = argv[2]
algorithm = argv[3]

railroad = Railroad()
railroad.loadStations()
totalCritical = railroad.addTotalCritical()

dienstregeling = Dienstregeling(maxTrajectories, maxLength, totalCritical)

if algorithm == "hillclimber":
    dienstregeling.addTrajectories(railroad)
    counter = 0
    for i in range(100000):
        counter += 1
        hillclimber(dienstregeling, railroad)
        score = dienstregeling.calculateScore()
        if (counter % 10000) == 0:
            print(f"counter: {counter} score: {score}")

    for trajectory in dienstregeling.trajectories:
        print(trajectory[0])
        print("\n")

if algorithm == "genetic":
    genetic(dienstregeling, railroad)
