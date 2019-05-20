# Koffie uit G | Heuristieken: Rail NL 

## The Case
This case is about making the line management of intercity trains and consists of two parts: one that focuses on the 22 stations in North- and South-Holland and one that focuses on all 61 stations in the Netherlands, both including a number of critical stations. Critical stations are the stations that must be ridden in a specific timetable. Now it is up to us to set out different routes that ensure that (at least) these critical stations and their connections are ridden. We will plot this for the tracks of North and South Holland and then for the entire Netherlands. A number of important conditions for North and South Holland are: a maximum of seven trajectories can be used to reach the stations, and each trajectory can take a maximum of 120 minutes. For the railways of the entire Netherlands, this may be a maximum of twenty trajectories within a span of 180 minutes per trajectory.

A target function has been established for the quality of the line management: 
- K = p * 10000 - (T * 20 + Min / 10).

Herein K is the quality of the lines, p is the fraction of the critical connections used (so between 0 and 1), T is the number of trajectories and Min is the number of minutes in all trajectories together. In order to get the highest score we are aiming for a line management which covers as many critical connections with the least amount of trains in the shortest time possible.

## Bounds and State Space
The bounds and state space have been calculated for both cases. 

For North- and South-Holland the lower bound is -224 based on:
- p = 0, meaning no critical connections are covered
- T = 7, the maximum amount of trains are used
- min = 840, the maximum amount of minutes are used (7 trajectories x 120 min)

The upper bound is estimated at 9911,3 based on:
- p = 1, meaning all critical connections are covered
- T = 3, because three trains are needed to cover a 287 minute trajectory
- min = 287,  based on the theory that all critical connections are connected

The maximum number of possible trajectories in North- and South-Holland is equal to 48.114. Therefore the state space for the case is: 5,96898e+32. This is the maximum number of possible lines, calculated according to (48.114)^ 7. 


For the entire Netherlands the lower bound is -760 based on:
- p = 0, meaning no critical connections are covered
- T = 20, the maximum amount of trains are used
- min = 3600,  the maximum amount of minutes are used (20 trajectories x 180 min)

The upper bound is estimated at 9704 based on:
- p = 1, meaning all critical connections are covered
- T = 8, because eigth trains are needed to cover a 1360 minute trajectory
- min = 1360, based on the theory that all critical connections are connected

The maximum number of possible trajectories in the entire Netherlands is equal to 12 * 10^9. Therefore the state space for the case is: 3.83376e+201. This is the maximum number of possible lines, calculated according to (12 * 10^9)^ 20. 

Based on these calculations it was decided that brute force would be unrealistic, as this would take way too much time. Instead we decided to implement a random algorithm, a greedy algorithm, two types of hillclimbers, a genetic algorithm and a simulated annealing algorithm.

## File Structure
The files are structured in four main folders:
- Algorithms, containing all algorithms used to run the program
- Classes, containing the data structure used to run the program
- csvFiles, containing all the csv files used to run the program
- Helpers,  containing all code used to visualize the program

## Getting Started
Make sure that you have a copy of Python 3.7 or higher installed on your machine. You’ll also need to install `pip`. If you downloaded Python from [Python’s website](https://www.python.org/downloads/), you likely already have `pip` installed (you can check by running `pip` in a terminal window). If you don’t have it installed, be sure to install it before moving on!
1. Clone or download our GitHub repository 
2. In a terminal window, navigate to the directory you saved this repository on.
3. Run `pip3 install -r requirements.txt` in your terminal window to make sure that all of the necessary Python packages are installed.
4. Run `python main.py` to get started

## Authors
Lars de Roos, Maarten Wijstma en Nienke Luijcks