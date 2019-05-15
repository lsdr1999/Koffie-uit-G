import random
from randomAlgo import make_random_route
from classes import station
from classes import railroad
from classes import trajectory
from station import Station
from railroad import Railroad
from traject import Trajectory

def greedy_traject(trainlining, railroad, maxLength):

    # Find random start station
    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    traject = Trajectory(maxLength)
    traject.addVisitedStations(start_station)

    # sorteer connection in railroad.station_dict[start_station].connections op de volgende manier:
        # niet bezocht en kritiek?
        # kortste tijd?
        # niet bezocht?
    # maken van traject op basis van iteratie over sorted list
            # niet bezocht en kritiek gevonden -> kies deze boven andere opties (onafhankelijk van tijd)
            # korste tijd gevonden en niet kritiek in connections -> kies deze boven andere opties
            # niet bezocht gevonden en niet kritiek of korte tijd -> kies dan deze , maar vervang wanneer mogelijk

    time = 0

    while (traject.length < traject.calculateLength):
        sorted = sorted(railroad.station_dict[start_station].connections, key = lambda connection:(connection[3].critical, connection[2]))

        for connection in sorted:
            next_station = connection
            if (next_station[1] not in traject.visitedStations) and (not (((start_station, next_station[1]) in traject.visitedCritical) or ((next_station[1], start_station) in traject.visitedCritical))):
                break

        if next_station:
            next_station_name = next_station[0]

            if next_station[2].critical or start_station.critical:
                traject.addVisitedCritical(next_station[1])
            traject.addVisitedStations(next_station_name)

            time = next_station[3]
            start_station = next_station_name

        else:
            break

    traject.calculateLength()

    return ([traject.visitedStations, traject.length, traject.visitedCritical])
