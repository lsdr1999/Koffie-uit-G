import random
from station import Station
from railroad import Railroad
from traject import Trajectory

def make_random_route():
    railroad = Railroad()
    railroad.loadStations()
    railroad.addTotalCritical()
    maxLength = 120
    traject = Trajectory(maxLength)

    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    print(start_station)

    while True:
        next_station = random.choice(railroad.station_dict[start_station].connections)
        end_station_name = next_station[0]
        time = next_station[1]
        print(next_station)

        if traject.length + time < traject.maxLength:
            traject.addVisitedStations(next_station)
            traject.addLength(time)
            start_station = end_station_name
        else:
            break

    return traject
