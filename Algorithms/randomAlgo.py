import random
from classes import station
from classes import railroad
from classes import trajectory as tj

def make_random_route(railroad, maxLength):
    railroad = railroad
    maxLength = maxLength
    trajectory = tj.Trajectory(maxLength)

    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    trajectory.addVisitedStations(start_station)

    while True:
        next_station = random.choice(railroad.station_dict[start_station].connections)
        next_station_name = next_station[0]
        time = next_station[1]
        critical = next_station[2]
        id = next_station[3]

        if trajectory.length + time < trajectory.maxLength:
            trajectory.addVisitedStations(next_station_name)
            trajectory.addConnection(start_station, next_station_name, time, critical, id)
            trajectory.calculateLength()
            start_station = next_station_name
        else:
            break

    return trajectory
