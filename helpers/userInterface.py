def userInterface():
    print("Welcome to RailNL")
    print("_______________________________________________________________________ \n")
    # print("Please select the maximum amount of trajectories")
    print("Would you like your trainlining to run over Holland or the Netherlands?")
    while True:
        csvChoice = input("Type 'h' to select Holland, type 'n' for the Netherlands: \n")
        if csvChoice == "h" or csvChoice == "H":
            print("Your trainlining will run through Holland.")
            break
        elif csvChoice == "n" or csvChoice == "N":
            print("Your trainlining will run through the Netherlands.")
            break
        else:
            print("Invalid input! Please type in 'h' or 'n'")

    print("_______________________________________________________________________ \n")
    while True:
        maxTrajectories = input("Please choose the maximum number of trajectories.\n\
    This number must be between 1 and 30: \n")
        if maxTrajectories.isdigit() is False:
            print("\nPlease fill in an integer")
        elif int(maxTrajectories) < 1 or int(maxTrajectories) > 30:
            print("\nThe maximum of trajectories must be between 1 and 30.")
        else:
            break
    print(f"Your raillining will have a maximum of {maxTrajectories} trajectories.")
    print("_______________________________________________________________________ \n")
    while True:
        maxLength = input("Please choose the maximum length of the trajectories in minutes. \n\
    This number must be between 30 and 250: \n")
        if maxLength.isdigit() is False:
            print("\nPlease fill in an integer.")
        elif int(maxLength) < 30 or int(maxLength) > 250:
            print("\n The maximum length of your trajectories must be between 30 and 250 minutes.")
        else:
            break
    print(f"Your trajectories will have the maximum length of {maxLength} minutes.")
    print("_______________________________________________________________________ \n")
    algorithmOptions = ["r", "R", "ge", "GE", "gr", "GR", "h", "H", "a", "A", "s", "S", "info", "INFO"]
    while True:
        algorithm = input("Please select one of the algorithms below: \n\
    'r' = random\n'ge' = genetic \n'gr' = greedy \nh' = hillclimber \n'a' = advanced hillclimber\n\
    's' = simulated annealing\n\nFor more information regarding the algorithms type 'info'\n")
        if algorithm not in algorithmOptions:
            print("Please select one of the options.\n")
            continue
        elif algorithm.lower() == "r":
            algorithm = "random"
        elif algorithm.lower() == "ge":
            algorithm = "genetic"
        elif algorithm.lower() == "gr":
            algorithm = "greedy"
        elif algorithm.lower() == "h":
            algorithm = "hillclimber"
        elif algorithm.lower() == "a":
            algorithm = "advancedHillclimber"
        elif algorithm.lower() == "s":
            algorithm = "simulatedAnnealing"
        elif algorithm.lower() == "info":
            print("Random\n\
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
    ...")
            continue

        print(f"You have chosen the following algorithm: {algorithm}\n")
        break
