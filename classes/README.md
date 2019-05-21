# Classes

This folder contains all the classes used to resolve this case. 

The folder contains the following files:
- railroad.py

    Class that connects the stations with each other, forming the foundation for different tracks.
    
- station.py

    Defines a station object, a station has a name, coordinates, and has connections with other stations that take a certain time to reach.

- trainlining.py 

    Class that creates the trajectories, calculates the length of trajectories and calculates the score (the quality of the trainlining).

- trajectory.py

    Class that creates a trajectory out of stations and connections. It adds visited Stations and connections and calculates both the total visitedCritical as the total Length of the trajectory.
