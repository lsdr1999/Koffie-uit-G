from matplotlib import style
from Classes import railroad as rail
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def makeCard(railroad, dienstregeling):
    style.use('classic')
    ax1.clear()

    railroad = rail.Railroad()
    railroad.loadStations()

    xcor = []
    ycor = []

    # get the x and y coordinates from the card
    for key, value in railroad.station_dict.items():
        ycor.append(float(value.xcoordinate.strip()))
        xcor.append(float(value.ycoordinate.strip()))
    # make a scatterplot
    ax1.scatter(xcor,ycor, color='k')

    # make a dictionary of all of the trajectories and its coordinate lists
    coord_dict = {}
    counter = 1
    for trajectory in dienstregeling.trajectories:
        x = []
        y = []
        for city in trajectory.visitedStations:
            for key, value in railroad.station_dict.items():
                if city == key:
                    x.append(float(value.ycoordinate.strip()))
                    y.append(float(value.xcoordinate.strip()))
        coord_dict[str(counter)] = x, y
        counter += 1

    # plot each trajectory
    for key in coord_dict:
        ax1.plot(coord_dict[key][0], coord_dict[key][1])

    plt.title('Dienstregeling')
    plt.xlabel('x-coördinaten')
    plt.ylabel('y-coördinaten')
    plt.show()
