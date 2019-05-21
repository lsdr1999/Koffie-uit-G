
def calculateScores(scoresList):
    scores = []
    for list in scoresList:
        for value in list:
            scores.append(value)

    average = mean(scores)
    highest = 0
    lowest = 10000
    for score in scores:
        if score > highest:
            highest = score
        elif score < lowest:
            lowest = score
