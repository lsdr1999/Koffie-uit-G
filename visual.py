from railroad import Railroad
import matplotlib.pyplot as plt
import csv

def makeCard(railroad, trajectories):
    railroad = Railroad()
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



    for key, value in railroad.station_dict.items():
        ycor.append(float(value.xcoordinate.strip()))
        xcor.append(float(value.ycoordinate.strip()))

    plt.scatter(xcor,ycor, color='k')

    trajectories = trajectories
    counter = 1
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
        if counter < len(trajectories):
            counter += 1
        else:
            break

    plt.plot(x1,y1, 'r', x2,y2, 'b', x3,y3, 'y', x4,y4, 'g', x5,y5, 'm', \
            x6,y6, 'c', x7,y7, 'r--', x8,y8, 'b--', x9,y9, 'y--', x10,y10, \
            'g--', x11,y11, 'm--', x12,y12, 'c--', x13,y13, 'r:', x14,y14, \
            'b:', x15,y15, 'y:', x16,y16, 'g:', x17,y17, 'm:', x18,y18, 'c:', \
             x19,y19, 'r-.', x20,y20, 'b-.')
    plt.show()
