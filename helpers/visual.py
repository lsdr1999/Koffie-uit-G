from matplotlib import style
from classes import railroad as rail
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
style.use('classic')

def makeCard(railroad, trainlining):
    """
    Makes a visual representation of the trainlining based on the coordinates in\
    railroad.

    Args:
        railroad (Class): lays out the connections of the Netherlands or Holland.
        trainlining (Class): generated solution of an algorithm of a trainlining\
        through Holland or the Netherlands.
    """

    criticalCoordinates = []
    normalCoordinates = []
    for key, value in railroad.connections.items():
        if value[3]:
            criticalCoordinates.append(value[0])
            criticalCoordinates.append(value[1])
        else:
            normalCoordinates.append(value[0])
            normalCoordinates.append(value[1])

    criticalX = []
    criticalY = []
    for coordinate in criticalCoordinates:
        criticalY.append(float(railroad.stationDict[coordinate].xCoordinate.strip()))
        criticalX.append(float(railroad.stationDict[coordinate].yCoordinate.strip()))

    plotCriticalX = []
    plotCriticalY = []
    for i in range(len(criticalX)):
        plotCriticalY.append(criticalY[i])
        plotCriticalX.append(criticalX[i])
        i += 1
        if (i % 2 == 0):
            if i != (len(criticalX)):
                ax1.plot(plotCriticalX, plotCriticalY, color = 'k')
            else:
                ax1.plot(plotCriticalX, plotCriticalY, color = 'k', label = 'Unvisited critical')
            plotCriticalX.clear()
            plotCriticalY.clear()


    normalX = []
    normalY = []
    for coordinate in normalCoordinates:
        normalY.append(float(railroad.stationDict[coordinate].xCoordinate.strip()))
        normalX.append(float(railroad.stationDict[coordinate].yCoordinate.strip()))

    plotNormalX = []
    plotNormalY = []

    for i in range(len(normalX)):
        plotNormalY.append(normalY[i])
        plotNormalX.append(normalX[i])
        i += 1
        if (i % 2 == 0):
            if i != len(normalX):
                ax1.plot(plotNormalX, plotNormalY, color = '#8F8987')
            else:
                ax1.plot(plotNormalX, plotNormalY, color = '#8F8987', label = 'Unvisited noncritical')
            plotNormalX.clear()
            plotNormalY.clear()

    xCritical = []
    yCritical = []
    xNormal = []
    yNormal = []

    for trajectory in trainlining.trajectories:
        for connection in trajectory.connections:
            for key, value in railroad.connections.items():
                if (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1]):
                    for i in range(2):
                        if connection[3]:
                            xCritical.append(float(railroad.stationDict[connection[i]].yCoordinate.strip()))
                            yCritical.append(float(railroad.stationDict[connection[i]].xCoordinate.strip()))
                        else:
                            xNormal.append(float(railroad.stationDict[connection[i]].yCoordinate.strip()))
                            yNormal.append(float(railroad.stationDict[connection[i]].xCoordinate.strip()))

    plotXCritical = []
    plotYCritical = []

    for i in range(len(xCritical)):
        plotXCritical.append(xCritical[i])
        plotYCritical.append(yCritical[i])
        i += 1
        if (i % 2 == 0):
            if i != len(xCritical):
                ax1.plot(plotXCritical, plotYCritical, color = '#ff0000')
            else:
                ax1.plot(plotXCritical, plotYCritical, color = '#ff0000', label = 'Visited critical')
            plotXCritical.clear()
            plotYCritical.clear()

    plotXNormal = []
    plotYNormal = []
    for i in range(len(xNormal)):
        plotXNormal.append(xNormal[i])
        plotYNormal.append(yNormal[i])
        i += 1
        if (i % 2 == 0):
            if i != len(xNormal):
                ax1.plot(plotXNormal, plotYNormal, color = '#0000FF')
            else:
                ax1.plot(plotXNormal, plotYNormal, color = '#0000FF', label = 'Visited noncritical')
            plotXNormal.clear()
            plotYNormal.clear()

    plt.title('Trainlining')
    plt.xlabel('xcoordinates')
    plt.ylabel('ycoordinates')
    plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 0.1), ncol = 4, prop = {'size': 6.5})
    plt.show()

def makeGraph(countList, scoreList):
    """
    Constructs a graph using the counter (how many runs) and the score (quality\
    of the solution) as x and y coordinate.

    Args:
        countList (list): list from 0 to x (runs).
        scoreList (list): list of the values of the solutions of the trainlining.
    """
    ax1.plot(countList, scoreList)

    plt.title('Performance ')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()

def makeTotalGraph(list):
    """
    Constructs a graph using a list of all of the algorithms.

    Args:
        List of the following variables per algorithm:
            countList (list): list from 0 to x (runs).
            scoreList (list): list of the values of the solutions of the trainlining.
    """
    digit = 1
    for lists in list:
        if digit == 1:
            ax1.plot(lists[0], lists[1], label = 'Simulated Annealing', color = '#FFC300')
        elif digit == 2:
            ax1.plot(lists[0], lists[1], label = 'Random', color = '#BAD303')
        elif digit == 3:
            ax1.plot(lists[0], lists[1], label = 'Greedy', color = '#FF5733' )
        elif digit == 4:
            ax1.plot(lists[0], lists[1], label = 'Hillcimber', color = '#C70039')
        elif digit == 5:
            ax1.plot(lists[0], lists[1], label = 'Genetic', color = '#900C3F')
        else:
            ax1.plot(lists[0], lists[1], label = 'Advanced Hillclimber', color = '#20639B')
        digit += 1

    plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 0.2), ncol = 3, prop = {'size': 9})
    plt.title('All algorithms')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()
