from classes import station as st
import csv

class Railroad(object):
    """
    Class that connects the stations with each other, forming the foundation
    for different tracks
    """

    def __init__(self):
        """ Initializes a railroad object """
        self.stationDict = {}
        self.connections = {}
        self.totalCritical = []

<<<<<<< HEAD
    def loadStations(self):
        # Open the Stations file and create empty station dictionaryd
        with open("csvFiles/stationsHolland.csv") as f:
=======

    def loadStations(self, csvChoice, csvConnections):
        """
        Loads stations and connnections from csvFiles, creates station objects and adds them to the stationDict

        Args:
            csvChoice (string): Chosen csv file with stations, South- and North-Holland or the entire Netherlands
            csvConnections (string): Chosen csv file with connections, South- and North-Holland or the entire Netherlands
        """

        # Open the Stations file and create empty station dictionary
        with open(csvChoice) as f:
>>>>>>> 781142ae1605fa17e5f49aa5c1ae8776c165d787
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

<<<<<<< HEAD
        # Open the the connections files
        with open("csvFiles/connectiesHolland.csv") as g:
=======
        # Open the connections files
        with open(csvConnections) as g:
>>>>>>> 781142ae1605fa17e5f49aa5c1ae8776c165d787
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
        """
        Fills a connections dictionary out of the csv files with information about stations, time and 'critical'

        Args:
            ID (int): id of connection
            station1 (string): the first/start station
            station2 (string): the second/go to station
            time (int): the time between two stations
            critcal (bool): critical connection
        """
        self.connections[ID] = [station1, station2, time, critical]


    def addTotalCritical(self):
        """
        Adds critical stations out of connections dict to totalCritical list

        Returns:
            The length of totalCritical
        """
        for key,value in self.connections.items():
            if value[3]:
                self.totalCritical.append([value[0], value[1]])
        return len(self.totalCritical)
