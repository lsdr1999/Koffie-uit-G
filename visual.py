from matplotlib import style
from Classes import railroad as rail
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def makeCard(railroad, trajectories):
    style.use('classic')
    ax1.clear()

    railroad = rail.Railroad()
    railroad.loadStations()
    # lists of coordinates for the entire map
    xcor = []
    ycor = []

    # lists of trajectories 1-20
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []
    x5 = []
    y5 = []
    x6 = []
    y6 = []
    x7 = []
    y7 = []
    x8 = []
    y8 = []
    x9 = []
    y9 = []
    x10 = []
    y10 = []
    x11 = []
    y11 = []
    x12 = []
    y12 = []
    x13 = []
    y13 = []
    x14 = []
    y14 = []
    x15 = []
    y15 = []
    x16 = []
    y16 = []
    x17 = []
    y17 = []
    x18 = []
    y18 = []
    x19 = []
    y19 = []
    x20 = []
    y20 = []

    # get the x and y coordinates from the card
    for key, value in railroad.station_dict.items():
        ycor.append(float(value.xcoordinate.strip()))
        xcor.append(float(value.ycoordinate.strip()))
    # make a scatterplot
    ax1.scatter(xcor,ycor, color='k')

    # get the trajectories
    trajectories = trajectories
    counter = 1

    # for each trajectory, make its own line with x and y coordinates
    for trajectory in trajectories:
        for city in trajectory[0]:
            for key, value in railroad.station_dict.items():
                if city == key:
                    if counter == 1:
                        x1.append(float(value.ycoordinate.strip()))
                        y1.append(float(value.xcoordinate.strip()))
                    elif counter == 2:
                        x2.append(float(value.ycoordinate.strip()))
                        y2.append(float(value.xcoordinate.strip()))
                    elif counter == 3:
                        x3.append(float(value.ycoordinate.strip()))
                        y3.append(float(value.xcoordinate.strip()))
                    elif counter == 4:
                        x4.append(float(value.ycoordinate.strip()))
                        y4.append(float(value.xcoordinate.strip()))
                    elif counter == 5:
                        x5.append(float(value.ycoordinate.strip()))
                        y5.append(float(value.xcoordinate.strip()))
                    elif counter == 6:
                        x6.append(float(value.ycoordinate.strip()))
                        y6.append(float(value.xcoordinate.strip()))
                    elif counter == 7:
                        x7.append(float(value.ycoordinate.strip()))
                        y7.append(float(value.xcoordinate.strip()))
                    elif counter == 8:
                        x8.append(float(value.ycoordinate.strip()))
                        y8.append(float(value.xcoordinate.strip()))
                    elif counter == 9:
                        x9.append(float(value.ycoordinate.strip()))
                        y9.append(float(value.xcoordinate.strip()))
                    elif counter == 10:
                        x10.append(float(value.ycoordinate.strip()))
                        y10.append(float(value.xcoordinate.strip()))
                    elif counter == 11:
                        x11.append(float(value.ycoordinate.strip()))
                        y11.append(float(value.xcoordinate.strip()))
                    elif counter == 12:
                        x12.append(float(value.ycoordinate.strip()))
                        y12.append(float(value.xcoordinate.strip()))
                    elif counter == 13:
                        x13.append(float(value.ycoordinate.strip()))
                        y13.append(float(value.xcoordinate.strip()))
                    elif counter == 14:
                        x14.append(float(value.ycoordinate.strip()))
                        y14.append(float(value.xcoordinate.strip()))
                    elif counter == 15:
                        x15.append(float(value.ycoordinate.strip()))
                        y15.append(float(value.xcoordinate.strip()))
                    elif counter == 16:
                        x16.append(float(value.ycoordinate.strip()))
                        y16.append(float(value.xcoordinate.strip()))
                    elif counter == 17:
                        x17.append(float(value.ycoordinate.strip()))
                        y17.append(float(value.xcoordinate.strip()))
                    elif counter == 18:
                        x18.append(float(value.ycoordinate.strip()))
                        y18.append(float(value.xcoordinate.strip()))
                    elif counter == 19:
                        x19.append(float(value.ycoordinate.strip()))
                        y19.append(float(value.xcoordinate.strip()))
                    else:
                        x20.append(float(value.ycoordinate.strip()))
                        y20.append(float(value.xcoordinate.strip()))
        #check whether all of the trajectories are plotted
        if counter < len(trajectories):
            counter += 1
        else:
            break

    # plot all of the coordinates of the trajectories
    ax1.plot(x1,y1, '#B22222', x2,y2, '#FF4500', x3,y3, '#FFA500', x4,y4, \
            '#FFD700', x5,y5, '#7FFF00', x6,y6, '#008000', x7,y7, '#00FA9A', \
            x8,y8, '#20B2AA', x9,y9, '#00FFFF', x10,y10, '#00BFFF', x11,y11, \
            '#000080', x12,y12, '#0000FF', x13,y13, '#8A2BE2', x14,y14, \
            '#8B008B', x15,y15, '#FF00FF', x16,y16, '#FF1493', x17,y17, \
            '#D2691E', x18,y18, '#FFC0CB', x19,y19, '#9400D3', x20,y20, '#7FFFD4')
    plt.title('Dienstregeling')
    plt.xlabel('x-coördinaten')
    plt.ylabel('y-coördinaten')
    plt.show()

def animate():
    ani = animation.FuncAnimation(plt, makeCard, interval=1000)
    plt.show()
