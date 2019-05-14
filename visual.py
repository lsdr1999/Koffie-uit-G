from matplotlib import style
from Classes import railroad as rail
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def makeCard(railroad, dienstregeling):
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
        y.append(float(railroad.station_dict[connection].xcoordinate.strip()))
        x.append(float(railroad.station_dict[connection].ycoordinate.strip()))

    criticalX = []
    criticalY = []
    for coordinate in coordinates:
        criticalY.append(float(railroad.station_dict[coordinate].xcoordinate.strip()))
        criticalX.append(float(railroad.station_dict[coordinate].ycoordinate.strip()))

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

    for trajectory in dienstregeling.trajectories:
        for connection in trajectory.connections:
            for key, value in railroad.connections.items():
                if (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1])and value[3]:
                    for i in range(2):
                        xCritical.append(float(railroad.station_dict[connection[i]].ycoordinate.strip()))
                        yCritical.append(float(railroad.station_dict[connection[i]].xcoordinate.strip()))
                elif (connection[0] == value[0] and connection[1] == value[1]) or \
                    (connection[1] == value[0] and connection[0] == value[1]):
                    for i in range(2):
                        xNormal.append(float(railroad.station_dict[connection[i]].ycoordinate.strip()))
                        yNormal.append(float(railroad.station_dict[connection[i]].xcoordinate.strip()))


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

    plt.title('Dienstregeling')
    plt.xlabel('x-coördinaten')
    plt.ylabel('y-coördinaten')
    plt.show()

def makeGraph(count_list, score_list):
    style.use('classic')

    ax1.plot(count_list, score_list)

    plt.title('Prestatie random')
    plt.xlabel('Counter')
    plt.ylabel('Score')
    plt.show()
