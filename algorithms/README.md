## Genetic 
Generates a random population of x raillinings of which the scores are calculated. Based on these scores, probabilities for each raillining are generated. The higher the probability the higher the chance that a raillining is chosen. For x times, children are generated out of two raillinings. Out of these parents and children, two are are randomly chosen to 'battle' against each other. The one with the highest score survives. This goes on for the entire population until the population is halved. Finally, the cycle starts all over again, but then with the surviving raillinings as starting point. 
 
## Greedy 
A greedy trajectory starts at a random start station, and then keeps on choosing the best option. In this case this choice is based on whether a neighbouring connection is critical, whether it has the shortest travel time, and whether it has already been visited. This continues until the maximum time of a trajectory is reached. Then a new trajectory is generated through the same procedure. 

## Hillclimber 
The hillclimber first selects a randomly generated raillining. First, the initial score of this raillining is calculated. Second, an extra trajectory is added to the raillining, and a score is calculated. Third, the score is calculated for the raillining with one of its initial trajectories replaced by another random trajectory. Finally, the scores are compared to one another, and the best option for the raillining is chosen. This procedure continues for a set amount of iterations. 

## Advanced Hillclimber
The advanced hillclimber is slightly different than the hillclimber described above. This version compares more altered versions of a raillining, but still chooses the best option. The advanced version also takes smaller steps in order to generate better scores. To elaborate: it first calculates the old score of the raillining, then it removes a randomly chosen trajectory and calculates the score. Then the algorithm pops (i.e. removes the last variable in a list) a selected number of stations and calculates the score afterwards. Additionally, it adds the same number of stations before the startstation of the trajectory and calculates the score. At last it also adds an extra trajectory to the raillining and again calculates the score. Finally, these scores are compared and the best raillining is chosen. This algorithm also runs for a chosen amount of iterations. 

## Random
 
## Simulated Annealing 

