import io
import sys
import math
import numpy as np


f = open("input.in", "r", encoding='utf-8')
reading = True
trees = []

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    trees += [[int(x) for x in line if x != '\n']]

ntrees = np.array(trees)
nvisible = np.zeros(ntrees.shape)
nvision = np.ones(ntrees.shape)


def visible_from_left(tr, vr):
    h, w = tr.shape
    for i in range(h):
        max = -1
        for j in range(w):
            if tr[i, j] > max:
                vr[i, j] = 1
                max = tr[i, j]
    return vr


def left_scenic_score(tr, r):
    h, w = tr.shape
    vr = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            vision = 0
            jj = j - 1
            while jj >= 0:
                vision += 1
                if tr[i, jj] >= tr[i, j]:
                    break
                jj = jj - 1
            vr[i, j] = vision
    print(np.rot90(vr, -r), r)
    return vr


# for r in range(4):
#     nvisible = visible_from_left(np.rot90(ntrees, r), np.rot90(nvisible, r))
#     nvisible = np.rot90(nvisible, -r)

for r in range(4):
    nvision *= np.rot90(left_scenic_score(np.rot90(ntrees, r), r), -r)

print(ntrees)
print(nvision)
print(np.max(nvision))
