class Station(object):
    """
    Defines a station opbject, a station has a name, coordinates, and has
    connections with other stations that take a certain time to reach

    """

    def __init__(self, name, coordinates) :
        super(, self).__init__()
        self.name = name
        self.coordinates = coordinates
        self.connections = {}
        self.visited = False
        self.critical = False
