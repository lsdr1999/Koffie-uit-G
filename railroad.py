
class Railroad(object):
    """
    Class that connects the stations with each other, forming the foundation
    for different tracks
    """

    def __init__(self):
        self.station_dict = {}
        self.connections = {}

    def addStation(self, stationname, critical):
        self.station_dict[stationname] = [stationname, critical]

    def addConnection(self, station1, station2, time, critical):
        self.connections[station1] = [station2, time, critical]
        self.connections[station2] = [station1, time, critical]
