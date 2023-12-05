import os
import numpy as np

with open(os.path.join(os.getcwd(), 'src\\aoc\\1202\\input.txt'), 'r') as input:
        lines = input.readlines()

def part1():
        constraints = {"red":12,  "green":13,  "blue":14}
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

sum = 0
inventory = np.array()
for line in lines:
        line = line.split(":")[1]
        max_val = {"red":-1,  "green":-1,  "blue":-1}
        for gameset in line.split(";"):                
                for cell in gameset.split(","):
                        cell = cell.strip()
                        val = int(cell.split(" ")[0].strip())
                        color = cell.split(" ")[1].strip()
                        if max_val[color] < val: max_val[color] = val
        print(f"{max_val}")
        prod = 1
        for val in max_val.values():
                prod*=val
        sum += prod
print (sum)
assert sum == 66681