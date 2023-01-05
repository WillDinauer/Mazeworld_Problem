# test_sensorless
# William Dinauer, 2022

from SensorlessProblem import SensorlessProblem
from Maze import Maze

from astar_search import astar_search

# --------------------------------------------------------------------
# Here, we simply try to find where to robot is. We have no goal location.
maze = Maze("Mazes/maze2.maz")
test_sp = SensorlessProblem(maze)
result = astar_search(test_sp, test_sp.size_heuristic)
result.cost = len(result.path)-1
print(result)
test_sp.animate_path(result.path)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Here, we have a goal location. We want to guide the robot there ASAP
maze = Maze("maze4.maz")
test_sp = SensorlessProblem(maze, (3, 0))
size_search = astar_search(test_sp, test_sp.size_heuristic)
size_search.cost = len(size_search.path)-1
print(size_search)
test_sp.animate_path(size_search.path)

manhattan_search = astar_search(test_sp, test_sp.manhattan_heuristic)
manhattan_search.cost = len(manhattan_search.path)-1
print(manhattan_search)
test_sp.animate_path(manhattan_search.path)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# 6x6 maze without goal
maze = Maze("Mazes/maze9.maz")
test_sp = SensorlessProblem(maze)
size_search = astar_search(test_sp, test_sp.size_heuristic)
size_search.cost = len(size_search.path)-1
print(size_search)
test_sp.animate_path(size_search.path)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# 10x10 maze with goal
maze = Maze("Mazes/maze10.maz")
test_sp = SensorlessProblem(maze, (2, 5))
size_search = astar_search(test_sp, test_sp.size_heuristic)
size_search.cost = len(size_search.path)-1
print(size_search)
test_sp.animate_path(size_search.path)

manhattan_search = astar_search(test_sp, test_sp.manhattan_heuristic)
manhattan_search.cost = len(manhattan_search.path)-1
print(manhattan_search)
test_sp.animate_path(manhattan_search.path)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# 19x19 maze without goal
maze = Maze("Mazes/maze10.maz")
test_sp = SensorlessProblem(maze)
size_search = astar_search(test_sp, test_sp.size_heuristic)
size_search.cost = len(size_search.path)-1
print(size_search)
test_sp.animate_path(size_search.path)
# --------------------------------------------------------------------
