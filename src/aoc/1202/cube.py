import os
import numpy as np
import cupy as cp 
import timeit

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

def part2():
        sum = 0
        for line in lines:
                line = line.split(":")[1]
                max_val = {"red":-1,  "green":-1,  "blue":-1}
                for gameset in line.split(";"):                
                        for cell in gameset.split(","):
                                cell = cell.strip()
                                val = int(cell.split(" ")[0].strip())
                                color = cell.split(" ")[1].strip()
                                if max_val[color] < val: max_val[color] = val
                # print(f"{max_val}")
                prod = 1
                for val in max_val.values():
                        prod*=val
                sum += prod
        assert sum == 66681

def numpy_way():
        sum = 0
        inventory = None
        for line in lines:
                i = line.split(":")[0]
                line = line.split(":")[1]
                index = {"red":0,  "green":1,  "blue":2}
                row = np.ones(3) 
                for gameset in line.split(";"):                               
                        for cell in gameset.split(","):
                                cell = cell.strip()
                                val = int(cell.split(" ")[0].strip())
                                color = cell.split(" ")[1].strip()
                                if (row[index[color]] < val): row[index[color]] = val
                # print(f"{i}: {row}")
                if inventory is not None: inventory = np.vstack((inventory, row))
                else: inventory = np.array(row)
        # print(f"inventory shape after stacking: {np.shape(inventory)}")
        inventory = np.prod(inventory, axis=1)
        # print(f"inventory shape after mul: {np.shape(inventory)}")
        sum = np.sum(inventory, axis=0)
        assert sum == 66681

def cupy_way():
        sum = 0
        inventory = None
        for line in lines:
                i = line.split(":")[0]
                line = line.split(":")[1]
                index = {"red":0,  "green":1,  "blue":2}
                row = cp.ones(3) 
                for gameset in line.split(";"):                               
                        for cell in gameset.split(","):
                                cell = cell.strip()
                                val = int(cell.split(" ")[0].strip())
                                color = cell.split(" ")[1].strip()
                                if (row[index[color]] < val): row[index[color]] = val
                # print(f"{i}: {row}")
                if inventory is not None: inventory = cp.vstack((inventory, row))
                else: inventory = cp.array(row)
        # print(f"inventory shape after stacking: {cp.shape(inventory)}")
        inventory = cp.prod(inventory, axis=1)
        # print(f"inventory shape after mul: {cp.shape(inventory)}")
        sum = cp.sum(inventory, axis=0)
        assert sum == 66681

for x in [part2, numpy_way, cupy_way]:
        # Measure the execution time using timeit
        execution_time = timeit.timeit(x, number=50) * 1000
        print(f" {x.__name__} Exec Time: {execution_time} ms")
