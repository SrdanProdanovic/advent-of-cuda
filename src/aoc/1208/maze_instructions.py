import os


with open(os.path.join(os.getcwd(), 'src\\aoc\\1208\\input_small.txt'), 'r') as input:
        lines = input.readlines()

turns = list()
maze = dict()

for i, line in enumerate(lines):
    if  i == 0: turns = list(line[0:len(line)-1])
    elif i > 1:
        kv = line.split(" = (")
        key = kv[0]
        if key in maze: print("WARN: key already found in the maze!")
        vals = kv[1].split(", ")
        maze[key] = [vals[0], vals[1][0:3]]

step_cnt = 0
turn_idx = 0
cur_steps = [x for x in maze.keys() if x[2] == 'A'] 
cur_steps.remove('AAA')
print(f"starting steps {cur_steps}")
all_end_z = False
# all_z_endings = set()
while not all_end_z:
        turn = turns[turn_idx]
        next_steps = []       
        for x in cur_steps: 
                choice = maze[x]
                if turn == "L": next_step = choice[0]
                elif turn == "R": next_step = choice[1]
                next_steps.append(next_step)
        assert len(next_steps) == len(cur_steps)
        all_z_endings = [x for x in next_steps if x[2] == 'Z']
        if len(all_z_endings) > 3: 
                print(f"{all_z_endings}, step_cnt = {step_cnt}") 
        # for x in z_endings: all_z_endings.add(x) 
        all_end_z = len(all_z_endings) == len(cur_steps)
        cur_steps = next_steps            
        if turn_idx == len(turns) - 1: turn_idx = 0
        step_cnt += 1
        turn_idx += 1
        

print(f"final step count = {step_cnt}")
            

step = "AAA"
path = ""
def part1():
        path = step + " -> "
        step_cnt = 0
        si = 0
        assert turns[0] == 'L'
        assert turns[len(turns)-1] == 'R'
        print(f"steps = {len(turns)}")
        while(step != "ZZZ"):
                turn = turns[si]
                choice = maze[step]
                if turn == "L": step = choice[0]
                elif turn == "R": step = choice[1]
                else: print(F"ERROR WRONG TURN: {turn}")
                path += f" {turn} -> {step} "
                step_cnt += 1
                si += 1
                if si == len(turns):
                        print(f"RESET last step = {step}, turn = {turn}. step_cnt = {step_cnt}")     
                        si = 0

        print(f"step count = {step_cnt}")
        assert step_cnt == 19637
