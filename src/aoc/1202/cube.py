import os
import numpy as np

constraints = {"red":12,  "green":13,  "blue":14}

with open(os.path.join(os.getcwd(), 'src\\aoc\\1202\\input.txt'), 'r') as input:
        lines = input.readlines()

sum = 0
for line in lines:
        i = int(line[4:line.find(":")])
        line = line.split(":")[1]
        possible = True
        for gameset in line.split(";"):                
                for cell in gameset.split(","):
                        cell = cell.strip()
                        val = int(cell.split(" ")[0].strip())
                        color = cell.split(" ")[1].strip()
                        # print(f"{color}:{val}")
                        if color in constraints.keys():
                                if constraints[color] < val: possible = False
                        else: possible = False
        if possible: sum += i

print (sum)


