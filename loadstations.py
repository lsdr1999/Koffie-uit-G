from station import Station
from railroad import Railroad
import csv

# Open the Stations file and create empty station dictionary
with open("csv_bestanden/StationsHolland.csv") as f:
    stations = {}
    # Iterate over the lines
    for line in f:

        # Split the lines into words and save them into seperate variables
        station_data = (line.split(','))
        name = station_data[0]
        xcoordinate = station_data[1]
        ycoordinate = station_data[2]

        # If the station is critical save "Kritiek" as a boolean
        if station_data[3] == "Kritiek\n":
            critical = True
        else:
            critical = False

        # Initialize a station object and save it in a dictionary with
        # its name as the key
        railroad = Railroad()
        railroad.addStation(name, critical)
        station = Station(name, xcoordinate, ycoordinate, critical)
        stations[name] = station

# Close the file
f.close()

# Open the the connections files
with open("csv_bestanden/ConnectiesHolland.csv") as g:

    # Iterate over the lines
    for line in g:

        # Split the words on each lines and save them in seperate variables
        connection_data = line.split(',')
        station1 = connection_data[0]
        station2 = connection_data[1]
        time = int(connection_data[2])

        # If one of the stations in the connection is critical, save the
        # connection as a critical connection
        if stations[station1] == True or \
           stations[station2].critical == True:
            stations[station1].addConnection(station2, time, True)
            stations[station2].addConnection(station1, time, True)
            railroad.addConnection(station1, station2, time, True)

        # If neither station is critical, save it as a non-critical connection
        else:
            stations[station1].addConnection(station2, time, False)
            stations[station2].addConnection(station1, time, False)
            railroad.addConnection(station1, station2, time, False)

# Close the file
g.close()
