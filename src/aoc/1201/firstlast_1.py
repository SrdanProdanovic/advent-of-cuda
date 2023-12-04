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


NMAP = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def parse_text_numbers(line:str) -> list:
    num_pos = []
    key_pos = []
    for num_key in NMAP.keys():
        idx = line.find(num_key)
        while idx > -1:          
            key_pos.append((NMAP[num_key],idx))
            idx = line.find(num_key, idx+1)
    for num_key in NMAP.values():
        idx = line.find(num_key)
        while idx > -1:          
            key_pos.append((num_key,idx))
            idx = line.find(num_key, idx+1)
    keys_sorted_by_pos = list(sorted(key_pos, key=lambda item:item[1]))
    if len(keys_sorted_by_pos) > 0:
        num_pos.append(keys_sorted_by_pos[0])
        if len(keys_sorted_by_pos) > 1:
            num_pos.append(keys_sorted_by_pos[len(keys_sorted_by_pos)-1])
        if (len(num_pos) == 1):
            num_pos.append(num_pos[0])
    return num_pos


with open(os.path.join(os.getcwd(), 'src/aoc/1201/input.txt'), 'r') as input:
    lines = input.readlines()
    sum = 0
    for line in lines:
        txt_nums = parse_text_numbers(line)
        sum += int(txt_nums[0][0]+txt_nums[1][0]) 
        print(f"{txt_nums}, {line}")
    print(sum)




