import io
import sys
import math

sys.setrecursionlimit(8000)

f = open("input.in", "r", encoding='utf-8')
reading = True
stones = set()

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    stones.add(eval('('+line+')'))


def neighbors(stone):
    lstone = list(stone)
    nbhs = []
    for d in range(3):
        s0 = lstone.copy()
        s1 = lstone.copy()
        s0[d] += 1
        s1[d] -= 1
        nbhs += [tuple(s0), tuple(s1)]
    return nbhs


def surf_area(stonez):
    full_area = len(stonez)*6
    int_area = 0
    for s in stonez:
        for t in neighbors(s):
            if t in stonez:
                int_area += 1
    return full_area - int_area


x_coord = [x for (x, y, z) in stones]
y_coord = [y for (x, y, z) in stones]
z_coord = [z for (x, y, z) in stones]
min_x, max_x = min(x_coord), max(x_coord)
min_y, max_y = min(y_coord), max(y_coord)
min_z, max_z = min(z_coord), max(z_coord)

space = set()
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        for z in range(min_z, max_z+1):
            space.add((x, y, z))

stones_set = set([tuple(s) for s in stones])
empty_space = space - stones_set
bubbles = set()
outside = set()


def determine_outside(start):
    outside.add(start)
    for t in neighbors(start):
        if t not in outside | stones and t in space:
            determine_outside(t)


determine_outside((0, 0, 0))
bubbles = empty_space - outside

print(surf_area(stones) - surf_area(bubbles))


