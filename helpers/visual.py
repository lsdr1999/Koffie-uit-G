from matplotlib import style
from classes import railroad as rail
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def makeCard(railroad, trainlining):
    style.use('classic')
    coordinates = []
    connections = []
    for key, value in railroad.connections.items():
        if value[3]:
            coordinates.append(value[0])
            coordinates.append(value[1])
        else:
            connections.append(value[0])
            connections.append(value[1])

    x = []
    y = []
    for connection in connections:
        y.append(float(railroad.stationDict[connection].xCoordinate.strip()))
        x.append(float(railroad.stationDict[connection].yCoordinate.strip()))

    criticalX = []
    criticalY = []
    for coordinate in coordinates:
        criticalY.append(float(railroad.stationDict[coordinate].xCoordinate.strip()))
        criticalX.append(float(railroad.stationDict[coordinate].yCoordinate.strip()))

    plotX = []
    plotY = []
    for i in range(len(criticalX)):
        plotY.append(criticalY[i])
        plotX.append(criticalX[i])
        i += 1
        if (i % 2 == 0):
            ax1.plot(plotX,plotY, color = 'k')
            plotX.clear()
            plotY.clear()

    for i in range(len(x)):
        plotY.append(y[i])
        plotX.append(x[i])
        i += 1
        if (i % 2 == 0):
            ax1.plot(plotX,plotY, color = '#8F8987')
            plotX.clear()
            plotY.clear()

    xCritical = []
    yCritical = []
    xNormal = []
    yNormal = []

    for trajectory in trainlining.trajectories:
        for connection in trajectory.connections:
            for key, value in railroad.connections.items():
                if (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1])and value[3]:
                    for i in range(2):
                        xCritical.append(float(railroad.stationDict[connection[i]].yCoordinate.strip()))
                        yCritical.append(float(railroad.stationDict[connection[i]].xCoordinate.strip()))
                elif (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1]):
                    for i in range(2):
                        xNormal.append(float(railroad.stationDict[connection[i]].yCoordinate.strip()))
                        yNormal.append(float(railroad.stationDict[connection[i]].xCoordinate.strip()))


    for i in range(len(xCritical)):
        plotX.append(xCritical[i])
        plotY.append(yCritical[i])
        i += 1
        if (i % 2 == 0):
            ax1.plot(plotX,plotY, color = '#ff0000')
            plotX.clear()
            plotY.clear()

    for i in range(len(xNormal)):
        plotX.append(xNormal[i])
        plotY.append(yNormal[i])
        i += 1
        if (i % 2 == 0):
            ax1.plot(plotX,plotY, color = '#0000FF')
            plotX.clear()
            plotY.clear()

    plt.title('Trainlining')
    plt.xlabel('xCoordinates')
    plt.ylabel('yCoordinates')
    plt.show()

def makeGraph(countList, scoreList):
    style.use('classic')

    ax1.plot(countList, scoreList)

    plt.title('Performance')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()
