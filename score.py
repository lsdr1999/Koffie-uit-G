
def calculateScore(railroad, trajectories, totalCritical):

        trajectories = trajectories
        railroad = railroad
        minutes = 0
        visitedCriticalConnections = set()
        totalCritical = totalCritical

        for trajectory in trajectories:
            minutes += int(trajectory[1])
            visitedCriticalConnections.update(trajectory[2])

        p = float(len(visitedCriticalConnections)) / float(totalCritical)
        score = p * 10000 - (len(trajectories) * 20 + minutes / 10)

        return score
