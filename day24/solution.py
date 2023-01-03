import io
import sys
import math
from collections import defaultdict

f = open("input.in", "r", encoding='utf-8')
reading = True
blz_move = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
blocked = defaultdict(int)
blz = {'>': defaultdict(int), 'v': defaultdict(int),
       '<': defaultdict(int), '^': defaultdict(int)}

x, y = 0, 0
while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    for c in line:
        if c == '#':
            blocked[(x, y)] = 1
        for b in blz_move:
            if c == b:
                blz[b][(x, y)] = 1
        y += 1
    x, y = x + 1, 0

x_coords, y_coords = list(zip(*blocked.keys()))
max_x, min_x, max_y, min_y = max(x_coords), 0, max(y_coords), 0
start, target = (0, 1), (max_x, max_y-1)


# b in {>, v, <, ^}, t = time, u = x-coord, v = y-coord
def has_bliz(b, t, u, v):
    if (u, v) == start or (u, v) == target:
        return False
    o, p = blz_move[b][0], blz_move[b][1]
    un = (u - 1 - o*t) % (max_x - 1) + 1
    vn = (v - 1 - p*t) % (max_y - 1) + 1
    return blz[b][(un, vn)] == 1


def has_any_bliz(t, u, v):
    return any(has_bliz(b, t, u, v) for b in blz_move)


def not_blocked(u, v):
    return not blocked[(u, v)] == 1


time = 0

drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start_drs = [(1, 0)]
target_drs = [(-1, 0)]


def find_path(ss, tt):
    global time
    pos = {}
    pos[time] = {ss}
    while tt not in pos[time]:
        if time % 10 == 0:
            print('at', time, 'have', len(pos[time]), 'states')
        time += 1
        pos[time] = set()
        for (px, py) in pos[time-1]:
            # can we wait?
            if not has_any_bliz(time, px, py):
                pos[time].add((px, py))
            # can we move?
            ds = start_drs if (px, py) == start else (target_drs if (px, py) == target else drs)
            for (dx, dy) in ds:
                u, v = px+dx, py+dy
                if not_blocked(u, v) and not has_any_bliz(time, u, v):
                    pos[time].add((u, v))


find_path(start, target)
print('found target at time', time)
find_path(target, start)
print('found back to source at time', time)
find_path(start, target)
print('found target at time', time)
