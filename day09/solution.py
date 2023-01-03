import io
import sys
import math


f = open("input.in", "r", encoding='utf-8')
reading = True
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
hist = {(0, 0)}
dir_dict = {'D': [-1, 0], 'U': [1, 0], 'L': [0, -1], 'R': [0, 1]}


def physics(h, t):
    xd = h[0]-t[0]
    yd = h[1]-t[1]
    if max(abs(xd), abs(yd)) > 1:
        t[0] += int(xd/2 if (abs(xd) > 1) else xd)
        t[1] += int(yd/2 if (abs(yd) > 1) else yd)
    return t


while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    dir, rep = line.split()
    dir = dir_dict[dir]
    rep = int(rep)
    print('now doing dir and rep: ', dir, rep)
    for i in range(rep):
        rope[0][0] = rope[0][0] + dir[0]
        rope[0][1] = rope[0][1] + dir[1]
        for i in range(9):
            rope[i+1] = physics(rope[i], rope[i+1])
        hist.add((rope[9][0], rope[9][1]))
         
print(len(hist))
