import io
import sys
import math
from collections import defaultdict

f = open("input.in", "r", encoding='utf-8')
reading = True
read_x, read_y = 0, 0
elves = {}
id = 0

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    while read_y < len(line):
        if line[read_y] == '#':
            elves[id] = (read_x, read_y)
            id += 1
        read_y += 1
    read_x, read_y = read_x+1, 0


def print_elves(e, printing):
    x_coords, y_coords = list(zip(*e.values()))
    max_x, min_x = max(x_coords), min(x_coords)
    max_y, min_y = max(y_coords), min(y_coords)
    empty_fields = 0
    for i in range(max_x-min_x+1):
        line = ''
        for j in range(max_y-min_y+1):
            if (min_x + i, min_y + j) in e.values():
                line += '#'
            else:
                line += '.'
                empty_fields += 1
        if printing:
            print(line)
    return empty_fields


drs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
# 0 = North, 1 = East, 2 = South, 3 = West
pri_dict = {0: [(-1, -1), (-1, 0), (-1, 1)], 
            1: [(-1, 1), (0, 1), (1, 1)], 
            2: [(1, 1), (1, 0), (1, -1)], 
            3: [(1, -1), (0, -1), (-1, -1)]}
priorities = [0, 2, 3, 1]

round = 0
elf_no = len(elves)

print_elves(elves, False)

while True:
    planned_moves = defaultdict(int)
    elves_by_move = defaultdict(list)
    for id in elves:
        x, y = elves[id]
        (xp, yp) = (x, y)
        nbs = {(c, d): False if (x+c, y+d) in elves.values() else True for (c, d) in drs}
        if not all(nbs.values()):
            found_move = False
            p, r = 0, 0
            while not found_move and p < 4:
                r = priorities[(p + round) % 4]
                dir_r_blocked = False
                for s, t in pri_dict[r]:
                    if not nbs[(s, t)]:
                        dir_r_blocked = True        
                if not dir_r_blocked:
                    found_move = True
                    (xp, yp) = (x + pri_dict[r][1][0], y + pri_dict[r][1][1])
                else:
                    p += 1
        planned_moves[id] = (xp, yp)
        elves_by_move[(xp, yp)].append(id)
    
    not_moving = 0

    for id in elves:
        (xp, yp) = planned_moves[id]
        (x, y) = elves[id]
        if (x, y) == (xp, yp):
            not_moving += 1
            continue
        elif len(elves_by_move[(xp, yp)]) == 1:
            elves[id] = (xp, yp)
    print('in round', round + 1, not_moving, 'out of', elf_no, 
          'elves didn\'t move, with', print_elves(elves, False), 'empty tiles')
    if not_moving == elf_no:
        print('DONE in round', round + 1)
        break            
    round += 1
