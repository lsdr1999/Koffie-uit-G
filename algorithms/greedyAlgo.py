import random
from algorithms import randomAlgo

from classes import station
from classes import railroad
from classes import trajectory as tj
from classes import trainlining

def greedy_traject(trainlining, railroad, maxLength):

    # Find random start station
    keylist = []
    for key, value in railroad.stationDict.items():
        keylist.append(key)
    startStation = random.choice(keylist)
    trajectory = tj.Trajectory(maxLength)
    trajectory.addVisitedStations(startStation)

    # sorteer connection in railroad.station_dict[startStation].connections op de volgende manier:
        # niet bezocht en kritiek?
        # kortste tijd?
        # niet bezocht?
    # maken van traject op basis van iteratie over sorted list
            # niet bezocht en kritiek gevonden -> kies deze boven andere opties (onafhankelijk van tijd)
            # korste tijd gevonden en niet kritiek in connections -> kies deze boven andere opties
            # niet bezocht gevonden en niet kritiek of korte tijd -> kies dan deze , maar vervang wanneer mogelijk

    time = 0

    while (trajectory.length < trainlining.trackLength):
        iets = sorted(railroad.stationDict[startStation].connections, key = lambda connection:(1- connection[2], connection[1]))
        # print(iets)

        for connection in iets:
            nextStation = connection
            if (nextStation[0] not in trajectory.visitedStations) and (not (((startStation, nextStation[0]) in trajectory.visitedCritical) or ((nextStation[0], startStation) in trajectory.visitedCritical))):
                break

        if nextStation:
            nextStationName = nextStation[0]
            trajectory.calculateVisitedCritical()
            trajectory.addVisitedStations(nextStationName)
            time = nextStation[1]
            startStation = nextStationName

        else:
            break

    return ([trajectory.visitedStations, trajectory.length, trajectory.visitedCritical])
