# test_mazeworld
# William Dinauer, 2022

from MazeworldProblem import MazeworldProblem
from Maze import Maze

from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("Mazes/maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
# test_mp.animate_path(result.path)

# Your additional tests here:

# -------------------------------------------------------
#  START:
#  .....
#  C.##.
#  .#.B.
#  ...D.
#  A...#

#  GOAL:
#  .....
#  B.##.
#  .#.A.
#  ...C.
#  D...#

# This test is a basic maze to show that we can perform A* with 4 robots just fine
test_maze4 = Maze("Mazes/maze4.maz")
test_mp = MazeworldProblem(test_maze4, (3, 2, 0, 3, 3, 1, 0, 0))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
# -------------------------------------------------------

# -------------------------------------------------------
# this is a 40x40 maze to show that A* works for a single
# robot in a very large maze
test_maze5 = Maze("Mazes/maze5.maz")
test_mp = MazeworldProblem(test_maze5, (15, 39))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
# -------------------------------------------------------

# -------------------------------------------------------
# This is a simple maze where one robot (C) first must move AWAY from
# its goal location in order for all the robots to reach their goal
test_maze6 = Maze("Mazes/maze6.maz")
test_mp = MazeworldProblem(test_maze6, (1, 1, 3, 1, 2, 1))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)
# -------------------------------------------------------

# -------------------------------------------------------
# In this maze, the robots start in a very narrow corridor and must
# back up all the way to the top left to rearrange themselves. Since
# robots must first move away from their goal to rearrange themselves,
# we see that the manhattan heuristic is not admissible, and leads to
# a worse solution that with the null_heuristic.
test_maze7 = Maze("Mazes/maze7.maz")
test_mp = MazeworldProblem(test_maze7, (1, 2, 1, 1, 1, 0))

result = astar_search(test_mp,  null_heuristic)
print(result)

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
# test_mp.animate_path(result.path)
# -------------------------------------------------------

# -------------------------------------------------------
# In this maze, we have 5 robots that must rearrange themselves in an
# interesting way to allow all the robots to reach their
# respective goal locations. It's a very tight squeeze
test_maze8 = Maze("Mazes/maze8.maz")
test_mp = MazeworldProblem(test_maze8, (4, 0, 4, 1, 4, 3, 4, 4, 4, 2))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)
# -------------------------------------------------------
