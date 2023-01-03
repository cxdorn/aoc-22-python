import io
import sys
import math
import numpy as np

f = open("input.in", "r", encoding='utf-8')
reading = True
map = []
start = (-1, -1)
end = (-1, -1)


def alnum(l):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    if l == 'S':
        return 0
    if l == 'E':
        return 25.1
    else:
        return alph.find(l)


while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    map += [[alnum(x) for x in line[:-1]]]

map = np.array(map)
visiting = set()
visited = set()
distance = np.zeros(map.shape)

m, n = map.shape
for i in range(m):
    for j in range(n):
        if map[i, j] > 25:
            end = (i, j)
            visiting.add(end)
            visited.add(end)

steps = 1


def p2cond(vis):
    for (i, j) in vis:
        if map[i, j] == 0:
            print('solution: ', distance[i, j])
            return False
    return True


while p2cond(visiting):
    next_visiting = set()
    for (s, t) in visiting:
        nbs = [(s + 1, t),
               (s, t + 1),
               (s - 1, t),
               (s, t - 1)]
        for (i, j) in nbs:
            if i >= 0 and j >= 0 and i < m and j < n:
                if (i, j) not in visited and map[i, j] > map[s, t] - 1.5:
                    next_visiting.add((i, j))
                    visited.add((i, j))
                    distance[i, j] = steps
    visiting = next_visiting
    steps += 1
