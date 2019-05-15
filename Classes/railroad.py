from classes import station as st
import csv

class Railroad(object):
    """
    Class that connects the stations with each other, forming the foundation
    for different tracks
    """

    def __init__(self):
        self.station_dict = {}
        self.connections = {}
        self.totalCritical = []
        self.criticalConnectionList = []

    def loadStations(self):
        # Open the Stations file and create empty station dictionaryd
        with open("csvBestanden/stationsNationaal.csv") as f:
            # Iterate over the lines
            for line in f:

                # Split the lines into words and save them into seperate variables
                station_data = (line.split(','))
                name = station_data[0]
                xcoordinate = station_data[1]
                ycoordinate = station_data[2]

                # If the station is critical save "Kritiek" as a boolean
                if len(station_data) > 3:
                    if station_data[3] == "Kritiek\n":
                        critical = True
                else:
                    critical = False
                # Initialize a station object and save it in a dictionary with
                # its name as the key
                station = st.Station(name, xcoordinate, ycoordinate, critical)
                self.station_dict[name] = station
        # Close the file
        f.close()

        # Open the the connections files
        with open("csvBestanden/connectiesNationaal.csv") as g:
            ID_counter = 0
            # Iterate over the lines
            for line in g:

                # Split the words on each lines and save them in seperate variables
                connection_data = line.split(',')
                station1 = connection_data[0]
                station2 = connection_data[1]
                time = float(connection_data[2])
                Connection_ID = int(ID_counter)
                ID_counter += 1

                # If one of the stations in the connection is critical, save the
                # connection as a critical connection
                if self.station_dict[station1].critical or \
                    self.station_dict[station2].critical:
                    self.station_dict[station1].addConnection(station2, time, True, ID_counter)
                    self.station_dict[station2].addConnection(station1, time, True, ID_counter)

                    self.addConnection(Connection_ID, station1, station2, time, True)

                # If neither station is critical, save it as a non-critical connection
                else:
                    self.station_dict[station1].addConnection(station2, time, False, ID_counter)
                    self.station_dict[station2].addConnection(station1, time, False, ID_counter)

                    self.addConnection(Connection_ID, station1, station2, time, False)

        # Close the file
        g.close()

    def addConnection(self, ID, station1, station2, time, critical):
        self.connections[ID] = [station1, station2, time, critical]

    def addTotalCritical(self):
        for key,value in self.connections.items():
            if value[3]:
                self.totalCritical.append([value[0], value[1]])
        return len(self.totalCritical)
