# CPSC481_-GRIDWORLD-INTELLIGENT-AGENT
This is a project to build a GRIDWORLD INTELLIGENT AGENT for Artificial Intelligent class. The project will include different phases.


1.Phase 1: Build a Gridworld environment  + Add intelligence using Breadth-First Search (BFS)

What is the state representation?

- Each state is represented as a tuple ([row],[col]). This represents the agent’s position in the grid.
The grid itself is not stored in the state. Only the agent’s current location is considered the state.


Why does BFS guarantee the shortest path in this grid?
- Because BFS explores the grid at each state. First all states 1 step away. Then move on to all states 2 steps away. Again, then 3 steps away, etc.
Since every move cost 1 step. BFS always find the goal using the minimum of steps. Therefore, BFS guarantee the shortest path in the grid. 

My results:

Path length = 8
Nodes expanded = 14