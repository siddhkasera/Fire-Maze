Implemented DFS and BFS algorithms using Stacks and Queues to solve the static maze. Of the two DFS is a better choice since it consumes much less memory space and will reach the goal node in a less period than BFS if it traverses in the right path. Unlike BFS it does not require extra memory space to store the nodes at every branch, which can be very high in problems like finding a path in a maze with higher dimensions.


Plot for DFS


![dfs](https://github.com/siddhkasera/Fire-Maze/assets/58352099/9483ef5a-1079-4859-b37d-339f6002e3ed)


Plot for BFS


![BFS](https://github.com/siddhkasera/Fire-Maze/assets/58352099/80a00548-4fa6-42eb-837d-522af2f1a75c)


If there is no path from S to G the nodes explored by A* will be more than the node than BFS.

Largest dimension that can be solved using DFS at p = 0.3 in less than a minute -- low mid 3700's
Largest dimension that can be solved using BFS at p = 0.3 in less than a minute -- 7000 - 8000 
Largest dimension that can be solved using A* at p = 0.3 in less than a minute -- less than 50

Our Strategy 3 introduces a heuristic that will allow the agent to determine which tile to go to based on the distance from the goal and the distance from the fire. It will choose the point that minimizes the distance from the goal and maximizes the distance from the fire. The formula goes as follows, where G is the distance from the goal and F is the distance from the fire.

h = G - alpha * F

The value alpha will represent how much the agent prioritizes fire distance--the larger $\alpha$ is, the more the formula will prioritize fire. If alpha is too large, the agent will then develop an increasingly bigger tendency to get itself cornered into a wall, failing to solve the maze.


The strategy is along the same line as DFS but instead of a stack, we are using a Priority Queue. Nodes are pushed into this priority queue and popped out based on the values calculated by the heuristic where the smallest value has the highest priority. 

So while the heap is not empty pop the node with the highest priority from the queue and check if it is that node is on fire, if it is that means the agent was burned before it could reach the destination. If the node is not on fire check to see if it is equal to the destination node it is a success and the agent reached its destination goal. If not reached the destination look for all the possible neighbors for that node. Check if they are valid (not outside the range of the grid, not a wall on fire or visited before). Mark that node as visited push it on the queue and continue. 

As the flammability increases the average success rate decreases gradually for all three strategies. 

They are different in the average time it takes for each strategy to find a path from start to goal. Strategy 3 takes the longest since there are more computations involved with each step compared to strategy 2 and strategy 1 where it only checks for a cell with fire and is not concerned with the future state of fire.

Plot for Strategy 1 (the agent does not check updates for fire):


![fire1_1](https://github.com/siddhkasera/Fire-Maze/assets/58352099/10712081-bebc-450a-a83e-32cf3f64183c)


Plot for Strategy 2 (will now check for fire):


![fire2_2](https://github.com/siddhkasera/Fire-Maze/assets/58352099/03c4718a-6611-4c56-8055-cb62c0ffb4bd)


Plot for Strategy 3 (our strategy):


![strategy3](https://github.com/siddhkasera/Fire-Maze/assets/58352099/8a22b7e6-8850-4377-a7b8-90bea1d6ec79)

The drawback of strategy 3 is that if we increase the alpha the agent can corner itself to a wall failing to solve the maze. So if we had unlimited computational resources we would introduce beta to our original heuristic formula. The beta will represent how much the agent prioritizes distance from the wall. The value of beta should balance the value chosen for alpha to make the agent less greedy. The new formula will be: 

h = beta * G - alpha * F

If we could only take 10 seconds using heuristics will not work since calculating them takes longer than 10 seconds. Instead, we could give the agent a maximum sight range where it can see the fire, and if there is no fire greater than, say 10 blocks then continue with strategy 2.











