import random
from station import Station
from railroad import Railroad

def make_random_route()

    connections = []
    traject = Trajectory(connections)
    start_station = random.choice(railroad.station_list)

    while True:
        next_station = random.choice(station.begin_station.connections])
        end_station_name = next_station[0]
        time = next_station[1]
        print(begin_station)
        print(end_station)

        if traject.length + time < traject.maxLength:
            traject.addConnection(begin_station, end_station_name, time)
            traject.addTime(time)
            start_station = end_station_name
        else:
            break
    print(traject)
    return traject
