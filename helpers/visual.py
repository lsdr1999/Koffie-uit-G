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
                    (connection[1] == value[0] and connection[0] == value[1])and value[3]:
                    for i in range(2):
                        xCritical.append(float(railroad.stationDict[connection[i]].yCoordinate.strip()))
                        yCritical.append(float(railroad.stationDict[connection[i]].xCoordinate.strip()))
                elif (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1]):
                    for i in range(2):
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

    plt.title('Dienstregeling')
    plt.xlabel('x-coördinaten')
    plt.ylabel('y-coördinaten')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), ncol=4, prop = {'size': 6.5})
    plt.show()

def makeGraph(countList, scoreList):
    style.use('classic')

    ax1.plot(countList, scoreList)

    plt.title('Prestatie random')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()
