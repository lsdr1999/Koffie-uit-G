# Koffie uit G | Heuristieken: Rail NL 

## The Case
This case is about making the line management of intercity trains and consists of two parts: one that focuses on the 22 stations in North- and South Holland and one that focuses on all 61 stations in the Netherlands, both including a number of critical stations. Critical stations are the stations that need to be visited within a specified timeframe. Now it is up to us to set out different routes that ensure that (at least) these critical stations and their connections are ridden. We will plot this for the tracks of North- and South Holland and then for the Netherlands. A number of important conditions for North- and South Holland are: a maximum number of seven trajectories can be used to reach the stations, and each trajectory can use a maximum of 120 minutes. For the railways of the entire Netherlands, these constraints consist of a maximum of twenty trajectories within a timespan of 180 minutes per trajectory.

A target function has been established for the quality of the line management: 
- K = p * 10000 - (T * 20 + Min / 10).

Herein K is the quality of the lines, p is the fraction of the critical connections used (i.e. between 0 and 1), T is the number of trajectories and Min is the number of minutes in all trajectories together. In order to get the highest score we are aiming for a line management that covers as many critical connections with the smallest number of trains used in the shortest time possible. 

For more information regarding the case (in Dutch), see [Heuristieken wiki](http://heuristieken.nl/wiki/index.php?title=RailNL)

For our final presentation regarding the case (in Dutch), see [RailNL presentation](https://docs.google.com/presentation/d/11t8Py1WT8P4TOpoIWnB-mr0J_s3CpGcKq8vqqiOTE3w/edit?usp=sharing)

## Getting Started
Make sure that you have a copy of Python 3.7 or higher installed on your machine. You’ll also need to install `pip`. If you downloaded Python from [Python’s website](https://www.python.org/downloads/), you likely already have `pip` installed (you can check by running `pip` in a terminal window). If you don’t have it installed, be sure to install it before moving on!
1. Clone or download our GitHub repository 
2. In a terminal window, navigate to the directory you saved this repository on.
3. Run `python -m pip install -r requirements.txt` in your terminal window to make sure that all of the necessary Python packages are installed.
4. Run`python main.py long` or `pyhon main.py short` to get started. For those who use this project the first time, we advise you to use `python main.py long`.
5. Follow the steps shown in the table below. 

#### Command-line steps:

The following steps are available in the User Interface:

| Step | Command | Choice|
|--------|---------|---------------------|
| 0 |  | Run`python main.py long` or `pyhon main.py short` to get started. `Long` will give a full experience, while `short` will give a minimalistic experience (this is for people who are familiar with the project). |
|   | `q` | Exits the program at any given point. |
| 1 |  | Please choose if you like your trainlining to run over Holland or the Netherlands. Type `h` to select Holland, type `n` for the Netherlands. |
| 2 |  | Please choose the maximum number of trajectories. Type a number between *1 and 30*. For `h` we advise `7`, for `n` we advise `20`.|
| 3 |  | Please choose the maximum length of the trajectories in minutes. Type a number between *30 and 250*. For `h` we advise `120`, for `n` we advise `180`.|
| 4.1 |  | Please select one of the algorithms: `r` = random, `ge` = genetic, `gr` = greedy, `h` = hillclimber, `a` = advanced hillclimber, `s` = simulated annealing, `all` = all algorithms. |
| 4.2 |  | For more information regarding the algorithms type `info`. |
| 5 | `r` | You will be redirected to step 6. |
|   |  `ge` | Please insert the populationSize (between 10 and 100) or choose `d` for default settings. |
|   |  | Please insert the recombinationCoefficient (between 0 and 1) or choose `d` for default settings. | 
|   |  | Please insert the mutationRate (between 0 and 1) or choose `d` for default settings. You will be redirected to step 6. |
|   | `gr`| You will be redirected to step 6. |
|   | `h` | You will be redirected to step 6. |
|   | `a` | You will be redirected to step 6. |
|   | `s` | Please insert the hillclimber you want to use. For Advanced select `a`, for Normal select `n`. You will be redirected to step 6. |
|   | `all` |  Will run all algorithms for 100000 iterations in default settings. It will take approximately 20 minutes to run this function, and it will provide a graph at the end. |
| 6 |  | Please choose how many iterations your algorithm should run. Type a *positive integer*. |
| 7 |  | Please choose if you would like to rerun this a 100 times. Type `y` to select yes, type `n` to select no. |
| 8 | `y` | Your algorithm will start, it reruns 100 times and give a lowest, highest, and average value at the end. This option does not provide a visual at the end and takes longer than average to run. |
|   | `n` | Please choose if you would like to see a visual of your trainlining or a graph of its performance. Type `v` to select visual, type `g` to select graph. |
| 9 | `v` | A visualization of the trainlining with an overview of the current state of the connections will show. In the terminal the score and all trajectories will be printed. To close this run, close the figure pop-up screen.
|   | `g` | A performance graph will show. In the terminal the score and all trajectories will be printed. To close this run, close the figure pop-up screen. |
|   | `o` | A visualization of the trainlining with the trajectories will show. In the terminal the score and all trajectories will be printed. To close this run, close the figure pop-up screen. |

## File Structure
The files are structured in four main folders:
- Algorithms, containing all algorithms used to run the program
- Classes, containing the data structure used to run the program
- csvFiles, containing all the csv files used to run the program
- Helpers,  containing all code used to visualize the program

The program will be running via the main.py file

## Bounds and State Space
The bounds and state space have been calculated for both cases. 

For North- and South Holland the lower bound is -224 based on:
- p = 0, meaning no critical connections are covered
- T = 7, the maximum number of trajectories is used
- min = 840, the maximum number of minutes is used (7 trajectories x 120 min)

The upper bound is estimated at 9911,3 based on:
- p = 1, meaning all critical connections are covered
- T = 3, since three trains are needed to cover a 287 minute trajectory
- min = 287,  based on the theory that all critical connections are connected

The maximum number of possible trajectories in North- and South Holland is equal to 48.114. Therefore the state space for the case is: 5,96898e+32. This is the maximum number of possible lines, calculated according to (48.114)^ 7. 


For the Netherlands the lower bound is -760 based on:
- p = 0, meaning no critical connections are visited
- T = 20, the maximum number of trajectories is used
- min = 3600,  the maximum number of minutes is used (20 trajectories x 180 min)

The upper bound is estimated at 9738,9 based on:
- p = 1, meaning all critical connections are visited
- T = 8, since eight trains is the minimum we found through the algorithms
- min = 1011, based on the theory that all critical connections are connected

The maximum number of possible trajectories in the entire Netherlands is equal to 12 * 10^9. Therefore the state space for the case is: 3.83376e+201. This is the maximum number of possible lines, calculated according to (12 * 10^9)^ 20. 

Based on these calculations, it was decided that brute force would be unrealistic, as this would take way too much time. Instead we decided to implement a random algorithm, a greedy algorithm, two types of hillclimbers, a genetic algorithm and a simulated annealing algorithm.

## Authors
Lars de Roos, Maarten Wijstma and Nienke Luijcks.

## Acknowledgements
First of all we would like to thank Bram van den Heuvel for all the guidance and advice we've received during the development of this project. Credit is also due to Quinten van der Post who gave us advice on our presentation, and at times gave interesting insight into the workings of certain algorithms. Lastly we would like to thank everyone involved in the organisation of the course Heuristieken 2019, as we had a lot of fun working on this project.
