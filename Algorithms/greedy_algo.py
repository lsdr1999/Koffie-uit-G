import random
from Classes import station
from Classes import railroad
from Classes import traject

    # Finds the shortest path between critical stations
    # When adding stations to a trajectory we take into account whether
    # a stations has been visited yet. If we don't do this the program would
    # try to add the same stations over and over again.
    # Trajectories are added to linefeedings based on whether the linefeeding
    # score increases when said trajectory is added

    # CriticalConnections = setVisitedCriticalConnections
    #
    # addStation to Trajectory
    # visited
    #
    # trajectory toevoegen aan dienstregeling

def greedy(stations, maxLength):
    critical_visited = {}
    stations = stations
    maxLength = maxLength
    time = 0

    # Find random start station
    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    traject = Trajectory(maxLength)
    traject.addVisitedStations(start_station)

    for connection in railroad.station_dict[start_station].connections
        next_station = connection
        next_station[1] < next_station[1]
        # bovenstaande kan niet
        # hierna is het de bedoeling dat de laagste tijd wordt doorgegven aan de while
        shortest_connection = next_station[1]

    while (traject.length + time < traject.maxLength):

        for connection in railroad.station_dict[start_station].connections
            next_station = connection

            if next_station == critical and not traject.visitedCritical or traject.visitedStations #incl. shortest
                next_station_name = next_station[0]
                time += shortest_connection # kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                for connection in railroad.station_dict[start_station].connections:
                    if connection[0] == next_station_name and connection[2] == True:
                        traject.addVisitedCritical(connection[3])
                        break
                start_station = next_station_name
            elif next_station == critical and (not traject.visitedCritical or traject.visitedStations) #excl. shortest
                next_station_name = next_station[0]
                time += next_station[1] # niet kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                for connection in railroad.station_dict[start_station].connections:
                    if connection[0] == next_station_name and connection[2] == True:
                        traject.addVisitedCritical(connection[3])
                        break
            elif next_station != critical and not in traject.visitedStations #incl. shortest
                next_station_name = next_station[0]
                time += shortest_connection # kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                start_station = next_station_name
            elif next_station not in traject.visitedStations #excl. shortest
                next_station_name = next_station[0]
                time += next_station[1] # niet kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                start_station = next_station_name


# Pseudo:

# if connection of start_station is critical and shortest and not visited
#     choose this connection and repeat
#     startstation = next station
# elif connection of start_station is critical and shortest
#     choose this connection and repeat
#     startstation = next station
# elif connection of start_station is critical and not visited
#     choose this connection and repeat
#     startstation = next station
# elif connection of start_station is not visited and shortest
#     choose this connection and repeat
#     startstation = next station
# elif connection of start_station is shortest
#     choose this connection and repeat
#     startstation = next station
# else (connection of start_station is not visited)
#     choose this connection and repeat
#     startstation = next station

# Andere optie

# sortedconnections = sorted(railroad.station_dict[start_station].connections, key = lambda x: (1- x[1].critical, x[2]))
# next_station = False
#
# for connection in sortedconnections
#     next_station = connection
#     if (next_station[1] not in traject.VisitedStations) and (not (((start_station, next_station[1]) in critical_visited) or ((next_station[1], start_station) in critical_visited))):
#         break
#     next_station = False
#
# if next_station:
#     if next_station.critical or start_station.critical:
#         critical_visited = {(next_station[1], start_station): True}
