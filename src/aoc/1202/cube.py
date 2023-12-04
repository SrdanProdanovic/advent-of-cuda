import os
import numpy as np

constraints = {"red":12,  "green":13,  "blue":14}

with open(os.path.join(os.getcwd(), 'src\\aoc\\1202\\input.txt'), 'r') as input:
        lines = input.readlines()

for line in lines:
        i = int(line[4:line.find(":")])
        line = line.split(":")[1]
        for group in line.split(";"):
                for cells in group.split(","):
                        print(cells)
