from os import sep

algorithmOptions = ["r", "ge", "gr", "h", "a", "s", "info", "all"]

def userInterfaceLong():
    print("     Welcome to RailNL")
    print("     _______________________________________________________________________ \n")

    print("     Would you like your trainlining to run over Holland or the Netherlands?")

    while True:
        csvChoice = input("     Type 'h' to select Holland, type 'n' for the Netherlands: \n")

        if csvChoice.lower() == "h":
            csvChoice = f"csvFiles{sep}stationsHolland.csv"
            csvConnections = f"csvFiles{sep}connectiesHolland.csv"
            print("     Your trainlining will run through Holland.")
            break

        elif csvChoice.lower() == "n":
            print("     Your trainlining will run through the Netherlands.")
            csvChoice = f"csvFiles{sep}stationsNationaal.csv"
            csvConnections = f"csvFiles{sep}connectiesNationaal"
            break

        else:
            print("     Invalid input! Please type in 'h' or 'n'.")

    print("     _______________________________________________________________________ \n")

    while True:
        maxTrajectories = input("     Please choose the maximum number of trajectories.\n\
     This number must be between 1 and 30: \n")

        if maxTrajectories.isdigit() is False:
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

        if maxLength.isdigit() is False:
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

        if algorithm.lower() not in algorithmOptions:
            print("Please select one of the options.\n")
            continue

        elif algorithm.lower() == "r":
            algorithm = "random"

        elif algorithm.lower() == "ge":
            algorithm = "genetic"
            while True:
                populationSize = input("     Please insert the populationSize (between 10 and 100) or choose 'd' for default settings.\n")

                if populationSize == "d":
                    populationSize = 40

                if int(populationSize) < 10 or int(populationSize) > 100:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                recombinationCoefficient = input("      Please insert the recombinationCoefficient (between 0 and 1) or choose 'd' for default. \n\
    This number defines the distribution of the trajectories of the parents used to generate the children. \n")

                if recombinationCoefficient == "d":
                    recombinationCoefficient = 0.5

                if float(recombinationCoefficient) < 0 or float(recombinationCoefficient) > 1:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                mutationRate = input("      Please insert the mutationRate (between 0 and 1) or choose 'd' for default.\n")

                if mutationRate == "d":
                    mutationRate = 1

                if float(mutationRate) < 0 or float(mutationRate) > 1:
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

                if hill != "a" and hill != "n":
                    print("     invalid input!\n")
                    continue
                break
        elif algorithm.lower() == "all":
            infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, 40, 0.5, 1, "hillclimber", 10000, "graph"]
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
    and the probabilities that higher scores are accepted increases.\n\
    All\n\
    Will run all algorithms for 10000 iterations in default settings.")
            continue

        print(f"     You have chosen the following algorithm: {algorithm}\n")
        break
    print("     _______________________________________________________________________ \n")

    while True:
        runs = input("     How many iterations should your algorithm run?\n\
     Your answer should be a positive integer.\n")

        if runs.isdigit() is False or int(runs) == 0:
            print("     Please insert a positive integer.\n")
            continue
        print(f"     Your algorithm will run {runs} times.\n")
        break
    print("     _______________________________________________________________________ \n")

    while True:
        image = input("     Would you like to see a visual of your trainlining or a graph of its performance?\n\
     'v' = visual\n     'g' = graph\n")

        if image.lower() != "v" and image.lower() != "g":
            print("     Please insert a valid option.\n")
            continue

        elif image.lower() == "v":
            image = "visual"

        else:
            image = "graph"
        print(f"     At the end of your runs, the program will show a {image}.\n")
        break
    print("     Your algorithm will start now.")

    if algorithm == "genetic":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, populationSize, recombinationCoefficient, mutationRate, runs, image]

    elif algorithm == "simulatedAnnealing":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, hill, runs, image]

    else:
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, runs, image]

    return infoList


def userInterfaceShort():
    while True:
        csvChoice = input("     Holland ('h') or the Netherlands ('n')\n")

        if csvChoice.lower() != "h" and csvChoice.lower() != "n":
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

        if maxTrajectories.isdigit() is False or int(maxTrajectories) < 1 or \
int(maxTrajectories) > 30:
            print("     Invalid input!")
            continue
        break
    while True:
        maxLength = input("     Maximum length per trajectory (30-250 minutes)\n")

        if maxLength.isdigit() is False or int(maxLength) < 30 or int(maxLength) \
> 250:
            print("     Invalid input!")
            continue
        break
    while True:
        algorithm = input("     algorithm (options: random ('r'), genetic ('ge'), greedy ('gr'), hillclimber ('h'), advanced hillclimber ('a'),\n     simulated annealing ('s'), all('all'). )\n")

        if algorithm.lower() not in algorithmOptions:
            print("     Invalid input!")
            continue

        elif algorithm.lower() == 'r':
            algorithm = "random"

        elif algorithm.lower() == 'ge':
            algorithm = "genetic"
            while True:
                populationSize = input("     Please insert the populationSize (between 10 and 100) or choose 'd' for default\n")

                if populationSize == "d":
                    populationSize = 40

                if int(populationSize) < 10 or int(populationSize) > 100:
                    print("     Invalid input!\n")
                    continue

                break

            while True:
                recombinationCoefficient = input("      Please insert the recombinationCoefficient (between 0 and 1) or choose 'd' for default.\n")

                if recombinationCoefficient == "d":
                    recombinationCoefficient = 0.5

                if float(recombinationCoefficient) < 0 or float(recombinationCoefficient) > 1:
                    print("     Invalid input!\n")
                    continue
                break

            while True:
                mutationRate = input("      Please insert the mutationRate (between 0 and 1) or choose 'd' for default.\n")

                if mutationRate == "d":
                    mutationRate = 1

                if float(mutationRate) < 0 or float(mutationRate) > 1 :
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

                if hill != "a" and hill != "n":
                    print("     invalid input!\n")
                    continue

                elif hill == "a":
                    hill = advancedHillclimber

                elif hill == "n":
                    hill = hillclimber

        elif algorithm.lower() == "all":
            infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, 40, 0.5, 1, "hillclimber", 10000, "graph"]
            return infoList
        break

    while True:
        runs = input("      How many runs?\n")

        if runs.isdigit() is False or int(runs) < 1:
            print("     Invalid input!")
            continue
        break

    while True:

        image = input("     Visual ('v') or graph ('g')?\n")

        if image.lower() != "g" and image.lower() != "v":
            print("     Invalid input!")
            continue

        elif image.lower() == "g":
            image = "graph"

        else:
            image = "visual"
        break
    print("     Your algorithm will start now. \n")
    print("     _______________________________________________________________________ \n")

    if algorithm == "genetic":
        infoList =[csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, populationSize, recombinationCoefficient, mutationRate, runs, image]

    elif algorithm == "simulatedAnnealing":
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, hill, runs, image]

    else:
        infoList = [csvChoice, csvConnections, maxTrajectories, maxLength, algorithm, runs, image]

    return infoList
