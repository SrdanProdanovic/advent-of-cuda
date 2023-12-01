import cupy as cp
import numpy as np
import os

# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form 
# a single two-digit number.
# For example:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?

def first_part():
    with open(os.path.join(os.getcwd(), 'src\\aoc\\1201\\input.txt'), 'r') as input:
        lines = input.readlines()
    sum = 0
    for line in lines:
        start = None
        end = None
        for c in line:
            if c.isdigit():
                end = c
                if not start:
                    start = c
                
        d = None
        if start:
            if end:
                d = int(start+end)
            else:
                d = int(start)
        print(f"line = {line}, d = {d}, s={sum}")
        if d > 0:
            sum += d    
    print(f"sum={sum}")




