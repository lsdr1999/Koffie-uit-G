from algorithms import advancedHillclimber as ah
from algorithms import hillclimberAlgo as ha
from algorithms import geneticAlgo as ge
from algorithms import greedyAlgo as gr
from algorithms import randomAlgo as ra
from algorithms import simulatedAnnealing as sa
from classes import railroad as rail
from classes import trainlining as tl
from helpers import userInterface as UI
from helpers import visual


def runAll(userChoice):
    """
    Receives whether the user wants to use the long or short UI. Then runs the UI, \
    generates the information for the algorithms and runs the specified algorithm.

    Args: userChoice (string)
    """
    
    if userChoice == "long":
        info = UI.userInterfaceLong()
    elif userChoice == "short":
        info = UI.userInterfaceShort()

    csvChoice = info[0]
    csvConnections = info[1]
    maxTrajectories = info[2]
    maxLength = info[3]
    algorithm = info[4]

    if algorithm == "genetic":
        populationSize = info[5]
        recombinationCoefficient = info[6]
        mutationRate = info[7]
        runs = info[8]
        image = info[9]

    elif algorithm == "simulatedAnnealing":
        hill = info[5]
        runs = info[6]
        image = info[7]

    elif algorithm == "all":
        populationSize = info[5]
        recombinationCoefficient = info[6]
        mutationRate = info[7]
        hill = info[8]
        runs = info[9]
        image = info[10]

    else:
        runs = info[5]
        image = info[6]

    railroad = rail.Railroad()
    railroad.loadStations(csvChoice, csvConnections)
    totalCritical = railroad.addTotalCritical()
    trainlining = tl.Trainlining(maxTrajectories, maxLength, totalCritical)

    if algorithm == "random":
        ra.runRandom(railroad, trainlining, runs, algorithm, image)

    elif algorithm == "greedy":
        gr.runGreedy(railroad, trainlining, runs, algorithm, image)

    elif algorithm == "hillclimber":
        ha.runHillclimber(railroad, trainlining, runs, algorithm, image)

    elif algorithm == "genetic":
        ge.genetic(trainlining, railroad, runs, algorithm, populationSize, recombinationCoefficient, mutationRate, image)

    elif algorithm == "advancedHillclimber":
        ah.runAdvancedHillclimber(railroad, trainlining, runs, algorithm, image)

    elif algorithm == "simulatedAnnealing":
        sa.simAnnealing(railroad, trainlining, runs, algorithm, hill, image)

    elif algorithm == "all":
        list1 = ra.runRandom(railroad, trainlining, runs, algorithm, image)
        list2 = gr.runGreedy(railroad, trainlining, runs, algorithm, image)
        list3 = ha.runHillclimber(railroad, trainlining, runs, algorithm, image)
        list4 = ge.genetic(trainlining, railroad, runs, algorithm, populationSize, recombinationCoefficient, mutationRate, image)
        list5 = ah.runAdvancedHillclimber(railroad, trainlining, runs, algorithm, image)
        list6 = sa.simAnnealing(railroad, trainlining, runs, algorithm, hill, image)

        list = [list1, list2, list3, list4, list5, list6]
        visual.makeTotalGraph(list)
