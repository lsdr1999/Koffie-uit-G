from sys import argv
from helpers import run


if __name__ == "__main__":
    if len(argv) != 2:
        print("main.py, short/long")

    userChoice = argv[1]
    run.runAll(userChoice)
