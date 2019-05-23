from os import sep

algorithmOptions = ["r", "ge", "gr", "h", "a", "s", "info", "all"]

def userInterfaceLong():
    """
    Receives input from user regarding the variables required for the algorithms\
    to be executed. Additionaly, this version contains more information about the\
    algorithms for the user to understand them.

    Returns a list of the following variables:
        csvChoice (string): defines whether the railroad is constructed through\
        Holland or the Netherlands.
        csvConnections (string): defines whether the connections of the stations\
        are through Holland or the Netherlands.
        maxTrajectories (int): defines the maximum number of trajectories in\
        the trainlining.
        maxLength (int): the maximum length per trajectory in minutes.
        algorithm (string): defines which algorithm is to be used.
            if genetic:
                populationSize (int): defines how many parents and children\
                are generated.
                recombinationCoefficient (float):  defines the distribution \
                of the trajectories of the parents used to generate the children.
                mutationRate (float): defines the severity of a mutation.
            if simulatedAnnealing:
                hill (string): defines whether a hillclimber or advancedHillclimber\
                is used.
        runs (int): defines how many iterations the algorithm runs.
        rerun (string): defines whether the user wants to rerun the algorithm 100 times.
        image (string): defines what image is generated after the algorithm.

    """

    print("     Welcome to RailNL")
    print("     _______________________________________________________________________ \n")

    print("     If you'd like to quit during this UI, please type 'q' and press enter.\n\
        When the algorithm starts, you can only quit by pressing [ctrl][c] or [command][c].\n")

    print("     Would you like your trainlining to run over Holland or the Netherlands?")

    while True:
        csvChoice = input("     Type 'h' to select Holland, type 'n' for the Netherlands: \n")
        if csvChoice.lower() == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif csvChoice.lower() == "h":
            csvChoice = f"csvFiles{sep}stationsHolland.csv"
            csvConnections = f"csvFiles{sep}connectiesHolland.csv"
            print("     Your trainlining will run through Holland.")
            break

        elif csvChoice.lower() == "n":
            print("     Your trainlining will run through the Netherlands.")
            csvChoice = f"csvFiles{sep}stationsNationaal.csv"
            csvConnections = f"csvFiles{sep}connectiesNationaal.csv"
            break

        else:
            print("     Invalid input! Please type in 'h' or 'n'.")

    print("     _______________________________________________________________________ \n")

    while True:
        maxTrajectories = input("     Please choose the maximum number of trajectories.\n\
     This number must be between 1 and 30: \n")
        if maxTrajectories == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif maxTrajectories.isdigit() is False:
            print("\n     Please fill in an integer.")

        elif int(maxTrajectories) < 1 or int(maxTrajectories) > 30:
            print("\n     The maximum of trajectories must be between 1 and 30.")

        else:
            break
    print(f"     Your raillining will have a maximum of {maxTrajectories} trajectories.")
    print("     _______________________________________________________________________ \n")

    while True:
        maxLength = input("     Please choose the maximum length of the trajectories in minutes. \n\
     This number must be between 30 and 250: \n")
        if maxLength == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif maxLength.isdigit() is False:
            print("\n    Please fill in an integer.")

        elif int(maxLength) < 30 or int(maxLength) > 250:
            print("\n    The maximum length of your trajectories must be between 30 and 250 minutes.")

        else:
            break
    print(f"     Your trajectories will have the maximum length of {maxLength} minutes.")
    print("     _______________________________________________________________________ \n")

    while True:
        algorithm = input("     Please select one of the algorithms below: \n\
     'r' = random\n     'ge' = genetic \n     'gr' = greedy \n     'h' = hillclimber \n     'a' = advanced hillclimber\n\
     's' = simulated annealing\n     'all' = all algorithms\n\n     For more information regarding the algorithms type 'info'\n")
        if algorithm == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif algorithm.lower() not in algorithmOptions:
            print("Please select one of the options.\n")
            continue

        elif algorithm.lower() == "r":
            algorithm = "random"

        elif algorithm.lower() == "ge":
            algorithm = "genetic"
            while True:
                populationSize = input("     Please insert the populationSize (between 10 and 100) or choose 'd' for default settings.\n")
                if populationSize == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif populationSize == "d":
                    populationSize = 40
                elif populationSize.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif int(populationSize) < 10 or int(populationSize) > 100:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                recombinationCoefficient = input("      Please insert the recombinationCoefficient (between 0 and 1) or choose 'd' for default. \n\
    This number defines the distribution of the trajectories of the parents used to generate the children. \n")
                if recombinationCoefficient == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif recombinationCoefficient == "d":
                    recombinationCoefficient = 0.5
                elif recombinationCoefficient.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif float(recombinationCoefficient) < 0 or float(recombinationCoefficient) > 1:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                mutationRate = input("      Please insert the mutationRate (between 0 and 1) or choose 'd' for default.\n")

                if mutationRate == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif mutationRate == "d":
                    mutationRate = 1
                elif mutationRate.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif float(mutationRate) < 0 or float(mutationRate) > 1:
                    print("     Invalid input!\n")
                    continue
                break

        elif algorithm.lower() == "gr":
            algorithm = "greedy"

        elif algorithm.lower() == "h":
            algorithm = "hillclimber"

        elif algorithm.lower() == "a":
            algorithm = "advancedHillclimber"

        elif algorithm.lower() == "s":
            algorithm = "simulatedAnnealing"

            while True:
                hill = input("      Please insert the hillclimber you want to use (Advanced: 'a' or normal 'n')\n")
                if hill == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif hill != "a" and hill != "n":
                    print("     invalid input!\n")
                    continue
                break
        elif algorithm.lower() == "all":
            infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, 40, 0.5, 1, "hillclimber", 100000, "n", "graph"]
            return infoList

        elif algorithm.lower() == "info":
            print("    Random\n\
    Generates a random raillining with the maximum number of trajectories\n\n\
    Genetic\n\
    Generates a random population of x raillinings of which the scores are calculated.\n\
    Based on these scores, probabilities for each raillining are generated. The higher the \n\
    probability the higher the chance that a raillining is chosen. For x times, children \n\
    are generated out of two raillinings. Out of these parents and children, two are \n\
    are randomly chosen to 'battle' against each other. The one with the highest score \n\
    survives. This goes on for the entire population until the population is halved. \n\
    Finally, the cycle starts all over again, but then with the surviving raillinings as \n\
    starting point. \n\n\
    Greedy\n\
    A greedy trajectory starts at a random start station, and then keeps on choosing the \n\
    best option. In this case this choice is based on whether a neighbouring connection is critical, \n\
    whether it has the shortest traveltime, and whether it has already been visited. \n\
    This continues until the maximum time of a trajectory is reached. Then a new trajectory is \n\
    generated through the same procedure.\n\n\
    Hillclimber\n\
    The hillclimber first selects a randomly generated raillining. First, the initial score \n\
    of this raillining is calculated. Second, an extra trajectory is added to the raillining, \n\
    and a score is calculated. Third, the score is calculated for the raillining with one of \n\
    its initial trajectories replaced by another random trajectory. Finally, the scores are \n\
    compared to one another, and the best option for the raillining is chosen. This procedure \n\
    continues for a set amount of iterations.\n\n\
    Advanced Hillclimber\n\
    The advanced hillclimber is slightly different than the hillclimber described above. \n\
    This version compares more altered versions of a raillining, but still choses the best option. \n\
    The advanced version also takes smaller steps in order to generate better scores. To elaborate: \n\
    it first calculates the old score of the raillining, then it removes a randomly chosen trajectory \n\
    and calculates the score. Then the algorithm pops (i.e. removes the last variable in a list) a selected \n\
    number of stations and calculates the score afterwards. Additionaly, it adds the same number of stations \n\
    before the startstation of the trajectory and calculates the score. At last it also adds an extra \n\
    trajectory to the raillining and again calculates the score. \n\
    Finally, these scores are compared and the best raillining is chosen. This algorithm also runs for a \n\
    chosen amount of iterations. \n\n\
    Simulated Annealing\n\
    The Simulated annealing algorithm builds upon the hillclimber algorithm but instead of accepting the best change,\n\
    all changes are given a probability of acceptance based on a softmax of their respective scores.  \n\
    As the algorithm runs the probability that lower scores are accepted decreases,\n\
    and the probabilities that higher scores are accepted increases.\n\n\
    All\n\
    Will run all algorithms for 100000 iterations in default settings.\n\
    It will take approximately 20 minutes to run this function, and it will provide a graph at the end. \n\n")
            continue

        print(f"     You have chosen the following algorithm: {algorithm}\n")
        break
    print("     _______________________________________________________________________ \n")

    while True:
        runs = input("     How many iterations should your algorithm run?\n\
     Your answer should be a positive integer between 100 and 1000000.\n")
        if runs == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif runs.isdigit() is False:
            print("     Please insert a positive integer.\n")
            continue
        elif int(runs) < 100 or int(runs) > 1000000:
            print("     Your input has exceeded the minimum or maximum requirements!\n")
            continue
        print(f"     Your algorithm will run {runs} times.\n")
        break
    print("     _______________________________________________________________________ \n")

    while True:
        rerun = input ("    Would you like to rerun this a 100 times?\n\
    This will give a lowest, highest, and average value at the end.\n\
    This option does not provide a visual at the end and takes longer than average to run.\n\
    'y' = yes, 'n' = no\n")
        if rerun == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif rerun == "n":
            print("     Your algorithm will not rerun.")
        elif rerun == "y":
            print("     Your algorithm will rerun 100 times.")
        else:
            print("     Invalid input!\n")
            continue
        break
    print("     _______________________________________________________________________ \n")

    while True:
        if rerun == "y":
            image = "graph"
            break
        image = input("     Would you like to see a visual of your trainlining or a graph of its performance?\n\
        You can choose for a visual with the trajectories ('o'), or an overview of the current state of the connections.\n\
     'v' = visual\n     'g' = graph\n     'o' = old visual")

        if image == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()

        if image.lower() != "v" and image.lower() != "g" and image.lower() != 'o':
            print("     Please insert a valid option.\n")
            continue

        elif image.lower() == "v":
            image = "visual"
        elif image.lower() == "o":
            image = "old"
        else:
            image = "graph"
        print(f"     At the end of your runs, the program will show a {image}.\n")
        break
    print("     Your algorithm will start now.")

    if algorithm == "genetic":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, populationSize, recombinationCoefficient, mutationRate, runs, rerun, image]

    elif algorithm == "simulatedAnnealing":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, hill, runs, rerun, image]

    else:
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, runs, rerun, image]

    return infoList


def userInterfaceShort():
    """
    Receives input from user regarding the variables required for the algorithms\
    to be executed.

    Returns a list of the following variables:
        csvChoice (string): defines whether the railroad is constructed through\
        Holland or the Netherlands.
        csvConnections (string): defines whether the connections of the stations\
        are through Holland or the Netherlands.
        maxTrajectories (int): defines the maximum number of trajectories in\
        the trainlining.
        maxLength (int): the maximum length per trajectory in minutes.
        algorithm (string): defines which algorithm is to be used.
            if genetic:
                populationSize (int): defines how many parents and children\
                are generated.
                recombinationCoefficient (float):  defines the distribution \
                of the trajectories of the parents used to generate the children.
                mutationRate (float): defines the severity of a mutation.
            if simulatedAnnealing:
                hill (string): defines whether a hillclimber or advancedHillclimber\
                is used.
        runs (int): defines how many iterations the algorithm runs.
        rerun (string): defines whether the user wants to rerun the algorithm 100 times.
        image (string): defines what image is generated after the algorithm.

    """
    print("     Welcome to RailNL. To quit press 'q' as an answer to any question.\n\
      During the algorithm you can quit by pressing [ctrl][c] or [command][c]\n")
    while True:
        csvChoice = input("     Holland ('h') or the Netherlands ('n')\n")
        if csvChoice == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()

        elif csvChoice.lower() != "h" and csvChoice.lower() != "n":
            print("     Invalid input!")
            continue

        elif csvChoice.lower() == "h":
            csvChoice = f"csvFiles{sep}stationsHolland.csv"
            csvConnections = f"csvFiles{sep}connectiesHolland.csv"
            break

        else:
            csvChoice = f"csvFiles{sep}stationsNationaal.csv"
            csvConnections = f"csvFiles{sep}connectiesNationaal.csv"
        break
    while True:
        maxTrajectories = input("     Maximum trajectories (1-30)\n")
        if maxTrajectories == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()

        elif maxTrajectories.isdigit() is False or int(maxTrajectories) < 1 or \
int(maxTrajectories) > 30:
            print("     Invalid input!")
            continue
        break
    while True:
        maxLength = input("     Maximum length per trajectory (30-250 minutes)\n")
        if maxLength == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif maxLength.isdigit() is False or int(maxLength) < 30 or int(maxLength) \
> 250:
            print("     Invalid input!")
            continue
        break
    while True:
        algorithm = input("     algorithm (options: random ('r'), genetic ('ge'), greedy ('gr'), hillclimber ('h'), advanced hillclimber ('a'),\n     simulated annealing ('s'), all('all'). )\n")
        if algorithm == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif algorithm.lower() not in algorithmOptions:
            print("     Invalid input!")
            continue

        elif algorithm.lower() == 'r':
            algorithm = "random"

        elif algorithm.lower() == 'ge':
            algorithm = "genetic"
            while True:
                populationSize = input("     Please insert the populationSize (between 10 and 100) or choose 'd' for default\n")
                if populationSize == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif populationSize == "d":
                    populationSize = 40
                elif populationSize.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif int(populationSize) < 10 or int(populationSize) > 100:
                    print("     Invalid input!\n")
                    continue

                break

            while True:
                recombinationCoefficient = input("      Please insert the recombinationCoefficient (between 0 and 1) or choose 'd' for default.\n")

                if recombinationCoefficient == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif recombinationCoefficient == "d":
                    recombinationCoefficient = 0.5
                elif recombinationCoefficient.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif float(recombinationCoefficient) < 0 or float(recombinationCoefficient) > 1:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                mutationRate = input("      Please insert the mutationRate (between 0 and 1) or choose 'd' for default.\n")
                if mutationRate == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif mutationRate == "d":
                    mutationRate = 1
                elif mutationRate.isdigit() is False:
                    print("     Invalid input!\n")
                    continue
                elif float(mutationRate) < 0 or float(mutationRate) > 1 :
                    print("     Invalid input!\n")
                    continue
                break

        elif algorithm.lower() == 'gr':
            algorithm = "greedy"

        elif algorithm.lower() == 'h':
            algorithm = "hillclimber"

        elif algorithm.lower() == 'a':
            algorithm = "advancedHillclimber"

        elif algorithm.lower() == 's':
            algorithm = "simulatedAnnealing"

            while True:
                hill = input("      Hillclimber (Advanced: 'a' or normal 'n')\n")
                if hill == "q":
                    print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
                    quit()
                elif hill != "a" and hill != "n":
                    print("     invalid input!\n")
                    continue
                break

        elif algorithm.lower() == "all":
            infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, 40, 0.5, 1, "hillclimber", 100000, "n", "graph"]
            return infoList
        break

    while True:
        runs = input("      How many runs (100-1000000)?\n")
        if runs == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif runs.isdigit() is False:
            print("     Invalid input!")
            continue
        elif int(runs) < 100 or int(runs) > 1000000:
            print("     Invalid input!\n")
            continue
        break

    while True:
        rerun = input ("    Would you like to rerun this a 100 times?\n 'y' = yes, 'n' = no\n")
        if rerun == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif rerun != "n" and rerun != "y":
            print("     Invalid input!")
            continue
        break

    while True:

        if rerun == "y":
            image = "graph"
            break
        image = input("     Visual ('v'), old visual ('o') or graph ('g')?\n")

        if image == "q":
            print("     Thank you for choosing RAIL NL. We wish you a nice day. \n     Good bye.")
            quit()
        elif image.lower() != "g" and image.lower() != "v" and image.lower() != "o":
            print("     Invalid input!")
            continue
        elif image.lower() == "g":
            image = "graph"
        elif image.lower() == "o":
            image = "old"
        else:
            image = "visual"
        break
    print("     Your algorithm will start now. \n")
    print("     _______________________________________________________________________ \n")

    if algorithm == "genetic":
        infoList =[csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, populationSize, recombinationCoefficient, mutationRate, runs, rerun, image]

    elif algorithm == "simulatedAnnealing":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, hill, runs, rerun, image]

    else:
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, runs, rerun, image]

    return infoList
