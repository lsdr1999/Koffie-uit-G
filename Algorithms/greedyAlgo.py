import random
from randomAlgo import makeRandomRoute
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
    startStation = random.choice(keylist)
    traject = Trajectory(maxLength)
    traject.addVisitedStations(startStation)

    # sorteer connection in railroad.station_dict[startStation].connections op de volgende manier:
        # niet bezocht en kritiek?
        # kortste tijd?
        # niet bezocht?
    # maken van traject op basis van iteratie over sorted list
            # niet bezocht en kritiek gevonden -> kies deze boven andere opties (onafhankelijk van tijd)
            # korste tijd gevonden en niet kritiek in connections -> kies deze boven andere opties
            # niet bezocht gevonden en niet kritiek of korte tijd -> kies dan deze , maar vervang wanneer mogelijk

    time = 0

    while (traject.length < traject.calculateLength):
        sorted = sorted(railroad.station_dict[startStation].connections, key = lambda connection:(connection[3].critical, connection[2]))

        for connection in sorted:
            nextStation = connection
            if (nextStation[1] not in traject.visitedStations) and (not (((startStation, nextStation[1]) in traject.visitedCritical) or ((nextStation[1], startStation) in traject.visitedCritical))):
                break

        if nextStation:
            nextStationName = nextStation[0]

            if nextStation[2].critical or startStation.critical:
                traject.addVisitedCritical(nextStation[1])
            traject.addVisitedStations(nextStationName)

            time = nextStation[3]
            startStation = nextStationName

        else:
            break

    traject.calculateLength()

    return ([traject.visitedStations, traject.length, traject.visitedCritical])
