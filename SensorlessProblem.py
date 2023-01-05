# SensorlessProblem
# William Dinauer, 2022

from Maze import Maze
from time import sleep


class SensorlessProblem:
    # You write the good stuff here:
    def __init__(self, maze, goal_position=None):
        self.maze = maze
        self.goal_position = goal_position
        self.start_state = set()

        # add all tiles to list of possible states
        for x in range(0, self.maze.width):
            for y in range(0, self.maze.height):
                if self.maze.is_floor(x, y):
                    self.start_state.add(self.maze.index(x, y))

        # static start_state
        self.start_state = tuple(self.start_state)
        # possible_pos begins as the start_state, but will change
        self.possible_pos = tuple(self.start_state)

    def __str__(self):
        string = "Blind robot problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        # self.maze.robotloc = tuple(self.start_state)

        d = []
        for i in range(1, len(path)):
            state = path[i]
            prev = path[i-1]
            successors = []
            self.try_move(successors, prev, 1, 0)
            if successors[0] == state:
                d.append("east")
            else:
                successors = []
                self.try_move(successors, prev, -1, 0)
                if successors[0] == state:
                    d.append("west")
                else:
                    successors = []
                    self.try_move(successors, prev, 0, 1)
                    if successors[0] == state:
                        d.append("north")
                    else:
                        successors = []
                        self.try_move(successors, prev, 0, -1)
                        if successors[0] == state:
                            d.append("south")

        print("Set of Directions:")
        print(d)

    # heuristic function, simply returns the current number of possible states
    def size_heuristic(self, state):
        return len(state)

    # calculates the distance from every possible location of the robot to the goal location
    def manhattan_heuristic(self, state):
        dist = 0
        # goal x and y
        x = self.goal_position[0]
        y = self.goal_position[1]

        # every idx is a possible location of the robot
        for idx in state:
            rx = int(idx % self.maze.width)
            ry = self.maze.height - 1 - int((idx - x) / self.maze.height)
            dist += abs(rx - x) + abs(ry - y)
        return dist

    def min_manhattan(self, state):
        minimum = 0
        x = self.goal_position[0]
        y = self.goal_position[1]

        for idx in state:
            rx = int(idx % self.maze.width)
            ry = self.maze.height - 1 - int((idx - x) / self.maze.height)
            minimum = min(minimum, abs(rx-x)+abs(ry-y))
        return minimum

    # possible moves
    def get_successors(self, state):
        # list of valid successors
        successors = []

        # try moving east, west, north, south
        self.try_move(successors, state, 1, 0)
        self.try_move(successors, state, -1, 0)
        self.try_move(successors, state, 0, 1)
        self.try_move(successors, state, 0, -1)

        return successors

    # for the robot's move in the current state, find possible states that remain
    def try_move(self, successors, state, dx, dy):
        new_state = set()
        # for each possible position that the robot may be in...
        for idx in state:
            # calculate x and y of robot
            x = int(idx % self.maze.width)
            y = self.maze.height - 1 - int((idx - x) / self.maze.height)
            # floor tile: the robot can move here, so it remains a possible location
            new_idx = self.maze.index(x+dx, y+dy)
            if self.maze.is_floor(x+dx, y+dy):
                new_state.add(new_idx)
            else:
                new_state.add(idx)
        successors.append(tuple(new_state))

    def goal_test(self, state):
        if len(state) == 1:
            if self.goal_position is None or state[0] == self.maze.index(self.goal_position[0], self.goal_position[1]):
                return True
        return False

    def transition_cost(self, child, curr_node):
        return curr_node.transition_cost

# A bit of test code
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
