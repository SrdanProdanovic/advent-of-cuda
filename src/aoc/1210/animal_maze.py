import os

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

with open(os.path.join(os.getcwd(), 'src\\aoc\\1210\\input_small.txt'), 'r') as input:
    lines = input.readlines()

# SHIFTS FOR SYMBOLS BY ROWS AND COLS, WHEN GOING IN DOWN or RIGHT DIR
shift = {'|':[1,0,], '-':[0,1], 'L':[0,1], 'J':[1,0], '7':[0,1], 'F':[0,1]}
# IF GOING UP OR LEFT, THESE VALUES NEED TO BE * -1 

ROWS = len(lines)
COLS = len(lines[0])
pos = [0,0]
maze = list()
for i, line in enumerate(lines):
    s_col = line.find('S')
    if s_col != -1: pos = [i, s_col]
    maze.append(list(line.removesuffix("\n")))
    assert len(line) == COLS, f"row {i}: {line}, {len(line)} != {COLS} "
assert len(maze) == ROWS

for coord in [0,1]
end = False
steps = []
while not end:
    for x,y in [[0,1],[1,0]]:
        if maze[x + pos[0]][y + pos[y]] in shift.keys():
            next = maze[shift[] + pos[0]][y + pos[y]]


print(maze)