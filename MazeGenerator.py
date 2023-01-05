# MazeGenerator
# Generates random (potentially) valid mazes
# William Dinauer, 2022

import random


def generateMaze(filename, x, y):
    random.seed()
    f = open(filename, "w")
    for row in range(y):
        line = ""
        for col in range(x):
            i = random.randint(0, 3)
            if i is 0:
                line += "#"
            else:
                line += "."
        line += "\n"
        f.write(line)
    f.close()


# generateMaze("maze4.maz", 5, 5)
# generateMaze("maze5.maz", 40, 40)
# generateMaze("maze6.maz", 10, 5)
# generateMaze("maze7.maz", 8, 8)
# generateMaze("maze8.maz", 16, 24)
