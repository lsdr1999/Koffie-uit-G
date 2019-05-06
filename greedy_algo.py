import random
from random_algo import make_random_route

def greedy(dienstregeling, railroad):
    dienstregeling = dienstregeling
    railroad = railroad

    # Find random start station
    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    traject = Trajectory(maxLength)
    traject.addVisitedStations(start_station)

    sorted = []
    # sorteer connection in railroad.station_dict[start_station].connections op de volgende manier:
        # niet bezocht en kritiek?
        # kortste tijd?
        # niet bezocht?

    for connection in railroad.station_dict[start_station].connections:
        TODO

    # maken van traject op basis van iteratie over sorted list
            # niet bezocht en kritiek gevonden -> kies deze boven andere opties (onafhankelijk van tijd)
            # korste tijd gevonden en niet kritiek in connections -> kies deze boven andere opties
            # niet bezocht gevonden en niet kritiek of korte tijd -> kies dan deze , maar vervang wanneer mogelijk

    while (traject.length + time < traject.maxLength):

        for connection in railroad.station_dict[start_station].connections:
            next_station = connection

            if next_station == critical and not traject.visitedCritical or traject.visitedStations: #incl. shortest
                next_station_name = next_station[0]
                time += shortest_connection # kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                for connection in railroad.station_dict[start_station].connections:
                    if connection[0] == next_station_name and connection[2] == True:
                        traject.addVisitedCritical(connection[3])
                        break
                start_station = next_station_name

            elif next_station == critical and (not traject.visitedCritical or traject.visitedStations): #excl. shortest
                next_station_name = next_station[0]
                time += next_station[1] # niet kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                for connection in railroad.station_dict[start_station].connections:
                    if connection[0] == next_station_name and connection[2] == True:
                        traject.addVisitedCritical(connection[3])
                        break

            elif next_station != critical and not in traject.visitedStations: #incl. shortest
                next_station_name = next_station[0]
                time += shortest_connection # kortste next_station
                traject.addVisitedStations(next_station_name)
                traject.addLength(time)
                start_station = next_station_name

            elif next_station not in traject.visitedStations: #excl. shortest
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
