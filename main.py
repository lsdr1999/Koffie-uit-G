# from dienstregeling import Dienstregeling
from railroad import Railroad
from sys import argv
from random_algo import make_random_route
from dienstregeling import Dienstregeling
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

dienstregeling = Dienstregeling(maxTrajectories, maxLength, algorithm)
dienstregeling.make_dienstregeling()
