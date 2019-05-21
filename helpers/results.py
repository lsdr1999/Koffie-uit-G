from __future__ import division
from statistics import mean

def calculateScores(scoresList):
    """
    Calculates the highest, lowest, and average score of 100 runs of an algorithm\
    of n iterations.

    Args:
        scoresList (list): list of lists containing the solutions of the algorithm.
    """
    scores = []
    for list in scoresList:
        for value in list:
            scores.append(value)

    average = mean(scores)
    highest = max(scores)
    lowest = min(scores)

    print("_______________________________________________________________________")
    print(f"Average: {average}\n")
    print(f"Highest: {highest}\n")
    print(f"Lowest: {lowest}\n")
