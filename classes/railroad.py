from classes import station as st
import csv

class Railroad(object):
    """
    Class that connects the stations with each other, forming the foundation
    for different tracks
    """

    def __init__(self):
        self.stationDict = {}
        self.connections = {}
        self.totalCritical = []
        self.criticalConnectionList = []

    def loadStations(self):
        # Open the Stations file and create empty station dictionaryd
        with open("csvFiles/stationsHolland.csv") as f:
            # Iterate over the lines
            for line in f:

                # Split the lines into words and save them into seperate variables
                stationData = (line.split(','))
                name = stationData[0]
                xCoordinate = stationData[1]
                yCoordinate = stationData[2]

                # If the station is critical save "Kritiek" as a boolean
                if len(stationData) > 3:
                    if stationData[3] == "Kritiek\n":
                        critical = True
                    else:
                        critical = False
                else:
                    critical = False
                # Initialize a station object and save it in a dictionary with
                # its name as the key
                station = st.Station(name, xCoordinate, yCoordinate, critical)
                self.stationDict[name] = station
        # Close the file
        f.close()

        # Open the the connections files
        with open("csvFiles/connectiesHolland.csv") as g:
            IDCounter = 0
            # Iterate over the lines
            for line in g:

                # Split the words on each lines and save them in seperate variables
                connection_data = line.split(',')
                station1 = connection_data[0]
                station2 = connection_data[1]
                time = float(connection_data[2])
                connectionID = int(IDCounter)
                IDCounter += 1

                # If one of the stations in the connection is critical, save the
                # connection as a critical connection
                if self.stationDict[station1].critical or \
                    self.stationDict[station2].critical:
                    self.stationDict[station1].addConnection(station2, time, True, IDCounter)
                    self.stationDict[station2].addConnection(station1, time, True, IDCounter)

                    self.addConnection(connectionID, station1, station2, time, True)

                # If neither station is critical, save it as a non-critical connection
                else:
                    self.stationDict[station1].addConnection(station2, time, False, IDCounter)
                    self.stationDict[station2].addConnection(station1, time, False, IDCounter)

                    self.addConnection(connectionID, station1, station2, time, False)

        # Close the file
        g.close()

    def addConnection(self, ID, station1, station2, time, critical):
        self.connections[ID] = [station1, station2, time, critical]

    def addTotalCritical(self):
        for key,value in self.connections.items():
            if value[3]:
                self.totalCritical.append([value[0], value[1]])
        return len(self.totalCritical)
