# MazeworldProblem
# William Dinauer, 2022

from Maze import Maze
from time import sleep


class MazeworldProblem:
    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.start_state = list(maze.robotloc)
        self.start_state.insert(0, 0)
        self.start_state = tuple(self.start_state)
        self.goal_locations = goal_locations

    def __str__(self):
        string = "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(.1)

            print(str(self.maze))

    def manhattan_heuristic(self, state):
        # calculate the sum of the x and y distance for each robot from its current position to its goal
        manhattan_dist = 0
        # for each robot...
        for i in range(1, len(state), 2):
            # get the x and y of the robot
            robot_x = state[i]
            robot_y = state[i + 1]

            # get the goal x and y of the robot
            goal_x = self.goal_locations[i - 1]
            goal_y = self.goal_locations[i]

            # manhattan distance is the absolute value of the distance from the goal for both x and y
            manhattan_dist += abs(robot_x - goal_x) + abs(robot_y - goal_y)

        return manhattan_dist

    def get_successors(self, state):
        # list of valid successors
        successors = []

        self.maze.robotloc = tuple(state[1:])

        # robot to move
        robot_number = state[0]

        # next robot to move
        new_num = (robot_number + 1) % int(len(self.maze.robotloc) / 2)
        s = list(state)
        s[0] = new_num
        s = tuple(s)

        # no move - giving up turn
        successors.append(s)

        # try moving the robot in each of the cardinal directions
        self.try_state(successors, s, robot_number, 1, 0)
        self.try_state(successors, s, robot_number, -1, 0)
        self.try_state(successors, s, robot_number, 0, 1)
        self.try_state(successors, s, robot_number, 0, -1)

        return successors

    # create a new state, adding it to successors if it is valid
    def try_state(self, successors, state, robot_number, dx, dy):
        new_state = list(state)
        # try to move the robot by the dx and dy given
        new_state[robot_number * 2 + 1] += dx
        new_state[robot_number * 2 + 2] += dy
        # validate the robot's move
        if self.validate_state(new_state, robot_number):
            new_state = tuple(new_state)
            successors.append(new_state)

    # validate a given state for a specific robot's position
    # Returns True only if the robot is on an unoccupied floor space in the new state
    def validate_state(self, new_state, robot_number):
        x = new_state[robot_number * 2 + 1]
        y = new_state[robot_number * 2 + 2]
        if self.maze.has_robot(x, y) or not self.maze.is_floor(x, y):
            return False
        return True

    # test if we have reached our goal state
    def goal_test(self, state):
        if state[1:] == self.goal_locations:
            return True
        return False

    # Cost for how much fuel we've expended. Only increment if the robot moved.
    def transition_cost(self, child, curr_node):
        g = curr_node.transition_cost
        if child[1:] != curr_node.state[1:]:  # robot moved if our child state differs from our current state
            g += 1
        return g


## A bit of test code. You might want to add to it to verify that things
#  work as expected.
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
